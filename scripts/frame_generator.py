import json
from API import *

frames = {"frames":[]}

for i in range(512):
    frame = []
    if i < 256:
        for cols in INDEX_COLS:
            for col in cols:
                key = [col, [i % 256, i % 256, i % 256], i % 256]
                frame.append(key)
    if i >= 256:
        for cols in INDEX_COLS:
            for col in cols:
                key = [col, [255 - (i % 256), 255 - (i % 256), 255 - (i % 256)], 255 - (i % 256)]
                frame.append(key)

    frames["frames"].append(frame)

with open('res.json', 'w', encoding ='utf8') as json_file:
    json.dump(frames, json_file, ensure_ascii = False)

print(frames)