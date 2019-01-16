import pylab, numpy
from example import Example

class Data(object):
    def __init__(self, file, options):
        self.file = file
        self.options = options
        self.points = []

    def read(self):
        #read in data
        hrList, stElevList, ageList, prevACSList, classList = [],[],[],[],[]
        cardiacData = open(self.file, 'r')
        for l in cardiacData:
            l = l.split(',')
            hrList.append(int(l[0]))
            stElevList.append(int(l[1]))
            ageList.append(int(l[2]))
            prevACSList.append(int(l[3]))
            classList.append(int(l[4]))
        if self.options.do_scale():
            hrList = z_scale(hrList)
            stElevList = z_scale(stElevList)
            ageList = z_scale(ageList)
            prevACSList = z_scale(prevACSList)
        #Build points
        self.points = []
        for i in range(len(hrList)):
            features = pylab.array([hrList[i], prevACSList[i],\
                                    stElevList[i], ageList[i]])
            pIndex = str(i)
            self.points.append(Example(self.options, 'P'+ pIndex, features, classList[i]))
    
    def get_examples(self):
        return self.points;
        
def z_scale(vals):
    vals = pylab.array(vals)
    mean = sum(vals)/len(vals)
    sd = numpy.std(vals)
    vals = vals - mean
    return vals/sd