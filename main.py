def on_button_pressed_a():
    OLED.show_string_with_new_line("button A is pressed")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    OLED.show_string_with_new_line("Good Day!")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    OLED.show_string_with_new_line("button B is pressed")
input.on_button_pressed(Button.B, on_button_pressed_b)

OLED.init(64, 128)