def on_pin_pressed_p0():
    global Number2
    radio.send_number(4)
    Number2 = 4
    basic.show_leds("""
        . # # # .
        . # . . .
        . # # # .
        . # . . .
        . # . . .
        """)
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)
def on_received_number(receivedNumber):
    global Score_1, score_2, Number2
    if Number2 == 2 and receivedNumber == 1 or Number2 == 1 and receivedNumber == 3 or Number2 == 1 and receivedNumber == 3:
        basic.show_string("w")
        radio.send_string("L")
        Score_1 += 1
    if Number2 == 2 and receivedNumber == 2 or Number2 == 1 and receivedNumber == 1 or Number2 == 3 and receivedNumber == 3:
        basic.show_string("D")
        radio.send_string("D")
    if Number2 == 2 and receivedNumber == 3 or Number2 == 1 and receivedNumber == 2 or Number2 == 3 and receivedNumber == 2 or Number2 == 3 and receivedNumber == 1:
        basic.show_string("L")
        radio.send_string("W")
        score_2 += 1
    if Number2 == 4 and receivedNumber == 3 or Number2 == 4 and receivedNumber == 2:
        basic.show_string("W")
        radio.send_string("L")
        Score_1 += 1
    if Number2 == 4 and receivedNumber == 1:
        basic.show_string("L")
        radio.send_string("W")
        score_2 += 1
    if Number2 == 4 and receivedNumber == 4:
        basic.show_string("D")
        radio.send_string("D")
    Number2 = 0
    basic.clear_screen()
radio.on_received_number(on_received_number)
def on_button_pressed_a():
    global Number2
    radio.send_number(1)
    Number2 = 1
    basic.show_leds("""
        . . . . .
        . # # # .
        . # # # .
        . # # # .
        . . . . .
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)
def on_button_pressed_ab():
    global Number2
    radio.send_number(3)
    Number2 = 3
    basic.show_leds("""
        # . . . #
        . # . # .
        . . # . .
        # # . # #
        # # . # #
        """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)
def on_received_string(receivedString):
    basic.show_string(receivedString)
    basic.clear_screen()
radio.on_received_string(on_received_string)
def on_button_pressed_b():
    global Number2
    radio.send_number(2)
    Number2 = 2
    basic.show_leds("""
        . . . . .
        . . . . .
        # # # # #
        . . . . .
        . . . . .
        """)
input.on_button_pressed(Button.B, on_button_pressed_b)
Number2 = 0
Number2 = 0
score_2 = 0
Score_1 = 0
def on_forever():
    pass
basic.forever(on_forever)
