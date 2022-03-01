#TODO 1. Create a greeting for your program.
print("Welcome to the Band Name Generator.")

#TODO 2. Ask the user for the city that they grew up in.
city_name = input("What's name of the city you grew up in?\n")

#TODO 3. Ask the user for the name of a pet.
pet_name = input("What's your pet's name?\n")

#TODO 4. Combine the name if their city and pet and show them their band name.
band_name = city_name + " " + pet_name
print("Your band name could be {} ".format(band_name))

#TODO 5. Make sure the input cursor shows on a new line, see the example at:
# https://band-name-generator-end.appbrewery.repl.run/