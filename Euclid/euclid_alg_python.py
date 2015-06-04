import random
from collections import defaultdict
import collections
import matplotlib.pyplot as plt

def gcd(p, q):
     while (q != 0):
          temp = q
          q = p % q
          p = temp
     return p 
          

def gcd_iter(p, q):
     i = 0
     while (q != 0):
          temp = q
          q = p % q
          p = temp
          i = i + 1
     return i

    
def main():
     directory = []
     x = []
     y = []
     dictionary = defaultdict(int)
     for i in range(0,10000):
          p = random.randint(0,10**10) + 1
          q = random.randint(0,10**10) + 1
          d  = gcd_iter(p, q)
          
          directory += [[p,q,d]]
          
          dictionary[str(d)] += 1


     longest_gcds = []
     
     checkmax = []
     
     for i in directory:
          checkmax += [i[2]]
          
     maximum_iterations = max(checkmax)
     
     for i in directory:
          if i[2] == maximum_iterations:
               longest_gcds += [i]
     print
     
     print "The following p's and q's return the largest number of iterations:\n"
     for i in longest_gcds:
          print  "gcd(" + str(i[0]) + ", " + str(i[1]) + ")  |  Iterations:" + str(i[2])
     
     
     for i in dictionary:
          x += [int(i)]
          y += [dictionary[i]]
          
          
                                                                                          
     
     fig = plt.figure()
     ax = plt.subplot(111)
     ax.bar(x,y)
     plt.xlabel("Number of Iterations to finish the Euclidean algorithm")
     plt.ylabel("Number of times the iteration amount appeared")
     plt.title("Eucidean Algorithm Iterations: for 1000 digit numbers")
     plt.show()
     
main()