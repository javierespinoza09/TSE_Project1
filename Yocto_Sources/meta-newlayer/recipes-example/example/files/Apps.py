from threading import Thread
from time import sleep
import gi
import sys

gi.require_version("Gst", "1.0")
from gi.repository import Gst, GLib

Gst.init(sys.argv)

main_loop = GLib.MainLoop()
main_loop_thread = Thread(target=main_loop.run)
main_loop_thread.start()

while True:
    print("\nElija la aplicación que desea\n")
    print("1 ) Filtro Chormahold\n")
    print("2 ) Filtro gamma\n")
    print("Digite 3 para terminar el programa\n")

    user_input = int(input(": "))

    if user_input == 3:
        break

    elif user_input == 1:
        r_value = int(input("Valor de rojo deseado (0-255):"))
        b_value = int(input("Valor de azul deseado (0-255):"))
        g_value = int(input("Valor de verde deseado (0-255):"))
        pipeline_str = "filesrc location=INKART480.mp4 ! decodebin ! videoconvert ! chromahold target-r={r_val} target-g={g_val} target-b={b_val} ! videoconvert ! ximagesink".format(r_val=r_value, g_val=g_value, b_val=b_value)
        pipeline = Gst.parse_launch(pipeline_str)

        pipeline.set_state(Gst.State.PLAYING)

        bus = pipeline.get_bus()
        msg = bus.timed_pop_filtered(Gst.CLOCK_TIME_NONE, Gst.MessageType.ERROR | Gst.MessageType.STATE_CHANGED | Gst.MessageType.EOS)

        try:
            while True:
                sleep(0.1)
        except KeyboardInterrupt:
            pass

        pipeline.set_state(Gst.State.NULL)
        main_loop.quit()
        main_loop_thread.join()

    elif user_input == 2:
        gamma_value = float(input("Digite un valor para gamma (mayor a 1 hace brillantes partes oscuras y menor a 1 oscurece partes brillantes)\n"))
        pipeline_str = "filesrc location=INKART480.mp4 ! decodebin ! videoconvert ! gamma gamma={gamma_val} ! videoconvert ! xvimagesink".format(gamma_val=gamma_value)
        pipeline = Gst.parse_launch(pipeline_str)

        pipeline.set_state(Gst.State.PLAYING)

        bus = pipeline.get_bus()
        msg = bus.timed_pop_filtered(Gst.CLOCK_TIME_NONE, Gst.MessageType.ERROR | Gst.MessageType.STATE_CHANGED | Gst.MessageType.EOS)

        try:
            while True:
                sleep(0.1)
        except KeyboardInterrupt:
            pass

        pipeline.set_state(Gst.State.NULL)
        main_loop.quit()
        main_loop_thread.join()

    else:
        print("Entrada inválida, seleccione otra opción\n")






