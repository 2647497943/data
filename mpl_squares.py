import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]


plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.plot(input_values, squares, linewidth = 2)
ax.set_title("q", fontsize = 14)
ax.set_xlabel("x", fontsize = 14)
ax.set_ylabel("y", fontsize = 14)
ax.tick_params(axis = 'both', labelsize = 10)

plt.show()








