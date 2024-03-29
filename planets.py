planet_list = ["Mercury", "Mars"]

#Pracice
#Instructions:
#1. Use append() to add Jupiter and Saturn at the end of the list.
planet_list.append("Jupiter")
planet_list.append("Saturn")

#2. Use the extend() method to add another list of the last two planets in our solar system to the end of the list.
planet_list.extend(["Uranus", "Neptune"])

#3. Use insert() to add Earth, and Venus in the correct order.
planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")

#4. Use append() again to add Pluto to the end of the list.
planet_list.append("Pluto")

#5. Now that all the planets are in the list, slice the list in order to get the rocky planets into a new list called rocky_planets.
rocky_slice = slice(4)
rocky_planets = planet_list[rocky_slice]

#6. Being good amateur astronomers, we know that Pluto is now a dwarf planet, so use the del operation to remove it from the end of planet_list.
planet_list.remove("Pluto")

# print(planet_list)

# Challenge
# Create another list containing tuples. Each tuple will hold the name of a spacecraft that we have launched, and the names of the planet(s) that it has visited, or landed on.
# Example spacecraft list
spacecraft = [
   ("Cassini", "Saturn"),
   ("Viking", "Mars"),
   ("Venera 3", "Venus"),
   ("Galileo", "Jupiter"),
   ("Ruff", "Jupiter")
]
# Iterate over your list of planets, and inside that loop, iterate over the list of tuples. Print, for each planet, which satellites have visited it.
# ©
for planet in planet_list:
    planet_craft = []
    for craft in spacecraft:
        if planet == craft[1]:
            planet_craft.append(craft[0])
    print(f'{planet}:')
    for craft in planet_craft:
        print(craft)