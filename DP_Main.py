import numpy as np
import scipy.stats as sp
from stickbreak import stickbreak
import matplotlib.pyplot as plt
fig=plt.figure()
#Stick breaking and Multinomial
t = np.arange(100)
colors=['b','g','r','c','m','k','purple','teal','darkorange']
for step in range(0,6):
    cluster=[]
    alpha=np.linspace(np.finfo(float).eps,2,6)
    weights=stickbreak(alpha[3])
    weights=stickbreak(1.5)
    n=100
    R = np.random.multinomial(n,weights/sum(weights))
    ind=R[np.nonzero(R)]

#Parameters for NIW
    dof=np.linspace(2,10,6)
    lam=np.linspace(0.001,1,6)
    par=np.linspace(0.001,1,6)
    Tau=par[step]*np.identity(2)+(1-par[step])*np.ones((2,2))
    dof=dof[3]
    lam=lam[3]
    mu0=np.linspace(2,10,6)
    mu0=[mu0[step]]*2

#Generate the parameters for the MVNs. The number of parameters generated
#(max(R)) is based on the output of the stick-breaking/multinomial
    W=[]
    mu=[]
    for i in range(0,len(ind)):
        random=sp.invwishart.rvs(df=dof,scale=Tau)
        W.append(random)
        mu.append(np.random.multivariate_normal(mu0,np.squeeze(W[i])/lam))

#Select the parameters for the MVN based on the outputs of the DP
    for j in range(0,len(ind)):
        cluster.append(np.random.multivariate_normal(mu[j],W[j],ind[j]))

    fig.add_subplot(2,3,step+1)
    for i in range(0,len(ind)):      
        plt.scatter(cluster[i][:,0],cluster[i][:,1],c=colors[i])
        plt.locator_params(nbins=4)
        plt.title('gamma = '+str(par[step]))
plt.tight_layout() 
plt.show()
fig.savefig('psi.png')