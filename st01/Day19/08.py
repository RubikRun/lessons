from gui import Window, Label, Button

# How to hide a button


def when_clicked():
    button.hide()


window = Window("My First App")

button = Button(window, "Click Me", when_clicked)

window.run()
