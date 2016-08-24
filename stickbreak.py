import numpy as np

def stickbreak(alpha):
    weights = np.random.beta(1, alpha,1)
    i=1
    while 1-sum(weights)>0.001:
        i=i+1
        b = np.random.beta(1, alpha)
        weights=np.append(weights,b * (1.0 - sum(weights[0:i-1])))
        print((weights))
        if sum(weights)>=1.0:        
            break
    return weights
