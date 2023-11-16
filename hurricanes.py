windfall = input("What are the mph?")
mph = int(windfall)

if 74 <= mph <= 95:
    print("Category 1 with minimal damage at landfall and storm surge of 4-5 feet")
elif 96 <= mph <= 110:
    print("Category 2 with moderate damage at landfall and storm surge of 6-8 feet")
elif 111 <= mph <= 130:
    print("Category 3 with extensive damage at landfall and storm surge of 9-12 feet")
elif 131 <= mph <= 155:
    print("Category 4 with extreme damage at landfall and storm surge of 13-18 feet")
elif mph >= 155 :
    print("Category 5 with catastrophic damage at landfall and storm surge of 19+ feet")