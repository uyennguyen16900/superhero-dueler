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
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        ''' Add ability to abilities list
            ability: Ability Object
        '''
        # Add ability object to abilities:List
        self.abilities.append(ability)

    # attack: No Parameters
    def attack(self):
        ''' Calculate the total damage from all ability attacks.
            return: total_damage: Int
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

    def take_damage(self, damage):
        ''' Updates self.current_health to reflect
            the damage minus the defense.
            Parameters: damage
        '''
        # Create a method that updates self.current_health to the current
        # minus the the amount returned from calling self.defend(damage).
        self.current_health = self.current_health - self.defend(damage)

    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not.
        '''
        # Check whether the hero is alive and return true or false
        return self.current_health > 0

    def add_kill(self, num_kills):
        ''' Update kills with num_kills'''
        # This method should add the number of kills to self.kills
        self.kills += num_kills
        return self.kills

    def add_deaths(self, num_deaths):
        ''' Update deaths with num_deaths'''
        # This method should add the number of deaths to self.deaths
        self.deaths += num_deaths
        return self.deaths

    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.
            Parameters: opponent: Hero Class
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

        # update the number of kills the hero has when the opponent dies.
        # Also update the number of deaths for whoever dies in the fight
        if self.is_alive():
            self.add_kill(1)
            opponent.add_deaths(1)
            print(self.name + " won!")
        else:
            opponent.add_kill(1)
            self.add_deaths(1)
            print(opponent.name + " won!")

class Weapon(Ability):
    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        # Use what you learned to complete this method.
        return random.randint(self.max_damage // 2, self.max_damage)

class Team(object):
    def __init__(self, name):
        ''' Initialize your team with its team name
        '''
        # Implement this constructor by assigning the name and heroes, which should be an empty list
        self.name = name
        self.heroes = []

    def remove_hero(self, name):
        ''' Remove hero from heroes list.
            If Hero isn't found return 0.
        '''
        # Implement this method to remove the hero from the list given their name.
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                return self.heroes
        return 0

    def view_all_heroes(self):
        '''Prints out all heroes to the console.'''
        # Loop over the list of heroes and print their names to the terminal.
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        '''Add Hero object to self.heroes.'''
        # TODO: Add the Hero object that is passed in to the list of heroes in
        # self.heroes
        self.heroes.append(hero)

    def attack(self, other_team):
        ''' Battle each team against each other.'''
        # Randomly select a living hero from each team and have
        # them fight until one or both teams have no surviving heroes.
        # Hint: Use the fight method in the Hero class.
        # for hero in self.heroes:
        #     if hero.is_alive() == False:
        #         self.heroes.remove_hero(hero.name)
        #
        # for hero in other_team.heroes:
        #     if hero.is_alive() == False:
        #         other_team.heroes.remove_hero(hero.name)

        while len(other_team.hero) > 0 and len(self.heroes) > 0:
            hero1 = self.heroes[randint(0, len(self.heroes))]
            hero2 = other_team.heroes[randint(0, len(other_team.heroes))]
            if hero1.is_alive() == False:
                self.heroes.remove_hero(hero.name)
            elif hero2.is_alive() == False:
                other_team.heroes.remove_hero(hero.name)
            else:
                hero1.fight(hero2)

    def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health'''
        # This method should reset all heroes health to their
        # original starting value.
        for hero in self.heroes:
            hero.current_health = health

    def stats(self):
        '''Print team statistics'''
        # This method should print the ratio of kills/deaths for each
        # member of the team to the screen.
        # This data must be output to the console.
        # Hint: Use the information stored in each hero.
        for hero in self.heroes:
             print("{} has the ratio of kills/deaths of {}.".format(hero.name, hero.kills//hero.deaths))


if __name__ == "__main__":
    # hero1 = Hero("Wonder Woman")
    # hero2 = Hero("Dumbledore")
    # ability1 = Ability("Super Speed", 300)
    # ability2 = Ability("Super Eyes", 130)
    # ability3 = Ability("Wizard Wand", 80)
    # ability4 = Ability("Wizard Beard", 20)
    # hero1.add_ability(ability1)
    # hero1.add_ability(ability2)
    # hero2.add_ability(ability3)
    # hero2.add_ability(ability4)
    # hero1.fight(hero2)

    team = Team("One")
    jodie = Hero("Jodie")
    team.add_hero(jodie)
    print(team.heroes)
    team.remove_hero("Jodie")
    print(len(team.heroes))

    # ability = Ability("Debugging Ability", 20)
    # print(ability.name)
    # print(ability.attack())
