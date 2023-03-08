import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst

Gst.init(None)

pipeline = Gst.Pipeline()

# Elemento para capturar el audio desde un micrófono o entrada de línea
source = Gst.ElementFactory.make('autoaudiosrc')

# Elemento para aplicar el filtro de cancelación de ruido
noisereduction = Gst.ElementFactory.make('noisereduction')

# Elemento para reproducir el audio en los altavoces
sink = Gst.ElementFactory.make('autoaudiosink')

# Agregamos los elementos al pipeline
pipeline.add(source)
pipeline.add(noisereduction)
pipeline.add(sink)

# Conectamos los elementos con un enlace
source.link(noisereduction)
noisereduction.link(sink)

# Configuramos el filtro de cancelación de ruido
noisereduction.set_property('profile', 'low')

# Iniciamos el pipeline
pipeline.set_state(Gst.State.PLAYING)

# Esperamos a que se interrumpa la reproducción
bus = pipeline.get_bus()
msg = bus.timed_pop_filtered(Gst.CLOCK_TIME_NONE, Gst.MessageType.ERROR | Gst.MessageType.EOS)
