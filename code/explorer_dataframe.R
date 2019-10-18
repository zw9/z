
colnames(df) #: shows the name of each column in the data frame
dim(df) #: shows the dimensions of the data frame by row and column
dim(df)[1] #: shows the dimensions of the data frame by row and column
ls(df)
ncol(df)
nrow(df)

str(df) #: shows the structure of the data frame
names(df)
summary(df)
print(summary(df)) #: provides summary statistics on the columns of the data frame
#display(df) #: shows a spreadsheet-like display of the entire data frame
print(head(df)) #: shows the first 6 rows of the data frame
print(tail(df)) #: shows the last 6 rows of the data frame

ls() # list objects in the working environment

class(df) # class of an object (numeric, matrix, data frame, etc)
library(Hmisc)
describe(df)

library(pastecs)
stat.desc(df) 

library(psych)
describe(df)

args <- commandArgs(trailingOnly=FALSE)
print(args)
#setwd(args[1])
 