#!/usr/bin/env bash
# =============================================================================
# Script Name: server_explore.sh
# Description: Comprehensive Unix server exploration tool
#              Gathers hardware, software, user, service, and Docker info
#
# How to run:
#   chmod +x server_explore.sh
#   ./server_explore.sh
#
#   Or as root for full detail:
#   sudo ./server_explore.sh
#
#   Schedule via cron (runs daily at 2am):
#   0 2 * * * /path/to/server_explore.sh
# =============================================================================

SCRIPT_NAME="server_explore.sh"
OUTPUT_DIR="/mnt/Web/cron"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
REPORT="${OUTPUT_DIR}/server_report_${TIMESTAMP}.txt"
HOSTNAME=$(hostname -f 2>/dev/null || hostname)

# Ensure output directory exists
mkdir -p "${OUTPUT_DIR}" || { echo "ERROR: Cannot create ${OUTPUT_DIR}"; exit 1; }

# ─── Helpers ─────────────────────────────────────────────────────────────────
hr()      { printf '%.0s─' {1..72} >> "${REPORT}"; echo >> "${REPORT}"; }
section() { echo >> "${REPORT}"; hr; printf "  %-68s\n" "▶  $1" >> "${REPORT}"; hr; }
cmd()     { echo "$ $*" >> "${REPORT}"; "$@" >> "${REPORT}" 2>&1 || true; echo >> "${REPORT}"; }
has()     { command -v "$1" &>/dev/null; }

# ─── Header ──────────────────────────────────────────────────────────────────
{
  echo "=============================================================="
  echo "  SERVER EXPLORATION REPORT"
  echo "  Script  : ${SCRIPT_NAME}"
  echo "  Host    : ${HOSTNAME}"
  echo "  Date    : $(date)"
  echo "  User    : $(whoami)"
  echo "=============================================================="
} > "${REPORT}"

# =============================================================================
# HARDWARE
# =============================================================================
section "HARDWARE — CPU"
cmd cat /proc/cpuinfo | grep -E "^(processor|model name|cpu MHz|cache size|physical id|core id|siblings|cpu cores)" | sort -u
cmd nproc --all
has lscpu   && cmd lscpu
has dmidecode && cmd dmidecode -t processor 2>/dev/null || true

section "HARDWARE — Memory"
cmd free -h
cmd cat /proc/meminfo
has dmidecode && cmd dmidecode -t memory 2>/dev/null | grep -E "(Size|Type|Speed|Manufacturer|Part)" || true

section "HARDWARE — Storage & Disks"
cmd df -hT
cmd lsblk -o NAME,SIZE,TYPE,FSTYPE,MOUNTPOINT,MODEL
has fdisk   && cmd fdisk -l 2>/dev/null || true
has nvme    && cmd nvme list 2>/dev/null || true
has smartctl && { for d in $(lsblk -dpno NAME); do cmd smartctl -a "$d"; done; } || true

section "HARDWARE — PCI / USB Devices"
has lspci && cmd lspci -v
has lsusb && cmd lsusb

section "HARDWARE — Network Interfaces"
cmd ip addr show
cmd ip route show
cmd ip -s link
has ethtool && for iface in $(ip -o link show | awk -F': ' '{print $2}' | grep -v lo); do
  echo "--- $iface ---" >> "${REPORT}"
  ethtool "$iface" >> "${REPORT}" 2>&1 || true
done
has iwconfig && cmd iwconfig 2>/dev/null || true

section "HARDWARE — System / Firmware"
cmd uname -a
cmd cat /etc/os-release 2>/dev/null || cat /etc/redhat-release 2>/dev/null || true
has dmidecode && cmd dmidecode -t system 2>/dev/null || true
has dmidecode && cmd dmidecode -t bios   2>/dev/null || true

section "HARDWARE — Temperature & Power"
has sensors     && cmd sensors
has ipmitool    && cmd ipmitool sdr list 2>/dev/null || true
has powerstat   && cmd powerstat -d 0 1 2>/dev/null || true

# =============================================================================
# SOFTWARE
# =============================================================================
section "SOFTWARE — Kernel & Modules"
cmd uname -r
cmd uname -a
cmd lsmod | head -60
cmd sysctl -a 2>/dev/null | grep -E "^(kernel|vm|net\.core)" | head -80

section "SOFTWARE — Installed Packages"
if has rpm;      then cmd rpm -qa --qf '%{NAME}-%{VERSION}-%{RELEASE}.%{ARCH}\n' | sort
elif has dpkg;   then cmd dpkg -l | grep '^ii'
elif has pacman; then cmd pacman -Q
elif has apk;    then cmd apk info -v
fi

section "SOFTWARE — Running Processes"
cmd ps auxf
cmd top -bn1 | head -30

section "SOFTWARE — Open Files & Network Connections"
has lsof && cmd lsof -i -n -P | head -80
cmd ss -tulpn
cmd netstat -tulpn 2>/dev/null || true

section "SOFTWARE — Environment & Shell"
cmd printenv | sort
cmd cat /etc/shells
cmd cat /etc/profile 2>/dev/null || true

section "SOFTWARE — Scheduled Jobs (cron)"
cmd crontab -l 2>/dev/null || echo "(no user crontab)"
for f in /etc/cron.d/* /etc/cron.daily/* /etc/cron.hourly/* /etc/cron.weekly/* /etc/cron.monthly/*; do
  [ -f "$f" ] && { echo "--- $f ---" >> "${REPORT}"; cat "$f" >> "${REPORT}"; echo >> "${REPORT}"; }
done
cmd cat /etc/crontab 2>/dev/null || true

section "SOFTWARE — System Logs (tail)"
for log in /var/log/syslog /var/log/messages /var/log/auth.log /var/log/secure; do
  [ -f "$log" ] && { echo "--- $log (last 30 lines) ---" >> "${REPORT}"; tail -30 "$log" >> "${REPORT}" 2>&1; echo >> "${REPORT}"; }
done
has journalctl && cmd journalctl -n 50 --no-pager

# =============================================================================
# USERS
# =============================================================================
section "USERS — Accounts"
cmd cat /etc/passwd
cmd awk -F: '$3 >= 1000 && $3 < 65534 {print $0}' /etc/passwd
cmd cat /etc/shadow 2>/dev/null || echo "(no read access to /etc/shadow)"
cmd cat /etc/group

section "USERS — Logged-in & Recent Activity"
cmd w
cmd who
cmd last | head -40
cmd lastlog | grep -v "Never" | head -40
cmd lastb 2>/dev/null | head -20 || echo "(lastb not available)"

section "USERS — sudo & Privileges"
cmd cat /etc/sudoers 2>/dev/null || echo "(no read access)"
cmd ls -la /etc/sudoers.d/ 2>/dev/null || true
cmd id
cmd groups

section "USERS — SSH"
cmd cat /etc/ssh/sshd_config 2>/dev/null | grep -v "^#" | grep -v "^$" || true
for u in $(awk -F: '$3 >= 1000 && $3 < 65534 {print $1}' /etc/passwd); do
  home=$(awk -F: -v u="$u" '$1==u{print $6}' /etc/passwd)
  for ak in "$home/.ssh/authorized_keys" "$home/.ssh/authorized_keys2"; do
    [ -f "$ak" ] && { echo "--- $ak ---" >> "${REPORT}"; cat "$ak" >> "${REPORT}"; echo >> "${REPORT}"; }
  done
done

# =============================================================================
# SERVICES
# =============================================================================
section "SERVICES — systemd Units"
if has systemctl; then
  cmd systemctl list-units --type=service --all --no-pager
  cmd systemctl list-units --type=socket  --all --no-pager
  cmd systemctl list-timers --all --no-pager
fi

section "SERVICES — Service Status (key services)"
KEY_SERVICES=(ssh sshd nginx apache2 httpd mysql mariadb postgresql redis memcached \
              docker containerd kubelet cron crond atd rsyslog auditd ufw firewalld)
for svc in "${KEY_SERVICES[@]}"; do
  if has systemctl; then
    out=$(systemctl is-active "$svc" 2>/dev/null)
    echo "  ${svc}: ${out}" >> "${REPORT}"
  fi
done

section "SERVICES — Init / Legacy (rc.d)"
if [ -d /etc/init.d ]; then
  cmd ls -la /etc/init.d/
  has service && cmd service --status-all 2>/dev/null || true
fi

section "SERVICES — Firewall"
has ufw        && cmd ufw status verbose
has firewall-cmd && cmd firewall-cmd --list-all 2>/dev/null || true
has iptables   && cmd iptables -L -n -v
has nft        && cmd nft list ruleset 2>/dev/null || true

section "SERVICES — Web Server Config"
for f in /etc/nginx/nginx.conf /etc/apache2/apache2.conf /etc/httpd/conf/httpd.conf; do
  [ -f "$f" ] && { echo "--- $f ---" >> "${REPORT}"; cat "$f" >> "${REPORT}"; echo >> "${REPORT}"; }
done
[ -d /etc/nginx/sites-enabled ]  && cmd ls -la /etc/nginx/sites-enabled/
[ -d /etc/apache2/sites-enabled ] && cmd ls -la /etc/apache2/sites-enabled/

section "SERVICES — Listening Ports Summary"
cmd ss -tulpn
cmd cat /etc/services 2>/dev/null | grep -v "^#" | grep -v "^$" | head -60

# =============================================================================
# DOCKER
# =============================================================================
section "DOCKER — Version & Info"
if has docker; then
  cmd docker version
  cmd docker info
else
  echo "  Docker not found on this system." >> "${REPORT}"
fi

section "DOCKER — Images"
has docker && cmd docker images -a

section "DOCKER — Containers (all)"
has docker && cmd docker ps -a --format "table {{.ID}}\t{{.Image}}\t{{.Status}}\t{{.Names}}\t{{.Ports}}"

section "DOCKER — Networks"
has docker && cmd docker network ls
has docker && cmd docker network inspect $(docker network ls -q) 2>/dev/null || true

section "DOCKER — Volumes"
has docker && cmd docker volume ls
has docker && cmd docker volume inspect $(docker volume ls -q) 2>/dev/null || true

section "DOCKER — Compose Projects"
if has docker; then
  if docker compose version &>/dev/null 2>&1; then
    cmd docker compose ls 2>/dev/null || true
  elif has docker-compose; then
    echo "  docker-compose (v1) detected" >> "${REPORT}"
    cmd docker-compose ls 2>/dev/null || true
  fi
fi

section "DOCKER — Container Details"
if has docker; then
  for cid in $(docker ps -q 2>/dev/null); do
    echo "━━━ Container: $cid ━━━" >> "${REPORT}"
    docker inspect "$cid" >> "${REPORT}" 2>&1
    docker stats  "$cid" --no-stream >> "${REPORT}" 2>&1 || true
    docker logs   "$cid" --tail=20  >> "${REPORT}" 2>&1 || true
    echo >> "${REPORT}"
  done
fi

section "DOCKER — Daemon Config"
[ -f /etc/docker/daemon.json ] && cmd cat /etc/docker/daemon.json
has systemctl && cmd systemctl status docker --no-pager 2>/dev/null || true

# =============================================================================
# SECURITY SUMMARY
# =============================================================================
section "SECURITY — Failed Logins & Auth"
for log in /var/log/auth.log /var/log/secure; do
  [ -f "$log" ] && { echo "--- failed logins in $log ---" >> "${REPORT}"; grep -i "failed\|invalid\|error" "$log" | tail -30 >> "${REPORT}" 2>&1; }
done

section "SECURITY — SUID/SGID Binaries"
cmd find / -xdev \( -perm -4000 -o -perm -2000 \) -type f -ls 2>/dev/null | head -50

section "SECURITY — World-writable Files"
cmd find / -xdev -perm -0002 -type f -ls 2>/dev/null | grep -v "^/proc" | head -30

section "SECURITY — Open Ports vs Services"
cmd ss -tulpn

# =============================================================================
# FOOTER
# =============================================================================
{
  echo
  hr
  echo "  Report complete: ${REPORT}"
  echo "  Generated by   : ${SCRIPT_NAME}"
  echo "  Finished at    : $(date)"
  hr
} >> "${REPORT}"

echo "=================================================="
echo "  Done! Report saved to:"
echo "  ${REPORT}"
echo "=================================================="
