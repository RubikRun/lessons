from gui import Window, Label, Button

# Flashcards: (language A → language B)
flashcards = [
    ["el perro", "dog"],
    ["el gato", "cat"],
    ["la manzana", "apple"],
    ["la casa", "house"],
    ["el libro", "book"]
]

x = 0
y = 0

def when_clicked1():
    global x
    label.set(flashcards[x][0] + " - " + flashcards[x][1])
    button1.hide()
    button2.show()
    button3.show()

def when_clicked2():
    global x
    global y
    x += 1
    y += 1

    if x < len(flashcards):
        label.set(flashcards[x][0])
        button1.show()
        button2.hide()
        button3.hide()
    else:
        label.set("You knew " + str(y) + " out of " + str(len(flashcards)) + " words")
        button1.hide()
        button2.hide()
        button3.hide()

def when_clicked3():
    global x
    x += 1

    if x < len(flashcards):
        label.set(flashcards[x][0])
        button1.show()
        button2.hide()
        button3.hide()
    else:
        label.set("You knew " + str(y) + " out of " + str(len(flashcards)) + " words")
        button1.hide()
        button2.hide()
        button3.hide()
        

# ---------------------------------
# GUI SETUP
# ---------------------------------
window = Window("Flashcards")

label = Label(window, flashcards[0][0])
button1 = Button(window, "Show", when_clicked1)
button2 = Button(window, "I knew it", when_clicked2)
button3 = Button(window, "I didn't know", when_clicked3)

button2.hide()
button3.hide()

window.run()
