import pint
import icontract

ureg = pint.UnitRegistry()
def assert_compatible_with(a,b):
   a.to(b.units) 

class Drone:

    num_drone:int
    charge_utile:int
    autonomie: pint.Quantity=0*ureg.second
    statut :bool
    coordonnee_depart:int

    def __init__(self, num_drone:int, charge_utile:int, autonomie: pint.Quantity,statut :bool,coordonnee_depart:int):
        pass

    @icontract.ensure(lambda self,result:result>0*ureg.second)
    def get_autonomy(self):
        pass
    def get_plan_livraison(self):
        pass
    def get_etat_mission(self):
        pass

class Etat:
    def __init__(self):
        pass

class IODeliv:
    def __init__(self):
        pass


class Operateur_drone:
    def __init__(self, num_ope):
        self.num_ope=num_ope
        
        pass

class Zone:
    num_zone:int
    population : int
    delivrer: bool
    prio:int

    def __init__(self, num_zone:int, population : int, delivrer: bool, prio:int):
        pass



        
        