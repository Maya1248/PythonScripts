import random
import matplotlib.pyplot as plt

def sigmoid(x,derivative):
    if derivative:
        return sigmoid(x,False) * (1 - sigmoid(x,False))
    else:
        return 1 / (1 + 2.718281**-int(x))

def relu(x,derivative):
    if derivative:
        if x >= 0:
            return 1
        else:
            return 0
    else:
        if x >= 0:
            return x
        else:
            return 1


def activation(param,func="sigmoid",deriv=False):
    if func == "sigmoid":
        return sigmoid(param,deriv)
    elif func == "relu":
        return relu(param,deriv)
    else:
        return "Not a function..."


class neuralnet:
    def __init__(self,inp,hid,out,act):
        self.w1 = []
        self.w2 = []
        self.w3 = []
        self.inpSize = inp
        self.hidSize = hid
        self.outSize = out
        self.hid1 = []
        self.hid2 = []
        self.out = []

        self.act = act

        
        for i in range(hid):
            self.w1.append([])
            self.hid1.append(1)
            for j in range(inp):
                self.w1[i].append(random.randint(0,10))

        for i in range(hid):
            self.w2.append([])
            self.hid2.append(1)
            for j in range(hid):
                self.w2[i].append(random.randint(0,10))

        for i in range(out):
            self.w3.append([])
            self.out.append(1)
            for j in range(hid):
                self.w3[i].append(random.randint(0,10))


    def predict(self,inp):
        if "list" not in str(type(inp)):
            return "Input must be a list"
        if len(inp) != self.inpSize:
            return "Invalid input size"


        for i in range(len(self.w1)):
            neuron = 0
            for j in range(len(self.w1[i])):
                neuron += inp[j] * self.w1[i][j]
            self.hid1[i] = activation(neuron,self.act)

        for i in range(len(self.w2)):
            neuron = 0
            for j in range(len(self.w2[i])):
                neuron += self.hid1[j] * self.w2[i][j]
            self.hid2[i] = activation(neuron,self.act)

        for i in range(len(self.w3)):
            neuron = 0
            for j in range(len(self.w3[i])):
                neuron += self.hid2[j] * self.w3[i][j]
            self.out[i] = activation(neuron,self.act)
            
        return self.out


    def train(self,inp,corr,RoC=1):
        if "list" not in str(type(inp)) or "list" not in str(type(corr)):
            return "Must be a list"
        if len(inp) != self.inpSize or len(corr) != self.outSize:
            return "Invalid size"

        out_err = []
        hid2_err = []
        hid1_err = []
        
        for i in range(self.outSize):
            out_err.append(0)

        out = self.predict(inp)
        for i in range(self.outSize):
            out_err[i] = corr[i] - out[i]

        
        for i in range(self.hidSize):
            neuron_error = 0
            hid2_err.append(1)
            for j in range(self.outSize):
                neuron_error += out_err[j] * activation(out[j],self.act,True) * self.w3[j][i]
            hid2_err[i] = neuron_error

        for i in range(self.hidSize):
            neuron_error = 0
            hid1_err.append(1)
            for j in range(self.hidSize):
                neuron_error += hid2_err[i] * activation(self.hid2[j],self.act,True) * self.w2[j][i]
            hid1_err[i] = neuron_error


        for i in range(self.inpSize):
            for j in range(self.hidSize):
                self.w1[j][i] += hid1_err[j] * RoC * inp[i]

        for i in range(self.hidSize):
            for j in range(self.hidSize):
                self.w2[j][i] += hid2_err[j] * RoC * self.hid1[i]
        
        for i in range(self.hidSize):
            for j in range(self.outSize):
                self.w3[j][i] += out_err[j] * RoC * self.hid2[i]
                

    def quickTrain(self,x,y,roc=10**-8):
        # delete after
        x = [i for i in range(-10,11)]
        y = [i**2 for i in range(-10,11)]
        
        for _ in range(1000):
            for i in range(len(x)):
                self.train([x[i]],[y[i]],roc)

    def quickCompare(self):
        x = [i for i in range(-10,11)]
        p = [self.predict([i])[0] for i in range(-10,11)]

        plt.plot(x,p)
        plt.show()

"""
n = neuralnet(1,10,1,"relu")
for _ in range(100):
    n.quickTrain(0,0)
n.quickCompare()
"""
