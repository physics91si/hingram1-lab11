import string 
import numpy as np
# First Task 


first10 = [x for x in list(string.ascii_lowercase)
 if list(string.ascii_lowercase).index(x) < 10]

# print (first10)


# Second Task
first10 = [x for x in list(string.ascii_lowercase)
 if list(string.ascii_lowercase).index(x) < 10 and 
 list(string.ascii_lowercase).index(x) != 6 -1 ]

# print (first10)

# Third Task 

first10 = [x for x in np.arange(5) for x in list(string.ascii_lowercase)
 if list(string.ascii_lowercase).index(x) < 10 and 
 list(string.ascii_lowercase).index(x) != 6 -1 ]



print (first10)

