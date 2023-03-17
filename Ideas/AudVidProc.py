from threading import Thread
from time import sleep


import gi

gi.require_version("Gst", "1.0")

from gi.repository import Gst, GLib

Gst.init()

main_loop = GLib.MainLoop()
main_loop_thread = Thread(target=main_loop.run)
main_loop_thread.start()

pipeline = Gst.parse_launch("pulsesrc device=alsa_input.pci-0000_00_14.2.analog-stereo ! audioconvert ! audioresample ! audioecho ! audioconvert ! autoaudiosink v4l2src ! decodebin ! videoconvert ! edgetv ! videoconvert ! autovideosink")

pipeline.set_state(Gst.State.PLAYING)


try:
    while True:
        sleep(0.1)
except KeyboardInterrupt:
    pass

pipeline.set_state(Gst.State.NULL)
main_loop.quit()
main_loop_thread.join()

