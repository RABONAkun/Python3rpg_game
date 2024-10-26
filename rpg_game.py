# Python3rpg_game
import random

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def is_alive(self):
        return self.health > 0

    def attack(self, other):
        damage = random.randint(1, self.attack_power)
        other.health -= damage
        print(f"{self.name} attacks {other.name} for {damage} damage!")
        print(f"{other.name}'s health: {other.health}")

class Player(Character):
    def heal(self):
        heal_amount = random.randint(5, 15)
        self.health += heal_amount
        print(f"{self.name} heals for {heal_amount} health!")
        print(f"{self.name}'s health: {self.health}")

class Enemy(Character):
    pass

def main():
    print("Welcome to the RPG Game!")

    # プレイヤーを作成
    player_name = input("Enter your character's name: ")
    player = Player(name=player_name, health=100, attack_power=20)

    # 敵を作成
    enemy = Enemy(name="Goblin", health=50, attack_power=15)

    while player.is_alive() and enemy.is_alive():
        print("\nChoose an action:")
        print("1. Attack")
        print("2. Heal")
        choice = input("Enter the number of your action: ")

        if choice == "1":
            player.attack(enemy)
        elif choice == "2":
            player.heal()
        else:
            print("Invalid choice! Please select again.")
            continue

        # 敵の攻撃
        if enemy.is_alive():
            enemy.attack(player)

    # 勝敗のメッセージ
    if player.is_alive():
        print(f"\n{player.name} has defeated {enemy.name}!")
    else:
        print(f"\n{enemy.name} has defeated {player.name}...")

if __name__ == "__main__":
    main()
