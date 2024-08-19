#First person information
gender1 = "boy"
height1 = 185
weight1 = 83
eye_Color1 = "black"
name1 ="you are Ali"

#Information of the second person
gender2 = "boy"
height2 = 181
weight2 = 78
eye_Color2 = "blue"
name2 ="you are Hossein"

#Third party information
gender3 = "girl"
height3 = 181
weight3 = 70
eye_Color3 = "brown"
name3 ="you are Fatemeh"

#Getting information from the user with input

gender4 = input("Enter your gender:\n")
while (True):
    try:
        height4 = int(input("Enter your height:\n"))
        break
    except:
        print("Please enter a number")
while (True):
    try:
        weight4 = int(input("Enter your weight:\n"))
        break
    except:
        print("Please enter a number")
eye_Color4 = input("Enter your eye color:\n")

#Checking whether the entered information is 
#the same as the information of each registered user
if gender4 == "boy" and height4 == 185 and weight4 == 83 and eye_Color4 == "black" :
    print(f"\n{name1}😊")
elif gender4 == "boy" and height4 == 181 and weight4 == 78 and eye_Color4 == "blue" :
    print(f"\n{name2}😊")
elif gender4 == "girl" and height4 == 181 and weight4 == 70 and eye_Color4 == "brown":
    print(f"\n{name3}😊")
else :
    print("There is no person with this profile in the program!🤨")