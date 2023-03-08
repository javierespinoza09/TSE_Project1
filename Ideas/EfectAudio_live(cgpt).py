import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst

Gst.init(None)

pipeline = Gst.parse_launch('pulsesrc ! audioconvert ! audioresample ! audiopanorama panorama=0.0 ! autoaudiosink')
pipeline.set_state(Gst.State.PLAYING)

try:
    while True:
        message = pipeline.get_bus().timed_pop_filtered(Gst.CLOCK_TIME_NONE, Gst.MessageType.STATE_CHANGED | Gst.MessageType.ERROR | Gst.MessageType.EOS)
        if message:
            t = message.type
            if t == Gst.MessageType.ERROR:
                err, debug = message.parse_error()
                print("Error: %s" % err, debug)
                break
            elif t == Gst.MessageType.EOS:
                print("End-Of-Stream reached")
                break
            elif t == Gst.MessageType.STATE_CHANGED:
                if message.src == pipeline:
                    old_state, new_state, pending_state = message.parse_state_changed()
                    print("Pipeline state changed from %s to %s." %
                          (old_state.value_nick, new_state.value_nick))
        else:
            print("No message received")
except KeyboardInterrupt:
    pass

pipeline.set_state(Gst.State.NULL)
