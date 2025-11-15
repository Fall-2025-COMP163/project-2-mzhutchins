
**RPG Character System (Python):**

A simple role-playing game system written in Python.  
This project demonstrates classes and their inheritance systems.

**Logic breakdown:**

-Base class is created and initialized with the __init__, attack(), take damage and display stat methods.
-Derived classes inherit methods and base constructors.
    -Classes use a hierarchy system called on by super().__init__()
    -Each class uses the attack methods and adds on a critical strike
-Each section returns the target health 
-The weapon class creates its on constructors and stats and overrides display_stats()

**Features:**

-Base Character class for shared stats and methods
-Player class extends Character with new elements such as level, gold, and class skills.
-Subclasses:
  - Warrior – strong melee fighter with Power Strike ability.
  - Mage – powerful spellcaster with Fireball ability.
  - Rogue – agile attacker with critical hits and Sneak Attack.
  - Tank – high-health defender with Shield and steady attacks.
-Weapon class allows additional bonus of player stats.
-Simple combat system using attack() and ability methods like fireball() or power_strike().

**Basic (Attribute - Description):**

Health - Determines how much damage a character can take.
Strength - Affects attack damage through physical scaling
Magic - Affects attack damage through magic scaling

Characters attack each other using methods like:
player1.attack(player2)
