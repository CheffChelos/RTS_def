from matplotlib.pyplot import plot, show
from numpy import zeros, sin, cos, random, pi
from time import time

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

def dft(signal):
	res = zeros(N)
	for p in range(N):
		sum = 0
		for k in range(N):
			angle = 2 * pi * p * k / N
			sum += signal[k] * complex(cos(angle), -sin(angle))
		res[p] = abs(sum)
	return res

def fft(signal):
	N = len(signal)
	if N == 1: return signal
	res = zeros(N)
	res_half1 = fft(signal[::2])
	res_half2 = fft(signal[1::2])
	for p in range(int(N / 2)):
		angle = 2 * pi * p / N
		turn_coef = complex(cos(angle), -sin(angle))
		res[p] = res_half1[p] + turn_coef * res_half2[p]
		res[p + int(N / 2)] = res_half1[p] - turn_coef * res_half2[p]
	return res

Ns = []
coefs = []
for i in range(1,11):
	N = 100 * i
	Ns.append(N)
	random_signal = generate_signal()
	dft_begin = time()
	dft(random_signal)
	dft_end = time()
	fft_begin = time()
	fft(random_signal)
	fft_end = time()
	coefs.append((dft_end - dft_begin) / (fft_end - fft_begin))

plot(Ns, coefs)
show()