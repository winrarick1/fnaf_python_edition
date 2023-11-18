# created by winrarick1

import random
import time

if __name__ == "__main__":
    phone = False
    doors = {"left": False, "right": False}
    energy = 101
    used = 1
    freddy = ["none", False]
    action = None
    time_of_freddy = 0

print("""
Five Nights at Freddy (Python Edition)

1. Play
2. Exit""")

while True:
    menu = input('\nNumber of button: ')
    if menu == "1":
        print('Loading...')
        time.sleep(2)
        break
    elif menu == "2":
        print('Exiting...')
        time.sleep(1)
        break
    else:
        print("Error!")
        continue

print('Night 1')

phone = True

print("""
Example:
left true
phone false""")
for i in range(100):
    energy -= used
    if energy <= 1:
        print("\nGame Over...")
        break
    if freddy[0] == "left" and doors["left"] == True or freddy[0] == "right" and doors["right"] == True:
        freddy = ["none", False]
        time_of_freddy = 0
    elif freddy[0] == "none":
        time_of_freddy = 0
    else:
        time_of_freddy += 1
        if time_of_freddy == 3:
            print("\nGame Over...")
            energy = 0
            break
    random_freddy = random.randint(1, 5)
    if random_freddy == 4:
        if random.randint(1, 2) == 1:
            freddy[0] = "left"
        else:
            freddy[0] = "right"
        freddy[1] = True
    print(f"""
Doors: {doors}
Freddy_is_here?: {freddy}
Phone_is_calling?: {phone}
Energy: {energy}%
    """)
    print("Your action:", end=" ")
    action = input()
    action = action.split()
    if len(action) == 2:
        if "left" in action[0] or "right" in action[0]:
            if action[1] == "false":
                if doors[action[0]] == True:
                    doors[action[0]] = False
                    used -= 1
            elif action[1] == "true":
                if doors[action[0]] == False:
                    doors[action[0]] = True
                    used += 1
        if "phone" in action[0]:
            if action[1] == "false":
                if phone == True:
                    phone = False
                    used -= 1
if energy >= 0:
    print("\n6 AM!")

input("Press Enter to Continue... ")
