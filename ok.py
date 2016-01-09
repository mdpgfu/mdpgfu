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

"""For Debug"""
def print_stats(character):
    print "Name", character.name
    print "Race", character.race
    print "Class", character.player_class
    print "Health", character.current_health, '/', character.max_health

##MAIN GAME SECTION
print_menu(main_menu_list)
main_menu_choice = get_menu_choice()
if main_menu_choice == '1':
    x = get_player_name()
    y = get_player_race()
    z = get_player_class()
    new_player = Player(x, y, z)
    print_stats(new_player)
else:
    print "Peace Out"


##def generate_character():
##    new_character = Player()
##
##def launch_game():
##    generate_character()
##    
##def run_game_loop():
##    state = True
##    while state == True:
##        print 'OK'



