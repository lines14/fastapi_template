import os
import json
import classutilities
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class DataUtils(classutilities.ClassPropertiesMixin):
    @classutilities.classproperty
    def responses():
        with open('../templates/responses.json', 'r', encoding='utf-8') as data:
            return type("Responses", (object, ), json.loads(data.read()))