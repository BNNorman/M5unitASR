# M5unitASR
Circuitpython driver and examples for the M5unit-ASR

The M5unit-ASR responds to a set of preprogrammed words returning, via a serial port, the recognised word command code.

The M5unit-ASR is preprogrammed with a standard set of words it knows. It only supports one language so if you want to change it and/or the keywords then you must re-flash the unit. The flashing program is written in Chinese - oh hum! So I left mine programmed as standard - in English as I bought it here.

The unit responds, via a serial line, to the command words it recognises. It seems to go to sleep quickly after the wakeup command "Hi, M five" if you don't say anything.

You can issue a number of commands after the wakeup.

However, it has some issues with identifying some words:- "two","six","up". It always recognises the wakeup command.


# software

## flashing

You can download the flashing software from this page. I haven't used it because it's in Chinese and I need to go to night school to learn it.

https://docs.m5stack.com/en/guide/offline_voice/unit_asr/firmware

## M5unit_ASR.py

This is my driver. It just sets up the serial port then provides a method (update) to return any codes returned.

## M5unit_ASR_example1.py

This is intended to show how you can incorporate handlers for recognised word commands.

The default list of commands is a dictionary keyed on the command number and contains tuples (word,handler). You must change this to match your ASR if you re-flash it.



```
commandList={
    # wakeup
    0xFF: ("I'm here",h_wakeup),
    # direction control
    0x01: ("up",h_direction),
    0x02: ("down", h_direction),
    0x03: ("left", h_direction),
    0x04: ("turn left", h_direction),
    0x05: ("right", h_direction),
    0x06: ("turn right", h_direction),
    0x07: ("forward", h_direction),
    0x08: ("front", h_direction),
    0x09: ("backward", h_direction),
    0x0A: ("back", h_direction),
    # operation commands
    0x10: ("open",None),
    0x11: ("close",None),
    0x12: ("start",None),
    0x13: ("stop",None),
    0x14: ("turn on",None),
    0x15: ("turn off",None),
    0x16: ("play",None),
    0x17: ("pause",None),
    0x18: ("turn on the lights",None),
    0x19: ("turn off the lights",None),
    0x1A: ("previous",None),
    0x1B: ("next",None),
    # numbers
    0x20: ("zero",None),
    0x21: ("one",None),
    0x22: ("two",None),
    0x23: ("three",None),
    0x24: ("four",None),
    0x25: ("five",None),
    0x26: ("six",None),
    0x27: ("seven",None),
    0x28: ("eight",None),
    0x29: ("nine",None),
    # acknowledgement & greeting
    0x30: ("ok",None),
    0x31: ("Hi, A S R",None),
    0x32: ("hello",None),
    #
    0x40: ("increase volume",None),
    0x41: ("decrease volume",None),
    0x42: ("maximum volume",None),
    0x43: ("medium volume",None),
    0x44: ("minimum volume",None),
    0x45: ("check firmware version",None), # unit just speaks "Version one"
    #
    0xFE: ("Hi, I am ASR",None)
    
}
```















