import numpy as np
list=np.random.normal(size=1000)

print("Normal Distribution")
print("Mean",np.average(list))
print("Variable",np.var(list))
print("SD:",np.std(list))

print()
print("Poisson Distribution")
list=np.random.poisson(size=1000)
print("Mean",np.average(list))
print("Variable",np.var(list))
print("SD:",np.std(list))