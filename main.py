from PyQt5.QtWidgets import QApplication
from src.window import KeyboardApp
from src.keyboard import HIDDeviceManager
import sys

if __name__ == "__main__":
    # Uygulama ve pencereyi başlat
    app = QApplication(sys.argv)
    app.setStyleSheet(open("./assets/theme.css").read())
    xml_file = "./assets/layout.xml"
    background_image = "./assets/kb_600.png"

    VID = 0x1A2C
    PID = 0x2002

    HIDDeviceManager.initialize(vendor_id=VID, product_id=PID)

    window = KeyboardApp(xml_file, background_image)
    window.show()
    sys.exit(app.exec_())
