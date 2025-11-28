import matplotlib.pyplot as plt

products = ["potatoes", "cabbages", "sausages", "porridge", "tea"]
weights = [1000, 500, 675, 100, 50]
weights1 = [10.8, 50.5, 75.3, 10.6, 501.9]


fig, axis = plt.subplots(2, 2)
axis[0,0].plot(products, weights, color='#00FF00', marker='^', linewidth=5, linestyle='--', label="Weights")
axis[0,1].bar(products, weights1)
axis[1,0].pie(weights1, labels=products)
axis[1,1].scatter(products, weights1)


# 

# plt.plot(products, weights1, color="#9900FF", marker='^', linewidth=5, linestyle='--', label="Weights1")
# plt.pie(weights1, labels=products)
# plt.hist(weights1, bins= 3, edgecolor="black")


# plt.xlabel("Products")
plt.ylabel("Weights")
plt.title("Product Weights")
plt.legend()
plt.xticks(rotation=45, ha='right')
plt.grid()
plt.show()
