import tkinter as tk

class App(tk.Tk):
    def __init__(window):
        super().__init__()

        ##initializing the window
        window.title("To-Do List")
        window.geometry("400x700")
        window.resizable(False,False)
        window.iconphoto(False, tk.PhotoImage(file="assets/title_photo.png"))

if __name__ == "__main__":
    app = App()
    app.mainloop()
    
