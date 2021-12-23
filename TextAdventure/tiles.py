import os.path
import winsound

import items, enemies, actions, world, sounds


class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves

    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())

        return moves


class StartingRoom(MapTile):
    # override the intro_text method in the superclass
    def intro_text(self):
        return """
        You suddenly come across an old mansion while exploring the forest. 
        Despite previous warnings about the place, a curious traveler like yourself can not resist visiting this building.
        Equipe yourself with great gear and a brave heart for a challenging adventure ahead, many secrets and exciting challenges are waiting for you!.
        """

    def modify_player(self, player):
        # Room has no action on player
        pass


class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, player):
        player.inventory.append(self.item)

    def modify_player(self, player):
        self.add_loot(player)


class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy), actions.Equip(), actions.Heal()]
        else:
            return self.adjacent_moves()


class EmptyDarkPath(MapTile):
    def intro_text(self):
        return """
        Another darker side  of the mansion . Move forward.
        """

    def modify_player(self, player):
        pass


class GiantSpiderRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.GiantSpider())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A giant spider jumps down from its web in front of you!
            """
        else:
            return """
            The corpse of a dead spider rots on the ground.
            """


class BatsRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Bats())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            Group of bats Hanging in front of you!
            """
        else:
            return """
            The corpse of a dead bats rots on the ground.
            """


class ZombieRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Zombie())

    def intro_text(self):
        if self.enemy.is_alive():
            sounds.zombie()
            return """
            Group of Zombies attacking you!
            """
        else:
            return """
            The corpse of a dead Zombies rots on the ground.
            """


class MonsterRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Monster())

    def intro_text(self):
        if self.enemy.is_alive():
            sounds.monsterSound()
            return """
            Monster is attacking you!
            """
        else:
            return """
            The corpse of a dead Monster rots on the ground.
            """


class LeaveMansion(MapTile):
    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer! It's sunlight!!
         .....Level 1 Completed...... You have Max HP now.....          
        You reached outside the Mansion !!! You have to cross the river.
        Grab the boat...         
        """

    def modify_player(self, player):
        player.victory = True
        # player.level = player.level + 1


class StartingRiverView(MapTile):
    # override the intro_text method in the superclass
    def intro_text(self):
        return """
        You are now in the Boat...
        Relax.....
        More adventure is waiting.....
        """

    def modify_player(self, player):
        # Room has no action on player
        pass


class EmptyriverWay(MapTile):
    def intro_text(self):
        return """
        Boe the boat and enjoy the nature. 
        
        Move forward with hope....
        """

    def modify_player(self, player):
        # Room has no action on player
        pass


class CatFishRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.CatFish())

    def intro_text(self):
        if self.enemy.is_alive():
            # sounds.monsterSound()
            return """
            CatFish is attacking you!
            """
        else:
            return """
            The corpse of a dead Catfish flowing.
            """


class AlligatorRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Alligator())

    def intro_text(self):
        if self.enemy.is_alive():
            sounds.monsterSound()
            return """
            Alligator is attacking you!
            """
        else:
            return """
            The corpse of a dead Alligator found in the way.
            """


class Crocodiles(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Crocodiles())

    def intro_text(self):
        if self.enemy.is_alive():
            sounds.monsterSound()
            return """
            Crocodiles is attacking you!
            """
        else:
            return """
            Crocodiles dead.
            """


class CrabRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Crab())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            Crab is attacking you!
            """
        else:
            return """
            The corpse of a dead crab rots flowing.
            """


class LeaveRiverWay(MapTile):
    def intro_text(self):
        return """
        You crossed the river with hope. 
        Completed level 2!!!!!!
        Freezing cold is waiting for you!!!
              
        """

    def modify_player(self, player):
        player.victory = True
        # player.level = player.level + 1


class StartingFreeze(MapTile):
    # override the intro_text method in the superclass
    def intro_text(self):
        return """
        Now you are in level 3... 
        You are now in an snow land..Adventures are on the way...
        """

    def modify_player(self, player):
        # Room has no action on player
        pass


class EmptySnowPath(MapTile):
    def intro_text(self):
        return """
        It's snow.... Move forward with cold heart...
        """

    def modify_player(self, player):
        # Room has no action on player
        pass


class PolarBearRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.PolarBear())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             A Polar Bear jumps down in front of you!
             """
        else:
            return """
             The corpse of a dead Bear is on the ground.
             """


class CrawlerRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Crawler())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             A Crawler is attacking you!
             """
        else:
            return """
             The corpse of a dead Crawler is on the ground.
             """


class RatHumanoidRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.RatHumanoid())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             A RatHumanoid is attacking you!
             """
        else:
            return """
             The corpse of a dead RatHumanoid is on the ground.
             """


class PenguinsRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Penguins())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             A Penguins is attacking you!
             """
        else:
            return """
             The corpse of a dead Penguins is on the ground.
             """


class LeaveSnowLand(MapTile):
    def intro_text(self):
        return """
        You crossed the snow land 
        Completed level 3!!!!!!
        Now it's time for some horror things...
        You will see a light, Follow the light...

        """

    def modify_player(self, player):
        player.victory = True
        # player.level = player.level + 1


class StartingCave(MapTile):
    # override the intro_text method in the superclass
    def intro_text(self):
        return """
        You are now in cave.... Reached level 4 
        Move forward to the light you are seeing...
        """

    def modify_player(self, player):
        # Room has no action on player
        pass


class EmptyCavePath(MapTile):
    def intro_text(self):
        return """
        Another unremarkable part of the cave. You must forge onwards.
        """

    def modify_player(self, player):
        # Room has no action on player
        pass


class WolfRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Wolf())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             A wolf jumps down in front of you!
             """
        else:
            return """
             The corpse of a dead wolf is on the ground.
             """


class HellhoundRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Hellhound())

    def intro_text(self):
        if self.enemy.is_alive():
            sounds.monsterSound()
            return """
             An Hellhound is attacking you!
             """
        else:
            return """
             The corpse of a dead Hellhound is on the ground.
             """


class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())

    def intro_text(self):
        return """
        Your notice something shiny in the corner.
        It's a dagger! You pick it up.
        """


class LeaveCaveRoom(MapTile):
    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer! It's sunlight!
        
        Finally you did it.... Completed all the levels with bravery heart.....
 
 
        Victory is yours!
        """

    def modify_player(self, player):
        player.victory = True
