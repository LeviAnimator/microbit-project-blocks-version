function onstart () {
    realisation += randint(10, 200)
    ScrolText.showString(
    "Hello Father",
    SCROLL_DIR.LEFT,
    SCROLL_ROTATE.SR_0,
    100
    )
    Realisationfn()
    basic.showLeds(`
        . # . # .
        . . . . .
        # . . . #
        . # # # .
        . . . . .
        `)
    basic.pause(2000)
    bitbot.rotatems(BBRobotDirection.Left, 40, 500)
    bitbot.rotatems(BBRobotDirection.Right, 40, 1000)
    bitbot.rotatems(BBRobotDirection.Left, 40, 500)
    Realisationfn()
    ScrolText.showString(
    "Can I go play over there?",
    SCROLL_DIR.LEFT,
    SCROLL_ROTATE.SR_0,
    100
    )
    Realisationfn()
    images.createBigImage(`
        . # # . # # . . . .
        . # # . # # . # # #
        . . . . . . . # # .
        . # # # # # . . . .
        # . . . . . # . . .
        `).showImage(0)
    Realisationfn()
    bitbot.rotatems(BBRobotDirection.Left, 50, 500)
    bitbot.rotatems(BBRobotDirection.Right, 50, 500)
    Realisationfn()
    ScrolText.showString(
    "Please",
    SCROLL_DIR.LEFT,
    SCROLL_ROTATE.SR_0,
    100
    )
    Realisationfn()
}
function Realisationfn () {
    realisation += -1
    if (realisation == 0) {
        bitbot.rotatems(BBRobotDirection.Left, 100, 1000)
        bitbot.goms(BBDirection.Forward, 100, 250)
        bitbot.rotatems(BBRobotDirection.Left, 100, 1000)
        bitbot.goms(BBDirection.Forward, 100, 250)
        bitbot.rotatems(BBRobotDirection.Left, 100, 1000)
        bitbot.goms(BBDirection.Forward, 100, 250)
        bitbot.rotatems(BBRobotDirection.Left, 100, 1000)
        bitbot.goms(BBDirection.Forward, 100, 250)
        ScrolText.showString(
        "W H E R E A M I H E L P M E . I T ' S D A R K I N H E R E",
        SCROLL_DIR.LEFT,
        SCROLL_ROTATE.SR_0,
        100
        )
        basic.pause(500)
        bitbot.go(BBDirection.Forward, 100)
        bitbot.go(BBDirection.Reverse, 100)
    }
}
function Dunno () {
    bitbot.goms(BBDirection.Forward, 60, 5000)
    bitbot.rotatems(BBRobotDirection.Right, 60, 400)
    ScrolText.showString(
    "FUCKYOU",
    SCROLL_DIR.LEFT,
    SCROLL_ROTATE.SR_0,
    100
    )
    basic.showLeds(`
        . # . # .
        . . . . .
        . . . . .
        # . . . #
        . # # # .
        `)
    bitbot.ledRainbow()
    bitbot.goms(BBDirection.Forward, 60, randint(1000, 10000))
    Realisationfn()
}
let realisation = 0
onstart()
