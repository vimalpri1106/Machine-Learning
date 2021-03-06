'''This k-means is a type of clustering which is more appropriately called as grouping.
This concept is mainly used to group the data base on some criteria.In our problem we 
are going to group the customers of the mall based on their annual income and spending score.
'''
#libraries to import 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#importing the datasets
datasets =pd.read_csv('Mall_customers.csv')
X=datasets.iloc[:, 3:5].values

#to perform elbow method
'''this elbow method is used to identify the no. of clusters for better results '''

from sklearn.cluster import KMeans
wcss =[]
for i in range(1,11):
    kmeans = KMeans(n_clusters = i, init='k-means++',n_init=10, max_iter=300,random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)#inbuild library to perform summation for wcss
plt.plot(range(1,11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

# Fitting K-Means to the dataset
kmeans = KMeans(n_clusters = 5, init = 'k-means++', random_state = 42)#5 clusters are found from elbow method which more efficientfor our problem
y_kmeans = kmeans.fit_predict(X)#this method is used to predict the given customer belongs to which cluster or which catagory

# Visualising the clusters
plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')
plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()








