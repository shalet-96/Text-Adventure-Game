class Enemy:
    def __init__(self, name, hp, damage, experience):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.experience = experience

    def is_alive(self):
        return self.hp > 0


class GiantSpider(Enemy):
    def __init__(self):
        super().__init__(name="Giant Spider", hp=10, damage=2, experience=10)


class Bats(Enemy):
    def __init__(self):
        super().__init__(name="Bats", hp=25, damage=15, experience=30)


class Zombie(Enemy):
    def __init__(self):
        super().__init__(name="Zombie", hp=25, damage=15, experience=20)


class Monster(Enemy):
    def __init__(self):
        super().__init__(name="Monster", hp=5, damage=10, experience=5)


class CatFish(Enemy):
    def __init__(self):
        super().__init__(name="CatFish", hp=5, damage=10, experience=10)


class Alligator(Enemy):
    def __init__(self):
        super().__init__(name="Alligator", hp=10, damage=10, experience=10)


class Crocodiles(Enemy):
    def __init__(self):
        super().__init__(name="Crocodiles", hp=10, damage=10, experience=10)


class Crab(Enemy):
    def __init__(self):
        super().__init__(name="Crab", hp=5, damage=5, experience=5)


class Ogre(Enemy):
    def __init__(self):
        super().__init__(name="Ogre", hp=30, damage=15, experience=10)


class Dog(Enemy):
    def __init__(self):
        super().__init__(name="Dog", hp=20, damage=10, experience=5)


class Wolf(Enemy):
    def __init__(self):
        super().__init__(name="Wolf", hp=25, damage=15, experience=5)


class Hellhound(Enemy):
    def __init__(self):
        super().__init__(name="Hellhound", hp=20, damage=10, experience=20)


class PolarBear(Enemy):
    def __init__(self):
        super().__init__(name="Bear", hp=25, damage=15, experience=30)


class RatHumanoid(Enemy):
    def __init__(self):
        super().__init__(name="RatHumanoid", hp=25, damage=15, experience=10)


class Penguins(Enemy):
    def __init__(self):
        super().__init__(name="Penguins", hp=25, damage=15, experience=10)


class Crawler(Enemy):
    def __init__(self):
        super().__init__(name="Crawler", hp=25, damage=15, experience=35)
