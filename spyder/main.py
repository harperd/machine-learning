import random
from model import Model
from data import Data
from options import Options

def try_kmeans(data, options):
    """Calls kmeans num_trials times and returns the result with the
          lowest dissimilarity"""
    m = Model(data, options)
    m.cluster()
    best_model = m
    min_dissimilarity = m.dissimilarity()
    
    trial = 1
    while trial < options.get_num_trials():
        try:
            m = Model(data, options)
            m.cluster()
            model_dissimilarity = m.dissimilarity()
            
            if model_dissimilarity < min_dissimilarity:
                best_model = m
                
            min_dissimilarity = model_dissimilarity
            trial += 1
        except ValueError:
            continue #If failed, try again

    return best_model


def print_clustering(model):
    """Assumes: clustering is a sequence of clusters
       Prints information about each cluster
       Returns list of fraction of pos cases in each cluster"""
    pos_fracs = []
    clusters = model.get_clusters()
    id = 0
    
    for c in clusters:
        cluster_size = 0
        cluster_positives = 0
        for p in c.members():
            cluster_size += 1
            if p.get_label() == 1:
                cluster_positives += 1
        fracPos = cluster_positives/cluster_size
        pos_fracs.append(fracPos)
        
        print('Cluster ' + str(id) + ': Size = ' + str(cluster_size) + ', % Positive = ' +
              str(round(fracPos, 4)) + ', Variability = ' + str(round(c.variability(), 4)))

        id = id + 1
        
    print('Average Cluster Distance = ' + str(round(model.get_avc_cluster_distance(), 4)))
    print('Dissimilarity = ' + str(round(model.dissimilarity(), 4)))
        

def test_clustering(data, options, seed = 0):
    random.seed(seed)
    best_model = try_kmeans(data, options)
    print_clustering(best_model)


options = Options()
options.set_scale(True)
options.set_distance(2)
options.set_num_clusters(4)
options.set_num_trials(5)
options.set_verbose(False)
options.set_cluster_method('kmeans')

data = Data('../data/cardiacData.csv', options)
data.read()

seed = 0

options.show()

for k in (options.get_num_clusters(),):
    print('\nTest K-Means')
    test_clustering(data, options, seed)

#cluster_positives = 0
#for p in patients:
#    if p.getLabel() == 1:
#        cluster_positives += 1
#print('Total number of positive patients =', cluster_positives)