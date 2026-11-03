# Agglomerative Hierarchical Clustering
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

iris = load_iris()

data = pd.DataFrame(iris.data, columns=iris.feature_names)

print("First 5 records:")
print(data.head())

Z = linkage(data, method="ward")

plt.figure(figsize=(10, 6))

dendrogram(Z, truncate_mode="level", p=5)

plt.title("Dendrogram - Agglomerative Hierarchical Clustering")
plt.xlabel("Data Points")
plt.ylabel("Distance")
plt.show()

model = AgglomerativeClustering(
    n_clusters=3,
    linkage="ward"
)
clusters = model.fit_predict(data)

data["Cluster"] = clusters

print("\nClustered Data:")
print(data.head(10))

print("\nNumber of data points in each cluster:")
print(data["Cluster"].value_counts().sort_index())

plt.figure(figsize=(8, 6))
plt.scatter(
    data.iloc[:, 0],
    data.iloc[:, 1],
    c=data["Cluster"],
    cmap="rainbow",
    s=50
)
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Agglomerative Hierarchical Clustering")
plt.show()