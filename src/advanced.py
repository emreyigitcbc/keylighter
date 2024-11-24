from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QLabel, QSlider, QLineEdit, QCheckBox, QHBoxLayout, QColorDialog, QStackedWidget, QWidget
from PyQt5.QtCore import Qt, QRect, pyqtSignal
from PyQt5.QtGui import QPixmap, QColor, QImage, QPainter

from src.keyboard import HIDDeviceManager

from .spectrum import * 
from .commands import *

class LightingPage(QWidget):
    def __init__(self, name, key):
        super().__init__()
        self.name = name
        self.key = key

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel(f"Ayarlar: {name}"))

        self.colors = [0,0,0]
        self.colorful = 0x80
        self.pwm = 255
        self.speed = 1

        self.sliders = {}
        self.textboxes = {}
        for color in ["R", "G", "B"]:
            slider_layout = QHBoxLayout()
            label = QLabel(color)
            slider = QSlider(Qt.Horizontal)
            slider.setRange(0, 255)
            slider.setValue(0)
            textbox = QLineEdit("0")
            textbox.setFixedWidth(50)
            self.sliders[color] = slider
            self.textboxes[color] = textbox

            slider.valueChanged.connect(lambda value, c=color: self.update_textbox(c, value))
            textbox.textChanged.connect(lambda value, c=color: self.update_slider(c, value))

            slider_layout.addWidget(label)
            slider_layout.addWidget(slider)
            slider_layout.addWidget(textbox)
            layout.addLayout(slider_layout)

        self.pwm_slider = self.add_slider(layout, "Parlaklık", 0, 255)
        self.pwm_slider.valueChanged.connect(lambda value: self.change_pwm_value(value))
        self.pwm_slider.valueChanged.connect(self.update_keyboard_settings)

        self.speed_slider = self.add_slider(layout, "Işık Hızı", 1, 5)
        self.speed_slider.valueChanged.connect(lambda value: self.change_speed_value(value))
        self.speed_slider.valueChanged.connect(self.update_keyboard_settings)

        hex_layout = QHBoxLayout()
        hex_label = QLabel("HEX:")
        self.hex_input = QLineEdit("#FFFFFF")
        self.hex_input.setFixedWidth(100)
        self.hex_input.textChanged.connect(self.update_from_hex)
        self.hex_input.textChanged.connect(self.update_keyboard_settings)
        hex_layout.addWidget(hex_label)
        hex_layout.addWidget(self.hex_input)
        layout.addLayout(hex_layout)

        self.checkbox = QCheckBox("Renkli")
        self.checkbox.setChecked(True)
        self.checkbox.stateChanged.connect(lambda value: self.change_colorful_value(value))
        self.checkbox.stateChanged.connect(self.update_keyboard_settings)
        layout.addWidget(self.checkbox)

        self.color_spectrum = SpectrumWidget()
        self.color_spectrum.color_changed.connect(self.update_from_spectrum)
        layout.addWidget(self.color_spectrum)

    def update_keyboard_settings(self):
        HIDDeviceManager.send_settings(self.key, self.colors, self.pwm, self.colorful, self.speed)

    def change_pwm_value(self, pwm):
        self.pwm = pwm

    def change_speed_value(self, speed):
        self.speed = speed

    def change_colorful_value(self, colorful):
        self.colorful = 0x80 if colorful else 0

    def add_slider(self, layout, label_text, min_val, max_val):
        slider_layout = QHBoxLayout()
        label = QLabel(label_text)
        slider = QSlider(Qt.Horizontal)
        slider.setRange(min_val, max_val)
        textbox = QLineEdit(str(min_val))
        textbox.setFixedWidth(50)

        slider.valueChanged.connect(lambda value: textbox.setText(str(value)))
        textbox.textChanged.connect(lambda value: slider.setValue(int(value) if value.isdigit() else slider.value()))

        slider_layout.addWidget(label)
        slider_layout.addWidget(slider)
        slider_layout.addWidget(textbox)
        layout.addLayout(slider_layout)

        return slider

    def open_color_dialog(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.update_ui_from_color(color)

    def update_ui_from_color(self, color):
        self.colors[0] = color.red()
        self.colors[1] = color.green()
        self.colors[2] = color.blue()
        self.sliders["R"].setValue(color.red())
        self.sliders["G"].setValue(color.green())
        self.sliders["B"].setValue(color.blue())
        self.hex_input.setText(color.name().upper())

    def update_from_spectrum(self, color):
        self.update_ui_from_color(color)

    def update_textbox(self, color, value):
        self.textboxes[color].setText(str(value))
        self.update_ui_from_sliders()

    def update_slider(self, color, value):
        if value.isdigit():
            self.sliders[color].setValue(int(value))
        self.update_ui_from_sliders()

    def update_ui_from_sliders(self):
        r = self.sliders["R"].value()
        g = self.sliders["G"].value()
        b = self.sliders["B"].value()
        color = QColor(r, g, b)
        self.update_ui_from_color(color)

    def update_from_hex(self, hex_value):
        if len(hex_value) == 7 and hex_value.startswith("#"):
            try:
                color = QColor(hex_value)
                if color.isValid():
                    self.update_ui_from_color(color)
            except ValueError:
                pass