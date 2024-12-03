from array import *

def maxsubarraysum(a, a_size):

 max = 0
 cmax = 0
 for i in range(0, a_size):
   cmax = cmax + a[i] 
   if(max < cmax):
     max =cmax
   if(cmax <0 ):
     cmax = 0
 return max      

numbers =array ("i", [1,2,3,-4,6,-7,8,16])

print(maxsubarraysum(numbers,8))
