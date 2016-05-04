import numpy
from matplotlib import pyplot as plt
class particle:
    def __init__(self,x=0,y=0,vx=0,vy=0):
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.fx=0
        self.fy=0
    def copy(self):
        newpart=particle(self.x,self.y,self.vx,self.vy)
        newpart.fx=self.fx
        newpart.fy=self.fy
        return newpart
    def get_forces(self,other):
        dx=self.x-other.x
        dy=self.y-other.y
        rsquare=dx*dx+dy*dy
        r=numpy.sqrt(rsquare)
        r3=r*rsquare
        myfx=dx/r3
        myfy=dy/r3
        self.fx-=myfx
        self.fy-=myfy
        other.fx+=myfx
        other.fy+=myfy
        return r
    def clear_forces(self):
        self.fx=0
        self.fy=0
    def update_simple(self,dt):
        self.x=self.x+dt*self.vx
        self.y=self.y+dt*self.vy
        self.vx=self.vx+dt*self.fx
        self.vy=self.vy+dt*self.fy
    def average_derivs(self,other):
        self.vx=0.5*(self.vx+other.vx)
        self.vy=0.5*(self.vy+other.vy)
        self.fx=0.5*(self.fx+other.fx)
        self.fy=0.5*(self.fy+other.fy)
    def get_kinetic(self):
        return 0.5*(self.vx*self.vx+self.vy*self.vy)
    def __repr__(self):
        a='x and y: ' + repr(self.x)+'  '+repr(self.y)
        b='vx and vy: ' + repr(self.vx)+'  '+repr(self.vy)
        c='fx and fy: ' + repr(self.fx)+'  '+repr(self.fy)
        return a+'\n'+b+'\n'+c
p0=particle(0,0,0,0.5*numpy.sqrt(2))
p1=particle(1,0,0,-0.5*numpy.sqrt(2))

#for simplicity, let's assume G&m are all equal to 1
dt=0.01
dprint=10
tmax=50

plt.ion()
step=0
plt.clf() 
for t in numpy.arange(0,tmax,dt):    
    p0.clear_forces()
    p1.clear_forces()
    
    r=p0.get_forces(p1)
    pot=-1.0/r
    kin=p0.get_kinetic()+p1.get_kinetic()
    
    p0_tmp=p0.copy()
    p1_tmp=p1.copy()
    p0_tmp.update_simple(dt)
    p1_tmp.update_simple(dt)

    if 1:  #do second order
        p0_tmp.clear_forces()
        p1_tmp.clear_forces()
        p0_tmp.get_forces(p1_tmp)
        
        #p0.average_derivs(p0_tmp)
        #p1.average_derivs(p1_tmp)
        p0.x+=dt*0.5*(p0.vx+p0_tmp.vx)
        p0.y+=dt*0.5*(p0.vy+p0_tmp.vy)

        p1.x+=dt*0.5*(p1.vx+p1_tmp.vx)
        p1.y+=dt*0.5*(p1.vy+p1_tmp.vy)

        p0.vx+=0.5*dt*(p0.fx+p0_tmp.fx)
        p0.vy+=0.5*dt*(p0.fy+p0_tmp.fy)

        p1.vx+=0.5*dt*(p1.fx+p1_tmp.fx)
        p1.vy+=0.5*dt*(p1.fy+p1_tmp.fy)

    else:
        p0=p0_tmp
        p1=p1_tmp
    #break
    if step%dprint==0: 
        print 'kin and pot are '  + repr(kin) + '   ' + repr(pot) + '  ' + repr(pot+kin)     
        #plt.clf()
        plt.plot(p0.x,p0.y,'rx')
        plt.plot(p1.x,p1.y,'b*')
        plt.ylim(-1.5,1.5)
        plt.xlim(-1,2)
        plt.draw()

    step+=1


