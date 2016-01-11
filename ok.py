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
        self.room_exits = {'North', 'East', 'South', 'West'}

class Character:
    def __init__(self):
        self.name = ""
        self.current_health = 1
        self.health_max = 1


class Player(Character):
    def __init__(self, name, race, player_class):
        Character.__init__(self)
        self.current_health = 100
        self.max_health = 100
        self.name = name
        self.race = race
        self.player_class = player_class

        self.player_room = 1

    def attack(self,target):
        print "%s attacks %s for 1 damage!", self.name

    def get_inventory(self):
        print 'This is %s inventory', self.name

    def print_stats(self):
        print "Name", self.name
        print "Race", self.race
        print "Class", self.player_class
        print "Health", self.current_health, '/', self.health_max


def initialize_player():
    x = get_player_name()
    y = get_player_race()
    z = get_player_class()
    new_player = Player(x, y, z)
    new_player.print_stats()
    return new_player


def get_action():
    action = raw_input("Enter Action:")
    return action


def player_action(action, player_id):
    if action == "health":
        print "Health = ", player_id.current_health


def display_room(room_number):
    print room_number.room_name
    print room_number.room_description
    print "Also here:", room_number.room_inhabitants
    print "Exits:", room_number.room_exits


def game_loop():
    player_1 = initialize_player()
    room1 = Room()
    x = True
    while x == 1:
        display_room(room1)
        next_act = get_action()
        player_action(next_act, player_1)






# MAIN GAME SECTION
print_menu(main_menu_list)
main_menu_choice = get_menu_choice()
if main_menu_choice == '1':
    game_loop()
else:
    print "Peace Out"




