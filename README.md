# 100_days_of_py_v3

3er intento

## Day 3

[youtube](https://www.youtube.com/watch?v=cM_ocyOrs_k)

```py
# character.py
from weapon import fists
from health_bar import HealthBar

class Character:
  #def __init__(self, name: str, health: int, damage: int) -> None:
  def __init__(self, name: str, health: int) -> None:
    self.name = name
    self.health = health
    self.health_max = health
    #self.damage = damage

    self.weapon = fists

  def attack(self, target) -> None:
    target.health -= self.weapon.damage
    target.health = max(target.health, 0)
    target.health_bar.update()
    #print(f"{self.name} dealth {self.weapon.damage} damage to {target.name} with {self.weapon.name}")

# class inheritance

class Hero(character):
  def __init__(self,name: str,health:int) -> None:
    super().__init__(name=name,health=health)

    self.default_weapon = self.weapon
    self.health_bar = HealthBar(self, color="blue")

  def equip(self, weapon) -> None:
    self.weapon = weapon
    print(f"{self.name} equipped a(n) {self.weapon.name}!")

  def drop(self) -> None:
    print(f"{self.name} dropped the {self.weapon}!")
    self.weapon = self.default_weapon


class Enemy(character):
  def __init__(self,name: str,health:int, weapon: str) -> None:
    super().__init__(name=name,health=health)
    self.weapon = weapon
    self.health_bar = HealthBar(self, color="red")

# weapon.py

class Weapon:
  def __init__(self,name:str,weapon_type: str, damage: int, value:int) -> None:
    self.name = name
    self.weapon_type = weapon_type
    self.damage = damage
    self.value = value

iron_sword = Weapon(name="Iron Sword",weapon_type="sharp",damage=5,value=10)
shrot_bow = Weapon(name="Short Bow",weapon_type="ranged",damage=4,value=8)
fists= Weapon(name="Fists",weapon_type="blunt",damage=2,value=0)

# main.py
import os
from character import Hero, Enemy
from weapon import short_bow, iron_sword

hero = Hero(name="hero", health=100)
hero.equip(iron_sword)
enemy = Enemy(name="enemy", health=100,weapon=short_bow)

while True:
  os.system("cls")

  hero.attack(enemy)
  enemy.attack(hero)

  hero.health_bar.draw()
  enemy.health_bar.draw()

  #print(f"Health of {hero.name} is {hero.health}")
  #print(f"Health of {enemy.name} is {enemy.health}")

  input()

# health_bar.py
import sys
os.system("")

class HealthBar:
  symbol_remaining: str = "#"
  symbol_lost: str = "_"
  barrier: str = "|"
  colors: dict = {
    "red": "\033[91m",
    "blue": "\33[34m",
    "default": "\033[0m"
  }


  def __init__(self, 
               entity, 
               length: int = 20,
               is_bolored: bool = True,
               color: str = "") -> None:
    self.entity = entity
    self.length = length
    self.max_value = entity.health_max
    self.current_value = entity.health

    self.is_colored = is_colored
    self.color = self.color.get(color) or self.colors["default"]

  def update(self) -> None:
    self.current_value = self.entity.health

  def draw(self) -> None:
    remainig_bars = round(self.current_value / self.max_value * self.length)
    lost_bars = self.length - remaining_bars
    print(f"{self.entity.name}'s HEALTH: {self.entity.health}/{self.entity.health_max}")
    print(f"{self.barrier}"
          f"{self.color if self.is_colored else ''}"
          f"{remaining_bars * self.symbol_remaining}"
          f"{lost_bars * self.symbol_lost}"
          f"{self.colors['default'] if self.is_colored else ''}"
          f"{self.barrie}")
```

Day 26: deployed Flask app [link](https://github.com/jaliagag/python_rest_api/tree/dev)


