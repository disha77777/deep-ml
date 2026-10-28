import math

def normal_pdf(x, mean, std_dev):	
	variance = std_dev**2
	first = 1/(math.sqrt((2*math.pi*variance)))
	second = math.exp(-1*((x-mean)**2)/(2*variance))
	val = first*second
	"""
	Calculate the probability density function (PDF) of the normal distribution.
	:param x: The value at which the PDF is evaluated.
	:param mean: The mean (μ) of the distribution.
	:param std_dev: The standard deviation (σ) of the distribution.
	"""
	# Your code here
	pass
	return round(val,5)