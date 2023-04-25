"""Mock SenseHAT class. If you have access to a SenseHAT (either via a Raspberry Pi or a SenseHAT emulator), you can use the real SenseHAT class instead of this one.)
To do that DELETE this file so that it will not shadow the sense_hat class installed in your system.
You do not need to understand this code to use it for the smiley exercise"""
import contextlib
import itertools
import logging
import multiprocessing as mp
import queue
import time
import tkinter as tk

DEFAULT_RGB = [(255, 255, 255)] * 64


logging.basicConfig(format="%(asctime)s.%(msecs)03d [%(levelname)s] %(name)s (%(filename)s:%(lineno)d): %(message)s",
                    level=logging.INFO,
                    datefmt="%Y-%m-%d %H:%M:%S")


class SenseHat:
    def __init__(self, background=DEFAULT_RGB):
        self.logger = logging.getLogger(__name__)
        self._low_light = False
        self.logger.info('Starting mock SenseHAT')
        self.queue = mp.Queue()
        self.process = mp.Process(target=self.run_hat_gui, args=(background,))
        time.sleep(1)  # Give the process some time to start
        self.logger.debug('Starting mock SenseHAT process')
        self.process.start()
        self.logger.debug('Started mock SenseHAT process')

    def run_hat_gui(self, initial_rgb_values):
        """tkinter GUI for the mock SenseHAT. Tkinter is not thread-safe, so we need to run it in a separate process."""
        self.logger.debug('Starting GUI')
        self.rgb_values = initial_rgb_values
        # self._low_light = False

        self.root = tk.Tk()
        self.root.title('Mock SenseHAT')
        self.led_matrix = [None] * 64
        self.create_led_matrix()

        # Set initial color of the LED matrix
        self.refresh_gui_from_queue()

        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.logger.debug('Starting mock SenseHAT GUI mainloop')
        self.root.mainloop()

    def refresh_gui_from_queue(self):
        """Updates the GUI using a queue for communication with the main process."""
        # TODO: investigate if using a queue is mandatory
        with contextlib.suppress(queue.Empty):
            message, payload = self.queue.get_nowait()
            if message == 'set_pixels':
                self._set_pixels(payload)
            elif message == 'low_light':
                self._low_light = payload
        self.root.after(1000, SenseHat.refresh_gui_from_queue, self)

    def create_led_matrix(self):
        """Creates the LED matrix for the GUI using a grid of tkinter Frames."""
        self.logger.debug('Creating mock SenseHAT LED matrix')
        for i, j in itertools.product(range(8), range(8)):
            frame = tk.Frame(self.root, width=30,
                             height=30, bd=1, relief='solid')
            frame.grid(row=i, column=j)
            self.led_matrix[i*8 + j] = frame  # type: ignore

    def _set_pixels(self, rgb_values):
        self.logger.debug('Setting mock SenseHAT LED matrix pixel values')
        self.logger.debug(f'{self.low_light=}')
        if self.low_light:
            dimming_factor = 0.6  # Adjust this value between 0 and 1 for different dimming levels
            rgb_values = [(int(r * dimming_factor), int(g * dimming_factor),
                           int(b * dimming_factor)) for r, g, b in rgb_values]

        self.rgb_values = rgb_values
        self.logger.debug(f'{self.rgb_values=}')
        for i, rgb in enumerate(rgb_values):
            self.led_matrix[i].config(bg='#%02x%02x%02x' % rgb)  # type: ignore
            # config is a method of tkinter.Frame, but mypy thinks it is a property

    def set_pixels(self, rgb_values):
        """Emulates the SenseHAT.set_pixels method"""
        self.logger.debug("set_pixels called")
        self.queue.put(('set_pixels', rgb_values))

    @property
    def low_light(self):
        """Emulates the SenseHAT.low_light property"""
        return self._low_light

    @low_light.setter
    def low_light(self, value):
        self.queue.put(('low_light', value))

    def close(self):
        self.root.destroy()


def main():  # sourcery skip: extract-duplicate-method
    """Used only to quickly test and demonstrate the mock SenseHAT class"""
    from signal import pause
    rgb_values = [(255, 0, 0)] * 64

    mock_sense_hat = SenseHat()
    mock_sense_hat.set_pixels(rgb_values)

    time.sleep(1)
    mock_sense_hat.set_pixels([(0, 255, 0)] * 64)
    time.sleep(1)
    mock_sense_hat.set_pixels([(0, 0, 255)] * 64)
    # To enable low_light mode, set the low_light attribute to True
    mock_sense_hat.low_light = True
    time.sleep(1)
    mock_sense_hat.set_pixels(rgb_values)
    time.sleep(1)
    mock_sense_hat.set_pixels([(0, 255, 0)] * 64)
    time.sleep(1)
    mock_sense_hat.set_pixels([(0, 0, 255)] * 64)
    mock_sense_hat.low_light = False
    time.sleep(1)
    mock_sense_hat.set_pixels(rgb_values)
    time.sleep(1)
    mock_sense_hat.set_pixels([(0, 255, 0)] * 64)
    time.sleep(1)
    mock_sense_hat.set_pixels([(0, 0, 255)] * 64)

    # Keep the main thread alive FOREVER
    pause()


if __name__ == '__main__':
    main()
