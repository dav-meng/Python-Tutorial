import Testmodule
#import module
import platform

Testmodule.greeting("The new guy")

x=Testmodule.person1["age"]
y=platform.system()
f=dir(platform)

print(y)
print(x)
print(f)
p=platform._Processor()
print(p)

#Class example
# 
class CharacterDesgin:
    character_version = 1.0
    def __init__(self,type,speed,armour,dmg):
        self.type=type
        self.speed = speed
        self.armour=armour
        self.dmg=dmg
    def Added_armour(self):
        self.armour*=1.5
    def __str__(self):
   #     """Return a string representation of the character's stats."""#
        return(f"Type: {self.type}, Speed: {self.speed}, Armour: {self.armour}, Damage: {self.dmg}")
warrior = CharacterDesgin(type="Heavy",speed=20,armour=60,dmg=50)
ninja = CharacterDesgin(type="Light",speed=80,armour=10,dmg=30)
print(warrior.armour)
print(f"Warrior Stats:",warrior)
print(f"Warrior Stats:",ninja)
warrior.Added_armour()
print(f"Warrior Version ",CharacterDesgin.character_version)

print(f"Updated Heavy armour:",warrior.armour)
print(f"Warrior Stats:",warrior)
print(f"Warrior Stats:",ninja)

