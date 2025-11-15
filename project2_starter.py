"""
COMP 163 - Project 2: Character Abilities Showcase
Name: Marcellus Hutchins
Date: 11-9-25

AI Usage: Define 'super().__init__()' constructor. Provided creative damage calculations.
"""
import math
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

    def __init__(self, name='', health=50, strength=5, magic=5):
            self.name = name
            self.health = health
            self.strength = strength
            self.magic = magic


    def attack(self, target):
        if target.strength > self.strength:
            damage = 1
        elif target.strength < self.strength:
            damage = 10
        else:
            damage = 3
        print(f"\n{self.name} attacks {target} with {damage} damage")
        return target.take_damage(damage)


    def take_damage(self, damage):
        if self.health >= 0:
            if (self.health - damage) <= 0:
                self.health = 0
            else:
                self.health -= damage
        return self.health


    def display_stats(self):
        print(f'{self.name}\n Health: {self.health}\n Strength: {self.strength}\n Magic: {self.magic}')




class Player(Character):

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
    
    def __init__(self, name):
        super().__init__(name, 'Warrior', 120, 15, 5)
        self.character_class = 'Warrior'

        
    def attack(self, target):
        if target.strength < self.strength:
            damage = self.strength
        elif target.strength > self.strength:
            damage = self.strength - 2
        else:
            damage = 5
        target.take_damage(damage)
        return target.health


    def power_strike(self, target):
        if target.strength < self.strength:
            damage = self.strength * 1.35
        elif target.strength > self.strength:
            damage = self.strength * 1.20
        else:
            damage = 10
        target.take_damage(damage)
        return target.health




class Mage(Player):
    
    def __init__(self, name):
        super().__init__(name, 'Mage', 80, 8, 20)
        self.character_class = 'Mage'

        
    def attack(self, target):
        if target.magic < self.magic:
            damage = self.magic * 0.28
        elif target.magic > self.magic:
            damage = self.magic * 0.11
        else:
            damage = 10
        target.take_damage(damage)
        return target.health

        
    def fireball(self, target):
        if target.magic < self.magic:
            damage = self.magic * 1.40
        elif target.magic > self.magic:
            damage = self.magic * 1.25
        else:
            damage = 15
        target.take_damage(damage)
        return target.health




class Rogue(Player):
    
    def __init__(self, name):
        super().__init__(name, 'Rogue', 90, 12, 10)
        self.character_class = 'Rogue'

        
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




class Tank(Player):

    def __init__(self, name):
        super().__init__(name, 'Tank', 210, 8, 10)
        self.character_class = 'Tank'


    def attack(self, target):
        damage = self.magic * 0.5 + self.strength * 2
        x = random.randint(1,5)
        if self.health <= (self.health * 0.25):
            if x == 3:
                self.health = self.health + 15
        target.take_damage(damage)
        return target.health


    def shield(self, target):
        damage = self.magic + self.strength
        x = random.randint(1,10)
        if x >7:
            self.health = self.health + math.fabs(self.health - target.health)
        target.take_damage(damage)
        return target.health




class Weapon:
    
    def __init__(self, name='Short Knife', damage_bonus=10):
        self.name = name
        self.damage_bonus = damage_bonus

        
    def display_info(self):
        print(self.name)
        print(self.damage_bonus)


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
