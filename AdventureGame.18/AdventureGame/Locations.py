class Location:
    def __init__(self, x, y, name, description, visited, img_path):
        self.x = x
        self.y = y
        self.name = name
        self.description = description
        self.visited = visited
        self.img_path = img_path


meadow = Location(0, 0, "Meadow", "A quaint meadow, with a sign off in the distance", True, "res/meadow.gif")
sign = Location(0, 1, "Sign", "A old wooden sign", False,  "res/sign.gif")
tavern = Location(1, 1, "Tavern", "A nice old tavern", False,  "res/tavern_beer_knife.gif")
forest_entrance = Location(-1, 1, "Forest entrance", "The forest entrance seems to be blocked by thick bushes", False,  "res/forest_entrance.gif")
blacksmith = Location(2, 1, "Blacksmith", "A blacksmiths forge, inhabited by a gruff old man", False, "res/blacksmith_axe.gif")
cave_entrance = Location(-3, 1, "Cave", "The entrance to a cold and damp cave", False, "res/cave_entrance.gif")
pasture = Location(0, 2, "Pasture", "A calm pasture full of cows", False, "res/pasture_cow.gif")

forest_path = Location(-2, 1, "Forest Path", "A path through the forest", False, "res/forest_path.gif")
fire_pit = Location(-2, 0, "Fire Pit", "A used fire pit", False, "res/camp_fire.gif")
cave_room1 = Location(-3, 2, "Cave room 1", "A dark room,so dark you can barely see anything", False, "res/cave_room1.gif")
cave_fork = Location(-3, 3, "Cave Fork", "Which way will you go?", False, "res/cave_fork.gif")
cave_water = Location(-2, 3, "Cave Water", "Water drips from the roof", False, "res/cave_water.gif")
cave_room2 = Location(-4, 3, "Cave room 2", "The cave smells very musty", False, "res/cave_room2.gif")
cave_flower = Location(-4, 4, "Cave_Flower", "A single flower growing deep in the cave", False, "res/cave_flower.gif")
cave_exit = Location(-4, 5, "Cave Exit", "There is a light at the end of the tunnel", False, "res/cave_exit.gif")

village_entrance = Location(-4, 6, "Village Entrance", "You can see a village on the horizon", False, "res/village_entrance.gif")
village_square = Location(-4, 7, "Village Square", "The center of a worn out alpine town", False, "res/town_square.gif")
bakery = Location(-5, 7, "Bakery", "A bakery full of fresh bread", False, "res/bakery_bread.gif")
village_exit = Location(-4, 8, "Village exit", "You Leave the village behind and head out into the mountains", False, "res/village_exit.gif")
mountain_meadow = Location(-4, 9, "Mountain meadow", "A quiet meadow at the base of 2 imposing mountains", False, "res/mountain_meadow.gif")

stream = Location(-3, 9, "Mountain Stream", "A crisp mountain stream", False, "res/stream.gif")
hobson_traverse = Location(-2, 9, "Hobson Traverse", "A perilous traverse, with cliffs on either side", False, "res/traverse.gif")
summit = Location(-1, 9, "Summit", "Your almost at the top!", False, "res/summit.gif")
stairway = Location(-1, 10, "The Stairway to heaven", "Something Something, Led Zeppelin reference", False, "res/stairway.gif")

false_summit = Location(-4, 12, "False Summit", "You see a door in the distance...", False, "res/false_summit.gif")
cliff_traverse = Location(-4, 10, "Traverse", "A dangerous mountain path, with a cliff face up ahead", False, "res/cliff_traverse.gif")
treasure_room = Location(-5, 14, "Treasure Room", "A room full of endless riches", False, "res/coming_soon.gif")
hillary_step = Location(-4, 11, "Hillary step", "An almost impossible climb, you might need some equipment...", False, "res/hillary_step.gif")
alpine_shop = Location(-3, 7, "Alpine Shop", "A old apine shop", False, "res/alpine_pick_torch_firework.gif")
entrance =  Location(-5, 12, "Entrance", "A mysterious hoel in the mountain", False, "res/entrance.gif")
dungeon_room = Location(-5, 13, "Dungeon room", "It's so dark you can't see anything, you don't know where your going...", False, "res/dark.gif")

def locations():
    locations = [meadow, sign, tavern, forest_entrance, blacksmith, cave_entrance, pasture, forest_path, fire_pit,
                 cave_room1, cave_fork, cave_water, cave_exit, cave_flower, cave_room2, village_entrance, village_square,
                 bakery, village_exit, stream, mountain_meadow, hobson_traverse, summit, stairway, treasure_room, cliff_traverse,
                 hillary_step, alpine_shop, false_summit, entrance]
    return locations


valid_coordinates = [(0, 0), (0, 1), (1, 1), (-1, 1), (2, 1), (-3, 1), (0, 2), (-2, 0), (-3, 2), (-3, 3), (-2, 3)
                     , (-4, 3), (-4, 4), (-4, 5), (-4, 6), (-4, 7), (-5, 7), (-4, 8), (-4, 9), (-3, 9), (-2, 9), (-1, 9),
                     (-4, 10), (-4, 11), (-3, 7), (-5, 12)]

