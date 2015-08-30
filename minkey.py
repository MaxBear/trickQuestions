# August 30, 2015
# by: Nancy Yang
#
# This function solves the question of putting characters to key pad
# that will let user key the list number of times to type all characters
# with different frequencies

def minKey(keySize, freq):
   keys = []
   for k in keySize:
      keys.append([None]*k)
   sorted_freq = sorted(freq.iteritems(), key=lambda (k,v):(v,k), reverse=False)
   maxSize = max(keySize)
   while sorted_freq:
      (k,v) = sorted_freq.pop()
      placed = False
      for i in range(maxSize):
         for key in keys:
	    try:
	       if not key[i]:
	          key[i] = k
		  placed = True
		  break
	    except:
	       pass
	 if placed:
	    break
   print keys
   

if __name__=="__main__":
   keySize = [3, 1, 2]
   freq = {'a': 3, 'b': 3, 'c':3, 'd': 2, 'e': 1, 'f': 1}
   
   minKey(keySize, freq)
