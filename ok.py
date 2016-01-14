from pprint import pprint

class_list = ('1: Warrior', '2: Ninja', '3: Priest', '4: Wizard')
race_list = ('1: Human', '2: Elf', '3: Goblin', '4: Orc')
main_menu_list = ('1: Play', '2: Quit')


def print_menu(menu_name):
    for i in menu_name:
        print i
        

def get_menu_choice():
    x = raw_input("Choose an option: ")
    return x


def get_player_name():
    player_name = raw_input("Choose your character's name: ")
    return player_name


def get_player_race():
    print_menu(race_list)
    menu_choice = get_menu_choice()
    return menu_choice


def get_player_class():
    print_menu(class_list)
    menu_choice = get_menu_choice()
    return menu_choice


class Room:
    def __init__(self):
        self.room_id = 1
        self.room_name = "Town Square"
        self.room_description = "This is a bustling town square."
        self.room_inhabitants = "Mayor Greenling"
        self.room_exits = ["North", "East", "South", "West"]

    def print_room_name(self):
        print self.room_name

    def print_room_description(self):
        print self.room_description

    def print_room_inhabitants(self):
        print "Also here:", self.room_inhabitants

    def print_room_exits(self):
        print "Obvious exits:", ", ".join(self.room_exits)

    def print_full_room(self):
        self.print_room_name()
        self.print_room_description()
        self.print_room_inhabitants()
        self.print_room_exits()


class Character:
    def __init__(self):
        self.name = ""
        self.current_health = 1
        self.health_max = 1


class Player(Character):
    def __init__(self, name, race, player_class, player_id):
        Character.__init__(self)
        self.current_health = 100
        self.max_health = 100
        self.name = name
        self.race = race
        self.player_class = player_class
        self.player_id = player_id
        self.current_room = room1

    def print_stats(self):
        print "Name", self.name
        print "Race", self.race
        print "Class", self.player_class
        print "Health", self.current_health, '/', self.max_health

    def player_action(self, action):
        if action == "health":
            print "Health = ", self.current_health

        elif action == "stats":
            self.print_stats()

        elif action == "exit":
            global game_status
            game_status = False

        else:
            self.current_room.print_full_room


def get_action():
    action = raw_input("Enter Action:")
    return action


def initialize_player():
    x = get_player_name()
    y = get_player_race()
    z = get_player_class()
    name = Player(x, y, z, 1)
    name.print_stats()
    return name


# def game_loop():
#     player1 = initialize_player()
#     room1 = Room()
#     x = True
#     while x == 1:
#         next_act = get_action()
#         player1.player_action(next_act)

# MAIN GAME SECTION

game_status = True

print_menu(main_menu_list)
main_menu_choice = get_menu_choice()
if main_menu_choice == '1':
    room1 = Room()
    player1 = initialize_player()

    while game_status == 1:
        next_act = get_action()
        player1.player_action(next_act)

else:
    print "Peace Out"


