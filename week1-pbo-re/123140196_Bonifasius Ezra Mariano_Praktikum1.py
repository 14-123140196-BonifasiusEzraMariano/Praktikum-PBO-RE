import random

class Robot:
    def __init__(self, name, attack, hp, mana, accuracy):
        self.name = name
        self.attack = attack
        self.hp = hp
        self.mana = mana
        self.max_hp = hp
        self.max_mana = mana
        self.accuracy = accuracy
        self.defense = 0
        self.stunned = False
        self.silence_turns = 0
        self.dodge = 0
        self.action = None
        self.selected_skill = None

    def attack_enemy(self, enemy):
        if self.stunned:
            print(f"{self.name} terkena STUN dan tidak bisa bergerak!")
            self.stunned = False
            return
        final_accuracy = max(0, self.accuracy - enemy.dodge)
        if random.randint(1, 100) <= final_accuracy:
            damage = max(0, self.attack - enemy.defense)
            enemy.hp -= damage
            print(f"{self.name} menyerang {enemy.name} dan memberikan {damage} damage!")
        else:
            print(f"{self.name} menyerang {enemy.name} tetapi serangannya meleset!")

    def use_skill(self, enemy):
        if self.selected_skill is None:
            return
        
        self.mana -= 5
        skill = self.selected_skill
        self.selected_skill = None  # Reset skill setelah digunakan
        
        if skill == "200_damage":
            damage = self.attack * 2
            enemy.hp -= damage
            print(f"{self.name} menggunakan 200% DAMAGE dan menyerang {enemy.name} dengan {damage} damage!")
        elif skill == "lifesteal":
            heal = self.attack * 0.5
            self.hp = min(self.hp + heal, self.max_hp)
            print(f"{self.name} menggunakan LIFESTEAL dan menyembuhkan {heal} HP!")
        elif skill == "buff_hp_attack":
            self.hp = min(self.hp * 1.2, self.max_hp)
            self.attack *= 1.2
            print(f"{self.name} meningkatkan HP dan ATTACK sebesar 20%!")
        elif skill == "buff_accuracy":
            self.accuracy += 50
            print(f"{self.name} meningkatkan ACCURACY sebesar 50%!")
        elif skill == "buff_dodge":
            self.dodge += 40
            print(f"{self.name} meningkatkan DODGE sebesar 40%!")
        elif skill == "stun":
            enemy.stunned = True
            print(f"{self.name} menggunakan STUN! {enemy.name} tidak bisa bergerak di giliran berikutnya.")
        elif skill == "silence":
            enemy.silence_turns = 3
            print(f"{self.name} menggunakan SILENCE! {enemy.name} tidak bisa memakai skill selama 3 ronde.")

    def defend(self):
        self.defense = 40
        print(f"{self.name} memilih DEFEND, mengurangi damage serangan di ronde ini!")

    def refresh_mp(self):
        self.mana = self.max_mana
        print(f"{self.name} menggunakan Refresh MP dan MP kembali ke {self.max_mana}!")

    def reset_round(self):
        self.defense = 0
        if self.silence_turns > 0:
            self.silence_turns -= 1
        self.action = None
        self.selected_skill = None

    def status(self):
        print(f"{self.name}: HP = {self.hp}, MP = {self.mana}, Attack = {self.attack}, Accuracy = {self.accuracy}, Dodge = {self.dodge}")

robot1 = Robot("Robot Atteraus", attack=25, hp=100, mana=10, accuracy=80)
robot2 = Robot("Robot Behemoth", attack=20, hp=120, mana=10, accuracy=85)

rounds = 1
while robot1.hp > 0 and robot2.hp > 0:
    print(f"\n=== ROUND {rounds} ===")
    
    def pilih_aksi(robot, enemy):
        print(f"\n[{robot.name}] Pilih Aksi: 1. Attack 2. Defend 3. Give Up", end="")
        if rounds % 2 == 0 and robot.silence_turns == 0 and robot.mana >= 5:
            print(" 4. Skill", end="")
        print()
        action = input("Pilihan: ")
        
        if action == "4" and (rounds % 2 == 0 and robot.silence_turns == 0 and robot.mana >= 5):
            print("Pilih Skill: 1. 200% Damage 2. Lifesteal 3. Buff HP & Attack 4. Buff Accuracy 5. Buff Dodge 6. Stun 7. Silence")
            skill_choice = input(f"{robot.name}, pilih skill: ")
            skills = ["200_damage", "lifesteal", "buff_hp_attack", "buff_accuracy", "buff_dodge", "stun", "silence"]
            if skill_choice in [str(i) for i in range(1, 8)]:
                robot.selected_skill = skills[int(skill_choice) - 1]
                if robot.selected_skill == "silence":
                    enemy.silence_turns = 3
                    print(f"{robot.name} menggunakan SILENCE! {enemy.name} tidak bisa memakai skill selama 3 ronde.")
                    robot.selected_skill = None
                    return pilih_aksi(robot, enemy)  # Kembali ke pilihan aksi tanpa skill
        return action
    
    robot1.action = pilih_aksi(robot1, robot2)
    robot2.action = pilih_aksi(robot2, robot1)
    
    for robot, enemy in [(robot1, robot2), (robot2, robot1)]:
        if robot.action == "1":
            robot.attack_enemy(enemy)
        elif robot.action == "2":
            robot.defend()
        elif robot.action == "3":
            print(f"{robot.name} menyerah! {enemy.name} MENANG!")
            exit()
    
    for robot, enemy in [(robot1, robot2), (robot2, robot1)]:
        if robot.selected_skill:
            robot.use_skill(enemy)
    
    robot1.reset_round()
    robot2.reset_round()
    
    robot1.status()
    robot2.status()
    
    rounds += 1

print("\n=== HASIL PERTARUNGAN ===")
if robot1.hp > 0:
    print(f"{robot1.name} MENANG!")
elif robot2.hp > 0:
    print(f"{robot2.name} MENANG!")
else:
    print("PERTARUNGAN SERI!")
