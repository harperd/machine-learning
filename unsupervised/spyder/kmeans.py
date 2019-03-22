import random
from cluster import Cluster

def cluster(options, data):
    #Get k randomly chosen initial centroids, create cluster for each
    initialCentroids = random.sample(data.get_examples(), options.get_num_clusters())
    clusters = []
    for e in initialCentroids:
        clusters.append(Cluster(options, [e]))
        
    #Iterate until centroids do not change
    converged = False
    numIterations = 0
    while not converged:
        numIterations += 1
        #Create a list containing k distinct empty lists
        newClusters = []
        for i in range(options.get_num_clusters()):
            newClusters.append([])
            
        #Associate each example with closest centroid
        for e in data.get_examples():
            #Find the centroid closest to e
            smallestDistance = e.distance(clusters[0].get_centroid())
            index = 0
            for i in range(1, options.get_num_clusters()):
                distance = e.distance(clusters[i].get_centroid())
                if distance < smallestDistance:
                    smallestDistance = distance
                    index = i
            #Add e to the list of examples for appropriate cluster
            newClusters[index].append(e)
            
        for c in newClusters: #Avoid having empty clusters
            if len(c) == 0:
                raise ValueError('Empty Cluster')
        
        #Update each cluster; check if a centroid has changed
        converged = True
        for i in range(options.get_num_clusters()):
            if clusters[i].update(newClusters[i]) > 0.0:
                converged = False
        if options.get_verbose() == True:
            print('Iteration #' + str(numIterations))
            for c in clusters:
                print(c)
            print('') #add blank line
    return clusters