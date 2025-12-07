from gui import Window, Label, Button

# How to change a button's text


def when_clicked():
    button.set("Clicked!")


window = Window("My First App")

button = Button(window, "Click Me", when_clicked)

window.run()
