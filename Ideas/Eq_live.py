import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst

Gst.init(None)

pipeline = Gst.Pipeline()

# Elemento para capturar el audio desde un micrófono o entrada de línea
source = Gst.ElementFactory.make('autoaudiosrc')

# Elemento para aplicar el filtro de ecualización
equalizer = Gst.ElementFactory.make('equalizer')

# Elemento para reproducir el audio en los altavoces
sink = Gst.ElementFactory.make('autoaudiosink')

# Agregamos los elementos al pipeline
pipeline.add(source)
pipeline.add(equalizer)
pipeline.add(sink)

# Conectamos los elementos con un enlace
source.link(equalizer)
equalizer.link(sink)

# Configuramos el filtro de ecualización
equalizer.set_property('band0', (0, 0)) # Frecuencia y ganancia del primer filtro
equalizer.set_property('band1', (500, 0)) # Frecuencia y ganancia del segundo filtro
equalizer.set_property('band2', (1000, 0)) # Frecuencia y ganancia del tercer filtro
equalizer.set_property('band3', (2000, 0)) # Frecuencia y ganancia del cuarto filtro
equalizer.set_property('band4', (4000, 0)) # Frecuencia y ganancia del quinto filtro
equalizer.set_property('band5', (8000, 0)) # Frecuencia y ganancia del sexto filtro

# Iniciamos el pipeline
pipeline.set_state(Gst.State.PLAYING)

# Esperamos a que se interrumpa la reproducción
bus = pipeline.get_bus()
msg = bus.timed_pop_filtered(Gst.CLOCK_TIME_NONE, Gst.MessageType.ERROR | Gst.MessageType.EOS)
