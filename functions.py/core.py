from abc import ABC,abstractmethod
class Character:
    def __inir__(self,hp):
        self._health =hp
        self.__inventory=[]
    @abstractmethod
    def attack(self,target):
        pass
    @property
    def inv(self):
        return self.__inventory
    @inv.setter
    def inv(self,n):
        self.__in.append=n
    @property
    def hp(self):
        return self._health
    @hp.setter
    def hp(self,n):
        if n<0:
            self._health=0
        else:
            self._health=n
    def __str__(self):
        return f"{self.hp}"
    def __repr__(self):
        return self.inv
    def __add__(self,o2):
        self.inv=o2
        return "recived"
    def __sud__(self,o2):
        if o2 in self.inv:
            self.inv.remove(o2)
            return "removed"
        else:
            return "not found"
    def __contains__(self, o2):
        return o2 in self.inv
class Warrior(Character):
    id=["axe","squrd","dualsqurd","bonesqured"]
    def __init__(self,name,item):
        self.name=name
        super().__init__(150)
        if self.valid(item):
            self.inv=item
        self.damage=50
    def attack(self,target):
        if self.damage>=target.hp:
            target.hp=0
        else:
            target.hp=self.damage
    def heal(self,reason="conbot"):
        if reason=="conbot":
            self.hp+=20
        else:
            self.hp+=10
    @staticmethod
    def valid(item):
        return item in Warrior.id
class Party:
    buff=0.2
    def __init__(self,*team):
        self.team=team
    def over(self):
        return self.hp
