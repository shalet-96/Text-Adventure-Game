import world
from player import Player
import items


def play():
    count = 1
    print('count', count)
    while count <= 4:
        world.load_tiles('map.txt')
        player = Player()
        if count == 2:
            world.load_tiles('map2.txt')
            player.inventory = [items.Rifles(), items.CrustaStun(), items.Rock()]
            player.victory = False
        if count == 3:
            world.load_tiles('map3.txt')
            player.inventory = [items.Rod(), items.Pillow(), items.Rock(), items.Gun()]
            player.victory = False
        if count == 4:
            world.load_tiles('map4.txt')
            player.inventory = [items.Dagger(), items.Pillow(), items.Rock(), items.Gun()]
            player.victory = False
        # These lines load the starting room and display the text
        room = world.tile_exists(player.location_x, player.location_y)
        print(room.intro_text())
        while player.is_alive() and not player.victory:
            room = world.tile_exists(player.location_x, player.location_y)
            room.modify_player(player)
            # Check again since the room could have changed the player's state
            if player.is_alive() and not player.victory:
                print("Choose an action:\n")
                available_actions = room.available_actions()
                for action in available_actions:
                    print(action)
                action_input = input('Action: ')
                for action in available_actions:
                    if action_input == action.hotkey:
                        player.do_action(action, **action.kwargs)
                        break
        if player.is_alive() and player.victory:
            count = count + 1
            continue


if __name__ == "__main__":
    play()
