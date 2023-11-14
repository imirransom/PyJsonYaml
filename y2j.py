import yaml
import json


def yaml_to_json_converter(yaml_file):
    with open(yaml_file, "r") as file, open(yaml_file.replace(".yaml", ".json"), "w") as json_file:
        yaml_object = yaml.safe_load(file)
        print(json.dump(yaml_object, json_file))


yaml_to_json_converter("verify.yaml")
yaml_to_json_converter("xmas.yaml")
