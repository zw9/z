
ls -lTR .

ls -lTR . | awk '{print "\""$10"\""";""\""$6" "$7", "$9"\""";""\""$5"\""}' > ls_list.csv


