#echo \# $0 $1 $2
fm=$1_$(uname -n)_$(basename $0 | cut -d. -f1)
fm=${fm//\//_}
#echo $fm

(
find $1 -type f
)>"${fm}.txt"

: '
#listing of full filenames for each hierachy

# rm $rptfn/*
 
find ~  -mindepth 1  -maxdepth 1 -type d  -exec bash make_fn.sh "{}" \;

bash $fn/make_ext_awk.sh



# su
find /   -mindepth 1  -maxdepth 1 -type d  -exec bash $fn/make_fn.sh {} \;
#echo \# $0 $1 $2
'
