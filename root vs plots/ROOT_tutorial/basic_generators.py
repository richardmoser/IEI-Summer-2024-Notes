from ROOT import TRandom

# Create a generator object
generator = TRandom()

# A uniform random number
x_uni = generator.Rndm()
print("Uniform random number: ", x_uni)

# A Gaussian-distributed random number
mean = 10
width = 3
x_gaus = generator.Gaus(mean, width)
print("Gaussian random number: ", x_gaus)

# Exponentially distributed random number
tau = 3
x_expo = generator.Exp(tau)
print("Exponential random number: ", x_expo)
