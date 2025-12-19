from numpy import random

x = random.poisson(lam=2, size=10)
print(x)

import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.poisson(lam=2, size=1000))
plt.show()

#Difference Between Normal and Poisson Distribution

data = {
  "normal": random.normal(loc=50, scale=7, size=1000),
  "poisson": random.poisson(lam=50, size=1000)
}
sns.displot(data, kind="kde")
plt.show()