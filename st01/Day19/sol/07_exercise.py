from gui import Window, Label, Button

# Create a program
# that tells you a joke, one sentence at a time.
# There should be a button for showing the next sentence of the joke.
#
# Example joke that you can use:
#     I asked my dog what 2 minus 2 is.
#     He said nothing.
#     Which is technically correct.

count = 0

def when_clicked():
    global count
    count += 1

    if count == 1:
        label.set("He said nothing.")
    elif count == 2:
        label.set("Which is technically correct.")
        button.hide() 


window = Window("My First App")

label = Label(window, "I asked my dog what 2 minus 2 is.")
button = Button(window, "Next", when_clicked)

window.run()
