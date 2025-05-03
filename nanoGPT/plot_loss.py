import matplotlib.pyplot as plt

layers = [2, 3, 5, 7]
losses = [1.9153, 1.8895, 1.9006, 1.8964] 

plt.plot(layers, losses, marker='o')
plt.xlabel('Number of Layers')
plt.ylabel('Validation Loss at Iteration 2000')
plt.title('Loss vs Number of Layers (Heads = 5)')
plt.grid(True)
plt.savefig('figures/loss_plot.png')
plt.show()