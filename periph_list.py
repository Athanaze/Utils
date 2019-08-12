# USAGE : sudo python3 periph_list.py
import evdev
devices = [evdev.InputDevice(path) for path in evdev.list_devices()]

for d in devices:
    print(d.fn, "|", d.name, "|", d.phys, "|", d.info)
