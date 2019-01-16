class Example(object):

    def __init__(self, options, name, features, label=None):
        # Assumes features is an array of floats
        self.options = options
        self.name = name
        self.features = features
        self.label = label

    def dimensionality(self):
        return len(self.get_features())

    def get_features(self):
        return self.features[:]

    def get_label(self):
        return self.label

    def get_name(self):
        return self.name
    
    def distance(self, other):
        # Minkowski where p = 2
        dist = 0
        p = self.options.get_distance()
        v1 = self.get_features()
        v2 = other.get_features()
        
        for i in range(len(v1)):
            dist += abs(v1[i] - v2[i])**p
            
        return dist**(1/p)

    def __str__(self):
        return self.name + ':' + str(self.features) + ':' \
               + str(self.label)
