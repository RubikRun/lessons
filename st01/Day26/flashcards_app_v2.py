from gui import Window, Label, Button

# Flashcards: (language A → language B)
flashcards1 = [
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

flashcards2 = [
    ["el conocimiento", "knowledge"],
    ["la sabiduría", "wisdom"],
    ["la comprensión", "understanding"],
    ["el desarrollo", "development"],
    ["la investigación", "research"],
    ["la evidencia", "evidence"],
    ["la teoría", "theory"],
    ["la hipótesis", "hypothesis"],
    ["el análisis", "analysis"],
    ["la síntesis", "synthesis"],
    ["la percepción", "perception"],
    ["la conciencia", "awareness"],
    ["la existencia", "existence"],
    ["la realidad", "reality"],
    ["la identidad", "identity"],
    ["la personalidad", "personality"],
    ["la creatividad", "creativity"],
    ["la innovación", "innovation"],
    ["la tecnología", "technology"],
    ["la comunicación", "communication"],
    ["la colaboración", "collaboration"],
    ["la responsabilidad", "responsibility"],
    ["la oportunidad", "opportunity"],
    ["la posibilidad", "possibility"],
    ["la dificultad", "difficulty"],
    ["el desafío", "challenge"],
    ["la solución", "solution"],
    ["la estrategia", "strategy"],
    ["la organización", "organization"],
    ["la administración", "management"],
    ["la economía", "economy"],
    ["la política", "politics"],
    ["la justicia", "justice"],
    ["la libertad", "freedom"],
    ["la igualdad", "equality"],
    ["la diversidad", "diversity"],
    ["la cultura", "culture"],
    ["la tradición", "tradition"],
    ["la filosofía", "philosophy"],
    ["la psicología", "psychology"],
    ["la sociología", "sociology"],
    ["la educación", "education"],
    ["el conocimiento científico", "scientific knowledge"],
    ["la inteligencia", "intelligence"],
    ["la memoria", "memory"],
    ["la imaginación", "imagination"],
    ["la emoción", "emotion"],
    ["la motivación", "motivation"],
    ["la intención", "intention"],
    ["la decisión", "decision"],
    ["la consecuencia", "consequence"],
    ["la circunstancia", "circumstance"],
    ["la experiencia", "experience"],
    ["la habilidad", "ability"],
    ["la capacidad", "capacity"],
    ["la competencia", "competence"],
    ["la eficiencia", "efficiency"],
    ["la productividad", "productivity"],
    ["la calidad", "quality"],
    ["la cantidad", "quantity"],
    ["la estructura", "structure"],
    ["la función", "function"],
    ["el proceso", "process"],
    ["el sistema", "system"],
    ["el método", "method"],
    ["el concepto", "concept"],
    ["la definición", "definition"],
    ["la interpretación", "interpretation"],
    ["la explicación", "explanation"],
    ["la descripción", "description"],
    ["la comparación", "comparison"],
    ["la relación", "relationship"],
    ["la conexión", "connection"],
    ["la influencia", "influence"],
    ["el impacto", "impact"],
    ["la transformación", "transformation"],
    ["la evolución", "evolution"],
    ["el progreso", "progress"],
    ["el cambio", "change"],
    ["la estabilidad", "stability"],
    ["la complejidad", "complexity"],
    ["la simplicidad", "simplicity"],
    ["la precisión", "precision"],
    ["la exactitud", "accuracy"],
    ["la validez", "validity"],
    ["la fiabilidad", "reliability"],
    ["la relevancia", "relevance"],
    ["la importancia", "importance"],
    ["el significado", "meaning"],
    ["el propósito", "purpose"],
    ["el objetivo", "objective"],
    ["la meta", "goal"],
    ["el resultado", "result"],
    ["el logro", "achievement"],
    ["el fracaso", "failure"],
    ["el éxito", "success"],
    ["la mejora", "improvement"],
    ["el crecimiento", "growth"]
]

flashcards = []

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


def when_clicked6():
    global flashcards
    label.show()
    button1.show()
    button6.hide()
    button7.hide()
    flashcards = flashcards2
    label.set(flashcards[0][0])

def when_clicked7():
    global flashcards
    label.show()
    button1.show()
    button6.hide()
    button7.hide()
    flashcards = flashcards1
    label.set(flashcards[0][0])



# ---------------------------------
# GUI SETUP
# ---------------------------------
window = Window("Flashcards")

label = Label(window, "")
button1 = Button(window, "Show", when_clicked1)
button2 = Button(window, "I knew it", when_clicked2)
button3 = Button(window, "I didn't know", when_clicked3)
button4 = Button(window, "finish", when_clicked4)
button5 = Button(window, "go back", when_clicked5)
button6 = Button(window, "киан", when_clicked6)
button7 = Button(window, "Kamran", when_clicked7)






button1.hide()
button4.hide()
button2.hide()
button3.hide()
button5.hide()
button7.show()
button6.show()
label.hide()


window.run()
