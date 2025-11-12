"""
COMP 163 - Project 2: Character Abilities Showcase
Name: Marcellus Hutchins
Date: 11-9-25

AI Usage: Define 'super().__init__()' constructor. Provided creative damage calculations.
"""
import random


# ============================================================================
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# ============================================================================

class SimpleBattle:
    """
    Simple battle system provided for you to test your characters.
    DO NOT MODIFY THIS CLASS - just use it to test your character implementations.
    """
    
    def __init__(self, character1, character2):
        self.char1 = character1
        self.char2 = character2
    
    def fight(self):
        """Simulates a simple battle between two characters"""
        print(f"\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===")
        
        # Show starting stats
        print("\nStarting Stats:")
        self.char1.display_stats()
        self.char2.display_stats()
        
        print(f"\n--- Round 1 ---")
        print(f"{self.char1.name} attacks:")
        self.char1.attack(self.char2)
        
        if self.char2.health > 0:
            print(f"\n{self.char2.name} attacks:")
            self.char2.attack(self.char1)
        
        print(f"\n--- Battle Results ---")
        self.char1.display_stats()
        self.char2.display_stats()
        
        if self.char1.health > self.char2.health:
            print(f"🏆 {self.char1.name} wins!")
        elif self.char2.health > self.char1.health:
            print(f"🏆 {self.char2.name} wins!")
        else:
            print("🤝 It's a tie!")

# ============================================================================
# YOUR CLASSES TO IMPLEMENT (6 CLASSES TOTAL)
# ============================================================================

class Character:
    """
    Base class for all characters.
    This is the top of our inheritance hierarchy.
    """
    
    def __init__(self, name='', health=50, strength=5, magic=5):
            self.name = name
            self.health = health
            self.strength = strength
            self.magic = magic

    """Initialize basic character attributes"""
    # TODO: Set the character's name, health, strength, and magic
    # These should be stored as instance variables
    pass
        
    def attack(self, target):
        if target.strength > self.strength:
            damage = 1
        elif target.strength < self.strength:
            damage = 10
        else:
            damage = 3
        print(f"\n{self.name} attacks {target} with {damage} damage")
        return target.take_damage(damage)



        """
        Basic attack method that all characters can use.
        This method should:
        1. Calculate damage based on strength
        2. Apply damage to the target
        3. Print what happened
        """
        # TODO: Implement basic attack
        # Damage should be based on self.strength
        # Use target.take_damage(damage) to apply damage
        pass
        
    def take_damage(self, damage):
        if self.health >= 0:
            if (self.health - damage) <= 0:
                self.health = 0
            else:
                self.health -= damage
        return self.health



        """
        Reduces this character's health by the damage amount.
        Health should never go below 0.
        """
        # TODO: Implement taking damage
        # Reduce self.health by damage amount
        # Make sure health doesn't go below 0
        pass
        
    def display_stats(self):
        print(f'{self.name}\n Health: {self.health}\n Strength: {self.strength}\n Magic: {self.magic}')

        """
        Prints the character's current stats in a nice format.
        """
        # TODO: Print character's name, health, strength, and magic
        # Make it look nice with formatting
        pass

class Player(Character):
    """
    Base class for player characters.
    Inherits from Character and adds player-specific features.
    """
    
    def __init__(self, name, character_class, health, strength, magic):
        super().__init__(name, health, strength, magic)
        self.character_class = character_class
        self.level = 1
        self.gold = 100
        self.class_skill_lvl = 1


        
    def display_stats(self):
        super().display_stats()
        print(f'Class-Skill Lvl: {self.class_skill_lvl}\n Gold: {self.gold}\n Level: {self.level}\n Class: {self.character_class}')

class Warrior(Player):
    """
    Warrior class - strong physical fighter.
    Inherits from Player.
    """
    
    def __init__(self, name):
        super().__init__(name, 'Warrior', 120, 15, 5)
        self.character_class = 'Warrior'

        """
        Create a warrior with appropriate stats.
        Warriors should have: high health, high strength, low magic
        """
        # TODO: Call super().__init__() with warrior-appropriate stats
        # Suggested stats: health=120, strength=15, magic=5
        pass
        
    def attack(self, target):
        if target.strength < self.strength:
            damage = self.strength
        elif target.strength > self.strength:
            damage = self.strength - 2
        else:
            damage = 5
        target.take_damage(damage)
        return target.health

        """
        Override the basic attack to make it warrior-specific.
        Warriors should do extra physical damage.
        """
        # TODO: Implement warrior attack
        # Should do more damage than basic attack
        # Maybe strength + 5 bonus damage?
        pass
        
    def power_strike(self, target):
        if target.strength < self.strength:
            damage = self.strength * 1.35
        elif target.strength > self.strength:
            damage = self.strength * 1.20
        else:
            damage = 10
        target.take_damage(damage)
        return target.health
        """
        Special warrior ability - a powerful attack that does extra damage.
        """
        # TODO: Implement power strike
        # Should do significantly more damage than regular attack
        pass

class Mage(Player):
    """
    Mage class - magical spellcaster.
    Inherits from Player.
    """
    
    def __init__(self, name):
        super().__init__(name, 'Mage', 80, 8, 20)
        self.character_class = 'Mage'
        """
        Create a mage with appropriate stats.
        Mages should have: low health, low strength, high magic
        """
        # TODO: Call super().__init__() with mage-appropriate stats
        # Suggested stats: health=80, strength=8, magic=20
        pass
        
    def attack(self, target):
        if target.magic < self.magic:
            damage = self.magic * 0.28
        elif target.magic > self.magic:
            damage = self.magic * 0.11
        else:
            damage = 10
        target.take_damage(damage)
        return target.health
        """
        Override the basic attack to make it magic-based.
        Mages should use magic for damage instead of strength.
        """
        # TODO: Implement mage attack
        # Should use self.magic for damage calculation instead of strength
        pass
        
    def fireball(self, target):
        if target.magic < self.magic:
            damage = self.magic * 1.40
        elif target.magic > self.magic:
            damage = self.magic * 1.25
        else:
            damage = 15
        target.take_damage(damage)
        return target.health
        """
        Special mage ability - a powerful magical attack.
        """
        # TODO: Implement fireball spell
        # Should do magic-based damage with bonus
        pass

class Rogue(Player):
    """
    Rogue class - quick and sneaky fighter.
    Inherits from Player.
    """
    
    def __init__(self, name):
        super().__init__(name, 'Rogue', 90, 12, 10)
        self.character_class = 'Rogue'

        """
        Create a rogue with appropriate stats.
        Rogues should have: medium health, medium strength, medium magic
        """
        # TODO: Call super().__init__() with rogue-appropriate stats
        # Suggested stats: health=90, strength=12, magic=10
        pass
        
    def attack(self, target):
        crit = random.randint(1, 10)
        if target.magic < self.magic or target.strength < self.strength:
            damage = self.magic * 0.28
            if crit >=8:
                damage = self.magic * 0.38
        elif target.magic > self.magic or target.strength > self.strength:
            damage = self.magic * 0.11
            if crit >=9:
                damage = self.magic * 0.15
        else:
            damage = 5
            if crit >=7:
                damage = 10
        target.take_damage(damage)
        return target.health
        """
        Override the basic attack to make it rogue-specific.
        Rogues should have a chance for extra damage (critical hits).
        """
        # TODO: Implement rogue attack
        # Could add a chance for critical hit (double damage)
        # Hint: use random.randint(1, 10) and if result <= 3, it's a crit
        pass
        
    def sneak_attack(self, target):
        overkill = random.randint(1, 20)
        if overkill >18:
            damage = 100
        if target.magic < self.magic or target.strength < self.strength:
            damage = self.magic * 1.55
        elif target.magic > self.magic or target.strength > self.strength:
            damage = self.magic * 1.15
        else:
            damage = 10
        target.take_damage(damage)
        return target.health

        """
        Special rogue ability - guaranteed critical hit.
        """
        # TODO: Implement sneak attack
        # Should always do critical damage
        pass

class Weapon:
    """
    Weapon class to demonstrate composition.
    Characters can HAVE weapons (composition, not inheritance).
    """
    
    def __init__(self, name='Short Knife', damage_bonus=10):
        self.name = name
        self.damage_bonus = damage_bonus


        """
        Create a weapon with a name and damage bonus.
        """
        # TODO: Store weapon name and damage bonus
        pass
        
    def display_info(self):
        print(self.name)
        print(self.damage_bonus)
        """
        Display information about this weapon.
        """
        # TODO: Print weapon name and damage bonus
        pass

# ============================================================================
# MAIN PROGRAM FOR TESTING (YOU CAN MODIFY THIS FOR TESTING)
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    print("Testing inheritance, polymorphism, and method overriding")
    print("=" * 50)
    
    # TODO: Create one of each character type
    # warrior = Warrior("Sir Galahad")
    # mage = Mage("Merlin")
    # rogue = Rogue("Robin Hood")
    
    # TODO: Display their stats
    # print("\n📊 Character Stats:")
    # warrior.display_stats()
    # mage.display_stats()
    # rogue.display_stats()
    
    # TODO: Test polymorphism - same method call, different behavior
    # print("\n⚔️ Testing Polymorphism (same attack method, different behavior):")
    # dummy_target = Character("Target Dummy", 100, 0, 0)
    # 
    # for character in [warrior, mage, rogue]:
    #     print(f"\n{character.name} attacks the dummy:")
    #     character.attack(dummy_target)
    #     dummy_target.health = 100  # Reset dummy health
    
    # TODO: Test special abilities
    # print("\n✨ Testing Special Abilities:")
    # target1 = Character("Enemy1", 50, 0, 0)
    # target2 = Character("Enemy2", 50, 0, 0)
    # target3 = Character("Enemy3", 50, 0, 0)
    # 
    # warrior.power_strike(target1)
    # mage.fireball(target2)
    # rogue.sneak_attack(target3)
    
    # TODO: Test composition with weapons
    # print("\n🗡️ Testing Weapon Composition:")
    # sword = Weapon("Iron Sword", 10)
    # staff = Weapon("Magic Staff", 15)
    # dagger = Weapon("Steel Dagger", 8)
    # 
    # sword.display_info()
    # staff.display_info()
    # dagger.display_info()
    
    # TODO: Test the battle system
    # print("\n⚔️ Testing Battle System:")
    # battle = SimpleBattle(warrior, mage)
    # battle.fight()
    
    print("\n✅ Testing complete!")
