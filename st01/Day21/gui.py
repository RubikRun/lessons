import tkinter as tk

class Window:
    def __init__(self, title="Window"):
        self._root = tk.Tk()
        self._root.title(title)
        self._root.geometry("640x480")
        self._root.resizable(False, True)

    def run(self):
        self._root.mainloop()


class BaseWidget:
    def show(self, pady=5):
        self._widget.pack(pady=pady)

    def hide(self):
        self._widget.pack_forget()


class Label(BaseWidget):
    def __init__(self, window, text=""):
        self._widget = tk.Label(window._root, text=text, font=("Arial", 20))
        self.show()

    def set(self, text):
        self._widget.config(text=text)


class Button(BaseWidget):
    def __init__(self, window, text="", on_click=None):
        self._widget = tk.Button(window._root, text=text, font=("Arial", 16))
        if on_click is not None:
            self._widget.config(command=on_click)
        self.show()
    def set(self, text):
        self._widget.config(text=text)


class Input(BaseWidget):
    def __init__(self, window):
        self._widget = tk.Entry(window._root, font=("Arial", 16))
        self.show()

    def get(self):
        return self._widget.get()

    def clear(self):
        self._widget.delete(0, "end")
