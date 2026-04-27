from gui import Window, Label, Button

# Flashcards: (language A → language B)
flashcards = [
    ["el perro", "dog"],
    ["el gato", "cat"],
    ["la casa", "house"],
    ["la manzana", "apple"],
    ["el libro", "book"],
    ["la mesa", "table"],
    ["la silla", "chair"],
    ["el coche", "car"],
    ["la puerta", "door"],
    ["la ventana", "window"],
    ["el agua", "water"],
    ["el pan", "bread"],
    ["el queso", "cheese"],
    ["la leche", "milk"],
    ["la comida", "food"],
    ["el amigo", "friend (male)"],
    ["la amiga", "friend (female)"],
    ["el niño", "boy"],
    ["la niña", "girl"],
    ["el hombre", "man"],
    ["la mujer", "woman"],
    ["el sol", "sun"],
    ["la luna", "moon"],
    ["la playa", "beach"],
    ["el árbol", "tree"],
    ["la flor", "flower"],
    ["la escuela", "school"],
    ["el maestro", "teacher (male)"],
    ["la maestra", "teacher (female)"],
    ["la ciudad", "city"],
    ["el campo", "countryside"],
    ["el trabajo", "job"],
    ["la tienda", "store"],
    ["el zapato", "shoe"],
    ["la camisa", "shirt"],
    ["el pantalón", "pants"],
    ["la mano", "hand"],
    ["el pie", "foot"],
    ["la cabeza", "head"],
    ["el pelo", "hair"],
    ["el ojo", "eye"],
    ["la boca", "mouth"],
    ["la nariz", "nose"],
    ["el perro", "dog"],
    ["el pescado", "fish"],
    ["la carne", "meat"],
    ["el huevo", "egg"],
    ["el teléfono", "phone"],
    ["el reloj", "watch/clock"],
    ["el papel", "paper"],
    ["el lápiz", "pencil"],
    ["el bolígrafo", "pen"],
    ["el color", "color"],
    ["rojo", "red"],
    ["azul", "blue"],
    ["verde", "green"],
    ["amarillo", "yellow"],
    ["negro", "black"],
    ["blanco", "white"],
    ["pequeño", "small"],
    ["grande", "big"],
    ["frío", "cold"],
    ["el calor", "heat"],
    ["la lluvia", "rain"],
    ["el viento", "wind"],
    ["el tiempo", "time/weather"],
    ["la música", "music"],
    ["la película", "movie"],
    ["el juego", "game"],
    ["el perro", "dog"],
    ["correr", "to run"],
    ["caminar", "to walk"],
    ["hablar", "to speak"],
    ["comer", "to eat"],
    ["beber", "to drink"],
    ["vivir", "to live"],
    ["ver", "to see"],
    ["oír", "to hear"],
    ["abrir", "to open"],
    ["cerrar", "to close"],
    ["leer", "to read"],
    ["escribir", "to write"],
    ["dormir", "to sleep"],
    ["jugar", "to play"],
    ["saltar", "to jump"],
    ["aprender", "to learn"],
    ["preguntar", "to ask"],
    ["escuchar", "to listen"],
    ["mirar", "to look/watch"],
    ["comprar", "to buy"],
    ["vender", "to sell"],
    ["cocinar", "to cook"],
    ["limpiar", "to clean"],
    ["el día", "day"],
    ["la noche", "night"],
    ["la mañana", "morning"],
    ["la tarde", "afternoon"],
    ["la ropa", "clothes"],
    ["la cama", "bed"],
    ["la calle", "street"],
    ["el río", "river"],
]

x = 0
y = 0

def when_clicked1():
    global x
    label.set(flashcards[x][0] + " - " + flashcards[x][1])
    button1.hide()
    button2.show()
    button3.show()
    button5.hide()

    button4.hide()
    button4.show()

def when_clicked2():
    global x
    global y
    x += 1
    y += 1
    button5.hide()

    if x < len(flashcards):
        label.set(flashcards[x][0])
        button1.show()
        button2.hide()
        button3.hide()
        button5.hide()

        button4.hide()
        button4.show()
    else:
        label.set("You knew " + str(y) + " out of " + str(len(flashcards)) + " words")
        button1.hide()
        button2.hide()
        button3.hide()
        button5.hide()

        button4.hide()
        button4.show()

def when_clicked3():
    global x
    x += 1

    if x < len(flashcards):
        label.set(flashcards[x][0])
        button1.show()
        button2.hide()
        button3.hide()
        button5.hide()

        button4.hide()
        button4.show()
    else:
        label.set("You knew " + str(y) + " out of " + str(len(flashcards)) + " words")
        button1.hide()
        button2.hide()
        button3.hide()
        button5.hide()

        button4.hide()
        button4.show()
        

def when_clicked4():
    global x

    label.set("You knew " + str(y) + " out of " + str(x) + " words")
    button1.hide()
    button2.hide()
    button3.hide()
    button4.hide()
    button5.show()


def when_clicked5():
    global x, y
    x = x - x
    y = 0
    label.set(flashcards[x][0])

    button1.show()
    button2.hide()
    button3.hide()
    button4.hide()
    button5.hide()


# ---------------------------------
# GUI SETUP
# ---------------------------------
window = Window("Flashcards")

label = Label(window, flashcards[0][0])
button1 = Button(window, "Show", when_clicked1)
button2 = Button(window, "I knew it", when_clicked2)
button3 = Button(window, "I didn't know", when_clicked3)
button4 = Button(window, "finish", when_clicked4)
button5 = Button(window, "go back", when_clicked5)

button2.hide()
button3.hide()
button5.hide()

window.run()
