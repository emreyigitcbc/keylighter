from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QLabel, QSlider, QLineEdit, QCheckBox, QHBoxLayout, QColorDialog, QStackedWidget, QWidget
from PyQt5.QtCore import Qt, QRect, pyqtSignal
from PyQt5.QtGui import QPixmap, QColor, QImage, QPainter
import math

class SpectrumWidget(QWidget):
    color_changed = pyqtSignal(QColor) 

    def __init__(self):
        super().__init__()
        self.setFixedSize(150, 150)  
        self.image = self.create_spectrum_image()
        self.selected_point = None  # Seçilen rengin pozisyonu

    def create_spectrum_image(self):
        """Dairesel spektrum için QImage oluştur."""
        diameter = self.width()
        radius = diameter / 2
        image = QImage(diameter, diameter, QImage.Format_ARGB32) 

        for x in range(diameter):
            for y in range(diameter):
                # Pixel merkezine göre konumlandırma
                dx = x - radius
                dy = y - radius
                distance = math.sqrt(dx**2 + dy**2)

                if distance <= radius: 
                    angle = math.atan2(dy, dx)  
                    hue = (math.degrees(angle) + 360) % 360
                    saturation = distance / radius 
                    value = 1.0 

                    color = QColor.fromHsvF(hue / 360, saturation, value)
                    image.setPixel(x, y, color.rgb())
                else:
                    image.setPixelColor(x, y, QColor(0, 0, 0, 0)) 

        return image

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(0, 0, self.image) 

        if self.selected_point:
            painter.setPen(QColor(255, 255, 255)) 
            painter.setBrush(QColor(0, 0, 0))
            x, y = self.selected_point
            painter.drawEllipse(x - 3, y - 3, 6, 6) 

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.update_color(event.pos())

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.update_color(event.pos())

    def update_color(self, pos):
        diameter = self.width()
        radius = diameter / 2
        dx = pos.x() - radius
        dy = pos.y() - radius
        distance = math.sqrt(dx**2 + dy**2)

        if distance <= radius: 
            angle = math.atan2(dy, dx)
            hue = (math.degrees(angle) + 360) % 360
            saturation = distance / radius
            value = 1.0  

            color = QColor.fromHsvF(hue / 360, saturation, value)
            self.selected_point = (pos.x(), pos.y())
            self.color_changed.emit(color) 
            self.update() 