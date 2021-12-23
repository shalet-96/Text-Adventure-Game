# Base class for all items
class Item():
    # __init__ is the contructor method
    def __init__(self, name, description, value):
        self.name = name  # attribute of the Item class and any subclasses
        self.description = description  # attribute of the Item class and any subclasses
        self.value = value  # attribute of the Item class and any subclasses

    # __str__ method is used to print the object
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)


# Extend the Items class
# Gold class will be a child or subclass of the superclass Item
class Gold(Item):
    # __init__ is the contructor method
    def __init__(self, amt):
        self.amt = amt  # attribute of the Gold class
        super().__init__(name="Gold",
                         description="A round coin with {} stamped on the front.".format(str(self.amt)),
                         value=self.amt)


class Potions(Item):
    def __init__(self, name, description, value, damage, amt, health):
        self.damage = damage
        self.amt = amt
        self.health = health
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage,
                                                             self.amt, self.health)


class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)


class BatKiller(Weapon):
    def __init__(self):
        super().__init__(name="BatKiller",
                         description="A Bat Killer is used to kill bat.",
                         value=0,
                         damage=25)


class FireBall(Weapon):
    def __init__(self):
        super().__init__(name="FireBall",
                         description="Great explosion radius",
                         value=10,
                         damage=5)


class Gun(Weapon):
    def __init__(self):
        super().__init__(name="Gun",
                         description="A Gun.",
                         value=5,
                         damage=25)


class HuntWeapon(Weapon):
    def __init__(self):
        super().__init__(name="Hunt Weapon",
                         description="To kill Monster",
                         value=10,
                         damage=10)


class Rifles(Weapon):
    def __init__(self):
        super().__init__(name="Rifle",
                         description="Rifle.",
                         value=10,
                         damage=25)


class CrustaStun(Weapon):
    def __init__(self):
        super().__init__(name="CrustaStun",
                         description="Electric Shock.",
                         value=10,
                         damage=25)


class Rod(Weapon):
    def __init__(self):
        super().__init__(name="Rod",
                         description="A Rod.",
                         value=5,
                         damage=5)


class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         description="A fist-sized rock, suitable for bludgeoning.",
                         value=0,
                         damage=5)


class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger",
                         description="A small dagger with some rust. Somewhat more dangerous than a rock.",
                         value=10,
                         damage=10)


class Pillow(Weapon):
    def __init__(self):
        super().__init__(name="Pillow",
                         description="A pillow super soft.",
                         value=1,
                         damage=1)


class SmallPotion(Potions):
    def __init__(self):
        super().__init__(
            name="small Potion",
            description="A small potion",
            value=5,
            amt=1,
            health=25,
            damage=0)
