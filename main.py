def on_button_pressed_a():
    pass
input.on_button_pressed(Button.A, on_button_pressed_a)

def sovietAnthem():
    midi.play_drum(MidiInstrument.ACOUSTIC_GRAND_PIANO)
def Korobeiniki():
    music.play_melody("B - F G A - G F ", 170)
    music.play_melody("E - E G B - A F ", 170)

ScrolText.show_string("M u s i c", SCROLL_DIR.LEFT, SCROLL_ROTATE.SR_0, 100)
if input.button_is_pressed(Button.A):
    ScrolText.show_string("T E T R I S", SCROLL_DIR.LEFT, SCROLL_ROTATE.SR_0, 100)
elif input.button_is_pressed(Button.B):
    ScrolText.show_string("F O O D", SCROLL_DIR.LEFT, SCROLL_ROTATE.SR_0, 100)
else:
    pass