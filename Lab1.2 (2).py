from matplotlib.pyplot import plot, show
from numpy import zeros, sin, random, pi

n = 6
ωгр = 1200
N = 64

def generate_signal():
	x = zeros(N)
	for i in range(n):
		amplitude = random.uniform(0.0, 1000.0)
		phase = random.uniform(-pi / 2, pi / 2)
		ω = ωгр / n * (i + 1)
		for t in range(N):
			x[t] += amplitude * sin(ω * t + phase)
	return x

def M(signal):
	res = 0
	for i in range(N):
		res += signal[i]
	return res / N

def D(signal):
	math_expectation = M(signal)
	res = 0
	for i in range(N):
		res += (signal[i] - math_expectation) ** 2
	return res / (N - 1)

def cor(x, y, τ):
	M1 = M(x)
	M2 = M(y)
	res = 0
	for t in range(N - τ):
		res += (x[t] - M1) * (y[t + τ] - M2)
	return res / (N - 1)

def autocor(x, τ):
	return cor(x, x, τ)

D_vals = []
for i in range(64, 1024):
	N = i
	random_signal = generate_signal()
	D_vals.append(D(random_signal))

plot(range(64, 1024), D_vals)
show()