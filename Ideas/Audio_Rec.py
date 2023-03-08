import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst

Gst.init(None)

pipeline = Gst.Pipeline()

# Elemento para capturar el audio desde un micrófono o entrada de línea
source = Gst.ElementFactory.make('autoaudiosrc')

# Elemento para grabar el audio en un archivo
encoder = Gst.ElementFactory.make('wavenc')
encoder
