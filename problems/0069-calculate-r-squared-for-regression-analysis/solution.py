
import numpy as np

def r_squared(y_true, y_pred):
	SSR = sum(np.subtract(y_true, y_pred)**2)
	SST = sum(np.subtract(y_true, np.mean(y_true))**2)
	reg = 1-(SSR/SST)
	return reg
	# Write your code here
	pass
