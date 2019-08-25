class Options(object):
    def __init__(self):
        self.set_distance(2)
        self.set_num_clusters(0)
        self.set_scale(False)
        self.set_num_trials(0)
        self.set_verbose(False)
        self.set_cluster_method('knn')
        
    def show(self):
        print('=== Options ===')
        print('p = ' + str(self.get_distance()))
        print('k = ' + str(self.get_num_clusters()))
        print('trials = ' + str(self.get_num_trials()))
        print('scale = ' + str(self.do_scale()))
        print('cluster method = ' + self.get_cluster_method())
                    
    def set_distance(self, p):
        self.p = p
        
    def get_distance(self):
        return self.p
        
    def set_num_clusters(self, k):
        self.k = k
        
    def get_num_clusters(self):
        return self.k
    
    def set_scale(self, scale):
        self.scale = scale
        
    def do_scale(self):
        return self.scale
    
    def set_num_trials(self, trials):
        self.trials = trials
        
    def get_num_trials(self):
        return self.trials
    
    def set_verbose(self, verbose):
        self.verbose = verbose
        
    def get_verbose(self):
        return self.verbose
    
    def set_cluster_method(self, method):
        self.cluster_method = method
        
    def get_cluster_method(self):
        return self.cluster_method
    