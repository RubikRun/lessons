from gui import Window, Label, Button

# Create a program
# that shows a "Hello, World!" label and 2 buttons,
# one that hides the label and another that shows it again.
#
# ( Hint: Showing a label/button after it has been hidden is done like this: label.show() or button.show() )


def when_clicked_show():
    label.show()

def when_clicked_hide():
    label.hide()


window = Window("My First App")

show_button = Button(window, "Show", when_clicked_show)
hide_button = Button(window, "Hide", when_clicked_hide)
label = Label(window, "Hello, World!")

window.run()
