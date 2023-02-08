def single_cluster(W):
    '''
    Input: motif adjacency matrix (W)
    Output:
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

    # Step 3: Calculate the eigenvector corrsponding to the second smallest eigenvalue of L
    # -----------------------------------------
    # calculate the eigenvalues and eigenvectors 
    eig = np.linalg.eig(L)
    eigenvalues, eigenvectors = eig[0], eig[1]

    # create sorted eigenvalue, eigenvector pairs
    eigenpairs = []
    for i in np.arange(len(eigenvalues)):
        eigenpairs.append((eigenvalues[i], eigenvectors[:,i]))
    
    # keep the eigenvector corresponding to the second smallest eigenvalue
    second_smallest_eigenvector = np.array(sorted(eigenpairs)[1][1])
    
    # Step 4: Create a vector sigma whose sorted value index i corresponds to node i
    # -----------------------------------------
    sigma = D@second_smallest_eigenvector

    # Step 5: Linear sweep for motif conductance minimization
    # obtain the sorted indices of sigma where the ith index represents node i
    sorted_sigma = sorted(list(zip(sigma, np.arange(1, len(sigma)+1))))

    # obtain the proper orderings of the row and columns
    order = np.array([x[1] for x in sorted_sigma]) - 1

    # reorder the rows and columns of the adjacency matrix
    C = W[order]
    C = C[:, order]

    # obtain the sum of each row
    row_sums = np.sum(C, 1)

    # calculate the volume of all clusters at each partition
    volumes = np.cumsum(row_sums)
    volumes_other = np.sum(np.sum(W, 0)) * np.ones((len(order))) - volumes

    # calculate the conductances at each partition
    conductances = np.cumsum(row_sums - 2 * np.sum(np.tril(C), 1)) / np.minimum(volumes, volumes_other)
    conductances = np.nan_to_num(conductances, nan = 1)

    # find the index of the minimal motif conductance
    minimum_index = np.argmin(conductances)

    # partition the cluster which achieves the minimum conductance
    optimal_cluster = np.array([x[1] for x in sorted_sigma[:minimum_index + 1]])
    return optimal_cluster