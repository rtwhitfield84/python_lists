planet_list = ["Mercury", "Mars"]
planet_list.append("Jupiter")
planet_list.append("Saturn")
print(planet_list)

planet_list.extend(["Uranus", "Neptune"])

print(planet_list)

planet_list.insert(1, "Earth")
planet_list.insert(1, "Venus")

print(planet_list)

rocky_planets = planet_list[0:4]

print(rocky_planets)

spacecraft = [("Cassini", "Jupiter"), ("Cassini", "Saturn"), ("Juno", "Jupiter"), ("Voyager 2", "Jupiter"), ("Voyager 2", "Uranus"), ("Voyager 2","Neptune")]



for planet in planet_list:
	for craft in spacecraft:
		if craft[1] == planet:
			print('{} visited {}'.format(craft[0], planet))
