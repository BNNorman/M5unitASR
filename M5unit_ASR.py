# M5unit_ASR.py
#
import board
import busio


class ASR:

    def __init__(self, TX=board.GP0, RX=board.GP1, baud=115200, debug=False):
        """
        The ASR unit TX should connect to Pico RX and ASR RX to Pico TX
        RX should connect to Pico TX (GP1) and TX tp Pico RX (GP0)
        or similar uart pins
        """
        self.uart = busio.UART(TX, RX, baudrate=baud)
        self.debug = debug

    def update(self):
        # no error cheking here
        msg = self.uart.read(5)  # should be 0xAA 0x55 <cmd> 0x55 0xAA
        b = []
        if msg is not None:
            for item in list(msg):
                b.append(hex(item))
            if self.debug:
                print(f"msg {b}")
            return list(msg)[2]
        else:
            return None


if __name__ == "__main__":
    asr = ASR()  # default serial
    print("Ready, speak now or forever hold your peace")
    while True:
        reply = asr.update()
        if reply is not None:
            print(f"< {hex(reply)}")


