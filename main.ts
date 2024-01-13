input.onButtonPressed(Button.A, function on_button_pressed_a() {
    OLED.showStringWithNewLine("button A is pressed")
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    OLED.showStringWithNewLine("Good Day!")
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    OLED.showStringWithNewLine("button B is pressed")
})
OLED.init(64, 128)
