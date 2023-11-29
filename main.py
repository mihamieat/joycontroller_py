import libevdev
import sys

fd = open('/dev/input/event1', 'rb')
d = libevdev.Device(fd)
if not d.has(libevdev.EV_KEY.BTN_LEFT):
     print('This does not look like a mouse device')
     sys.exit(0)

# Loop indefinitely while pulling the currently available events off
# the file descriptor
while True:
    for e in d.events():
        if not e.matches(libevdev.EV_KEY):
            continue

        if e.matches(libevdev.EV_KEY.BTN_LEFT):
            print('Left button event')
        elif e.matches(libevdev.EV_KEY.BTN_RIGHT):
            print('Right button event')
