from gui import Window, Label, Button

# Create a program
# that shows you the words from the flashcards list one by one.
# There should be a button for showing the next word in the list.
# When the words are finished, the button should hide itself.
#
# Hint: Exercise 7 is similar, you can use that as a base.


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


count = 0

def when_clicked():
    global count
    count += 1

    label.set(flashcards[count][0] + " - " + flashcards[count][1])
    if count == len(flashcards) - 1:
        button.hide()


window = Window("My First App")

label = Label(window, flashcards[count][0] + " - " + flashcards[count][1])
button = Button(window, "Next", when_clicked)

window.run()
