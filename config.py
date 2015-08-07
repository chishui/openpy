import os
import json
import sys

cur_directory = os.path.dirname(sys.argv[0] if len(sys.argv) else os.path.abspath(__file__))

class Config():
    
    config_file = os.path.join(cur_directory, 'config.json')

    def __init__(self) :
        with open(self.config_file) as f:
            self._config = json.loads(f.read())

    def __flush__(self) :
        with open(self.config_file, 'w') as f:
            f.write(json.dumps(self._config))

    def add_path(self, path) :
        path = os.path.abspath(path)
        if not os.path.exists(path):
            return False

        if path in self._config['config']['path']:
            return True

        self._config['config']['path'].append(path)
        self.__flush__()
        return True

    def remove_path(self, path) :
        path = os.path.abspath(path)
        if path not in self._config['config']['path']:
            return False

        index = self._config['config']['path'].index(path)
        del self._config['config']['path'][index]
        self.__flush__()
        return True

    def path(self) :
        return self._config['config']['path']

    def set_auto(self, auto = True) :
        self._config['config']['auto'] = auto
        self.__flush__()

    def is_auto(self) :
        return self._config['config']['auto']
