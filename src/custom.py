from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QVBoxLayout, QPushButton, QLabel, QSlider, QLineEdit, QCheckBox, QHBoxLayout, QColorDialog, QStackedWidget, QWidget
from PyQt5.QtCore import Qt, QRect, pyqtSignal
from PyQt5.QtGui import QPixmap, QColor, QImage, QPainter

from .customsettings import CustomSettings

from .keyboard import HIDDeviceManager

import json

class CustomPage(QWidget):
    def __init__(self, name, key):
        super().__init__()
        self.name = name
        self.key = key

        self.layout = QVBoxLayout()

        self.load_script_button = QPushButton("Script Yükle")
        self.load_script_button.clicked.connect(self.open_file_dialog)
        self.layout.addWidget(self.load_script_button)

        self.script_label = QLabel("Seçilen dosya: Yok")
        self.layout.addWidget(self.script_label)

        self.save_script_button = QPushButton("Scripti Kaydet")
        self.save_script_button.clicked.connect(self.save_script)
        self.layout.addWidget(self.save_script_button)

        self.run_script_button = QPushButton("Scripti Çalıştır")
        self.run_script_button.clicked.connect(self.run_custom_script)
        self.layout.addWidget(self.run_script_button)

        self.setLayout(self.layout)

    def open_file_dialog(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Bir script seçin", "", "Python Files (*.py);;All Files (*)")
        if file_name:
            self.script_label.setText(f"Seçilen dosya: {file_name}")

    def save_script(self):
        pass

    def run_custom_script(self):
        f = open('./scripts/res.json')
        data = json.load(f)
        cs = CustomSettings()
        cs.set_frames(data["frames"])
        HIDDeviceManager.send_framed_custom_settings(cs)
        pass