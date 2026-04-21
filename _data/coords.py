# Converts any map_locations with spreadsheet coords into coords for the upscaled map
import json
with open("./locations/locations.jsonc") as file:
    locations = json.load(file)

newloc = locations
for regionloc in newloc:
    for roomid in regionloc["children"]:
        for region in roomid["children"]:
            for map in region["map_locations"]:
                x = map["x"]
                y = map["y"]
                # We only want to affect locations with spreadsheet coords
                if isinstance(x, int):
                    continue

                # Convert the string in x to a number
                letters = list(x)
                letters.reverse()
                x = 0
                for i, l in enumerate(letters):
                    if i == 0:
                        x += ord(l) - 65
                    else:
                        x += 26
                y -= 1 # Spreadsheet header offset

                # Account for the map's padding and upscaling
                map["x"] = int((((x*4) + 14 + 2)*6) + 3)
                map["y"] = int((((y*4) + 8 + 2)*6) + 3)

with open("locations.jsonc", 'w', encoding="utf-8") as file:
    json.dump(newloc, file, indent="\t")