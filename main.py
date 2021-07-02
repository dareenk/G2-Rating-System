if question=="1":
    cafes=input("1: The Coffee Club 2: Starbucks 3: Cafe Arabia ")
    if cafes=="1":
        print("4.1/5 Star Rating")
    elif cafes=="2":
        print("3/5 Star Rating")
    elif cafes=="3":
        print("5/5 Star Rating")
    else:
        print("Sorry, it's not in the list")
if question == "2":  # question is the var chosen initially

    name = input("Please enter the resturant/cafe name.")  # name is the restaurant/cafe var
    print("Rating for", name)

    print("Please provide ratings on a scale of 1 to 5 stars.")
    food = int(input("How would you rate the food quality?"))  # food quality
    if food <= 2:  # var should be changed to a table index when the table is created
        input("Thank you for your honest review! Would you mind explaining the reasoning for this rating?")

    environment = int(input("How would you rate the overall enviroment?"))  # environment
    if environment <= 2:  # var should be changed to a table index when the table is created
        input("Thank you for your honest review! Would you mind explaining the reasoning for this rating?")

    service = int(input("How would you rate the service provided by staff?"))  # staff service
    if service <= 2:  # var should be changed to a table index when the table is created
        input("Thank you for your honest review! Would you mind explaining the reasoning for this rating?")
