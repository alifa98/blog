import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.svm import SVC

# Step 1: Generate a simple two-class dataset
X, y = make_blobs(n_samples=100,
                  centers=2,
                  n_features=2,
                  random_state=13,
                  cluster_std=1.5)

# Step 2: Train the SVM classifier
clf = SVC(kernel='linear', C=1.0)
clf.fit(X, y)

# Retrieve the coefficients (w) and intercept (b) from the model
w = clf.coef_[0]
b = clf.intercept_[0]

# Step 3: Plot the data points
plt.figure(figsize=(8,6))
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.coolwarm, edgecolors='k')
plt.title("SVM with Linear Kernel - Support Vectors Highlighted")

# Step 4: Plot the decision boundary
# The decision boundary is given by w.x + b = 0
# Solve for x2: x2 = (-w[0]*x1 - b) / w[1]
x_min, x_max = plt.xlim()
x_vals = np.linspace(x_min, x_max, 200)
y_vals = (-w[0]*x_vals - b) / w[1]

plt.plot(x_vals, y_vals, 'k-', label='Decision boundary')

# Step 5: Plot the margin lines
# The margins correspond to w.x + b = ±1
margin = 1 / np.sqrt(np.sum(w**2))
y_vals_up = y_vals + (w[0]/w[1])*margin
y_vals_down = y_vals - (w[0]/w[1])*margin

plt.plot(x_vals, y_vals_up, 'k--', label='Margin')
plt.plot(x_vals, y_vals_down, 'k--')

# Step 6: Highlight the support vectors
sv = clf.support_vectors_
plt.scatter(sv[:,0], sv[:,1], s=100, facecolors='none', edgecolors='green', linewidths=2, label='Support Vectors')

plt.legend()
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()
