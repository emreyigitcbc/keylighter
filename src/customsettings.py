from .API import *

class CustomSettings:
    def __init__(self):
        self.frames = []
        self.buffer = self.create_empty_buffer()

    def create_empty_buffer(self):
        buffer = [0] * 64 * 8
        # CONSTANTS
        for i in range(0, 64*8, 64):
            buffer[i] = 0x8B
            buffer[i+1] = 0x3C
            buffer[i+2] = int(i/64) * 0x3c
            buffer[i+3] = 0x00
            
            buffer[64*5+2] = 0x2c
            buffer[64*5+3] = 0x01

            buffer[64*6+2] = 0x68
            buffer[64*6+3] = 0x01

            buffer[64*7+1] = 0x14
            buffer[64*7+2] = 0xA4
            buffer[64*7+3] = 0x01

        return buffer
    
    def set_key(self, key : str, color : list[int], pwm : int):
        if str(key).lower() in KEY_ALL:
            i = self.fix_index(KEY_ALL[key])
            self.buffer[i] = color[0]
            self.buffer[i+1] = color[1]
            self.buffer[i+2] = color[2]
            self.buffer[i+3] = pwm

    def set_key(self, key : list[str], color : list[list[int]], pwm : list[int]):
        for k, j in enumerate(key):
            if str(key[j]).lower() in KEY_ALL:
                i = self.fix_index(KEY_ALL[key[j]])
                self.buffer[i] = color[j][0]
                self.buffer[i+1] = color[j][1]
                self.buffer[i+2] = color[j][2]
                self.buffer[i+3] = pwm[j]

    def set_key(self, key_index : int, color : list[int], pwm : int):
        if key_index in INDEX_ALL:
            i = self.fix_index(key_index)
            self.buffer[i] = color[0]
            self.buffer[i+1] = color[1]
            self.buffer[i+2] = color[2]
            self.buffer[i+3] = pwm

    def set_key(self, key_index : list[int], color : list[list[int]], pwm : list[int]):
        for k, j in enumerate(key_index):
            if key_index[j] in INDEX_ALL:
                i = self.fix_index(key_index[j])
                self.buffer[i] = color[j][0]
                self.buffer[i+1] = color[j][1]
                self.buffer[i+2] = color[j][2]
                self.buffer[i+3] = pwm[j]

    def set_frames(self, frames : list):
        all_buffer = []
        for frame in frames:
            frame_buffer = self.create_empty_buffer()
            for key in frame:
                index = self.fix_index(key[0])
                frame_buffer[index] = key[1][0]
                frame_buffer[index + 1] = key[1][1]
                frame_buffer[index + 2] = key[1][2]
                frame_buffer[index + 3] = key[2]
            all_buffer.append(frame_buffer)
        self.frames = all_buffer
        return all_buffer

    def get_buffer(self):
        return self.buffer
    
    def get_frames(self):
        return self.frames
    
    def fix_index(self, key):
        page = key // 15
        offset = (key % 15 + 1) * 4
        real_index = page * 64 + offset
        return real_index
 