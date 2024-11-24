import xml.etree.ElementTree as ET
import json

class API_Generator:
    KEY_ROWS = {}
    KEY_COLS  = {}
    KEY_ALL = {}

    INDEX_ROWS = [ [] for _ in range(6) ]
    INDEX_COLS = [ [] for _ in range(17) ]
    INDEX_ALL = []

    @classmethod
    def initiliaze(self, layout):
        tree = ET.parse(layout)
        root = tree.getroot()

        for key in root.find("Keyboard/KeyItems"):
            keys = key.get("row_col").split("#")
            row = int(keys[0].strip())
            col = int(keys[1].strip())

            if row not in self.KEY_ROWS:
                self.KEY_ROWS[row] = {}
            if col not in self.KEY_COLS:
                self.KEY_COLS[col] = {}

            self.KEY_ROWS[row][key.get("name").lower()] = int(key.get("key_index"))
            self.KEY_COLS[col][key.get("name").lower()] = int(key.get("key_index"))
            self.KEY_ALL[key.get("name").lower()] = int(key.get("key_index"))

            self.INDEX_ROWS[row].append(int(key.get("key_index")))
            self.INDEX_COLS[col].append(int(key.get("key_index")))
            self.INDEX_ALL.append(int(key.get("key_index")))

        print(json.dumps(self.KEY_ROWS))
        print(json.dumps(self.KEY_COLS))
        print(json.dumps(self.KEY_ALL))
        print()
        print(json.dumps(self.INDEX_ROWS))
        print(json.dumps(self.INDEX_COLS))
        print(json.dumps(self.INDEX_ALL))
