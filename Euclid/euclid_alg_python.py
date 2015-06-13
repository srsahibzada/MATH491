import numpy as np
import random
from collections import defaultdict
import collections
import matplotlib.pyplot as plt

#TEST TO SEE

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

def f(x):
     y = 1.618*x
     return y
    
def main():
     directory = []
     x = []
     y = []
     dictionary = defaultdict(int)
     for q in range(1,10**2):
          for p in range(q,10**2):
               d = gcd_iter(p,q)
               directory += [[p,q,d]]
               dictionary[str(d)] += 1
     
     '''for i in range(0,50000):
          q = random.randint(0,10**10)
          
          p = random.randint(q,10**10) 


          d  = gcd_iter(p, q)
          
          directory += [[p,q,d]]
          
          dictionary[str(d)] += 1'''


          
     longest_gcds = []
     
     shortest_gcds = []
     
     checkmax = []
     
     x1 = []
     x2 = []
     x3 = []
     x4 = []
     x5 = []
     x6 = []     
     x7 = []
     x8 = []
     x9 = []     
     x10 = []
     x11 = []
     x12 = []    
     x13 = []
     x14 = []
     x15 = []
     
     y1 = []
     y2 = []
     y3 = []
     y4 = []
     y5 = []
     y6 = []     
     y7 = []
     y8 = []
     y9 = []     
     y10 = []
     y11 = []
     y12 = []    
     y13 = []
     y14 = []
     y15 = []      
     
     
     for i in directory:
          checkmax += [i[2]]
          
     maximum_iterations = max(checkmax)
     minimum_iterations = min(checkmax)
     print
     checkmax = sorted(set(checkmax))
     
     '''s1 = checkmax[-1]
     s2 = checkmax[-2]
     s3 = checkmax[-3]
     s4 = checkmax[-4]
     s5 = checkmax[-5]
     s6 = checkmax[5]
     s7 = checkmax[6]
     s8 = checkmax[7]
     s9 = checkmax[8]
     s10 = checkmax[9]
     s11 = checkmax[10]
     s12 = checkmax[11]
     s13 = checkmax[12]
     s14 = checkmax[13]
     s15 = checkmax[14]
     x_667 = []
     y_667 = []  
     
     for i in directory:
          x_667 += [i[0]]
          y_667 += [i[2]]'''


     almost_longest = []
     
     print 
     
     for i in directory:
          if i[2] == maximum_iterations:
               longest_gcds += [i]
          if i[2] == minimum_iterations:
               shortest_gcds += [i]
          if (i[2] == checkmax[-2]) or (i[2] == checkmax[-3]) or (i[2] == checkmax[-4]):
               almost_longest +=[i]
              
          '''if i[2] == s1:
               x1 += [i[0]]
               y1 += [i[1]]
               
          if i[2] == s2:
               x2 += [i[0]]
               y2 += [i[1]]
               
          if i[2] == s3:
               x3 += [i[0]]
               y3 += [i[1]]
          
          if i[2] == s4:
               x4 += [i[0]]
               y4 += [i[1]]      
          if i[2] == s5:
               x5 += [i[0]]
               y5 += [i[1]]    
          if i[2] == s6:
               x6 += [i[0]]
               y6 += [i[1]]          
          if i[2] == s7:
               x7 += [i[0]]
               y7 += [i[1]]  
          if i[2] == s8:
               x8 += [i[0]]
               y8 += [i[1]]          
          if i[2] == s9:
               x9 += [i[0]]
               y9 += [i[1]]
               
          if i[2] == s10:
               x10 += [i[0]]
               y10 += [i[1]]
          
          if i[2] == s11:
               x11 += [i[0]]
               y11 += [i[1]]      
          if i[2] == s12:
               x12 += [i[0]]
               y12 += [i[1]]    
          if i[2] == s13:
               x13 += [i[0]]
               y13 += [i[1]]          
          if i[2] == s14:
               x14 += [i[0]]
               y14 += [i[1]]  
          if i[2] == s15:
               x15 += [i[0]]
               y15 += [i[1]]'''               
                    
     
               
          
     print
     
     print "The following p's and q's return the largest number of iterations:\n"
     for i in longest_gcds:
          print  "gcd(" + str(i[0]) + ", " + str(i[1]) + ")  |  Iterations:" + str(i[2])
          
     print "\n---------------------------------------------------------\n"
     
     print "The following p's and q's return the shortest number of iterations:\n"
     for i in shortest_gcds:
          print  "gcd(" + str(i[0]) + ", " + str(i[1]) + ")  |  Iterations:" + str(i[2])
     
     '''print "\n---------------------------------------------------------\n"
          
     print "The following p's and q's return a large number of iterations:\n"
     
     avg = 0.0
     k = 0
     
     for i in almost_longest:
          avg += float(i[0])/float(i[1])
          print  "gcd(" + str(i[0]) + ", " + str(i[1]) + ") | Ratio p/q: " +str(float(i[0])/float(i[1])) +" |  Iterations: " + str(i[2])
          k = k + 1
          
     avg = avg/k
     print "Average p/q: " + str(avg)'''
     
     



     for i in dictionary:
          x += [int(i)]
          y += [dictionary[i]]


     #t1 = np.arange(0.0, 100000.0, 10)
     
     
                                                                                          
     colors = np.random.rand(15)
     fig = plt.figure()
     ax = plt.subplot(111)
     ax.bar(x,y,1)
     '''#ax.scatter(x_667,y_667)
     
     ax.scatter(x1,y1, c = 'b')
     ax.scatter(x2,y2, c = 'g')
     ax.scatter(x3,y3, c = 'r')
     ax.scatter(x4,y4, c = 'c')
     ax.scatter(x5,y5, c= 'm')
     ax.scatter(x6,y6, c='r')
     ax.scatter(x7,y7,c= 'c')
     ax.scatter(x8,y8, c='c')
     #ax.scatter(x9,y9, c= 'm')
     #ax.scatter(x10,y10, c='m')
     #ax.scatter(x11,y11, c= 'y')
     #ax.scatter(x12,y12, c= 'y')
     #ax.scatter(x13,y13, c='k')
     #ax.scatter(x14,y14,c= 'k')
     #ax.scatter(x15,y15,c='w')
     plt.plot(t1,f(t1), 'k')'''

     
     plt.xlabel("Iterations")
     plt.ylabel("Frequency")
     plt.title("Iterations Frequency of all pairs of the gcd(p,q) such that q < p < 100")
     plt.show()
     
main()