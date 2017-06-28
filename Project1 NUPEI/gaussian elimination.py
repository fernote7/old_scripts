__author__ = 'fernando.ormonde'

#!/bin/python
#gauss.py
#written by Michael Harris
#12.2.2007
#This script solves systems of linear equations using Gauss Reduction
#The system is given by the coefficient|constant array a
#It will not solve ill-conditioned systems

print("Importing...")
from numpy import *
print("Running...")
import matplotlib.pyplot as plt

#define coefficient constant arrays
#a=array([[1.,1.,1.,-1.],[8.,4.,2.,-2.],[27.,9.,3.,1.]])

a = array([[1.,1.,1.],[8.,4.,2.],[27.,9.,3.]])




#creates arrays to use in the for() loops
rows=a.shape[0]
columns=a.shape[1]

answer=zeros(rows)

print(a)
print("-----")

#eliminate variables
for i in arange(0,columns): #variable to eliminate
   for j in arange(i+1,rows): #rows to eliminate said variable from
     tmp=a[i]*(-a[j][i]/a[i][i]) #multiply row
     a[j]=tmp+a[j] #add

#back substitute
for i in (arange(rows).shape[0]-arange(rows)-1):

   #subtract terms
   if(i<columns-2):
     a[i][columns-1]=a[i][columns-1]-(sum(a[i])-a[i][i]-a[i][columns-1])

   #calculate ith variable
   answer[i]=a[i][columns-1]/(a[i][i])
   #substitute variable by
   #multiply rows starting with i-1, column i by answer[i]
   for j in arange(0,i):
     a[j][i]=a[j][i]*answer[i]

#print out the answer

print(answer)


print("-----")

import numpy as np
from matplotlib.pyplot import *

x = [0., 1., 2., 3.]

y = [1., 0., -1., 2.]

coefficients = np.polyfit(x, y, 3)
polynomial = np.poly1d(coefficients)
ys = polynomial(x)
print coefficients


print("-----")

print polynomial

plot(x, polynomial(x), 'o')
plot(x, ys)
ylabel('y')
xlabel('x')
xlim(-10,10)
ylim(-10,10)

