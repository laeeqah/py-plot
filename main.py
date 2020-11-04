import matplotlib.pyplot as plt
import numpy as np


temp = np.array([220, 330, 190, 340, 410, 445, 415])
soup_sale = np.array([14.2,16.5,11.8,15.3,18.8,22.5,19.5])

plt.scatter(soup_sale, temp)

plt.plot( soup_sale,temp,'o')
m, b = np.polyfit( soup_sale,temp, 1)
plt.plot(soup_sale, m * soup_sale + b, color= "b")
plt.xlim([0,22.5])
plt.ylabel([0,450])

plt.title("Soup sales in relation to temperature")
plt.xlabel("Temperature")
plt.ylabel("Price in (R)")

plt.show()
