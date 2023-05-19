def on_button_pressed_a():
    global oprava
    oprava = zrychleni
input.on_button_pressed(Button.A, on_button_pressed_a)

def mereni():
    global zrychleni, naklon, hodnota_mereni
    zrychleni = input.acceleration(Dimension.X)
    naklon = zrychleni - oprava
    if naklon > 100:
        hodnota_mereni = 0
    elif naklon > 15:
        hodnota_mereni = 1
    elif naklon < -100:
        hodnota_mereni = 4
    elif naklon < -15:
        hodnota_mereni = 3
    else:
        hodnota_mereni = 2
    return hodnota_mereni
nova = 0
hodnota_mereni = 0
naklon = 0
zrychleni = 0
oprava = 0
basic.show_leds("""
    # . # . #
        . # # # .
        . . . . .
        . # # # .
        # . # . #
""")
oprava = 0
stara = 99

def on_forever():
    global nova, stara
    nova = mereni()
    if nova != stara:
        led.unplot(stara, 2)
        led.plot(nova, 2)
        stara = nova
basic.forever(on_forever)
