from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        parsed_content = toml.loads(request.urlopen(self._url).read().decode("utf-8"))
        tool = parsed_content["tool"]
        poetry = tool["poetry"]
        name = poetry["name"]
        description = poetry["description"]
        dependencies = poetry["dependencies"]
        listed_dependencies = []
        for key in dependencies:
            listed_dependencies.append(key)
        group = poetry["group"]
        dev = group["dev"]
        dev_dependencies = dev["dependencies"]
        listed_dev_dependencies = []
        for key in dev_dependencies:
            listed_dev_dependencies.append(key)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, listed_dependencies, listed_dev_dependencies)
