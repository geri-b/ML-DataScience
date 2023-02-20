import pandas as pd
import numpy as np

df = pd.read_csv("train.csv")
labels = df['label']
labels = np.array(labels)
dataset = df.drop('label', axis = 1)


def PCA(data, no_components):
    #Center Data
    data_C = data - np.mean(data, axis = 0)
    #Covariance Matrix
    cov_mat = np.cov(data_C, rowvar=False)
    #Eigen Values and Vectors
    eigen_values, eigen_vectors = np.linalg.eig(cov_mat)
    #Sort
    sorted_idx = np.argsort(eigen_values)[::-1]
    sorted_eigenval = eigen_values[sorted_idx]
    sorted_eigenvec = eigen_vectors[:,sorted_idx]
    #Select subset
    eigen_vector_subset = sorted_eigenvec[:, 0:no_components]
    #Data Transformation
    data_Reduced = np.dot(eigen_vector_subset.T, data_C.T).T

    return data_Reduced, data_Reduced.shape, sorted_eigenval

data_reduced, dimensions, eigen_values = PCA(dataset, 100)
finalReducedDataset = np.concatenate((labels.reshape(42000, 1), data_reduced), axis=1)
