
#treasure island , choose your own path game

print("")
print("         ,     \    /      ,         ")
print("        / \    )\__/(     / \        ")
print("       /   \  (_\  /_)   /   \       ")
print("  ____/_____\__\@  @/___/_____\____  ")
print(" |             |\../|              | ")
print(" |              \VV/               | ")
print(" |   Welcome to Treasure Island    | ")
print(" |_________________________________| ")
print("  |    /\ /      \\       \ /\    |  ")
print("  |  /   V        ))       V   \  |  ")
print("  |/     `       //        '     \|  ")
print("  `              V                '  ")
print("")

print("")
print("Your mission is to find the treasure!")
first_choice= input("You are stuck at a crossroad, do you go 'left' or 'right'? ")
if first_choice == "left":
    print("You head left and walk briskly on the path.")

    second_choice= input("A river blocks your path. You find a port. Do you 'wait' for a boat, or 'swim' across? ")
    if second_choice=="wait":
        print("You wait for a fisherman who comes and ferries you across the river!")

        third_choice= input("You reach a hut next to an old hut. Do you go into the 'hut' or into the 'cave'? ")
        if third_choice == "cave":
            print("Congratulations! You have found the treasure chest! YOU WIN!")

        else:
            print("A boulder rolls down the cliff ontop of you...GAME OVER!")

    else:
        print("A river spirit drags you into the depths of the river and you lose consciousness... GAME OVER!")

else:
    print("A harpy picks you up and carries you off... GAME OVER!")
