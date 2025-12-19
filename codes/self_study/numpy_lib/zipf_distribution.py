"""
used to sample data based on zipf's law.

a - distribution parameter.
size - The shape of the returned array.
"""

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.zipf(a=2, size=(2, 3))
print(x)

x = random.zipf(a=2, size=1000)
sns.displot(x[x<10])

plt.show()