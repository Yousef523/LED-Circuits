import pint
from pint import UnitRegistry
ureg = UnitRegistry()


r= 5.0 * ureg.ohm
i= 2.5 * ureg.milliampere
v= (r*i).to('volt')

resistance= v/i
resistor_quantity=3

def resistance (i,v):
    resistance= (v/i).to('ohm')
    print ("resistance:",r.to('ohm'))
    

def voltage (r,i):
    v= (r*i).to('volt')
    print("volt:",v.to('volt'))
    print("millivolt:",v.to('millivolt'))
    
    
    
    
    
def current (v,r):
    i=(v/r).to('milliampere')
    print ("Current:",i)



def serial_resistance(r):
    serial_resistance=(r*resistor_quantity).to('ohm')
    print("serial resistance:",serial_resistance.to('ohm'))
    


  
    
            







    
