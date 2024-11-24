KEY_ROWS = {"0": {"esc": 0, "f1": 1, "f2": 2, "f3": 3, "f4": 4, "f5": 5, "f6": 6, "f7": 7, "f8": 8, "f9": 9, "f10": 10, "f11": 11, "f12": 12, "printscreen": 13, "scrolllock": 14, "pause": 15}, "1": {"\"": 16, "1": 17, "2": 18, "3": 19, "4": 20, "5": 21, "6": 22, "7": 23, "8": 24, "9": 25, "0": 26, "*": 27, "-": 28, "backspace": 29, "insert": 30, "home": 31, "pgup": 32}, "2": {"tab": 37, "q": 38, "w": 39, "e": 40, "r": 41, "t": 42, "y": 43, "u": 44, "i": 45, "o": 46, "p": 47, "\u011f": 48, "\u00fc": 49, "del": 51, "end": 52, "pgdn": 53, "enter": 70}, "3": {",": 50, "capslock": 58, "a": 59, "s": 60, "d": 61, "f": 62, "g": 63, "h": 64, "j": 65, "k": 66, "l": 67, "\u015f": 68, "i\u0307": 69}, "4": {"lshift": 75, "<": 76, "z": 77, "x": 78, "c": 79, "v": 80, "b": 81, "n": 82, "m": 83, "\u00f6": 84, "\u00e7": 85, ".": 86, "rshift": 88, "\u2191": 89}, "5": {"lctrl": 94, "win": 95, "lalt": 96, "space": 98, "ralt": 100, "fn": 101, "app": 102, "rctrl": 103, "\u2190": 104, "\u2193": 105, "\u2192": 106}}
KEY_COLS = {"0": {"esc": 0, "\"": 16, "tab": 37, "capslock": 58, "lshift": 75, "lctrl": 94}, "1": {"f1": 1, "1": 17, "q": 38, "<": 76}, "2": {"f2": 2, "2": 18, "w": 39, "a": 59, "z": 77, "win": 95}, "3": {"f3": 3, "3": 19, "e": 40, "s": 60, "x": 78, "lalt": 96}, "4": {"f4": 4, "4": 20, "r": 41, "d": 61, "c": 79}, "5": {"f5": 5, "5": 21, "t": 42, "f": 62, "v": 80, "space": 98}, "6": {"f6": 6, "6": 22, "y": 43, "g": 63, "b": 81}, "7": {"f7": 7, "7": 23, "u": 44, "h": 64, "n": 82}, "8": {"f8": 8, "8": 24, "i": 45, "j": 65, "m": 83, "ralt": 100}, "10": {"f9": 9, "0": 26, "p": 47, "l": 67, "\u00e7": 85, "app": 102}, "11": {"f10": 10, "*": 27, "\u011f": 48, "\u015f": 68, ".": 86, "rctrl": 103}, "12": {"f11": 11, "-": 28, "\u00fc": 49, "i\u0307": 69, "\u2190": 104}, "13": {"f12": 12, "backspace": 29, ",": 50, "enter": 70, "rshift": 88, "\u2193": 105}, "14": {"printscreen": 13, "insert": 30, "del": 51, "\u2191": 89, "\u2192": 106}, "15": {"scrolllock": 14, "home": 31, "end": 52}, "16": {"pause": 15, "pgup": 32, "pgdn": 53}, "9": {"9": 25, "o": 46, "k": 66, "\u00f6": 84, "fn": 101}}
KEY_ALL = {"esc": 0, "f1": 1, "f2": 2, "f3": 3, "f4": 4, "f5": 5, "f6": 6, "f7": 7, "f8": 8, "f9": 9, "f10": 10, "f11": 11, "f12": 12, "printscreen": 13, "scrolllock": 14, "pause": 15, "\"": 16, "1": 17, "2": 18, "3": 19, "4": 20, "5": 21, "6": 22, "7": 23, "8": 24, "9": 25, "0": 26, "*": 27, "-": 28, "backspace": 29, "insert": 30, "home": 31, "pgup": 32, "tab": 37, "q": 38, "w": 39, "e": 40, "r": 41, "t": 42, "y": 43, "u": 44, "i": 45, "o": 46, "p": 47, "\u011f": 48, "\u00fc": 49, ",": 50, "del": 51, "end": 52, "pgdn": 53, "capslock": 58, "a": 59, "s": 60, "d": 61, "f": 62, "g": 63, "h": 64, "j": 65, "k": 66, "l": 67, "\u015f": 68, "i\u0307": 69, "enter": 70, "lshift": 75, "<": 76, "z": 77, "x": 78, "c": 79, "v": 80, "b": 81, "n": 82, "m": 83, "\u00f6": 84, "\u00e7": 85, ".": 86, "rshift": 88, "\u2191": 89, "lctrl": 94, "win": 95, "lalt": 96, "space": 98, "ralt": 100, "fn": 101, "app": 102, "rctrl": 103, "\u2190": 104, "\u2193": 105, "\u2192": 106}

INDEX_ROWS = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32], [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51, 52, 53, 70], [50, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69], [75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 88, 89], [94, 95, 96, 98, 100, 101, 102, 103, 104, 105, 106]]
INDEX_COLS = [[0, 16, 37, 58, 75, 94], [1, 17, 38, 76], [2, 18, 39, 59, 77, 95], [3, 19, 40, 60, 78, 96], [4, 20, 41, 61, 79], [5, 21, 42, 62, 80, 98], [6, 22, 43, 63, 81], [7, 23, 44, 64, 82], [8, 24, 45, 65, 83, 100], [25, 46, 66, 84, 101], [9, 26, 47, 67, 85, 102], [10, 27, 48, 68, 86, 103], [11, 28, 49, 69, 104], [12, 29, 50, 70, 88, 105], [13, 30, 51, 89, 106], [14, 31, 52], [15, 32, 53]]
INDEX_ALL = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 88, 89, 94, 95, 96, 98, 100, 101, 102, 103, 104, 105, 106]