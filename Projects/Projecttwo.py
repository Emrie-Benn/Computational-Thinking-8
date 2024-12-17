#Beginning

Farminggames_points = 0
Adventuregames_points = 0 


#Middle

answer = input("You can buy one book is it A) A book about local wildlife 0r B) A book about the best places to explore?")
if answer == "A":
    Farminggames_points += 1
elif answer == "B":
    Adventuregames_points += 1

answer = input( "A college is offering two extra classes, you can choose to participate in one, would you go to A) A class about where all the food in places like supermarkets, come from or B) a class where you visit different parks, museums, etc and participate in all sorts of activities?" )
if answer == "A":
    Farminggames_points += 1
elif answer == "B":
    Adventuregames_points += 1 

answer = input("You are hiking when you come across a crossroad, do you choose A) A trail that lead to steep hills, lakes, and caves or B) a trail lined with flowers and wildlife?")
if answer == "A":
    Adventuregames_points += 1
elif answer == "B":
    Farminggames_points += 1

answer = input("you are at a game store and can buy one game do you buy A) An escape game that is based in a cave or B) a game where you are running a farm and have to collect supplies?")
if answer == "A":
    Adventuregames_points += 1
elif answer == "B":
    Farminggames_points += 1

answer = input("You are going on a vacation with your friends and they are split evenly on where to go, you are the tiebreaker, do you want to go to A) A city with a flower festival or B) a backpacking trip up a mountain?")
if answer == "A":
    Farminggames_points += 1
elif answer == "B":
    Adventuregames_points += 1

#Ending

print("And you are a .....*Drumroll* ")

if Farminggames_points > Adventuregames_points:
    print("Farming game person")
elif Adventuregames_points > Farminggames_points:
    print("Adventure game person")