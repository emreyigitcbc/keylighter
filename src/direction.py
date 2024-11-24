from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QLabel, QSlider, QLineEdit, QCheckBox, QHBoxLayout, QColorDialog, QStackedWidget, QWidget
from PyQt5.QtCore import Qt, QRect, pyqtSignal
from PyQt5.QtGui import QPixmap, QColor, QImage, QPainter

class DirectionPage(QWidget):
    def __init__(self, name, key):
        super().__init__()
        self.name = name
        self.key = key

        self.direction = 0x80

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel(f"Ayarlar: {name}"))

        self.add_slider(layout, "Parlaklık", 0, 255)
        self.add_slider(layout, "Hız", 1, 5)

        direction_layout = QHBoxLayout()
        left_button = QPushButton("← Sol")
        right_button = QPushButton("Sağ →")
        direction_layout.addWidget(left_button)
        direction_layout.addWidget(right_button)
        layout.addLayout(direction_layout)

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