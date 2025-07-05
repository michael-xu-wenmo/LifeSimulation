import os
import json

class Checker():
    
    def __init__(self, directory):
        self.directory = directory
        self.filenames =  [f"{self.directory}/rounds_json/{name}" for name in (os.listdir(f"{self.directory}/rounds_json"))]
        self.current = 0
    
    def _read_pos(self):
        with open(self.filenames[self.current], "r") as file:
            raw = json.loads(file.read())
            file.close()
        for entity in raw["entities"]:
            yield tuple(entity[1])

    @staticmethod
    def check(arr):
        """Checks if any entity has the same position (returns True if entities overlap else returns False)"""

        exists: set[list[int]] = set()
        for position in arr:

            if position in exists:
                return True
            exists.add(position) 

        return False
    
    def check_file(self):
        for filename in self.filenames:
            exists = Checker.check(self._read_pos())
            yield filename, exists
            self.current += 1

if __name__ == "__main__":
    checker = Checker("dev_sim_records")
    for state in checker.check_file():
        print(state)