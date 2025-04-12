from M5unit_ASR_Example1 import ASR

asr = ASR(debug=True)  # using default serial settings


# set up the ASR message handling

def h_direction(cmdNum, word):
    # one handler for all direction commands
    print(f"h_direction cmdNum {cmdNum} word '{word}'")


def h_wakeup(cmdNum, word):
    print(f"h_wakeup cmdNum {cmdNum} word '{word}'")


# Command List
# the ASR only responds with messages of the format 0xAA 0x55 <cmdNum> 0x55 0xAA
# This dict contains the default command words
# to change the command words you need to re-flash the ASR
# to handle commands

commandList = {
    # wakeup
    0xFF: ("I'm here", h_wakeup),
    # direction control
    0x01: ("up", h_direction),
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
    0x10: ("open", None),
    0x11: ("close", None),
    0x12: ("start", None),
    0x13: ("stop", None),
    0x14: ("turn on", None),
    0x15: ("turn off", None),
    0x16: ("play", None),
    0x17: ("pause", None),
    0x18: ("turn on the lights", None),
    0x19: ("turn off the lights", None),
    0x1A: ("previous", None),
    0x1B: ("next", None),
    # numbers
    0x20: ("zero", None),
    0x21: ("one", None),
    0x22: ("two", None),
    0x23: ("three", None),
    0x24: ("four", None),
    0x25: ("five", None),
    0x26: ("six", None),
    0x27: ("seven", None),
    0x28: ("eight", None),
    0x29: ("nine", None),
    # acknowledgement & greeting
    0x30: ("ok", None),
    0x31: ("Hi, A S R", h_wakeup),
    0x32: ("hello", h_wakeup),
    #
    0x40: ("increase volume", None),
    0x41: ("decrease volume", None),
    0x42: ("maximum volume", None),
    0x43: ("medium volume", None),
    0x44: ("minimum volume", None),
    0x45: ("check firmware version", None),
    #
    0xFE: ("Hi, I am ASR", None)

}

# print("key,word,handler")
# for k in commandList.keys():
#    (word,handler)=commandList[k]
#    print(k,word,handler)


# mainloop
print("Ready and waiting, say something like 'Hi, M five'")
while True:
    cmdNum = asr.update()
    if cmdNum is not None:
        try:
            word, handler = commandList[cmdNum]
            if handler is None:
                print(f"<'{word}'")
            else:
                # pass the info to the handler
                handler(cmdNum, word)

        # this error occurs if no reponse has
        except KeyError:
            print("Unknown command number")
        except Exception as e:
            print(f"Exception {e}")

