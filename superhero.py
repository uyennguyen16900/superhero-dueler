import random

class Ability:
    def __init__(self, name, max_damage):
        '''Instance Variables:
          name:String
          max_damage: Integer
        '''
        # Instantiate the variables listed in the docstring with then
        # values passed in
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        ''' Return a value between 0 and the value set by self.max_damage.'''
        # Use random.randint(a, b) to select a random attack value.
        # Return an attack value between 0 and the full attack.
        # Hint: The constructor initializes the maximum attack value.
        return random.randint(0, self.max_damage)

class Armor:
    # Parameters: name: String, max_block: Integer
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        pass

class Hero:
    # Parameters: name:String, starting_health:Int (default value: 100)
    def __init__(self, name, starting_health):
        self.name = name
        slef.starting_health = 100

    # Parameters: ability:Ability Object
    def add_ability(self, ability):
        self.ability = Ability(name, )

    # attack: No Parameters
    def attack(self):
        pass

    # defend: incoming_damage: Integer
    def defend(self, incoming_damage):
        pass

    # take_damage: Parameters: damage
    def take_damage(self, damage):
        pass

    # is_alive: No Parameters
    def is_alive(self):
        pass

    # fight: Parameters: opponent: Hero Class
    def fight(self, opponent):
        pass

if __name__ == "__main__":
    hero = Ability("U", 100)
    print(hero.name)
    print(hero.attack())
