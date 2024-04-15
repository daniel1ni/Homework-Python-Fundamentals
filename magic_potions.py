potions = {"Invisibility potion":["Moonstone","Dragon scale","Fairy dust"], "Flying potion":["Phoenix feather", "Troll tooth", "Mermaid scale"], "Healing potion": ["Unicorn horn", "Elf hair", "Golden apple"]}
print("Welcome to the magic potion shop!")
print("Here are the potions we offer:")
for key in potions:
    print(key)

desired_potion = input('Which potion would you like to buy ingredients for?\n')
print()
print(f"The ingredients for the {desired_potion} are:")

def check_all_yes(inputs):
    return all(input_str.lower()== "yes" for input_str in inputs)

def someIngredients(x):
    ingredients = potions[x]
    for y in ingredients:
        print(y)
    print()
    print("Let's start buying the ingredients!")
    for y in ingredients:
        answer = []
        propose_to_buy = input(f"Do you want to buy {y} (yes/no)?")
        if propose_to_buy == "yes":
            print(f"You bought {y}")
            continue    
                     
        elif propose_to_buy == "no":
            print("You choose to stop shopping.")
            answer.append("no")
            break
        answer.append(propose_to_buy)

    if check_all_yes(answer):
        print(f"Congratulations! You bought all the ingredients for the {desired_potion}")
      
        
if desired_potion == "Invisibility potion":
    someIngredients(desired_potion)
elif desired_potion == "Flying potion":
   someIngredients(desired_potion)
elif desired_potion == "Healing potion":
   someIngredients(desired_potion)

    