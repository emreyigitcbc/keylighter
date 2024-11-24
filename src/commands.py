class Commands:
    @staticmethod
    def get_set_mode_buffer(mode):
        if mode < 1 or mode > 11:
            return
        else:
            buffer = [0] * 64
            buffer[0] = 0x88
            buffer[2] = mode
            return buffer

    @staticmethod
    def get_change_settings_buffer(mode, color=[0xFF,0xFF,0xFF], pwm=255, colorful=0, speed=0, direction=0):
        buffer = [0] * 64
        if mode == 1:
            # always on
            buffer[0] = 0x89
            buffer[2] = 0x04
            buffer[3] = color[0]
            buffer[4] = color[1]
            buffer[5] = color[2]
            buffer[6] = pwm
        elif mode == 2:
            buffer[0] = 0x89
            buffer[2] = colorful + speed
            buffer[3] = color[0]
            buffer[4] = color[1]
            buffer[5] = color[2]
            buffer[6] = pwm
        elif mode == 3:
            buffer[0] = 0x89
            buffer[2] = colorful + speed
            buffer[3] = color[0]
            buffer[4] = color[1]
            buffer[5] = color[2]
            buffer[6] = pwm
        elif mode == 4:
            buffer[0] = 0x89
            buffer[2] = colorful + speed
            buffer[3] = color[0]
            buffer[4] = color[1]
            buffer[5] = color[2]
            buffer[6] = pwm
        elif mode == 5:
            buffer[0] = 0x89
            buffer[2] = direction + speed
            buffer[3] = color[0]
            buffer[4] = color[1]
            buffer[5] = color[2]
            buffer[6] = pwm
        elif mode == 6:
            buffer[0] = 0x89
            buffer[2] = colorful + speed
            buffer[3] = color[0]
            buffer[4] = color[1]
            buffer[5] = color[2]
            buffer[6] = pwm
        elif mode == 7:
            buffer[0] = 0x89
            buffer[2] = 0x80 + speed
            buffer[3] = color[0]
            buffer[4] = color[1]
            buffer[5] = color[2]
            buffer[6] = pwm
        elif mode == 8:
            buffer[0] = 0x89
            buffer[2] = colorful + speed
            buffer[3] = color[0]
            buffer[4] = color[1]
            buffer[5] = color[2]
            buffer[6] = pwm
        elif mode == 9:
            buffer[0] = 0x89
            buffer[2] = colorful + speed
            buffer[3] = color[0]
            buffer[4] = color[1]
            buffer[5] = color[2]
            buffer[6] = pwm
        elif mode == 10:
            buffer[0] = 0x89
            buffer[2] = direction + speed
            buffer[3] = 0xFF
            buffer[4] = 0x00
            buffer[5] = 0x00
            buffer[6] = pwm
        elif mode == 11:
            pass
        return buffer


