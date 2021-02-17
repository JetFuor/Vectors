
# Aight, what do I want in my calcluator
# Start with choosing 2D or 3D, then moving to choose what type of equation want to calculate
# Then input and show the output
# Can choose go back, choose sth else
# Due date: Friday
# Start with home page, go to 2D or 3D
# Go to options screen with multiple calculators
# Then each individual calculator
# IDK finish by friday, might need alot of late nighters


from tkinter import *
import time
# Splash screen commands

class Splash(Toplevel):

    def __init__(self, parent):
        Toplevel.__init__(self, parent)

        # Designing the splash screen
        self.title("Stephen's Sucky Vector Calculator")
        self.geometry("1380x760")
        self.configure(background="black")
        self.overrideredirect(True)
        
        # Text for the splash screen
        spatxt = Label(self, text = "Yules Coding Company") 
        spatxt.config(font =("Courier", 60), bg="black", fg="white", borderwidth="4", relief="groove", padx="20", pady="4")
        spatxt.place(relx="0.5", rely="0.5")

        present = Label(self, text = "Presents:")
        present.config(font=("Times", 40), bg="black", fg="white")

        spatxt.pack(pady="200")
        present.pack()
        ## required to make window show before the program gets to the mainloop
        self.update()

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.withdraw()
        splash = Splash(self)

        ## setup stuff goes here
        self.title("Stephen's Sucky Vector Calculator")
        ## simulate a delay while loading
        time.sleep(3)

        ## finished loading so destroy splash
        splash.destroy()

        ## show window again
        self.deiconify()

        start = StartScreen(self)

class StartScreen(Toplevel):

    def __init__(self, parent):
        Toplevel.__init__(self, parent)

        self.configure(background="black")

        l = Label(self, text = "Vector Calculator") 
        l.config(font =("Courier", 80), bg="black", fg="white", borderwidth="4", relief="groove", padx="20", pady="4")
        l.pack(pady="80")

        dimension2 = Button(self, text="2D Vector", height="3", width="15", command=lambda: [dimension2.pack_forget(), dimension3.pack_forget(), l.pack_forget(), Exit.pack_forget()])
        dimension2.pack(pady="100")

        dimension3 = Button(self, text="3D Vector", height="3", width="15", command=lambda: [dimension2.pack_forget(), dimension3.pack_forget(), l.pack_forget(), Exit.pack_forget()])
        dimension3.pack(pady="20")

        Exit = Button(self, text="Exit", height="3", width="15", command=lambda: [self.destroy()])
        Exit.pack(pady="30")

        self.attributes('-fullscreen', True)  
        self.fullScreenState = False
        self.bind("<F11>", self.toggleFullScreen)
        self.bind("<Escape>", self.quitFullScreen)

        self.update()

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.attributes("-fullscreen", self.fullScreenState)


class D2Options(Toplevel):

    def __init__(self, parent):
        Toplevel.__init__(self, parent)

        l = Label(self, text = "GBVebenjerbae") 
        l.config(font =("Courier", 80), bg="black", fg="white", borderwidth="4", relief="groove", padx="20", pady="4")
        l.pack(pady="80")

        self.update()



if __name__ == "__main__":
    # Setting up the window
    home = App()

    home.mainloop()