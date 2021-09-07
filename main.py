def onstart():
    global realisation
    realisation += randint(10, 200)
    ScrolText.show_string("Hello Father", SCROLL_DIR.LEFT, SCROLL_ROTATE.SR_0, 100)
    Realisationfn()
    basic.show_leds("""
        . # . # .
                . . . . .
                # . . . #
                . # # # .
                . . . . .
    """)
    Realisationfn()
    basic.pause(2000)
    bitbot.rotatems(BBRobotDirection.LEFT, 40, 500)
    bitbot.rotatems(BBRobotDirection.RIGHT, 40, 1000)
    bitbot.rotatems(BBRobotDirection.LEFT, 40, 500)
    Realisationfn()
    ScrolText.show_string("Can I go play over there?",
        SCROLL_DIR.LEFT,
        SCROLL_ROTATE.SR_0,
        100)
    Realisationfn()
    images.create_big_image("""
        . # # . # # . . . .
                . # # . # # . # # #
                . . . . . . . # # .
                . # # # # # . . . .
                # . . . . . # . . .
    """).show_image(0)
    Realisationfn()
    bitbot.rotatems(BBRobotDirection.LEFT, 50, 500)
    bitbot.rotatems(BBRobotDirection.RIGHT, 50, 500)
    Realisationfn()
    ScrolText.show_string("Please", SCROLL_DIR.LEFT, SCROLL_ROTATE.SR_0, 100)
    Realisationfn()
    if input.button_is_pressed(Button.A):
        ScrolText.show_string("Thanks dad", SCROLL_DIR.LEFT, SCROLL_ROTATE.SR_0, 100)
        bitbot.rotatems(BBRobotDirection.LEFT, 50, 500)
        Realisationfn()
    elif input.button_is_pressed(Button.B):
        ScrolText.show_string("Okay dad.", SCROLL_DIR.LEFT, SCROLL_ROTATE.SR_0, 100)
        basic.show_leds("""
            . # . # .
                        . . . . .
                        . . . . .
                        . # # # .
                        # . . . #
        """)
        bitbot.rotatems(BBRobotDirection.RIGHT, 50, 500)
        bitbot.goms(BBDirection.FORWARD, 15, 5000)
        Realisationfn()
    else:
        pass
def whatPartToRun():
    if start == 1:
        onstart()
    elif two == 1:
        partTwo()
    elif three == 0:
        partThree()
    else:
        while realisation < 0:
            Realisationfn()
def partThree():
    ScrolText.show_string("DO THIS PART", SCROLL_DIR.LEFT, SCROLL_ROTATE.SR_0, 100)
def Sleep():
    ScrolText.show_string("Z z z z z z (_ _ \")..",
        SCROLL_DIR.LEFT,
        SCROLL_ROTATE.SR_0,
        100)
    Realisationfn()
    basic.pause(10000)
    bitbot.goms(BBDirection.REVERSE, 100, 2000)
    Realisationfn()
    ScrolText.show_string("I CANT SLEEP", SCROLL_DIR.LEFT, SCROLL_ROTATE.SR_0, 100)
    Realisationfn()

def on_gesture_six_g():
    GetHit()
    whatPartToRun()
input.on_gesture(Gesture.SIX_G, on_gesture_six_g)

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
def partTwo():
    bitbot.stop(BBStopMode.COAST)
def Shake():
    basic.show_leds("""
        # . . # .
                # . . # .
                . . . . .
                . . . . .
                . # # # #
    """)
    basic.show_leds("""
        . # . . #
                . # . . #
                . . . . .
                . . . . .
                # # # # .
    """)
    basic.show_leds("""
        # . . # .
                # . . # .
                . . . . .
                . . . . .
                . # # # #
    """)
    basic.show_leds("""
        . # . . #
                . # . . #
                . . . . .
                . . . . .
                # # # # .
    """)
    Realisationfn()
    images.icon_image(IconNames.SAD).show_image(0)
    Realisationfn()

def on_gesture_shake():
    Shake()
    whatPartToRun()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def GetHit():
    basic.show_leds("""
        . # . # .
                . . . . .
                . . . . .
                . # # # .
                # . . . #
    """)
    Realisationfn()
    basic.pause(2000)
    ScrolText.show_string("Why did you hit me? :(",
        SCROLL_DIR.LEFT,
        SCROLL_ROTATE.SR_0,
        100)
    ScrolText.show_string("I'm leaving this abuse you put me through! >:(",
        SCROLL_DIR.LEFT,
        SCROLL_ROTATE.SR_0,
        100)
    Realisationfn()
    bitbot.rotatems(BBRobotDirection.LEFT, 90, 600)
    bitbot.goms(BBDirection.FORWARD, 100, 2000)
    Realisationfn()

def on_gesture_logo_down():
    Sleep()
    whatPartToRun()
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

realisation = 0
start = 0
two = 0
three = 0
three = 1
two = 1
start = 1