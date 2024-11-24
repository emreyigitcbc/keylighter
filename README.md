
# Custom KeyLighter
### This is for GamePower-Eva7-M60 TR Layout

- Since the official light control program of GamePower Eva-7 60M Turkish keyboard is very bad, I decided to make it myself. It can do everything except 2 features that the original program can do. You cannot adjust the lights according to the light intensity on the screen and the volume for now, but the main focus of this program is the "Custom Lighting" section. You can make special lighting settings that you cannot make in the original program with this program.
- **Important:** You still can not change settings without connecting with cable. I tried a lot but the Bluetooth and 2.4G didn't work.

## Installation
First install the requirements,
```batch
pip install -r requirements.txt
```
Then, you can start the program!
```batch
python main.py
```

## Usage
- There are 11 options on the screen. The first 10 of them are the same with the original program. I want to focus on Custom option.

- You can adjust colors and brightness for each key.

- You must create CustomSettings class and set keys manually for now.

- One of the advantages of it is that whenever you change any value, color, brightness etc. it will change real-time. The official app doesn't have this feature.

```py
cs = CustomSettings()
# set_key(KEY, [R,G,B], BRIGHTNESS)
cs.set_key("Esc", [255,0,0], 255)
cs.set_key(",", [255,0,0], 255)
cs.set_key("5", [255,0,0], 255)
cs.set_key("B", [255,0,255], 255)
cs.set_key("Space", [0,0,255], 255)

HIDDeviceManager.send_custom_settings(cs)
```

## Future Plans
- Drawing bitmaps on keyboad.
- Animated custom settings.

## Notice
- This is not official program for GamePower Eva 7 60M, so if something happens to your device, i do not take any responsibility.