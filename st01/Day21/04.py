from gui import Window, Label, Button

# How to hide a label


def when_clicked():
    label.hide()


window = Window("My First App")

button = Button(window, "Click Me", when_clicked)
label = Label(window, "Hello, World!")

window.run()
