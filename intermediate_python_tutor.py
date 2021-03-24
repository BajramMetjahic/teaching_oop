import random


class Game():
    def __init__(self,enemy_type,gear,player_weapon):
        self.enemy = enemy_type
        self.weapon = gear
        self.hp = random.randrange(20,40)
        # maximum hp you can heal to:
            # can increase maxhp with armor, shields, etc
        self.maxhp = 200
        self.player_armor = "no armor"
        self.alive = True
        self.hit_lower = 0
        self.hit_upper = 20
        self.player_weapon = player_weapon
        self.player_hp = random.randrange(100,150)
        self.player_alive = True
        self.coins = 100
        self.player_hit_lower = 0
        self.player_hit_upper = 20
        self.armor_deflect = 0
        # 'weapon name': [price, lower bound damage, upper bound damage]
        self.store_inventory = {"axe":[40,12,22], "spear":[30,10,20], "bow":[35,11,21], "lightsaber":[1000,100,200],
        "katana":[50,15,25], "rock":[1,0,5], "flaming death sword":[1200,150,250], "broadsword":[350,35,45], "poisoned crossbow":[500,50,60]}

        # 'armor name': [price, new maxhp (heal to), deflection]
        self.armor_inventory = {"leather armor":[150,175,3], "chainmail armor":[250,200,5], "roman armor":[300,250,8], "steel armor":[350,275,12], "alien tech armor":[800,500,15], "star armor":[1000,650,25],"almost invincible armor":[5000,1000,50]}


    def fight_player(self, tgt):

        hit = random.randrange(self.player_hit_lower,self.player_hit_upper)
        print("\n")

        if self.alive == True and self.player_alive == True:
            print("You hit the " + self.enemy + " for " + str(hit) + ".")
            self.hp = self.hp - hit

            if self.hp >= 0:
                print("The " + self.enemy + " has " + str(self.hp) + " HP remaining.")

            elif self.hp <0:
                # not allowing for HP to go below zero
                self.hp = 0
                print("The " + self.enemy + " has " + str(self.hp) + " HP remaining.")
                self.alive = False

            # only allow enemy to attack if their HP is above 0:



    def fight_enemy(self, tgt):
        if self.hp > 0:

            print("\n")
            print("Enemy " + "Turn:")
            enemy_hit = random.randrange(self.hit_lower,self.hit_upper)
            print("The " + self.enemy + " tried to hit you for " + str(enemy_hit) + " damage.")
            print("Your armor deflected " + str(self.armor_deflect) + " damage")
            enemy_hit = enemy_hit - self.armor_deflect

            # if deflection greater than enemy_hit, do 0 damage, not negative
            if enemy_hit < 0:
                enemy_hit = 0

            print("The " + self.enemy + " actually hit you for " + str(enemy_hit) + " damage.")


            self.player_hp = self.player_hp - enemy_hit


            if self.player_hp >=0:
                print("You have " + str(self.player_hp) + " HP" + " remaining")

            elif self.player_hp < 0:
                self.player_hp = 0
                print("You have " + str(self.player_hp) + " HP" + " remaining")
                self.player_alive = False






    def heal(self, tgt):
            if self.player_alive == True and self.alive == True:
                player_heal = random.randrange(0,15)
                # only heal if healing would not exceed your maxhp:
                if player_heal + self.player_hp <= self.maxhp:
                    self.player_hp += player_heal
                    print("You healed " + str(player_heal) + " and now have " + str(self.player_hp) + " HP. You have " + str(self.coins) + " coins left.")
                    print("\n")
                else:
                    # refund coins if cannot heal
                    self.coins += 10
                    print("You cannot heal as you would exceed your max HP.")
                    print("\n")


    def store(self):


        print("\n")
        print("Welcome to the store, choose from my wares!")
        print("\n")
        choice = input("Do you want to look at weapons or armor? Type w for weapons, a for armor or s to leave.")

        # if they want to see weapons:
        if choice == "w":

            print(self.store_inventory)
            print("\n")
            print("You have " + str(self.coins) + " coins.")
            print("\n")
            print("Type the name of a weapon to buy and equip it or press s to leave:")
            print("\n")


            weapon_choice = input()

            if weapon_choice in self.store_inventory and self.coins >= self.store_inventory[weapon_choice][0]:
                self.player_weapon = weapon_choice
                self.coins = self.coins - self.store_inventory[weapon_choice][0]

                # set your new attack damage boundaries:
                self.player_hit_lower = self.store_inventory[weapon_choice][1]
                self.player_hit_upper = self.store_inventory[weapon_choice][2]


            # leave the store
            elif weapon_choice == "s":
                print('\n')
                print("Buy something next time you cheapskate!")
                print('\n')
                return


            # if you did not state a valid weapon:
            elif weapon_choice not in self.store_inventory:
                print("I dont have that weapon in stock, maybe try again")
                # recursion:
                self.store()


            # if you don't have enough money:
            elif self.coins < self.store_inventory[weapon_choice][0]:
                print("You dont have enough coins for that, come again later")

        # if they want to see armor:
        if choice == "a":

            print(self.armor_inventory)
            print("\n")
            print("You have " + str(self.coins) + " coins.")
            print("\n")
            print("Type the name of an armor to buy and equip it or press s to leave:")
            print("\n")


            armor_choice = input()

            if armor_choice in self.armor_inventory and self.coins >= self.armor_inventory[armor_choice][0]:
                self.player_armor = armor_choice
                self.coins = self.coins - self.armor_inventory[armor_choice][0]

                # set your new maxhp:
                self.maxhp = self.armor_inventory[armor_choice][1]
                # buying armor also heals you to your new maxhp:
                self.player_hp = self.maxhp
                # change your deflection:
                self.armor_deflect = self.armor_inventory[armor_choice][2]

            # leave the store
            elif armor_choice == "s":
                print('\n')
                print("Buy something next time you cheapskate!")
                print('\n')
                return


            # if you did not state a valid armor:
            elif armor_choice not in self.armor_inventory:
                print("I dont have that armor in stock, maybe try again")
                # recursion:
                self.store()


            # if you don't have enough money:
            elif self.coins < self.armor_inventory[armor_choice][0]:
                print("You dont have enough coins for that, come again later")



            print("you have " + str(self.coins) + " coins left")
            print("you have " + self.player_armor + " equipped as your armor")
            if self.player_armor != "no armor":
                print("your new max HP is " + str(self.maxhp) + " and you have been fully healed.")
            print("\n")

        if choice == "s":
            print('\n')
            print("Buy something next time you cheapskate!")
            print('\n')
            return




# game start:


# specify enemy type and weapon here:
    # make easier enemy types more numerous and thus more likely to get in a given fight

enemy_list = ["goblin", "goblin", "goblin", "goblin", "goblin", "goblin", "goblin", "goblin", "goblin", "goblin", "goblin", "goblin", "goblin", "goblin", "troll", "troll", "troll", "troll", "troll", "troll", "troll", "troll", "troll", "troll", "witch", "witch", "witch", "warlock", "warlock", "warlock", "werewolf", "werewolf", "dragon", "kracken"]


enemy_weapon_dict = {"dragon":"fire", "goblin":"knife", "troll":"club", "witch":"cursed broom", "warlock":"potion", "werewolf":"fangs", "kracken":"tentacles"}

enemy_hp_range = {"dragon":[500,600], "goblin":[10,20], "troll":[25,35], "witch":[40,50], "warlock":[100,150], "werewolf":[250,300], "kracken":[800,1000]}
enemy_d_range = {"dragon":[35,45], "goblin":[1,5], "troll":[5,10], "witch":[15,20], "warlock":[15,20], "werewolf":[20,30], "kracken":[50,70]}

# randomly choose an enemy for first enemy:
enemy1_type = random.choice(enemy_list)
# set correct weapon for this type of enemy:
enemy1_weapon = enemy_weapon_dict[enemy1_type]
# find an hp in specified range for this specific instance of this enemy type:
enemy1_hp = random.randrange(enemy_hp_range[enemy1_type][0], enemy_hp_range[enemy1_type][1])
# find damage range:
# enemy1_d = random.randrange(enemy_d_range[enemy1_type][0], enemy_d_range[enemy1_type][1])



foe = Game(enemy1_type, enemy1_weapon, "sword")
# set hp:
foe.hp = enemy1_hp
# upper and lower ranges of attack damage:
foe.hit_upper = enemy_d_range[enemy1_type][0]
foe.hit_upper = enemy_d_range[enemy1_type][1]



print("You are a fearsome warrior using a " + foe.player_weapon + " and with " + str(foe.player_hp) + " HP.")
print("You meet a " + foe.enemy + " using a " + foe.weapon + " weapon and with " + str(foe.hp) + " HP.")


# game loop:

end = False

# before game loop starts, game takes you to store:

foe.store()

turn = 0

while end != True:

    print("Type the a key to attack, h to heal, or q to quit then ENTER!")

    action = input()

    if action == "a":
        foe.fight_player(foe)
        foe.fight_enemy(foe)

    if action == "h":
        # only allow you to heal if you have enough coins to heal:
        if foe.coins >= 10:
            foe.heal(foe)
            foe.coins -= 10
            foe.fight_enemy(foe)
        # if you don't have enough coins to heal:
        else:
            print("You dont have enough coins to heal!")


    if action == "q":
        print('\n')
        print("The cowardly player fled the battlefield!")
        end = True

    if foe.alive == False:
        # game now goes until you die:
        print("You have slain the " + foe.enemy + ".")

        # you get a powerup based on type of enemy:
        if foe.enemy == "dragon":
            # if you kill a dragon, your hp is refilled to its max
            # and you get a bunch of coins
            foe.player_hp = foe.maxhp
            foe.coins = foe.coins*2
            print("You plundered the dragons horde and doubled your gold, and refilled your HP")
            print('You have ' + str(foe.coins) + " gold and " + str(foe.player_hp) + " HP")


            dragon_kill_turn = turn

            # increase damage by 50%:


            print("old lower: " + str(foe.player_hit_lower))
            print("old upper: " + str(foe.player_hit_upper))
            old_lower = foe.player_hit_lower
            old_upper = foe.player_hit_upper

            foe.player_hit_lower = foe.player_hit_lower*1.5
            foe.player_hit_upper = foe.player_hit_upper*1.5


            print("new lower: " + str(foe.player_hit_lower))
            print("new upper: " + str(foe.player_hit_upper))


            print("You are a mighty warrior and your damage has increased 50% for the next 5 battles")
            print('\n')


        # put damage back to normal after 5 turns:
        if turn - dragon_kill_turn >= 5:
            foe.player_hit_lower = old_lower
            foe.player_hit_upper = old_upper

            print("lower back to: " + str(foe.player_hit_lower))
            print("upper back to: " + str(foe.player_hit_upper))
            print("You have returned to normal strength, young warrior.")
            print("\n")


        if foe.enemy == "werewolf":
            # restore up to maxhp - 50
            if foe.player_hp < foe.maxhp - 50:
                foe.player_hp = foe.maxhp - 50
            else:
                foe.player_hp += 50

            foe.coins +=100
            print("You received 100 coins and a partial HP refill for slaying the mighty werewolf.")

        # increase to the next turn every time you kill an enemy:
        turn += 1



        # before you go to the store, let's update how many coins you have based on
            # initial HP of enemy you just killed:

        foe.coins = foe.coins + enemy1_hp

        # before you go on to next enemy, you get some coins and opportunity to go to the score:
        foe.store()


        # make a new enemy with new attributes:
        enemy_new = random.choice(enemy_list)
        foe.enemy = enemy_new
        foe.weapon = enemy_weapon_dict[enemy_new]
        enemy1_hp = random.randrange(enemy_hp_range[enemy_new][0], enemy_hp_range[enemy_new][1])
        foe.hp = enemy1_hp
        foe.hit_upper = enemy_d_range[enemy_new][0]
        foe.hit_upper = enemy_d_range[enemy_new][1]
        foe.alive = True






        print("You are a fearsome warrior using a " + foe.player_weapon + " and with " + str(foe.player_hp) + " HP.")
        print("You meet a " + foe.enemy + " using a " + foe.weapon + " weapon and with " + str(foe.hp) + " HP.")
        # end = True

    if foe.player_alive == False:
        print("You have been slain by the " + foe.enemy + ".")
        end = True








# working on now:


# inventory so you don't just lose weapons you have already bought
# different kinds of attacks with different buttons
# different effectiveness of weapons against different enemies
    # makes inventory useful






