def sorting_hat():
    houses = {"Gryffindor": 0, "Ravenclaw": 0, "Hufflepuff": 0, "Slytherin": 0}

    # Question 1
    answer = int(input("Do you like Dawn or Dusk?\n1) Dawn\n2) Dusk\n"))
    if answer == 1:
        houses["Gryffindor"] += 1
        houses["Ravenclaw"] += 1
    elif answer == 2:
        houses["Hufflepuff"] += 1
        houses["Slytherin"] += 1
    else:
        print("Wrong input.")

    # Question 2
    answer = int(input("When I’m dead, I want people to remember me as:\n1) The Good\n2) The Great\n3) The Wise\n4) The Bold\n"))
    if answer == 1:
        houses["Hufflepuff"] += 2
    elif answer == 2:
        houses["Slytherin"] += 2
    elif answer == 3:
        houses["Ravenclaw"] += 2
    elif answer == 4:
        houses["Gryffindor"] += 2
    else:
        print("Wrong input.")

    # Question 3
    answer = int(input("Which kind of instrument most pleases your ear?\n1) The violin\n2) The trumpet\n3) The piano\n4) The drum\n"))
    if answer == 1:
        houses["Slytherin"] += 4
    elif answer == 2:
        houses["Hufflepuff"] += 4
    elif answer == 3:
        houses["Ravenclaw"] += 4
    elif answer == 4:
        houses["Gryffindor"] += 4
    else:
        print("Wrong input.")

    # Determine the house with the most points
    max_points = max(houses.values())
    for house, points in houses.items():
        if points == max_points:
            print(f"The house with the most points is: {house}")

sorting_hat()