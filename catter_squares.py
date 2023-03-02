import matplotlib.pyplot as plt

plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.scatter(2, 4, s=200)
ax.set_title("p", fontsize=15)
ax.set_xlabel("x", fontsize=10)
ax.set_ylabel("y", fontsize=10)

ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()