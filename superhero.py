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
        '''Instance properties:
            name: String
            max_block: Integer
        '''
        # Create instance variables for the values passed in.
        self.name = name
        self.max_block = max_block

    def block(self):
        ''' Return a random value between 0 and the initialized max_block strength. '''
        return random.randint(0, self.max_block)

class Hero:
    # Parameters: name:String, starting_health:Int (default value: 100)
    def __init__(self, name, starting_health=100):
        '''Instance properties:
          abilities: List
          armors: List
          name: String
          starting_health: Integer
          current_health: Integer
        '''
        # Initialize instance variables values as instance variables
        # (Some of these values are passed in above,
        # others will need to be set at a starting value)
        # abilities and armors are lists that will contain objects that we can use
        self.name = name
        self.abilities = []
        self.armors = []
        self.current_health = starting_health

    def add_ability(self, ability):
        ''' Add ability to abilities list
            ability: Ability Object
        '''
        # Add ability object to abilities:List
        self.abilities.append(ability)

    # attack: No Parameters
    def attack(self):
        ''' Calculate the total damage from all ability attacks.
            return: total:Int
        '''
        # This method should run Ability.attack() on every ability
        # in self.abilities and returns the total as an integer.
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        ''' Add armor to self.armors
            Armor: Armor Object
        '''
        # Add armor object that is passed in to `self.armors`
        self.armors.append(armor)

    def defend(self, incoming_damage):
        ''' Runs `block` method on each armor.
            Returns sum of all blocks
            incoming_damage: Integer
        '''
        # This method should run the block method on each armor in self.armors
        sum = 0
        for armor in self.armors:
            sum += armor.block()
        return incoming_damage - sum

    # take_damage: Parameters: damage
    def take_damage(self, damage):
        ''' Updates self.current_health to reflect
            the damage minus the defense.
        '''
        # Create a method that updates self.current_health to the current
        # minus the the amount returned from calling self.defend(damage).
        self.current_health = self.current_health - self.defend(damage)

    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not.
        '''
        # Check whether the hero is alive and return true or false
        if self.current_health > 0:
            return True
        else:
            return False

    # fight: Parameters: opponent: Hero Class
    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.
        '''
        # Fight each hero until a victor emerges.
        # Print the victor's name to the screen.
        index = 0
        while self.is_alive() and opponent.is_alive():
            if len(opponent.abilities) == 0 and len(self.abilities) == 0:
                print("Draw")
                break
            else:
                if index < len(opponent.abilities):
                    self.take_damage(opponent.abilities[index].max_damage)
                if index < len(self.abilities):
                    opponent.take_damage(self.abilities[index].max_damage)
                index += 1

        if opponent.is_alive() == False:
            print(self.name + " won!")
        else:
            print(opponent.name + " won!")

if __name__ == "__main__":
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
