import matplotlib.pyplot as plt
import numpy as np

# marks = [ 70, 45, 90, 12]
# names = ["Memphis", "Godwin", "Thnado", "Thabo"]

# numpy works with arrays!

marks = np.array([70,45,90,12])
names = np.array(["Memphis", "Godwin", "Thnado", "Thabo"])

plt.bar(names,marks)
plt.show()