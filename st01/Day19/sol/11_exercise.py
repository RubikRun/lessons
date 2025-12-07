from gui import Window, Label, Button

# Create a program
# that shows a "Hello, World!" label and a button that says "Show/Hide",
# which hides/shows the label each time it is clicked.

hidden = False

def when_clicked():
    global hidden
    if hidden:
        hidden = False
        label.show()
    else:
        hidden = True
        label.hide()


window = Window("My First App")

button = Button(window, "Hide/Show", when_clicked)
label = Label(window, "Hello, World!")

window.run()
