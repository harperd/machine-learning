import kmeans

class Model(object):
    def __init__(self, data, options):
        self.options = options
        self.data = data
        self.clusters = []

    def dissimilarity(self):
        """Assumes clusters a list of clusters
           Returns a measure of the total dissimilarity of the
           clusters in the list"""
        totDist = 0
        for c in self.clusters:
            totDist += c.variability()
        return totDist
    
    def get_clusters(self):
        return self.clusters
    
    def get_avc_cluster_distance(self):
        total=0
        avg=0
        num_compares=len(self.clusters) * ( self.options.get_num_clusters() - 1 )
        
        for i in range(len(self.clusters)):
            for c in range(len(self.clusters)):
                if i != c:
                    total = self.clusters[i].distance(self.clusters[c])
                    
        if total > 0:
            avg = total / num_compares
            
        return avg
    
    def cluster(self):
        method = self.options.get_cluster_method()
        
        if method == 'kmeans':
            self.clusters = kmeans.cluster(self.options, self.data)
        else:
            raise Exception('Unknown cluster methiod: ' + method)
    

               

