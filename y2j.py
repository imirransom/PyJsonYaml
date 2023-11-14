import yaml
import json


def yaml_to_json_converter(yaml_file):
    with open(yaml_file, "r") as file:
        new_file = yaml.safe_load(file)

    with open(yaml_file.replace(".yaml", "") + ".json") as file:

