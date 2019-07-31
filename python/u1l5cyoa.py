SpaceShip = "Should we beam out of the space ship?"
WormHole = "Uh oh... looks like you got sucked into a wormhole!"
Vogsphere = "Welcome to Vogsphere! OH these Vogons are very unpleasent to be with... should we beam somewhere else?"
VogonJail = "Welp... looks like the Vogons didn't like you too much\n... They stuck you in jail before you could leave"
ExploreShip = "Would you like to explore the ship now?"
ExploreOther = "Yeah, this is pretty boring, would you like to explore another planet?"
VogonKitchen = "I bet the chefs will make us something! Do you want to ask?"
VogonChef = "The chefs filled you up, do you want to explore the ship now?"
END = "THE END"

done = False
while not(done):

    print("\nThe Adventure to Vogsphere")
    print("After every prompt, type y or n\n")

    num1 = input(SpaceShip+"  ")

    if num1.lower() == 'y': #leave the space ship
        num2 = input(Vogsphere+"  ")

        if num2.lower() == 'y': #beam off Vogon
            print(VogonJail)
            done = True
        else:
            num4 = input(VogonKitchen)
            if num4.lower() == 'y': #Vogon chefs
                num5 = input(VogonChef)
            else:
                num5 = input(ExploreShip)

            if num5.lower() == 'y': #explore
                print(VogonJail)
                done = True
            else:
                num6 = input(ExploreOther)

                if num6.lower() == 'y':
                    print("Ok, lets beam back up to the ship")
                    done = True
                else:
                    print("Guess you will just have find something else to do!")
                    done = True

    else:
        print(WormHole)
        done = True

    if done:
        print("Your adventure on Vogsphere has ended :(\n")
