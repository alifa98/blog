import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.svm import SVC

# Generate a two-class dataset
X, y = make_blobs(n_samples=100, centers=2, n_features=2, 
                  random_state=42, cluster_std=1.5)

# Define kernels to experiment with
kernels = ['linear', 'poly', 'rbf', 'sigmoid']

fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.flatten()

# Create a mesh to plot decision boundaries
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 300),
                     np.linspace(y_min, y_max, 300))

for i, kernel in enumerate(kernels):
    ax = axes[i]
    # Train SVM with given kernel
    clf = SVC(kernel=kernel, C=1.0, gamma='scale', degree=3)
    clf.fit(X, y)

    # Evaluate the decision function on the grid
    Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    # Plot contours for decision function
    # 0 contour line is the decision boundary
    # -1 and 1 lines are the margins
    ax.contour(xx, yy, Z, levels=[-1, 0, 1], alpha=0.7, 
               linestyles=['--', '-', '--'], colors='k')
    
    # Plot the training points
    ax.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.coolwarm, 
               edgecolors='k', s=50)
    
    # Highlight support vectors
    sv = clf.support_vectors_
    ax.scatter(sv[:, 0], sv[:, 1], s=100, facecolors='none', 
               edgecolors='green', linewidths=2, label='Support Vectors')

    ax.set_title(f'SVM with {kernel} kernel')
    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')
    ax.legend(loc='best')

plt.tight_layout()
plt.show()
