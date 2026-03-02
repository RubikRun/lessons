from gui import Window, Label, Button

# Flashcards: (language A → language B)
flashcards = [
    ["el perro", "dog"],
    ["el gato", "cat"],
    ["la manzana", "apple"],
    ["la casa", "house"],
    ["el libro", "book"]
]

index = 0
score = 0

def show_question():
    # Show only the word in language A
    global index
    word = flashcards[index][0]

    label.set(word)
    show_button.show()

    right_button.hide()
    wrong_button.hide()

def flip_card():
    # Show the answer in both languages
    word = flashcards[index][0]
    answer = flashcards[index][1]

    label.set(f"{word} - {answer}")

    show_button.hide()
    right_button.show()
    wrong_button.show()

def mark_right():
    # User marked correct
    global score
    score += 1
    next_card()

def mark_wrong():
    # User marked incorrect
    next_card()

def next_card():
    # Move to the next flashcard or show final score
    global index

    index += 1
    if index >= len(flashcards):
        label.set(f"You knew {score} out of {len(flashcards)}!")
        show_button.hide()
        right_button.hide()
        wrong_button.hide()
        return

    show_question()

# ---------------------------------
# GUI SETUP
# ---------------------------------
window = Window("Flashcards")

label = Label(window, "")
show_button = Button(window, "Show", flip_card)
right_button = Button(window, "I knew it ✔️", mark_right)
wrong_button = Button(window, "I didn't know ❌", mark_wrong)

# Start with the first question
show_question()

window.run()
