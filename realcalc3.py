
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
        l.config(font =("Courier", 80), bg="#6e2775", fg="white", borderwidth="4", relief="groove", padx="20", pady="4")
        l.pack(pady="80")

        dimension2 = Button(self, text="2D Vector", font=("Times", 20), command=lambda: self.switch_frame(D2Options))
        dimension2.config(height="2",
                            width="14",
                            bg="black",
                            fg="#97e6ca",
                            relief="groove",
                            borderwidth="4",
                            activebackground="#00ff00")
        dimension2.pack(pady="0")

        dimension3 = Button(self, text="3D Vector", font=("Times", 20), command=lambda: self.switch_frame(D3Options))
        dimension3.config(height="2",
                            width="14",
                            bg="black",
                            fg="#97e6ca",
                            relief="groove",
                            borderwidth="4",
                            activebackground="#00ff00")
        dimension3.pack(pady="80")

        Exit = Button(self, text="Exit", font=("Times", 20), command=lambda: [self.destroy()])
        Exit.config(height="2",
                        width="14",
                        bg="black",
                        fg="#97e6ca",
                        relief="groove",
                        borderwidth="4",
                        activebackground="#00ff00")
        Exit.pack(pady="0")

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

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        self._frame = new_frame
        self._frame.pack()

class D2Options(Toplevel):

    def __init__(self, parent):
        Toplevel.__init__(self, parent)

        self.configure(background="black")

        l = Label(self, text = "2D Vector Options") 
        l.config(font =("Courier", 80), bg="black", fg="white", borderwidth="4", relief="groove", padx="20", pady="4")
        l.pack(pady="80")

        magnitude = Button(self, text="Magnitude", font=("Times", 20), command=lambda: self.switch_frame(Mag2D))
        magnitude.config(height="2",
                            width="14",
                            bg="black",
                            fg="#97e6ca",
                            relief="groove",
                            borderwidth="4",
                            activebackground="#00ff00")
        magnitude.pack(pady="0")

        linequ = Button(self, text="Equation of Line", font=("Times", 20), command=lambda: self.switch_frame(Line2D))
        linequ.config(height="2",
                            width="14",
                            bg="black",
                            fg="#97e6ca",
                            relief="groove",
                            borderwidth="4",
                            activebackground="#00ff00")
        linequ.pack(pady="80")

        Exit = Button(self, text="Back", font=("Times", 20), command=lambda: [self.destroy()])
        Exit.config(height="2",
                        width="14",
                        bg="black",
                        fg="#97e6ca",
                        relief="groove",
                        borderwidth="4",
                        activebackground="#00ff00")
        Exit.pack(pady="0")

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

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        self._frame = new_frame
        self._frame.pack()

class D3Options(Toplevel):

    def __init__(self, parent):
        Toplevel.__init__(self, parent)

        self.configure(background="black")

        l = Label(self, text = "3D Vector Options") 
        l.config(font =("Courier", 80), bg="black", fg="white", borderwidth="4", relief="groove", padx="20", pady="4")
        l.pack(pady="80")

        Exit = Button(self, text="Back", font=("Times", 20), command=lambda: [self.destroy()])
        Exit.config(height="2",
                        width="14",
                        bg="black",
                        fg="#97e6ca",
                        relief="groove",
                        borderwidth="4",
                        activebackground="#00ff00")
        Exit.pack(pady="0")

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

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        self._frame = new_frame
        self._frame.pack()

class Mag2D(Toplevel):

    def __init__(self, parent):
        Toplevel.__init__(self, parent)

        self.configure(background="black")

        l = Label(self, text = "Magnitude of 2D") 
        l.config(font =("Courier", 80), bg="black", fg="white", borderwidth="4", relief="groove", padx="20", pady="4")
        l.pack(pady="80")

        Exit = Button(self, text="Back", font=("Times", 20), command=lambda: [self.destroy()])
        Exit.config(height="2",
                        width="14",
                        bg="black",
                        fg="#97e6ca",
                        relief="groove",
                        borderwidth="4",
                        activebackground="#00ff00")
        Exit.pack(pady="0")

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

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        self._frame = new_frame
        self._frame.pack()

class Line2D(Toplevel):

    def __init__(self, parent):
        Toplevel.__init__(self, parent)

        self.configure(background="black")

        l = Label(self, text = "Line 2D Equation")
        l.config(font =("Courier", 80), bg="black", fg="white", borderwidth="4", relief="groove", padx="20", pady="4")
        l.pack(pady="80")

        Exit = Button(self, text="Back", font=("Times", 20), command=lambda: [self.destroy()])
        Exit.config(height="2",
                        width="14",
                        bg="black",
                        fg="#97e6ca",
                        relief="groove",
                        borderwidth="4",
                        activebackground="#00ff00")
        Exit.pack(pady="0")

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

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        self._frame = new_frame
        self._frame.pack()

if __name__ == "__main__":
    # Setting up the window
    home = App()

    home.mainloop()