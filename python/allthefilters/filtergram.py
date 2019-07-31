#filtergram

#import our functions we made in filters.py
import filters

def main():
    # ask user for filename to modify
    filename=input("Enter the name of the image file:  ")
    #print(filename)

    #load the image
    image = filters.load_img(filename)

    #obama
    new_image = filters.invert(image)

    #save new image
    filters.save_img(new_image, "filtered.jpg")

if __name__ == '__main__':
    main()






    # apply the filter!
    #new_image = filters.obamicon(image)
    # done = False
    # while not done:
    #     addfilter = input("Would you like to add a filter?")
    #     if addfilter == "yes":
    #         filternames = []
    #         print(filternames)
    #         filtername =input("what filter would you like to add?")
    #     else:
    #         break
