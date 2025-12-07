from gui import Window, Label, Button

# Create a program
# that shows 2 buttons with the number 0 on them.
# Each time a button is clicked, the number on it should increase by 1.

num1 = 0
num2 = 0

def when_clicked1():
    global num1
    num1 += 1
    button1.set(str(num1))

def when_clicked2():
    global num2
    num2 += 1
    button2.set(str(num2))

window = Window("My First App")

button1 = Button(window, "0", when_clicked1)
button2 = Button(window, "0", when_clicked2)

window.run()
