import numpy as np
import matplotlib.pyplot as plt

# fig, ax = plt.subplots()
# ax.plot(range(5), marker = "o")

# plt.title('Title of the plot')
# plt.show()


# Other approach:
fig, ax = plt.subplots()
ax.plot(range(5), marker = "o")

ax.set_title('Title of the plot')
plt.show()

# while True:
#     year = input("Que año quieres revisar?: \n")
#     try:
#         year = int(year)
#         print("numero verificado: "+year)
#         break
#     except ValueError:
#         print("Esto no es un numero")

# print(str(year))