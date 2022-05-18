class Achievement:
    def __init__(self, name, description, difficulty, status):
        self.name = name
        self.description = description
        self.difficulty = difficulty
        self.status = status

why_does_everyone_do_this = Achievement("Why does everyone do this", "Try to kill the the blacksmith", "Easy", "Uncompleted")
cold_blooded_killer = Achievement("Cold Blooded Killer", "Kill the cow before talking to the blacksmith", "Medium", "Uncompleted")
adventurer = Achievement("Adventurer", "Visit every location in the game", "Hard", "Uncompleted")
speed_runner = Achievement("Speed runner", "Reach the treasure room faster than the developer", "Hard", "Uncompleted")
ouch = Achievement("Ouch", "Try to kill a cow bare handed", "Easy", "Uncompleted")

achievements = [cold_blooded_killer, adventurer, speed_runner, ouch, why_does_everyone_do_this]
