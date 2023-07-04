# testing 

# arknights standard banner roll thing simulation
# rates for gacha here:
# 2% for 6*, 8% for 5*, 50% for 4*, and 40% for 3*. Featured operators in banner will have a 50% chance to happen after the first check
# starting at 50, there will be a 2% increase in finding a 6* until it shines
# will do a 10 pull

import random
import string
import time

#this is for the user to see when pulling in gacha
sixname = ["Exusiai", "Siege", "Ifrit", "Eyjafjalla", "Angelina", "Shining", "Nightingale", "Hoshiguma", "Saria", "SilverAsh", "Skadi", "Ch'en", "Schwarz", "Hellagur", "Magallan", "Mostima", "Blaze", "Aak", "Ceobe", "Bagpipe", "Rosa (Poca)", "Suzuran", "Phantom", "Weedy", "Thorns", "Eunectes", "Surtr", "Blemishine", "Mudrock", "Mountain", "Archetto", "Saga", "Passenger", "Kal'tsit", "Carnelian", "Pallas", "Mizuki", "Saileach", "Fartooth", "Flametail", "Gnosis", "Lee", "Goldenglow", "Fiammetta", "Irene", "Ebenholz", "Pozëmka", "Dorothy", "Mlynar", "Stainless", "Penance"]

fivename = ["Ptilopsis", "Zima", "Texas", "Franka", "Lappland", "Specter", "Blue Poison", "Platinum", "Meteorite", "Skyfire", "Mayer", "Silence", "Warfarin", "Nearl", "Projekt Red", "Liskarm", "Croissant", "Provence", "Firewatch", "Cliffheart", "Pramanix", "Istina", "Sora", "Manticore", "FEater", "Nightmare", "Swire", "Glaucus", "Astesia", "Executor", "Waai Fu", "GreyThroat", "Broca", "Reed", "Hung", "Leizi", "Sesa", "Leonhardt", "Ayerscarpe", "Asbestos", "Tsukinogi", "Shamare", "Elysium", "Andreana", "Flint", "April", "Aosta", "Whisperain", "Kafka", "Iris", "Mr.Nothing", "Toddifons", "Akafuyu", "Kirara", "La Pluma", "Mulberry", "Ashlock", "Corroserum", "Aurora", "Blacknight", "Quercus", "Kazemaru", "Windflit", "Hibiscus the Purifier", "Cantabile", "Greyy the Lightningbearer", "Proviso", "Paprika", "Lunacub"]

fourname = ["Haze", "Gitano", "Jessica", "Meteor", "Shirayuki", "Scavenger", "Vigna", "Dobermann", "Matoimaru", "Frostleaf", "Mousse", "Gravel", "Rope", "Myrrh", "Perfumer", "Matterhorn", "Cuora", "Gummy", "Deepcolor", "Earthspirit", "Shaw", "Beehunter", "Greyy", "Sussurro", "Myrtle", "Vermeil", "May", "Ambriel", "Utage", "Podenco", "Click", "Cutter", "Jaye", "Aciddrop", "Arene", "Bubble", "Jackie", "Pinecone", "Beanstalk", "Indigo", "Roberta", "Totter"]

threename = ["Fang", "Vanilla", "Plume", "Melantha", "Cardigan", "Beagle", "Kroos", "Lava", "Hibiscus", "Ansel", "Steward", "Orchid", "Catapult", "Midnight", "Spot", "Popukar"]

#this is when the user wants to choose specific operators as featured or increased odds 50% before checking their pool
featuresixname = []
featurefivename = []
storedpulls = [] #this where all of user's six star and five star pulls stored, and if needed, show it on command


def info(): #this function shows all information of the program for the user
    print()
    print("This is made by DeVince(Twitter)/GitDeVince(Github).")
    print("All operators upto Joint Operation 8 (June 23, 2023 to July 4, 2023) except the 6 star alters in the global banner list are available.")
    print("Not sure if I'm able to provide a GUI for this project due to shift of interests thought I want to expand its capabilities as a gacha simulator.")

#standardtenpull means all operators are inside the pool
def standardtenpull(): #we first check the 1st pull if its guarantee six or 5 star. then we check the rest with a while loop

    #in ten pull, there will be 1 guarantee to be either 5 or 6 star
    goldguarantee = (random.randint(1, 100))

    if goldguarantee in range(1, 2):
        pulledsixstar = random.choice(sixname)
        print("6* " + pulledsixstar)
        storedpulls.append(pulledsixstar)

    else:
        pulledfivestar = random.choice(fivename)
        print("5* " + pulledfivestar)
        storedpulls.append(pulledfivestar)


    i = 1
    while i < 9:

        goldnotguarantee = (random.randint(1, 100))

        if goldnotguarantee in range(1, 2):
            pulledsixstar = random.choice(sixname)
            print("6* " + pulledsixstar)
            storedpulls.append(pulledsixstar)
            

        elif goldnotguarantee in range(3, 10):
            pulledfivestar = random.choice(fivename)
            print("5* " + pulledfivestar)
            storedpulls.append(pulledfivestar)
            


        elif goldnotguarantee in range(11, 40):
            pulledthreestar = random.choice(threename)
            print("3* " + pulledthreestar)

        else:
            pulledfourstar = random.choice(fourname)
            print("4* " + pulledfourstar)

        i += 1

def getsixstaroperator(): #input will type what operator will be in high odds. then we remove it from the main 6 star pool then add it in featuresixname
   while True:
        print()
        userinput = input("What 6 star operator you will feature? Type 'skip' if you are satisfied. ")
        userinput = userinput.title()

        if userinput in sixname:
            sixname.remove(userinput)
            print(f"{userinput} has chosen as featured operator!")
            featuresixname.append(userinput)

        elif userinput == "Skip":
            print("Let's proceed to the five stars.")
            break

        else:
            print()
            print(f"{userinput} is not found in the six star pool. Please input the full correct name.")
            continue

def getfivestaroperator(): # same thing as function getsixstaroperator but instead in featurefivename
    while True:
        print()
        userinput = input("What 5 star operator you will feature? Type 'skip if you are satisfied. ")
        userinput = userinput.title()
        print()

        if userinput in fivename:
            fivename.remove(userinput)
            print(f"{userinput} has chosen as featured operator!")
            featurefivename.append(userinput)
        
        elif userinput == "Skip":
            print("Let's proceed to the gacha.")
            break

        else:
            print()
            print(f"{userinput} is not found in the five star pool. Please input the full correct name.")
            continue

def featuredtenpull(): #same thing as standard but now we're looking first if gets the guarantee pull or the rest of the pool

    #goldguarantee is checking if its a 6 or 5 star operator
    goldguarantee = (random.randint(1, 100))

    if goldguarantee in range(1, 2):
        featurecheck = (random.randint(1, 100)) #this is another check to see if user gets the feature operator in 50% chance or take the other 50 in the pool

        if featurecheck in range(1, 50):
            pulledsixstar = random.choice(featuresixname) #uses picked six star as boosted odds
            print("6* " + pulledsixstar)
            storedpulls.append(pulledsixstar)


        else:
            pulledsixstar = random.choice(sixname)
            print("6* " + pulledsixstar)
            storedpulls.append(pulledsixstar)


    else: #same deal to the 5 star
        featurecheck = (random.randint(1, 100))

        if featurecheck in range(1, 50):
            pulledfivestar = random.choice(featurefivename) # uses picked five star as boosted odds
            print("5* " + pulledfivestar)
            storedpulls.append(pulledfivestar)


        else:
            pulledfivestar = random.choice(fivename)
            print("5* " + pulledfivestar)
            storedpulls.append(pulledfivestar)

    i = 1
    
    while i < 9:

        goldnotguarantee = (random.randint(1, 100))

        if goldnotguarantee in range(1, 2):
            featurecheck = (random.randint(1, 100))  # this is another check to see if user gets the feature operator in 50% chance or take the other 50 in the pool

            if featurecheck in range(1, 50):
                pulledsixstar = random.choice(featuresixname)
                print("6* " + pulledsixstar)
                storedpulls.append(pulledsixstar)


            else:
                pulledsixstar = random.choice(sixname)
                print("6* " + pulledsixstar)
                storedpulls.append(pulledsixstar)


        elif goldnotguarantee in range(3, 10):
            featurecheck = (random.randint(1, 100))

            if featurecheck in range(1, 50):
                pulledfivestar = random.choice(featurefivename)
                print("5* " + pulledfivestar)
                storedpulls.append(pulledfivestar)


            else:
                pulledfivestar = random.choice(fivename)
                print("5* " + pulledfivestar)
                storedpulls.append(pulledfivestar)


        elif goldnotguarantee in range(11, 40):
            pulledthreestar = random.choice(threename)
            print("3* " + pulledthreestar)


        else:
            pulledfourstar = random.choice(fourname)
            print("4* " + pulledfourstar)


        i += 1

def countdown(): #was thinking of putting a delay each ten pull
    print("waiting...")
    for x in range(2, 0, -1):
        time.sleep(1)


#start of the whole program
print("Arknights gacha simulator")

while True: 

    print()
    userpick = input("Do you want to go for a 'standard' or 'featured' pulls? Type 'show' to see the whole lists of 6 and 5 stars operator, type 'info' for more information, and type 'exit' to close the program. ")
    userpick = userpick.title().lower()

    if userpick == "standard":
        countdown()
        standardtenpull()
        print(storedpulls)

    elif userpick == "featured":
        getsixstaroperator()
        getfivestaroperator()

        while True:
            countdown()
            featuredtenpull()
            print(storedpulls)
            decision = input("Do you continue? Y/N: ")
            decision = decision.capitalize()
            if decision == "Y":
                print()
                continue
            elif decision == "N":
                break

    elif userpick == "show":
        print()
        print("These are the six star operators: ")
        print(sixname)
        print()
        print("These are the five star operators: ")
        print(fivename)
        print()

    elif userpick == "info":
        info()
    
    elif userpick == "exit":
        print('Thanks for playing!')
        break

    else:
        print("Please choose one of the options above.")
        continue