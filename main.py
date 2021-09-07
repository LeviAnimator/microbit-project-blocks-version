def onstart():
    global realisation
    realisation += randint(10, 200)
    ScrolText.show_string("Hello Father", SCROLL_DIR.LEFT, SCROLL_ROTATE.SR_0, 100)
    basic.show_leds("""
        . # . # .
                . . . . .
                # . . . #
                . # # # .
                . . . . .
    """)
    basic.pause(2000)
    bitbot.rotatems(BBRobotDirection.LEFT, 40, 500)
    bitbot.rotatems(BBRobotDirection.RIGHT, 40, 1000)
    bitbot.rotatems(BBRobotDirection.LEFT, 40, 500)
    ScrolText.show_string("Can I go play over there?",
        SCROLL_DIR.LEFT,
        SCROLL_ROTATE.SR_0,
        100)
    images.create_big_image("""
        . # # . # # . . . .
                . # # . # # . # # #
                . . . . . . . # # .
                . # # # # # . . . .
                # . . . . . # . . .
    """).show_image(0)
    bitbot.rotatems(BBRobotDirection.LEFT, 50, 500)
    bitbot.rotatems(BBRobotDirection.RIGHT, 50, 500)
    ScrolText.show_string("Please", SCROLL_DIR.LEFT, SCROLL_ROTATE.SR_0, 100)
def Realisationfn():
    global realisation
    realisation += -1
    if realisation == 0:
        bitbot.rotatems(BBRobotDirection.LEFT, 100, 1000)
        bitbot.goms(BBDirection.FORWARD, 100, 250)
        bitbot.rotatems(BBRobotDirection.LEFT, 100, 1000)
        bitbot.goms(BBDirection.FORWARD, 100, 250)
        bitbot.rotatems(BBRobotDirection.LEFT, 100, 1000)
        bitbot.goms(BBDirection.FORWARD, 100, 250)
        bitbot.rotatems(BBRobotDirection.LEFT, 100, 1000)
        bitbot.goms(BBDirection.FORWARD, 100, 250)
        ScrolText.show_string("W H E R E A M I H E L P M E . I T ' S D A R K I N H E R E",
            SCROLL_DIR.LEFT,
            SCROLL_ROTATE.SR_0,
            100)
        basic.pause(500)
        bitbot.go(BBDirection.FORWARD, 100)
        bitbot.go(BBDirection.REVERSE, 100)
def Dunno():
    bitbot.goms(BBDirection.FORWARD, 60, 5000)
    bitbot.rotatems(BBRobotDirection.RIGHT, 60, 400)
    ScrolText.show_string("FUCKYOU", SCROLL_DIR.LEFT, SCROLL_ROTATE.SR_0, 100)
    basic.show_leds("""
        . # . # .
                . . . . .
                . . . . .
                # . . . #
                . # # # .
    """)
    bitbot.led_rainbow()
    bitbot.goms(BBDirection.FORWARD, 60, randint(1000, 10000))
    Realisationfn()
realisation = 0
onstart()