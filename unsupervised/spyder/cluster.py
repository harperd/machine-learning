import pylab
from example import Example

pylab.rcParams['lines.linewidth'] = 6
#set general font size 
pylab.rcParams['font.size'] = 12
#set font size for labels on axes
pylab.rcParams['axes.labelsize'] = 18
#set size of numbers on x-axis
pylab.rcParams['xtick.major.size'] = 5
#set size of numbers on y-axis
pylab.rcParams['ytick.major.size'] = 5
#set size of markers
pylab.rcParams['lines.markersize'] = 10

class Cluster(object):
    
    def __init__(self, options, examples):
        """Assumes examples a non-empty list of Examples"""
        self.options = options
        self.examples = examples
        self.centroid = self.compute_centroid()
        
    def distance(self, other):        
        return self.centroid.distance(other.centroid)
        
    def update(self, examples):
        """Assume examples is a non-empty list of Examples
           Replace examples; return amount centroid has changed"""
        old_centroid = self.centroid
        self.examples = examples
        self.centroid = self.compute_centroid()
        return old_centroid.distance(self.centroid)
    
    def compute_centroid(self):
        vals = pylab.array([0.0]*self.examples[0].dimensionality())
        for e in self.examples: #compute mean
            vals += e.get_features()
        centroid = Example(self.options, 'centroid', vals/len(self.examples))
        return centroid

    def get_centroid(self):
        return self.centroid

    def variability(self):
        totDist = 0
        for e in self.examples:
            totDist += (e.distance(self.centroid))**2
        return totDist
        
    def members(self):
        for e in self.examples:
            yield e

    def __str__(self):
        names = []
        for e in self.examples:
            names.append(e.get_name())
        names.sort()
        result = 'Cluster with centroid '\
               + str(self.centroid.get_features()) + ' contains:\n  '
        for e in names:
            result = result + e + ', '
        return result[:-2] #remove trailing comma and space    


        
