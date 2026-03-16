import yaml
import json


def load_settings(file_path="config/settings.yaml"):
    with open(file_path, "r") as file:
        return yaml.safe_load(file)


def load_test_data(file_path):
    with open(file_path, "r") as file:
        return json.load(file)