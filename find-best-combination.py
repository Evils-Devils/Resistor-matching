import random
import itertools
import numpy
import datetime

n = [514.0778540942,496.7414560232,472.0732050522,424.4072601704,409.2460136882,408.4173296352,231.9321105186,231.430750781,218.6019372249,178.0995388418,168.9445462362,136.4417552422,121.9462821399,121.1108118612,103.2805350339,97.2803092338,62.7868368018,61.4571400314,56.7880418689,47.6169504241,24.2862104827,19.9551113786,13.1252860209,-34.708759337,-61.7048271062,-91.699052389,-110.0229763483,-111.3648273584,-125.1888856181,-135.695479733,-152.6927317535,-162.0270041711,-166.691293552,-215.0217345033,-220.3547057103,-222.6885586522,-257.6785351264,-269.3472985624,-286.1713587821,-340.1769957897,-346.1753515891,-398.6480885447,-419.9976996356,-491.9911085258]
#44 resistors' deviation from mean in ppm, averaged over multiple measurements (sorted)

start = datetime.datetime.now()
target = 0 #value to look for
tolerance = 1 #starting tolerance, doesn't matter unless it's very small
k = 9 #size of output subset
count = 0
for subset in itertools.combinations(n, k):#try every combination of k from n
    if abs(numpy.mean(subset)-target) <= tolerance: #check if the combination is worth anything
        if abs(numpy.mean(subset)-target) != tolerance: count+=1 #stops count if the exact target is reached, but more combinations are found
        print (count) 
        print (datetime.datetime.now()-start) # elapsed time
        print (numpy.mean(subset)) # found value
        print (subset, "\n") #set that makes up the value
        tolerance = abs(numpy.mean(subset)-target) #tighten tolerance
print ("Done, the paragraph above contains the best combination of",k,"from the set.")
