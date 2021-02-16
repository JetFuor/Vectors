
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

class Splash(Toplevel):

    def __init__(self, parent):
        Toplevel.__init__(self, parent)

        self.title("Stephen's Sucky Vector Calculator")
        self.geometry("1380x760")
        self.configure(background="black")
        self.overrideredirect(True)
        y = Label(self, text = "Yules Coding Company") 
        y.config(font =("Courier", 20), bg="black", fg="white")
        y.place(relx="0.5", rely="0.5")
        y.pack(pady="50")


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

        self.configure(background="black")

        l = Label(self, text = "Vector Calculator") 
        l.config(font =("Courier", 70), bg="black", fg="white" )
        l.pack(pady="50")

        dimension2 = Button(self, text="2D Vector", height="3", width="15")
        dimension2.pack(pady="100")

        dimension3 = Button(self, text="3D Vector", height="3", width="15")
        dimension3.pack(pady="20")

        self.attributes('-fullscreen', True)  
        self.fullScreenState = False
        self.bind("<F11>", self.toggleFullScreen)
        self.bind("<Escape>", self.quitFullScreen)
    
    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.attributes("-fullscreen", self.fullScreenState)




if __name__ == "__main__":
    # Setting up the window
    home = App()

    home.mainloop()
