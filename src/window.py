import xml.etree.ElementTree as ET

from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QLabel, QSlider, QLineEdit, QCheckBox, QHBoxLayout, QColorDialog, QStackedWidget, QWidget
from PyQt5.QtCore import Qt, QRect, pyqtSignal
from PyQt5.QtGui import QPixmap, QColor, QImage, QPainter

from .keyboard import *
from .simple import *
from .advanced import *
from .direction import *
from .custom import *
from .API import *

class KeyboardApp(QMainWindow):
    def __init__(self, xml_file, background_image):
        super().__init__()
        self.setWindowTitle("GamePower EVA 7-60M TR Layout | Light Control by: Emre Cebeci (v1.0, release: 24.11.2024)")
        self.setGeometry(100, 291, 600, 291)

        self.xml_file = xml_file
        self.background_image = background_image

        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)

        self.keyboard_widget = QLabel()
        self.keyboard_widget.setPixmap(QPixmap(self.background_image).scaled(800, 300, Qt.KeepAspectRatio))
        self.keyboard_widget.setFixedHeight(300)
        main_layout.addWidget(self.keyboard_widget)

        self.options_layout = QHBoxLayout()
        self.stacked_widget = QStackedWidget()
        main_layout.addLayout(self.options_layout)
        main_layout.addWidget(self.stacked_widget)

        self.create_options()
        #API_GENERATOR.initiliaze(self.xml_file)
        self.key_items = self.load_xml(self.xml_file)

    def load_xml(self, file_path):
        tree = ET.parse(file_path)
        root = tree.getroot()
        
        key_items = []
        for key in root.find("Keyboard/KeyItems"):
            rect = key.get("rect").split("#")
            x = int(rect[0].strip())
            y = int(rect[1].strip())
            width = int(rect[2].strip())
            height = int(rect[3].strip())

            key_items.append({key.get("name"): (x, y, width, height)})

        return key_items
    
    def create_options(self):
        options = [
            "Statik", "Kalp Atışı", "Şimşek", "Kar İzi", "Yönlü Şimşek",
            "Yıldızlar", "Spektrum", "Şok Dalgası", "Triggered", "At Koşusu", "Özel"
        ]

        for index, option in enumerate(options):
            button = QPushButton(option)
            button.clicked.connect(lambda _, idx=index: self.show_page(idx))
            self.options_layout.addWidget(button)

            if index in {1, 2, 3, 5, 7, 8}: 
                self.stacked_widget.addWidget(LightingPage(option, key=index+1))
            elif index in {4, 9}:  
                self.stacked_widget.addWidget(DirectionPage(option, key=index+1))
            elif index == 10:  
                self.stacked_widget.addWidget(CustomPage(option, key=index+1))
            elif index in {0, 6}:  
                self.stacked_widget.addWidget(SimplePage(option, key=index+1))

    def show_page(self, index):
        HIDDeviceManager.send_data(Commands.get_set_mode_buffer(index+1))
        self.stacked_widget.setCurrentIndex(index)

    def paint_key(self, key, color):
        self.painter.setPen(QColor(color[0], color[1], color[2], color[3]))
        x, y, width, height = key
        self.painter.drawRect(QRect(x, y, width, height))
        self.update()