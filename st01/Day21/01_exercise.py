from gui import Window, Label, Button

# Below is a program with a button
# that counts how many times you click it.
#
# Can you extend the program so that there are 2 such buttons?

x = 1

def when_clicked():
    global x

    button.set(x)
    x = x + 1

window = Window("My First App")

button = Button(window, "Click Me", when_clicked)

window.run()
