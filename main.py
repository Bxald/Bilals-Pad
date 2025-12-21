import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.extensions.encoder import RotaryEncoder
from kmk.extensions.oled import OLED
import busio
from kmk.handlers.sequences import simple_key_sequence

keyboard = KMKKeyboard()

# ------------------------
# Keys
# ------------------------
keyboard.matrix = KeysScanner(
    pins=[
        board.D2, board.D10, board.D4,
        board.D0, board.D3, board.D1,
    ],
    value_when_pressed=False,
)

# Default keymap, easy to change
keyboard.keymap = [
    [
        KC.Q, KC.W, KC.E,
        KC.A, KC.S, KC.D,
    ]
]

# Track last key pressed
keyboard.last_key = None
def track_last_key(keycode):
    keyboard.last_key = keycode

# Wrap keys to track last pressed
for r, key in enumerate(keyboard.keymap[0]):
    def make_callback(kc):
        return lambda: track_last_key(kc)
    keyboard.keymap[0][r] = simple_key_sequence([key, make_callback(key)])

# ------------------------
# Rotary Encoder
# ------------------------
encoder = RotaryEncoder(
    clk=board.GP27,  # A
    dt=board.GP26,   # B
    sw=board.GP28,   # S1
    value_when_pressed=False,
)

# Track volume for OLED
encoder.volume = 50  # start at 50%

def handle_rot(direction):
    if direction == "clockwise":
        encoder.volume = min(100, encoder.volume + 5)
        return KC.VOLU
    else:
        encoder.volume = max(0, encoder.volume - 5)
        return KC.VOLD

encoder.keymap = {
    "clockwise": handle_rot("clockwise"),
    "counter_clockwise": handle_rot("counter_clockwise"),
    "pressed": KC.MUTE,
}

keyboard.extensions.append(encoder)

# ------------------------
# OLED
# ------------------------
i2c = busio.I2C(scl=board.GP7, sda=board.GP6)

oled_ext = OLED(
    i2c=i2c,
    width=128,
    height=64,
    flip=False
)

def oled_display(oled):
    oled.fill(0)
    
    # Volume bar
    oled.text("Volume:", 0, 0)
    bar_width = int(encoder.volume / 100 * 120)
    oled.fill_rect(0, 10, bar_width, 10, 1)
    
    # Encoder press state
    pressed_text = "Pressed" if encoder.sw_pressed else "Idle"
    oled.text("Encoder: " + pressed_text, 0, 25)
    
    # Last key pressed
    last = str(keyboard.last_key) if keyboard.last_key else "None"
    oled.text("Key: " + last, 0, 40)
    
    oled.show()

oled_ext.display_func = oled_display
keyboard.extensions.append(oled_ext)

# ------------------------
# Run keyboard
# ------------------------
if __name__ == "__main__":
    keyboard.go()
