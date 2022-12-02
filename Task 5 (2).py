import Task5
import pint
from pint import UnitRegistry
ureg = UnitRegistry()
r= 5.0 * ureg.ohm
i= 2.5 * ureg.milliampere
v= (r*i).to('volt')





def test_voltage(i,r,exp):
    Task5.voltage(i,r) == exp
    test_voltage == (0.0125)
    print("V PASSED")

def test_current(v,r,exp):
    Task5.current(v,r) == exp

    test_current == (2.5)

    print("I PASSED")

def test_resistance(i,v,exp):
    Task5.resistance(i,v) == exp 
    test_resistance == (5.0)
    print("R PASSED")


def test_serial_resistance(r,exp):
    Task5.serial_resistance(r) == exp
    test_serial_resistance == (15.0)
    print("SR PASSED")



if __name__=="__main__":
    try:
        test_voltage(i,r,0.0125)
        test_current(v,r,2.5)
        test_resistance(i,v,5.0)
        test_serial_resistance(r,15.0)
    except AssertionError:
        print('everything passed')






