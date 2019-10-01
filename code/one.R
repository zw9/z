#!/usr/bin/env Rscript
# fn;fin

#direct output to a file 
sink(paste("/data/datalake/rptR/", fn), append=FALSE, split=FALSE)
#print(args)
print(fin)
print(fn)

mydata <- read.table(fin, header=TRUE, nrows=100, sep="," , stringsAsFactors=FALSE)

#print(mydata)

# sapply(mydata, mean, na.rm=TRUE)

print("# list objects in the working environment")
print('ls()')
print(ls())

print("# list the variables in mydata")
print('names(mydata)')
print(names(mydata))

print('# list the structure of mydata')
print(str(mydata))

#print('# list levels of factor v1 in mydata')
#levels(mydata$v1)

for (object in names(mydata)){
#print("# dimensions of an object")
print(dim(object))

# class of an object (numeric, matrix, data frame, etc)
print(class(object))
}
# print mydata 
#mydata

print('# print first 10 rows of mydata')
print(head(mydata, n=10))

print('# print last 5 rows of mydata')
print(tail(mydata, n=5))

#t(mydata)

