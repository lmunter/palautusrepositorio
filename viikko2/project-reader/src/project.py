class Project:
    def __init__(self, name, description, dependencies, dev_dependencies, license, authors):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.license = license
        self.authors = authors

    def _newline_list(self, list):
        result = "\n- ".join(list)
        return "\n- "+result

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}"
            f"\n "
            f"\nAuthors:"
            f"{self._newline_list(self.authors)}"
            f"\n "
            f"\nDependencies:"
            f"{self._newline_list(self.dependencies)}"
            f"\n "
            f"\nDevelopment dependencies:"
            f"{self._newline_list(self.dev_dependencies)}"
        )
