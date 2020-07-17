import json
# from pprint import pprint

# with open("film.json", "r") as jsonfile:
#     film = json.load(jsonfile)
 
# pprint(film)
# # alph order w pprint

class Film:

    def __init__(self, name, release_year, length):
        self.name = name
        self.release_year = release_year
        self.length = length

with open("film.json", "r") as jsonfile:
            json_dict = json.load(jsonfile)



jaws = Film(json_dict['name'], json_dict['release_year'], json_dict['length'])
print(jaws.name, jaws.release_year, jaws.length)