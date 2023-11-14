import json
import yaml

with open("donuts.json", 'r') as file:
    donuts = json.load(file)

with open("donuts.yaml", "w") as yaml_file:
    yaml.dump(donuts, yaml_file)

with open("donuts.yaml", "r") as yaml_file:
    print(yaml_file.read())