input.onPinPressed(TouchPin.P0, function () {
    radio.sendNumber(4)
    Number2 = 4
    basic.showLeds(`
        . # # # .
        . # . . .
        . # # # .
        . # . . .
        . # . . .
        `)
})
radio.onReceivedNumber(function (receivedNumber) {
    if (Number2 == 2 && receivedNumber == 1 || Number2 == 1 && receivedNumber == 3 || Number2 == 1 && receivedNumber == 3) {
        basic.showString("w")
        radio.sendString("L")
        Score_1 += 1
    }
    if (Number2 == 2 && receivedNumber == 2 || Number2 == 1 && receivedNumber == 1 || Number2 == 3 && receivedNumber == 3) {
        basic.showString("D")
        radio.sendString("D")
    }
    if (Number2 == 2 && receivedNumber == 3 || Number2 == 1 && receivedNumber == 2 || Number2 == 3 && receivedNumber == 2 || Number2 == 3 && receivedNumber == 1) {
        basic.showString("L")
        radio.sendString("W")
        score_2 += 1
    }
    if (Number2 == 4 && receivedNumber == 3 || Number2 == 4 && receivedNumber == 2) {
        basic.showString("W")
        radio.sendString("L")
        Score_1 += 1
    }
    if (Number2 == 4 && receivedNumber == 1) {
        basic.showString("L")
        radio.sendString("W")
        score_2 += 1
    }
    if (Number2 == 4 && receivedNumber == 4) {
        basic.showString("D")
        radio.sendString("D")
    }
    Number2 = 0
    basic.clearScreen()
})
input.onButtonPressed(Button.A, function () {
    radio.sendNumber(1)
    Number2 = 1
    basic.showLeds(`
        . . . . .
        . # # # .
        . # # # .
        . # # # .
        . . . . .
        `)
})
input.onButtonPressed(Button.AB, function () {
    radio.sendNumber(3)
    Number2 = 3
    basic.showLeds(`
        # . . . #
        . # . # .
        . . # . .
        # # . # #
        # # . # #
        `)
})
radio.onReceivedString(function (receivedString) {
    basic.showString(receivedString)
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function () {
    radio.sendNumber(2)
    Number2 = 2
    basic.showLeds(`
        . . . . .
        . . . . .
        # # # # #
        . . . . .
        . . . . .
        `)
})
let score_2 = 0
let Score_1 = 0
let Number2 = 0
Number2 = 0
basic.forever(function () {
	
})
