# NSS Python Planet List & Squared Randoms



## Exercise

1. Use `append()` to add Jupiter and Saturn at the end of the list.
1. Use the `extend()` method to add another list of the last two planets in our solar system to the end of the list.
1. Use `insert()` to add Earth, and Venus in the correct order.
1. Use `append()` again to add Pluto to the end of the list.
1. Now that all the planets are in the list, slice the list in order to get the rocky planets into a new list called `rocky_planets`.
1. Being good amateur astronomers, we know that Pluto is now a dwarf planet, so use the `del` operation to remove it from the end of `planet_list`.

## Iterating over planets

1. Create another list containing tuples. Each tuple will hold the name of a spacecraft that we have launched, and the names of the planet(s) that it has visited, or landed on. (e.g. `('Cassini', 'Jupiter')`).
1. Iterate over your list of planets, and inside that loop, iterate over the list of tuples. Print, for each planet, which sattelites have visited. 

## Instructions

1. Using the `random` module and the `range` method, generate a list of 20 random numbers between 0 and 49.
    ```
    import random

    random_numbers = [...insert awesome code here...]
    print(random_numbers)
    ```
2. With the resulting list, use a list comprehension to build a new list that contains each number squared. For example, if the original list is `[2, 5]`, the final list will be `[4, 25]`.

