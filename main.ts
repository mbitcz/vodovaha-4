input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    oprava = zrychleni
})
function mereni(): number {
    
    zrychleni = input.acceleration(Dimension.X)
    naklon = zrychleni - oprava
    if (naklon > 100) {
        hodnota_mereni = 0
    } else if (naklon > 15) {
        hodnota_mereni = 1
    } else if (naklon < -100) {
        hodnota_mereni = 4
    } else if (naklon < -15) {
        hodnota_mereni = 3
    } else {
        hodnota_mereni = 2
    }
    
    return hodnota_mereni
}

let nova = 0
let hodnota_mereni = 0
let naklon = 0
let zrychleni = 0
let oprava = 0
basic.showLeds(`
    # . # . #
        . # # # .
        . . . . .
        . # # # .
        # . # . #
`)
oprava = 0
let stara = 99
basic.forever(function on_forever() {
    
    nova = mereni()
    if (nova != stara) {
        led.unplot(stara, 2)
        led.plot(nova, 2)
        stara = nova
    }
    
})
