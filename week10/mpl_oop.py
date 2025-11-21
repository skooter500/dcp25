import matplotlib.pyplot as plt


x = ["Arsenal", "Leixlip Utd", "Manchester", "Barcelona"]
y1 = [3, 24, 17, 22]
y2 = [9, 10, 8, 17]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(5, 5))

ax1.plot(x, y1)
ax1.set_title('Season 1')

ax2.plot(x, y2)
ax2.set_title('Season 2')
plt.savefig("football.svg")
plt.show()
