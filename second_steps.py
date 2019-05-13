# Exercise 2

# Satellites:
sat_database = {"METEOSAT" : 3000,
                "LANDSAT"  : 30,
                "MODIS"    : 500
               }

# The dictionary above contains the names and spatial resolutions of some satellite systems.

# 1) Add the "GOES" and "worldview" satellites with their 2000/0.31m resolution to the dictionary [2P]

sat_database["GOES"] = 2000
sat_database["worldview"] = 0,31

print("I have the following satellites in my database:")

# 2) print out all satellite names contained in the dictionary [2P]

for x in sat_database.keys():
    print(x)

# 3) Ask the user to enter the satellite name from which she/he would like to know the resolution [2P]

# 4) Check, if the satellite is in the database and inform the user, if it is not [2P]

# 5) If the satellite name is in the database, print a meaningful message containing the satellite name and it's resolution [2P] 



# below this line is the answer to task 3), 4) and 5)

print(" ")
condition_check = True

while condition_check == True:
    print("What do you want to do?")
    userYesNo = input("Checking satellite resolutions[1]\rAdd/Delete entry[2]\rExit program[exit]\r ")
    
    
    print(" ")

    if userYesNo == "1":
        
        # answer to task 3)
        check_check = True
        userSat = input("From which satellite you'd like to know the resolution? ")
        
        while check_check == True:
            if userSat in sat_database: #answer to task 4)
                print("The spatial resolution of {} is {}".format(userSat, sat_database.get(userSat))) #answer to task 5)
                print(" ")
                check_check = True
                userSat = input("Check another one: ")

        
            else:
                print(" ")
                print("This entry doesn't exist. The resolution of the following satellites can be returned: ")
                for v in sat_database.keys():
                    print(v)
                    check_check = False
                print(" ")
        
#below this line is random stuff i did because i was bored.        
        
    elif userYesNo == "2":
        userAddDel = input("Do you want to add/delete a satellite or go back? (add/del/back)")
        
        if userAddDel == "add":
            userAddName = input("What's the name of your satellite? ")
            userAddValue = input("What's the resolution of your satellite? \r")
            sat_database[userAddName] = userAddValue
            print("The satellite '{}' with the resolution '{}' has been added to the database.".format(userAddName, userAddValue))
            print(" ")
            
        elif userAddDel == "del":
            print("The following satellites can be deleted.")
            for v in sat_database.keys():
                print(v)
                
            print(" ")    
            userDel = input("Please enter a name or go back. ('name'/back) ")
            
            if userDel in sat_database:
                print("The satellite '{}' with the resolution '{}' has been deleted.\r".format(userDel, sat_database.get(userDel)))
                sat_database.pop(userDel, 0)              
                continue
            
            elif userDel == "back":
                print(" ") 
                continue     
            
            else:
                print("This satellite doesnt exist.\r")           
            
        elif userAddDel == "back":
            continue    
    
    elif userYesNo == "exit":
        print("OK. Bye then. This little program was created by morphi01.")
        condition_check = False
        
    else:
        print("This was not a legitimate answer. Check the brackets. \r")
