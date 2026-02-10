# A for loop can also be used to iterate through a list, tuple, string or even a dictiomnary..

name="Amani"

for letter  in name:
    if letter == "a":
        print("the letter is a")
    else:
        print(letter)

print("=====================")         
# Below is a list of counties
counties=["Nairobi", "Mombasa", "Kisumu","Nakuru","Eldoret","Kajiado","Machakos","Meru","Embu"]

print(counties)

for county in counties:
    print(county)

print("=====================") 

for county in counties:
    if "Nakuru" in  counties:
        print("the county is part of the list Nakuru")
        break
    else:
        print("The county is not part of the list")

print("=====================") 
# The for loop can also be used to iteratethrough a dictionary

player={
    "name":"Mbappe",
    "Age":25,
    "teams":["PSG","Monaco","France"],
}
for key in player:
    print(key) 
print("=====================")

for value in player:
    print(player[value]) 
# print(player["name"])

print("=====================")
# loop throught the teams the player has played for
for team in player["teams"] :
    print(team)

         
      

    
        
    
    
    

    