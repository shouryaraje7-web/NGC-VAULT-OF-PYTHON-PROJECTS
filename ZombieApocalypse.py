print("🧟‍♂️ZOMBIE APOCALYPSE!!!")
print("created by NextGenCoder an intermediate python developer created his first game.")
print()

# Player
class Player:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

player = Player("User", 100, 25)

# Zombies
class enemy:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

# Types of Zombies and all variables     
walker = enemy("Walker", 50, 10)
runner = enemy("Runner", 30, 15)
mutant = enemy("Mutant", 80, 20)
zombie = "walker"
player_strike = "" 
zombie_strike = "" 

# If zombie attacks player
if zombie == "Walker":
    zombie_strike = player.hp - walker.attack
    player.hp = zombie_strike
    print(f"Walker HP: {player.hp}")
elif zombie == "Runner":
    zombie_strike = player.hp - runner.attack
    player.hp = zombie_strike
    print(f"Runner HP: {player.hp}")
elif zombie == "Mutant":
    zombie_strike = player.hp - mutant.attack
    player.hp = zombie_strike
    print(f"Mutant HP: {player.hp}")    

# Actual Story Visual
# Walker zombie
user = input("Type a name for your character: ").strip()
if not user:
    user = "Hero"
print("WOW! nice user name⭐")
print("➡️ Guide: Type 'A' for Attack or 'H' for heal ⬅️")
print()
print("================================")
print("📍 SYSTEM ALERT: Sector-7 Lab")
print("⚠️ STATUS: Virus Outbreak Active")
print("🚨 DETECTED: A Walker Zombie dropping from vent!")
print("================================")

choice2 = ""
while True:
    Choice = input(f"{user}'s Choice: ")
    choice = Choice.upper().strip()
    
    if choice == "A":
        print()
        print(f"💥 Walker Zombie was attacked by {user}")
        print(f"Walker Zombie HP: {walker.hp}")
        print()
        
        print(f"💥 The Walker zombie swiped at {user}!")
        print(f"🩸 {user}'s HP: {player.hp - walker.attack}")
        print()
        
        while True:
            Choice2 = input(f"{user}'s Choice: ")
            choice2 = Choice2.upper().strip()
            if choice2 in ["A", "H"]:
                break
            print("Invalid choice! Type 'A' or 'H'.\n")
        break
            
    elif choice == "H":
        print("Health is already full♥️♥️♥️♥️♥️\n")
    else:
        print("Invalid choice! Type 'A' or 'H'.\n")

if choice2 == "A":
    print(f"☠️ Boom! Walker zombie was defeated by {user}!\n")
elif choice2 == "H":
    print(f"✅ {user} healed himself, HP: {player.hp}")
    print(f"💥 Walker zombie again attacked on {user}")
    print(f"♥️ {user} HP: {player.hp - walker.attack}\n")
    
    while True:
        Choice3 = input(f"{user}'s Choice: ")
        choice3 = Choice3.upper().strip()

        if choice3 == "A":
            print(f"☠️ Boom! Walker zombie was defeated by {user}!💥\n")
            break
        elif choice3 == "H":
            print(f"♥️ {user} Healed and ☠️ Boom! Walker zombie was defeated by {user}💥\n")
            break
        else:
            print("Invalid choice! Type 'A' or 'H'.\n")

# Runner zombie 
print()
print("==========================================")
print("🚨 WARNING: FAST-MOVING THREAT DETECTED!")
print("==========================================")
print("The heavy metal doors at the end of the hall burst open!")
print("Screeching loudly, a hyper-aggressive RUNNER ZOMBIE sprints towards you at terrifying speed!")
print(f"⚡ Get ready {user}! The Runner Zombie is right in your face!")
print("==========================================\n")
print()

while True:
    Choice4 = input(f"{user}'s Choice: ")
    choice4 = Choice4.upper().strip()
    
    if choice4 == "A":
        print(f"💥 {user} attacked the runner zombie")
        print(f"Runner zombie HP: {runner.hp - player.attack}")
        print("Zombie ran away ☠️\n")
        break
    
    elif choice4 == "H":
        print(f"♥️ {user} healed hp: 95")
        print("🧟‍♂️ Runner zombie tried to bite {user}\n")
        
        while True:
            B = input("Type Dodge word to dodge here: ").strip().lower()
            if B == "dodge":
                print("💥 User dodged and shot the Runner zombie 🔥\n")
                break
            else:
                print("Invalid choice! Type 'dodge' to survive.\n")
        break
    else:
        print("Invalid choice! Type 'A' or 'H'.\n")

# Mutant boss
print()
print("==================================================")
print("🚨 🚨 🚨 CRITICAL THREAT LEVEL: MAXIMUM 🚨 🚨 🚨")
print("==================================================")
print("The ground trembles as massive footprints echo through Sector-7...")
print("A towering, bio-engineered MUTANT BOSS smashes through the wall!")
print(f"☠️ THIS IS THE FINAL BATTLE, {user}! SURVIVE OR PERISH! ☠️")
print("==================================================\n")
print()

while True:
    type_choice = input(f"Enter choice for {user} (A/B): ").upper().strip()
    if type_choice == "A":
        print(f"{user} tried to attack mutant zombie💥💥")
        print(f"mutant zombie HP♥️: {mutant.hp - player.attack}\n")
        print("USER SPECIAL ATTACK UNLOCK MAX POWER💥💥\n")
        break
    elif type_choice == "B":
        print(f"♥️ {user} healed hp\n")
        break
    else:
        print("Invalid choice! Type 'A' or 'B'.\n")

print("Type 'MAXX' to use power")    

while True:
    chose = input(f"{user}'s Choice: ").upper().strip()
    if chose == "MAXX":
        print(f"{user} used MAXX Power on the Mutant Boss")
        print("Mutant Boss is getting weaker!!!")
        print("Mutant Boss is finally defeated!\n")
        break
    else:
        print("Invalid choice! Type 'MAXX' to trigger your special power.\n")

print(f"After killing Mutant Boss, {user} was honoured with SuperMan award from the city mayor!") 
print(f"{user}'s Aura ♾️\n")

while True:
    thanks = input("Type A here to view credits: ").upper().strip()
    if thanks == "A":
        print("\nGame presented by an indie intermediate developer")
        print("NextGenCoder")
        print("ALL COPYRIGHTS RESERVED")
        break
    else:
        print("Nice try! But incorrect choice. Type 'A' to continue.")
        