import threading
import time
from pywinusb import hid

from .commands import * 
from .customsettings import *


class HIDDeviceManager:
    vendor_id = None
    product_id = None
    devices = []
    reports = []
    running = False
    monitor_thread = None

    @classmethod
    def initialize(cls, vendor_id, product_id):
        """
        Initializes the HIDDeviceManager with vendor and product IDs.
        """
        cls.vendor_id = vendor_id
        cls.product_id = product_id
        cls.running = True
        cls.start_monitoring()

    @classmethod
    def find_devices(cls):
        """
        Finds devices matching the specified vendor_id and product_id.
        """
        if cls.vendor_id is None or cls.product_id is None:
            print("Vendor ID and Product ID must be set before finding devices.")
            return
        filter = hid.HidDeviceFilter(vendor_id=cls.vendor_id, product_id=cls.product_id)
        cls.devices = filter.get_devices()

    @classmethod
    def initialize_reports(cls):
        """
        Initializes and stores the output reports of all connected devices.
        """
        cls.reports = []
        for device in cls.devices:
            device.open()
            device_output_reports = device.find_output_reports()
            if device_output_reports:
                cls.reports.extend(device_output_reports)

    @classmethod
    def send_data(cls, buffer):
        """
        Sends the given buffer to all initialized output reports.
        """
        if not cls.reports:
            print("No output reports initialized. Ensure devices are connected and initialized.")
            return
        for report in cls.reports:
            report.set_raw_data([0] + buffer)
            report.send()
            print(f"Data sent: {buffer}")

    @classmethod
    def send_settings(cls, mode, color=[0xFF,0xFF,0xFF], pwm=255, colorful=0, speed=0, direction=0):
        cls.send_data(Commands.get_change_settings_buffer(mode, color, pwm, colorful, speed, direction))

    @classmethod
    def change_mode(cls, mode):
        cls.send_data(Commands.get_set_mode_buffer(mode))

    @classmethod
    def send_custom_settings(cls, cs : CustomSettings):
        buffer = cs.get_buffer()
        for i in range(8):
            cls.send_data(buffer[i*64:(i+1)*64])

    @classmethod
    def send_framed_custom_settings(cls, cs : CustomSettings):
        frames = cs.get_frames()
        for frame in frames:
            for i in range(8):
                cls.send_data(frame[i*64:(i+1)*64])

    @classmethod
    def monitor_devices(cls):
        """
        Continuously monitors for devices with the specified VID and PID.
        """
        while cls.running:
            cls.find_devices()
            if cls.devices:
                print("Device found!")
                cls.initialize_reports()
            else:
                print("Device not found.")
            time.sleep(2)  # Check every 2 seconds

    @classmethod
    def start_monitoring(cls):
        """
        Starts the device monitoring in a separate thread.
        """
        if cls.monitor_thread and cls.monitor_thread.is_alive():
            print("Monitoring already running.")
            return
        cls.running = True
        cls.monitor_thread = threading.Thread(target=cls.monitor_devices, daemon=True)
        cls.monitor_thread.start()

    @classmethod
    def stop_monitoring(cls):
        """
        Stops the device monitoring.
        """
        cls.running = False
        if cls.monitor_thread:
            cls.monitor_thread.join()