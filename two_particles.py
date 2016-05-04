import numpy
from matplotlib import pyplot as plt
#let's start two partcles in what should be a circular orbit
x0=0;y0=0;vx0=0;vy0=0.5
x1=1;y1=0;vx1=0;vy1=-0.5;

#for simplicity, let's assume G&m are all equal to 1
dt=0.1
oversamp=400
dt_use=dt/oversamp
tmax=50
nstep=numpy.ceil(tmax/dt)
mypot=numpy.zeros(nstep)
mykin=numpy.zeros(nstep)
myr=numpy.zeros(nstep)

plt.ion()
step=0
for t in numpy.arange(0,tmax,dt):
    for ii in range(0,oversamp):
        dx=x0-x1
        dy=y0-y1
        rsquare=dx*dx+dy*dy
        r=numpy.sqrt(rsquare)
        r3=r*r*r
    #calculate the x and y  force components
        fx0=dx/r3;
        fy0=dy/r3
    #forces on particle 1 must be opposite of particle 0
        fx1 =-fx0
        fy1 =-fy0
    #update particle positions
        x0 +=dt_use*vx0
        y0 +=dt_use*vy0
        vx0 +=-dt_use*fx0
        vy0 +=-dt_use*fy0
    
        x1+= dt_use*vx1
        y1+=dt_use*vy1
        vx1 -= dt_use*fx1
        vy1 -= dt_use*fy1
    

    #plt.clf()
    plt.plot(x0,y0,'rx')
    plt.plot(x1,y1,'b*')
    plt.ylim(-1.5,1.5)
    plt.xlim(-1,2)
    
    plt.draw()
    pot=-1.0/r
    kin=0.5*(vx0*vx0+vy0*vy0+vx1*vx1+vy1*vy1)
    mypot[step]=pot
    mykin[step]=kin
    myr[step]=r
    step+=1
    print 'kin and pot are ' + repr(rsquare) + '  ' + repr(kin) + '   ' + repr(pot) + '  ' + repr(pot+kin) + '  ' + repr(r)
