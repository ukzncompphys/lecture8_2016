import numpy
from matplotlib  import pyplot as plt
import nbody

if __name__=='__main__':
    plt.ion()
    n=2
    part=nbody.particles(m=1.0/n,npart=n)
    part.x=numpy.array([-1,1])
    part.y=numpy.array([0,0])

    part.vx=numpy.array([0,0])
    part.vy=numpy.array([-1,1])



    plt.plot(part.x,part.y,'*')
    plt.show()
    
    for i in range(0,100):
        energy=part.evolve()
        print energy
        plt.clf()
        plt.plot(part.x,part.y,'*')
        plt.draw()


