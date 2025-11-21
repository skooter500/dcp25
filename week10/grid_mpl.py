import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

x = ["Arsenal", "Leixlip Utd", "Manchester", "Barcelona"]
y1 = [3, 24, 17, 22]

categories = ["Car", "Bus", "Bike", "Walk"]
values = [10, 8, 8, 1]


ax1.plot(x, y1, color='red')
ax1.set_title('First Plot')
ax2.bar(categories, values, color='blue')
ax2.set_title('Second Plot')
plt.tight_layout()
plt.show()

'''
x = ["Arsenal", "Leixlip Utd", "Manchester", "Barcelona"]
y1 = [3, 24, 17, 22]
y2 = [9, 10, 8, 17]
y3 = [3, 24, 17, 22]
y4 = [9, 10, 8, 17]


fig, axes = plt.subplots(2, 2, figsize=(10, 8))

axes[0, 0].plot(y1)  # top-left
axes[0, 1].plot(y2)  # top-right
axes[1, 0].plot(y3)  # bottom-left
axes[1, 1].plot(y4)  # bottom-right

plt.tight_layout()
plt.savefig("../grid1.png")
plt.show()
'''