from sklearn.cluster import KMeans

def k_clusters(W, k):
    '''
    Input: motif adjacency matrix (W), k (number of clusters)
    Output: a dictionary mapping each node i to its assigned cluster
    '''

    # Step 1: Form the Diagonal Matrix (D) from W
    # -----------------------------------------
    # obtain the sums of all the rows of W
    row_sums = np.sum(W, axis = 1)
    
    # calculate D (to the -1/2 power) utilizing the row sums
    D = np.diag(row_sums**(-1/2))
    
    # Step 2: Calculate the normalized Laplacian matrix (L)
    # -----------------------------------------
    L = np.identity(len(row_sums)) - D@W@D
    
    # Step 3: Calculate the eigenvectors corresponding to the k lowest eigenvalues of L
    # -----------------------------------------
    # calculate the eigenvalues and eigenvectors 
    eig = np.linalg.eig(L)
    eigenvalues, eigenvectors = eig[0], eig[1]
    
    # create sorted eigenvalue, eigenvector pairs
    eigenpairs = []
    for i in np.arange(len(eigenvalues)):
        eigenpairs.append((eigenvalues[i], eigenvectors[:,i]))
    
    # keep the first k eigenvectors
    k_eigenvectors = [pair[1] for pair in sorted(eigenpairs)[:k]]

    # Step 4: Create the matrix Y where its ith row represents node i
    # -----------------------------------------
    # create a matrix by concatenating the eigenvectors together as columns
    unmodified_matrix = np.matrix(k_eigenvectors).T
    
    # obtain all the squared row sums of the unmodified matrix
    squared_row_sums = np.sum(np.square(unmodified_matrix), axis = 1)

    # create a matrix Y where the ith row corresponds to node i
    Y = unmodified_matrix / squared_row_sums
    
    # Step 5: Perform k-means clustering on the rows of Y (each representing a node)
    # -----------------------------------------
    # perform kmeans clustering on Y
    kmeans = KMeans(n_clusters = k, random_state = 0).fit(np.array(Y))
    
    # obtain the labels and the cluster centers
    cluster_labels = kmeans.labels_
    
    # create a dictionary mapping each node to its cluster
    cluster_directory = dict(zip(np.arange(1, len(cluster_labels)+1), cluster_labels))
    
    # return the dictionary as the final output
    return cluster_directory