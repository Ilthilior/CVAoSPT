import csv
import json

locations_json = []
with open("../aos-poptracker - PopTracker Addresses.csv") as sheet:
    h = csv.reader(sheet)
    rows = list(h)
    prev_within = None
    for i, row in enumerate(rows):
        if i == 0:
            continue
        type = row[0]
        number = row[1]
        roomid = row[2]
        numberwithin = row[3]
        name = row[4]
        spec = row[5]
        address = row[6]
        region = address.removeprefix("@Locations/").removesuffix(f"/{roomid}/{name}{spec}")
        app = f"_{str(int(numberwithin)-1)}" if numberwithin != str(1) else ""
        fuck = False
        if region not in str([n.get("name") for n in locations_json]):
            locations_json.append(
                {
                    "name": f"{region} Locations",
                    "children": []
                }
            )
            fuck = True
        for i2, r in enumerate(locations_json):
            if r.get("name") == f"{region} Locations":
                region_index = i2
                break
        locations_json[i2]["children"].append(
            {
                "name": f"{roomid}{app}",
                "children": [
                    {
                        "name": f"{region}",
                        "access_rules": [],
                        "sections": [
                            {
                                "name": f"{name}"
                            }
                        ],
                        "map_locations": [
                            {
                                "map": "Dracula's Castle" if region != "Chaotic Realm" else "Chaotic Realm",
                                "x": 1750,
                                "y": 700
                            }
                        ]
                    }
                ]
            }
        )
        prev_within = numberwithin
with open("locations.jsonc", "w", encoding="utf-8") as output:
    json.dump(locations_json, output, indent="\t")