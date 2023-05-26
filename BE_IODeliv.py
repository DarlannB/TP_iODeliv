
import pint
import icontract
import math

currency_reg="""
kilogram=[currency]
"""

ureg = pint.UnitRegistry()
creg=pint.UnitRegistry(currency_reg.split('\n'))
def assert_compatible_with(a,b):
   a.to(b.units) 

@icontract.require(lambda charge_utile:charge_utile>=0)
class Drone:

    num_drone:int
    charge_utile:int #nombre de pastilles emport
    autonomie: pint.Quantity=0*ureg.second #autonomie en secondes
    statut :bool #a la base=0 en vol=1
    x:float#coordonnee_depart
    y:float

    def __init__(self, num_drone:int, charge_utile:int, autonomie:pint.Quantity,statut :bool,x:float,y:float):
        self.num_drone=num_drone
        self.charge_utile=charge_utile
        self.autonomie=autonomie
        self.statut=statut
        self.x = x
        self.y = y
        statut=0
        pass
    
    @icontract.ensure(lambda autonomie:autonomie>0*ureg.second)
    
    def get_autonomy(self):     #recupere le temps d'autonomie du drone
        pass
    def get_plan_livraison(self): # recupere le chemin a suivre pour les livraisons de pilule
        pass

class Etat:
    def __init__(self):
        pass

class IODeliv:
    def __init__(self):
        pass
    
    def get_etat_mission(Zone, Drone):
        if Drone.statut==1:
            print("Mission en cours dans la zone : ", Zone.num_zone)
        if Zone.deliver==0:
            #print("Mission partiellement achevee dans la zone : ", Zone.num_zone)
            print("Zone {} n'est pas livrée, population restante {} pax.".format(Zone.num_zone,Zone.population))
        if Zone.deliver==1:
            print("Zone {} mission completee".format(Zone.num_zone))

        pass

class Operateur_drone:
    def __init__(self, num_ope):
        self.num_ope=num_ope
        pass
    def enregistre(self):   #l'operateur doit s'enregistrer chez IODeliv
        pass


@icontract.require(lambda population: population >= 0)
class Zone:
    num_zone:int
    population:int #pint.Quantity=0*ureg.dimensionless #nombre de personnes sur zone à livrer
    delivrer: bool #livre=1 non-livre=0
    prio:int #scale from 1 to 10
    x:float  #coordonnee Zone
    y:float

    def __init__(self, num_zone:int, population:int, delivrer: bool, prio:int,x:float,y:float):
        self.num_zone=num_zone
        self.population=population
        self.delivrer=delivrer
        self.prio=prio
        self.x = x
        self.y = y
        delivrer=0
        pass
class Livraison():
    """@icontract.require(lambda population:population>=0)
    @icontract.snapshot(lambda self: self.charge_utile, name='charge_utile')
    @icontract.ensure(lambda OLD, self,charge_utile:OLD.charge_utile-Zone.population==charge_utile)""" #Ca ne marche pas :'(
    def livraison_pastilles(Zone,Drone):
        if Drone.charge_utile>=Zone.population:
            Drone.charge_utile-=Zone.population
            Zone.population=0
            Zone.deliver=1
        #print("Zone entièrement livrée")
            print("Charge utile du drone apres livraison: ",Drone.charge_utile)
        #print("deliver: ", Zone.deliver)
        else:
            Zone.deliver=0
            Zone.population-=Drone.charge_utile
            Drone.charge_utile=Zone.population-Drone.charge_utile
        #print("Zone partiellement livrée")
            print("population a livrer restante: ",Zone.population)
        #print("deliver: ", Zone.deliver)
        pass



def main():
    d=Drone(1, 15, 50,0,8,6)
    print("Charge utile : ",d.charge_utile)

    z=Zone(3, 10, 0, 5,3,5)
    print("Population initiale sur zone {} : {} ".format(z.num_zone,z.population))

    Livraison.livraison_pastilles(z,d)
    IODeliv.get_etat_mission(z,d)

main()



# APPORT PERSONNEL :) utilité : debut prblm optimisation sous contraintes
"""def DistanceCalculator(Zone,Drone):
    X1=Zone.x
    Y1=Zone.y
    X2=Drone.x
    Y2=Drone.y

    distance = math.sqrt((X2 - X1)**2 + (Y2 - Y1)**2)
    print(distance)
    return 


def main():
    d=Drone(1, 20, 50,0,0,0)
    z=Zone(3, 500, 0, 5, 6,5)
    DistanceCalculator(z,d)

main()"""