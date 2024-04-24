import json

fo= open('example1.json', 'r')
x= json.load(fo)
fo.close()

for i in x:
    if i["name"] == "Old Fashioned" and i["type"] == "donut":
        i["batters"]["batter"].append({"id": "1005", "type": "Tea"})

    else :
        i["batters"]["batter"].append({"id": "1006", "type": "TeaPowder"})
        break


fo = open('example1.json', 'w')
json.dump(x, fo, indent=2)
fo.close()