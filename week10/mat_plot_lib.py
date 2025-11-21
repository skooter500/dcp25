import matplotlib.pyplot as plt


x = [1, 2, 3, 4]
y = [10, 20, 15, 25]
y1 = [11, 2, 1, 2]

# 2. Plot (connect the dots)
plt.plot(x, y, 
         linestyle='--',    # dashed line
         alpha=0.7,         # transparency (0-1)
         label='Sales1')   # for legend
plt.plot(x, y1, label = "Sales2")
plt.legend()
plt.show()


tunes = ['Butterfly', 'Kesh', 'Silver Spear']
plays = [5, 8, 3]

plt.bar(tunes, plays)
plt.xlabel('Tune Name')
plt.ylabel('Times Played')
plt.xticks(rotation=45, ha='left')
plt.tight_layout()
plt.show()


days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
minutes = [30, 45, 20, 60, 40]

plt.plot(days, minutes, 
         color="#FF3564", 
         marker='^', 
         linewidth=10)
plt.grid(True)
plt.xlabel('Day of Week')
plt.ylabel('Practice Time (minutes)')
plt.title('My Weekly Practice Schedule')
# plt.show()

# 1. Data (can use plain Python lists)






# 3. Display (open the window)
# plt.show()
