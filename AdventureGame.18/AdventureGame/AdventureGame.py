from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
import Achievements
import GameObject
import Locations
import time

command_widget = None
image_label = None
description_widget = None
inventory_widget = None
north_button = None
south_button = None
east_button = None
west_button = None
map_button = None
root = None

map_is_clicked = False
has_knife = True

refresh_location = True
refresh_objects_visible = True

current_location = Locations.mountain_meadow

end_of_game = False

start = time.time()


def perform_command(verb, noun):
    
    if verb == "GO":
        perform_go_command(noun)
    elif verb == "N" or verb == "S" or verb == "E" or verb == "W":
        perform_go_command(verb)        
    elif verb == "NORTH" or verb == "SOUTH" or verb == "EAST" or verb == "WEST":
        perform_go_command(verb)        
    elif verb == "GET":
        perform_get_command(noun)
    elif verb == "PUT":
        perform_put_command(noun)
    elif verb == "LOOK":
        perform_look_command(noun)        
    elif verb == "KILL":
        perform_kill_command(noun)        
    elif verb == "READ":
        perform_read_command(noun)        
    elif verb == "OPEN":
        perform_open_command(noun)
    elif verb == "CHOP":
        perform_chop_command()
    elif verb == "ACHIEVEMENT":
        perform_print_achievement_command()
    elif verb == "HELP":
        perform_help_command()
    else:
        print_to_description("huh?")       


def perform_go_command(direction):

    global current_location
    global refresh_location

    new_location = 1

    x = current_location.x
    y = current_location.y

    valid_directions = check_valid_directions("")

    if direction == "N" or direction == "NORTH":
        if "North" in valid_directions:
            y += 1
    if direction == "S" or direction == "SOUTH":
        if "South" in valid_directions:
            y -= 1
    if direction == "E" or direction == "EAST":
        if "East" in valid_directions:
            x += 1
    if direction == "W" or direction == "WEST":
        if "West" in valid_directions:
            x -= 1

    for location in Locations.locations():
        if x == location.x:
            if y == location.y:
                current_location = location
                location.visited = True
                break
    validate_achievements("Go")
    validate_achievements("Speed")
    refresh_location = True


def perform_help_command():
    commands = ["Help", "Get", "Put", "Look", "Kill", "Read", "Open", "Chop", "Achievement"]
    for command in commands:
        print_to_description(command + "\n")


def validate_achievements(event):
    visited_counter = 0
    if event == "Blacksmith":
        if Achievements.why_does_everyone_do_this.status == "Uncompleted":
            Achievements.why_does_everyone_do_this.status = "Completed"
            print_to_description("Achievement Completed!:" + Achievements.why_does_everyone_do_this.name + "\n" + Achievements.why_does_everyone_do_this.description + "\n")
    if event == "Killer":
        if Achievements.cold_blooded_killer.status == "Uncompleted":
            Achievements.cold_blooded_killer.status = "Completed"
    if event == "Go":
        for achievement in Achievements.achievements:
            if achievement.name == "Adventurer":
                for location in Locations.locations():
                    if location.visited:
                        visited_counter += 1
                    else:
                        break
                if visited_counter == len(Locations.locations()):
                    achievement.status = "Completed"
                    print_to_description("Achievement Completed!:" + achievement.name + "\n" + achievement.description + "\n")
    if event == "cow":
        if Achievements.ouch.status == "Uncompleted":
            Achievements.ouch.status = "Completed"
            print_to_description("Achievement Completed!:" + Achievements.ouch.name + "\n" + Achievements.ouch.description + "\n")
    for achievement in Achievements.achievements:
        if not achievement.status == "Completed":
            break
        Locations.valid_coordinates.append((-1, 10))
        Locations.stairway.img_path = "res/summit_stairway.gif"
    if event == "Speed":
        if Locations.treasure_room.visited:
            end = time.time()
            if end < 100:
                Achievements.speed_runner.status = "Completed"
                print_to_description("Achievement Completed!:" + Achievements.ouch.name + "\n" + Achievements.ouch.description + "\n")


def perform_chop_command():
    for object in GameObject.game_objects:
        if object.name == "Axe":
            if object.carried:
                Locations.forest_entrance.description = "A path into a dark and gloomy forest"
                Locations.forest_entrance.img_path = "res/forest_entrance_chopped.gif"
                Locations.valid_coordinates.append((-2, 1))
                set_current_image()
                break
            else:
                print_to_description("You can't cut things with your bare hands")
                break


def perform_print_achievement_command():
    for achievement in Achievements.achievements:
        print_to_description('Name' + ':' + str(achievement.name) + '\n' + "Status:" + achievement.status + "\n")


def perform_get_command(object_name):
    
    global refresh_objects_visible
    game_object = get_game_object(object_name)
    
    if not (game_object is None):
        if game_object.location != current_location or game_object.visible == False:
            print_to_description("You don't see one of those here!")
        elif not game_object.movable:
            print_to_description("You can't pick it up!")
        elif game_object.carried:
            print_to_description("You are already carrying it")
        else:
            if game_object.name == "Steak":
                Locations.pasture.img_path = "res/pasture.gif"
            if game_object.name == "Knife":
                if Locations.tavern.img_path == "res/tavern_knife.gif":
                    Locations.tavern.img_path = "res/tavern.gif"
                if Locations.tavern.img_path == "res/tavern_beer_knife.gif":
                    Locations.tavern.img_path = "res/tavern_beer.gif"
            if game_object.name == "Beer":
                if Locations.tavern.img_path == "res/tavern_beer_knife.gif":
                    Locations.tavern.img_path = "res/tavern_knife.gif"
                if Locations.tavern.img_path == "res/tavern_beer.gif":
                    Locations.tavern.img_path = "res/tavern.gif"
            if game_object.name == "Bread":
                Locations.bakery.img_path = "res/bakery.gif"
            if game_object.name == "Axe":
                for object in GameObject.game_objects:
                    if object.name == "Steak":
                        if object.carried:
                            game_object.carried = True
                            game_object.visible = False
                            refresh_objects_visible = True
                            object.carried = False
                            print_to_description("Thank you for the steak, here is the Axe you asked for")
                            Locations.blacksmith.img_path = "res/blacksmith.gif"
                            set_current_image()
                        else:
                            print_to_description('"Bring me some steak, then you can have the Axe"')
            if game_object.name.upper() == "ICE PICK":
                if Locations.alpine_shop.img_path == "res/alpine_pick_torch_firework.gif":
                    Locations.alpine_shop.img_path = "res/alpine_firework_torch.gif"
                    game_object.carried = True
                    game_object.visible = False
                    refresh_objects_visible = True
                    set_current_state()
                    set_current_image()
                if Locations.alpine_shop.img_path == "res/alpine_firework_pick.gif":
                    Locations.alpine_shop.img_path = "res/alpine_firework.gif"
                    game_object.carried = True
                    game_object.visible = False
                    refresh_objects_visible = True
                    set_current_state()
                    set_current_image()
                if Locations.alpine_shop.img_path == "res/alpine_torch_pick.gif":
                    Locations.alpine_shop.img_path = "res/alpine_torch.gif"
                    game_object.carried = True
                    game_object.visible = False
                    refresh_objects_visible = True
                    set_current_state()
                    set_current_image()
                if Locations.alpine_shop.img_path == "res/alpine_pick.gif":
                    Locations.alpine_shop.img_path = "res/alpine.gif"
                    game_object.carried = True
                    game_object.visible = False
                    refresh_objects_visible = True
                    set_current_state()
                    set_current_image()
                Locations.hillary_step.description = "A perilous climb"
                Locations.valid_coordinates.append((-4, 12))
            if game_object.name == "Fireworks":
                if Locations.alpine_shop.img_path == "res/alpine_pick_torch_firework.gif":
                    Locations.alpine_shop.img_path = "res/alpine_torch_pick.gif"
                    game_object.carried = True
                    game_object.visible = False
                    refresh_objects_visible = True
                    set_current_state()
                    set_current_image()
                if Locations.alpine_shop.img_path == "res/alpine_firework_pick.gif":
                    Locations.alpine_shop.img_path = "res/alpine_pick.gif"
                    game_object.carried = True
                    game_object.visible = False
                    refresh_objects_visible = True
                    set_current_state()
                    set_current_image()
                if Locations.alpine_shop.img_path == "res/alpine_firework_torch.gif":
                    Locations.alpine_shop.img_path = "res/alpine_torch.gif"
                    game_object.carried = True
                    game_object.visible = False
                    refresh_objects_visible = True
                    set_current_state()
                    set_current_image()
                if Locations.alpine_shop.img_path == "res/alpine_firework.gif":
                    Locations.alpine_shop.img_path = "res/alpine.gif"
                    game_object.carried = True
                    game_object.visible = False
                    refresh_objects_visible = True
                    set_current_state()
                    set_current_image()
            if game_object.name == "Torches":
                if Locations.alpine_shop.img_path == "res/alpine_pick_torch_firework.gif":
                    Locations.alpine_shop.img_path = "res/alpine_firework_pick.gif"
                    game_object.carried = True
                    game_object.visible = False
                    refresh_objects_visible = True
                    set_current_state()
                    set_current_image()
                if Locations.alpine_shop.img_path == "res/alpine_torch_pick.gif":
                    Locations.alpine_shop.img_path = "res/alpine_pick.gif"
                    game_object.carried = True
                    game_object.visible = False
                    refresh_objects_visible = True
                    set_current_state()
                    set_current_image()
                if Locations.alpine_shop.img_path == "res/alpine_firework_torch.gif":
                    Locations.alpine_shop.img_path = "res/alpine_torch.gif"
                    game_object.carried = True
                    game_object.visible = False
                    refresh_objects_visible = True
                    set_current_state()
                    set_current_image()
                if Locations.alpine_shop.img_path == "res/alpine_torch.gif":
                    Locations.alpine_shop.img_path = "res/alpine.gif"
                    game_object.carried = True
                    game_object.visible = False
                    refresh_objects_visible = True
                    set_current_state()
                    set_current_image()
                Locations.dungeon_room.img_path = "res/dungeon_room.gif"
                Locations.dungeon_room.description = "You see a small passage way in the corner"
                Locations.valid_coordinates.append((-5, 14))


            else:
                # pick up the object
                set_current_image()
                game_object.carried = True
                game_object.visible = False
                refresh_objects_visible = True
    else:
        print_to_description("You don't see one of those here!")


def perform_put_command(object_name):

    global refresh_objects_visible
    game_object = get_game_object(object_name)
    
    if game_object is None:
        print_to_description("You are not carrying one of those!")

    if game_object.name == "Knife":
        if Locations.tavern.img_path == "res/tavern.gif":
            Locations.tavern.img_path = "res/tavern_knife.gif"
        if Locations.tavern.img_path == "res/tavern_beer.gif":
            Locations.tavern.img_path = "res/tavern_beer_knife.gif"
        game_object.location = current_location
        game_object.carried = False
        game_object.visible = True
        refresh_objects_visible = True
    if game_object.name == "Beer":
        print_to_description("You can't really put it back...")
    if game_object.name == "Axe":
        Locations.blacksmith.img_path = "res/blacksmith_axe.gif"
        game_object.location = current_location
        game_object.carried = False
        game_object.visible = True
        refresh_objects_visible = True
    if game_object.name == "Steak":
        Locations.blacksmith.img_path = "res/pasture_steak.gif"
        game_object.location = current_location
        game_object.carried = False
        game_object.visible = True
        refresh_objects_visible = True
    if game_object.name.upper() == "ICE PICK":
        if Locations.alpine_shop.img_path == "res/alpine_torch_firework.gif":
            Locations.alpine_shop.img_path = "res/alpine_pick_torch_firework.gif"
            game_object.location = current_location
            game_object.carried = False
            game_object.visible = True
            refresh_objects_visible = True
            set_current_state()
            set_current_image()
        if Locations.alpine_shop.img_path == "res/alpine_firework.gif":
            Locations.alpine_shop.img_path = "res/alpine_firework_pick.gif"
            game_object.location = current_location
            game_object.carried = False
            game_object.visible = True
            refresh_objects_visible = True
            set_current_state()
            set_current_image()
        if Locations.alpine_shop.img_path == "res/alpine_torch.gif":
            Locations.alpine_shop.img_path = "res/alpine_torch_pick.gif"
            game_object.location = current_location
            game_object.carried = False
            game_object.visible = True
            refresh_objects_visible = True
            set_current_state()
            set_current_image()
        if Locations.alpine_shop.img_path == "res/alpine.gif":
            Locations.alpine_shop.img_path = "res/alpine_pick.gif"
            game_object.location = current_location
            game_object.carried = False
            game_object.visible = True
            refresh_objects_visible = True
            set_current_state()
            set_current_image()
        else:
            game_object.location = current_location
            game_object.carried = False
            game_object.visible = True
            refresh_objects_visible = True
        Locations.hillary_step.description = "An almost impossible climb, you might need some equipment..."
        Locations.valid_coordinates.remove((-4, 12))


    if game_object.name == "Fireworks":
        if Locations.alpine_shop.img_path == "res/alpine_torch_pick.gif":
            Locations.alpine_shop.img_path = "res/alpine_pick_torch_firework.gif"
            game_object.location = current_location
            game_object.carried = False
            game_object.visible = True
            refresh_objects_visible = True
            set_current_state()
            set_current_image()
        if Locations.alpine_shop.img_path == "res/alpine_pick.gif":
            Locations.alpine_shop.img_path = "res/alpine_firework_pick.gif"
            game_object.location = current_location
            game_object.carried = False
            game_object.visible = True
            refresh_objects_visible = True
            set_current_state()
            set_current_image()
        if Locations.alpine_shop.img_path == "res/alpine_torch.gif":
            Locations.alpine_shop.img_path = "res/alpine_firework_torch.gif"
            game_object.location = current_location
            game_object.carried = False
            game_object.visible = True
            refresh_objects_visible = True
            set_current_state()
            set_current_image()
        if Locations.alpine_shop.img_path == "res/alpine_firework.gif":
            Locations.alpine_shop.img_path = "res/alpine_firework.gif"
            game_object.location = current_location
            game_object.carried = False
            game_object.visible = True
            refresh_objects_visible = True
            set_current_state()
            set_current_image()
        else:
            game_object.location = current_location
            game_object.carried = False
            game_object.visible = True
            refresh_objects_visible = True
    if game_object.name == "Torches":
        if Locations.alpine_shop.img_path == "res/alpine_torch_pick.gif":
            Locations.alpine_shop.img_path = "res/alpine_pick_torch_firework.gif"
            game_object.location = current_location
            game_object.carried = False
            game_object.visible = True
            refresh_objects_visible = True
            set_current_state()
            set_current_image()
        if Locations.alpine_shop.img_path == "res/alpine_pick.gif":
            Locations.alpine_shop.img_path = "res/alpine_torch_pick.gif"
            game_object.location = current_location
            game_object.carried = False
            game_object.visible = True
            refresh_objects_visible = True
            set_current_state()
            set_current_image()
        if Locations.alpine_shop.img_path == "res/alpine_firework.gif":
            Locations.alpine_shop.img_path = "res/alpine_firework_torch.gif"
            game_object.location = current_location
            game_object.carried = False
            game_object.visible = True
            refresh_objects_visible = True
            set_current_state()
            set_current_image()
        if Locations.alpine_shop.img_path == "res/alpine.gif":
            Locations.alpine_shop.img_path = "res/alpine_torch.gif"
            game_object.location = current_location
            game_object.carried = False
            game_object.visible = True
            refresh_objects_visible = True
            set_current_state()
            set_current_image()
        else:
            game_object.location = current_location
            game_object.carried = False
            game_object.visible = True
            refresh_objects_visible = True
        Locations.dungeon_room.img_path = "res/dark.gif"
        Locations.dungeon_room.description = "It's so dark you can't see anything, you don't know where your going..."
        Locations.valid_coordinates.remove((-5, 14))


    else:
        if not game_object.carried:
            print_to_description("You are not carrying one of those.")
    set_current_image()


def perform_look_command(object_name):

    global Axe_found
    global refresh_location
    global refresh_objects_visible
    
    game_object = get_game_object(object_name)
 
    if not (game_object is None):

        if ((game_object.carried == True) or (game_object.visible and game_object.location == current_location)):
            print_to_description(game_object.description)
        else:
            #recognized but not visible
            print_to_description("You can't see one of those!")
 
        #special cases - when certain objects are looked at, others are revealed!
        if (False):
            print_to_description("special condition")
            global refresh_objects_visible
            refresh_objects_visible = True

    else:
        if (object_name == ""):
            #generic LOOK
            refresh_location = True
            refresh_objects_visible = True
        else:
            #not visible recognized
            print_to_description("You can't see one of those!")

def perform_kill_command(object_name):

    game_object = get_game_object(object_name)
 
    if not (game_object is None):
        if game_object.name == "Blacksmith":
            validate_achievements("Blacksmith")
        if game_object.name == "Cow":
            if not Locations.blacksmith.visited:
                validate_achievements("Killer")
        if game_object.name == "Cow":
            if GameObject.knife.carried:
                print_to_description("The cow dies")
                game_object.visible = False
                for object in GameObject.game_objects:
                    if object.name == "Steak":
                        object.visible = True
                        Locations.pasture.img_path = "res/pasture_steak.gif"
                        global refresh_objects_visible
                        refresh_objects_visible = True
                        set_current_image()
            else:
                print_to_description("You can't kill a cow with your bare hands!")
                validate_achievements("cow")





        else:
            print_to_description("You can't kill that")
    else:

        print_to_description("You can't kill what you can't see")

def perform_read_command(object_name):

    game_object = get_game_object(object_name)
 
    if not (game_object is None):
        if (False):
            print_to_description("special condition")
        else:
            print_to_description("There is no text on it")
    else:
        print_to_description("I am not sure which " + object_name + "you are referring to")
# 
def perform_open_command(object_name):

    global door_openend
    game_object = get_game_object(object_name)
 
    if not (game_object is None):
        if (False):
            print_to_description("special condition")
        else:
            print_to_description("You can't open one of those.")
    else:
        print_to_description("You don't see one of those here.")


def describe_current_location():
    for location in Locations.locations():
        if current_location.x == location.x:
            if current_location.y == location.y:
                print_to_description(location.description)


def set_current_image():
    global current_location

    for location in Locations.locations():
        if current_location.x == location.x:
            if current_location.y == location.y:
                image_label.img = PhotoImage(file=location.img_path)
                image_label.config(image=image_label.img)

        
def get_game_object(object_name):
    sought_object = None
    for current_object in GameObject.game_objects:
        if (current_object.name.upper() == object_name):
            sought_object = current_object
            break
    return sought_object

def describe_current_visible_objects():
    
    object_count = 0
    object_list = ""
    
    for current_object in GameObject.game_objects:
        if ((current_object.location  == current_location) and (current_object.visible == True) and (current_object.carried == False)):
            object_list = object_list + ("," if object_count > 0 else "") + current_object.name
            object_count = object_count + 1
            
    print_to_description("You see: " + (object_list + "." if object_count > 0 else "nothing special.")) 

def describe_current_inventory():
    
    object_count = 0
    object_list = ""

    for current_object in GameObject.game_objects:
        if (current_object.carried):
            object_list = object_list + ("," if object_count > 0 else "") + current_object.name
            object_count = object_count + 1
    
    inventory = "You are carrying: " + (object_list if object_count > 0 else "nothing")
    
    inventory_widget.config(state = "normal")
    inventory_widget.delete(1.0, END)
    inventory_widget.insert(1.0, inventory)
    inventory_widget.config(state = "disabled")

def handle_special_condition():
    
    global end_of_game
    
    if (False):
        print_to_description("GAME OVER")
        end_of_game = True


def print_to_description(output, user_input=False):
    description_widget.config(state = 'normal')
    description_widget.insert(END, output)
    if (user_input):
        description_widget.tag_add("blue_text", CURRENT + " linestart", END + "-1c")
        description_widget.tag_configure("blue_text", foreground = 'blue')
    description_widget.insert(END, '\n')        
    description_widget.config(state = 'disabled')
    description_widget.see(END)



def build_interface():
    
    global command_widget
    global image_label
    global description_widget
    global inventory_widget
    global north_button
    global south_button
    global east_button
    global west_button
    global map_button
    global root

    root = Tk()
    root.resizable(0,0)
    
    style = ttk.Style()
    style.configure("BW.TLabel", foreground="black", background="white")

    image_label = ttk.Label(root)    
    image_label.grid(row=0, column=0, columnspan =3,padx = 2, pady = 2)

    description_widget = Text(root, width =50, height = 10, relief = GROOVE, wrap = 'word')
    description_widget.insert(1.0, "Welcome to my game\n\nGood Luck!. ")
    description_widget.config(state = "disabled")
    description_widget.grid(row=1, column=0, columnspan =3, sticky=W, padx = 2, pady = 2)

    command_widget = ttk.Entry(root, width = 25, style="BW.TLabel")
    command_widget.bind('<Return>', return_key_enter)
    command_widget.grid(row=2, column=0, padx = 2, pady = 2)
    
    button_frame = ttk.Frame(root)
    button_frame.config(height = 150, width = 150, relief = GROOVE)
    button_frame.grid(row=3, column=0, columnspan =1, padx = 2, pady = 2)

    north_button = ttk.Button(button_frame, text = "N", width = 5)
    north_button.grid(row=0, column=1, padx = 2, pady = 2)
    north_button.config(command = north_button_click)
    
    south_button = ttk.Button(button_frame, text = "S", width = 5)
    south_button.grid(row=2, column=1, padx = 2, pady = 2)
    south_button.config(command = south_button_click)

    east_button = ttk.Button(button_frame, text = "E", width = 5)
    east_button.grid(row=1, column=2, padx = 2, pady = 2)
    east_button.config(command = east_button_click)

    west_button = ttk.Button(button_frame, text = "W", width = 5)
    west_button.grid(row=1, column=0, padx = 2, pady = 2)
    west_button.config(command = west_button_click)
    
    inventory_widget = Text(root, width = 30, height = 8, relief = GROOVE , state=DISABLED )
    inventory_widget.grid(row=2, column=2, rowspan = 2, padx = 2, pady = 2,sticky=W)
    
def set_current_state():

    global refresh_location
    global refresh_objects_visible

    if (refresh_location):
        describe_current_location()
        set_current_image()
    
    if (refresh_location or refresh_objects_visible):
        describe_current_visible_objects()

    handle_special_condition()
    set_directions_to_move("")

    if (end_of_game == False):
        describe_current_inventory()
    
    refresh_location = False
    refresh_objects_visible = False
    
    command_widget.config(state = ("disabled" if end_of_game else "normal"))

def north_button_click():
    print_to_description("N", True)
    perform_command("N", "")
    set_current_state()

def south_button_click():
    print_to_description("S", True)
    perform_command("S", "")
    set_current_state()

def east_button_click():
    print_to_description("E", True)
    perform_command("E", "")
    set_current_state()

def west_button_click():
    print_to_description("W", True)
    perform_command("W", "")
    set_current_state()

def return_key_enter(event):
    if( event.widget == command_widget):
        command_string = command_widget.get()
        print_to_description(command_string, True)

        command_widget.delete(0, END)
        words = command_string.split(' ', 1)
        verb = words[0]
        noun = (words[1] if (len(words) > 1) else "")
        perform_command(verb.upper(), noun.upper())
        
        set_current_state()



def check_valid_directions(call_location):

    valid_directions = []

    if call_location == "Map":
        return valid_directions

    else:
        for location in Locations.locations():
            if location.name == current_location.name:
                x = location.x
                y = location.y

                if (x, y + 1) in Locations.valid_coordinates:  # North
                    valid_directions.append("North")

                if (x, y - 1) in Locations.valid_coordinates:  # South
                    valid_directions.append("South")

                if (x + 1, y) in Locations.valid_coordinates:  # East
                    valid_directions.append("East")

                if (x - 1, y) in Locations.valid_coordinates: # West
                    valid_directions.append("West")
        return valid_directions


def set_directions_to_move(call_location):
    valid_directions = check_valid_directions(call_location)
    if "North" in valid_directions:
        move_to_north = True
    else:
        move_to_north = False

    if "South" in valid_directions:
        move_to_south = True
    else:
        move_to_south = False

    if "West" in valid_directions:
        move_to_west = True
    else:
        move_to_west = False

    if "East" in valid_directions:
        move_to_east = True
    else:
        move_to_east = False


    
    north_button.config(state = ("normal" if move_to_north else "disabled"))
    south_button.config(state = ("normal" if move_to_south else "disabled"))
    east_button.config(state = ("normal" if move_to_east else "disabled"))
    west_button.config(state = ("normal" if move_to_west else "disabled"))


def main():
    build_interface()
    set_current_state()
    root.mainloop()
        
main()
