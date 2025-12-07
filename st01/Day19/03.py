from gui import Window, Label, Button

# How to make a button do something when clicked


def when_clicked():
    print("Button was clicked!")


window = Window("My First App")

button = Button(window, "Click Me", when_clicked)

window.run()
