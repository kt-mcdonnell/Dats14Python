# Control Flow

age = 17


if age >= 18:
    print("You can see any of the films here!")
elif age >= 15:
    print("You can watch a film rated anything other than 18")
elif age >= 12:
    print("You can watch films rated PG, U or 12")
elif age >= 8:
    print("You can watch a U, PG or a 12A whilst accompanied by an adult")
elif age < 8:
    print("You can watch any film rated 'U'!")
else:
    print("Please enter a valid age")

film_rating = "pg"

if film_rating.upper == "U":
    print("Subtable for all ages")
elif film_rating.upper == "PG":
    print("Appropriate for all with parental guidance where neccasary")
elif film_rating == "12" or film_rating == "12A":
    print("Suitible for anyone over 12 or under 12 when adult present")
elif film_rating == "15":
    print("Suitible for anyone 15 or older")
elif film_rating == "18":
    print("Suitible for anyone 18 or older")
else:
    print("Please enter a valid film rating")