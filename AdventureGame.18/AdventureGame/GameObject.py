import Locations

class GameObject:

    def __init__(self, name, location, movable, visible, carried, description):
        self.name = name
        self.location = location
        self.movable = movable
        self.visible = visible
        self.carried = carried
        self.description = description

blacksmith = GameObject("Blacksmith", Locations.blacksmith, False, False, False, "Blacksmith")
knife = GameObject("Knife", Locations.tavern, True, True, False, "A worn out dagger")
steak = GameObject("Steak", Locations.pasture, True, False, False, "Fresh Beef")
axe = GameObject("Axe", Locations.blacksmith, True, True, False, "A large battle axe")
cow = GameObject("Cow", Locations.pasture, False, True, False, "Bessy the cow")
fork = GameObject("Fork", Locations.cave_fork, True, True, False, "Fork")
beer = GameObject("Beer", Locations.tavern, True, True, False, "A foamy mug of beer")
bread = GameObject("Bread", Locations.bakery, True, True, False, "Fresh bread")
ice_pick = GameObject("Ice Pick", Locations.alpine_shop, True, True, False, "Ice Pickaxe")
fire_works = GameObject("Fireworks", Locations.alpine_shop, True, True, False, "Fireworks")
torches = GameObject("Torches", Locations.alpine_shop, True, True, False, "Torch")


game_objects = [steak, axe, cow, knife, beer, fork, bread, blacksmith, ice_pick, fire_works, torches]
