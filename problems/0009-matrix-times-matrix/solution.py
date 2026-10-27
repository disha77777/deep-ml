import numpy as np
def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:  
              if np.array(a).shape[1] == np.array(b).shape[0]:              
                c = np.dot(a,b)
                return c
              else: 
                return -1

