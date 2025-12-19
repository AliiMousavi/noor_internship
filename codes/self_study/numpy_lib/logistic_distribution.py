from numpy import random

x = random.logistic(loc=1, scale=2, size=(2, 3))
print(x)



import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.logistic(size=1000), kind="kde")
plt.show()


#Difference Between Logistic and Normal Distribution

data = {
  "normal": random.normal(scale=2, size=1000),
  "logistic": random.logistic(size=1000)
}
sns.displot(data, kind="kde")
plt.show()