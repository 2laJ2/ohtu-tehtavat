from urllib import request
from project import Project
import pytomlpp

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        pytomlpp_data = pytomlpp.loads(content)
        #print(content)
        poetry = pytomlpp_data.get('tool').get('poetry')
        print(poetry)
        name = poetry.get('name')
        desc = poetry.get('desc')
        depend = poetry.get('dependencies')
        dev_dep = poetry.get('dev-dependencies')

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, desc, depend, dev_dep)
