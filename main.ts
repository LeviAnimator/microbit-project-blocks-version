input.onButtonPressed(Button.A, function () {
	
})
function sovietAnthem () {
    midi.playDrum(MidiInstrument.AcousticGrandPiano)
}
function Korobeiniki () {
    music.playMelody("B - F G A - G F ", 170)
    music.playMelody("E - E G B - A F ", 170)
}
function layerOne () {
    ScrolText.showString(
    "M u s i c",
    SCROLL_DIR.LEFT,
    SCROLL_ROTATE.SR_0,
    100
    )
    if (input.buttonIsPressed(Button.A)) {
        ScrolText.showString(
        "T E T R I S",
        SCROLL_DIR.LEFT,
        SCROLL_ROTATE.SR_0,
        100
        )
        if (input.buttonIsPressed(Button.A)) {
            Korobeiniki()
        }
    } else if (input.buttonIsPressed(Button.B)) {
        ScrolText.showString(
        "F O O D",
        SCROLL_DIR.LEFT,
        SCROLL_ROTATE.SR_0,
        100
        )
    } else {
    	
    }
}
layerOne()
