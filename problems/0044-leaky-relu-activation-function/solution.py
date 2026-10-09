def leaky_relu(z: float, alpha: float = 0.01) -> float|int:
	if alpha:
		return max(alpha*z,z)
	return max(0, z)
	pass