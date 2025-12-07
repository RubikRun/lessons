from gui import Window, Label, Button

# Create a program
# that shows a button with the number 0 on it.
# Each time the button is clicked, the number should increase by 1.

num = 0

def when_clicked():
    global num
    num += 1
    button.set(str(num))

window = Window("My First App")

button = Button(window, "0", when_clicked)

window.run()
