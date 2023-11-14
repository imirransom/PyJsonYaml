import json
import yaml


def json_to_yaml_converter(json_file):
    with open(json_file, 'r') as file:
        new_file = json.load(file)

    with open(json_file.replace(".json", "") + ".yaml", "w") as yaml_file:
        yaml.dump(new_file, yaml_file)

    with open(json_file, "r") as yaml_file:
        print(yaml_file.read())


json_to_yaml_converter("donuts.json")
