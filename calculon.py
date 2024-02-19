from tkinter import *

class Calculon(Frame):
    def __init__(self, container):
        Frame.__init__(self, container, bg="white")
        self.setupLayout()
    def clear_display(self):
        self.display["text"] = ""
    # Method to perform backspace
    def backspace(self):
        current_text = self.display["text"]
        self.display["text"] = current_text[:-1]

    # Method to process button presses
    def process(self, value):
        self.display["text"] += value
    #some behaviors
    #put them in place
    def setupLayout(self):
        #create the display as a label
        self.display = Label(self, text="",\
                             anchor = E, height = 2,\
                             width = 15,\
                             font = ("Arial",50))
        self.display.grid(row=0, column=0,\
                          columnspan = 4,\
                          sticky = E+W+N+S)
        self.pack(fill=BOTH, expand=1)

        #lets make a 1 button
        #load an image from our machine
        img = PhotoImage(file="images/1.gif")
        #create a button object with that image on it
        button = Button(self, bg="white", image = img,\
                        command = lambda:self.process("1"))
        #assign the img object to the button.image mem
        button.image = img
        #shove this thing into the grid
        button.grid(row=4, column=0, sticky = N+S+E+W)

        #lets make a 2 button
        #load an image from our machine
        img = PhotoImage(file="images/2.gif")
        #create a button object with that image on it
        button = Button(self, bg="white", image = img,\
                        command = lambda:self.process("2"))
        #assign the img object to the button.image mem
        button.image = img
        #shove this thing into the grid
        button.grid(row=4, column=1, sticky = N+S+E+W)
        
        #lets make a 3 button
        #load an image from our machine
        img = PhotoImage(file="images/3.gif")
        #create a button object with that image on it
        button = Button(self, bg="white", image = img,\
                        command = lambda:self.process("3"))
        #assign the img object to the button.image mem
        button.image = img
        #shove this thing into the grid
        button.grid(row=4, column=2, sticky = N+S+E+W)

        #lets make a 4 button
        #load an image from our machine
        img = PhotoImage(file="images/4.gif")
        #create a button object with that image on it
        button = Button(self, bg="white", image = img,\
                        command = lambda:self.process("4"))
        #assign the img object to the button.image mem
        button.image = img
        #shove this thing into the grid
        button.grid(row=3, column=0, sticky = N+S+E+W)

        #lets make a 5 button
        #load an image from our machine
        img = PhotoImage(file="images/5.gif")
        #create a button object with that image on it
        button = Button(self, bg="white", image = img,\
                        command = lambda:self.process("5"))
        #assign the img object to the button.image mem
        button.image = img
        #shove this thing into the grid
        button.grid(row=3, column=1, sticky = N+S+E+W)

        #lets make a 6 button
        #load an image from our machine
        img = PhotoImage(file="images/6.gif")
        #create a button object with that image on it
        button = Button(self, bg="white", image = img,\
                        command = lambda:self.process("6"))
        #assign the img object to the button.image mem
        button.image = img
        #shove this thing into the grid
        button.grid(row=3, column=2, sticky = N+S+E+W)

        #lets make a 7 button
        #load an image from our machine
        img = PhotoImage(file="images/7.gif")
        #create a button object with that image on it
        button = Button(self, bg="white", image = img,\
                        command = lambda:self.process("7"))
        #assign the img object to the button.image mem
        button.image = img
        #shove this thing into the grid
        button.grid(row=2, column=0, sticky = N+S+E+W)

        #lets make a 8 button
        #load an image from our machine
        img = PhotoImage(file="images/8.gif")
        #create a button object with that image on it
        button = Button(self, bg="white", image = img,\
                        command = lambda:self.process("8"))
        #assign the img object to the button.image mem
        button.image = img
        #shove this thing into the grid
        button.grid(row=2, column=1, sticky = N+S+E+W)

        #lets make a 9 button
        #load an image from our machine
        img = PhotoImage(file="images/9.gif")
        #create a button object with that image on it
        button = Button(self, bg="white", image = img,\
                        command = lambda:self.process("9"))
        #assign the img object to the button.image mem
        button.image = img
        #shove this thing into the grid
        button.grid(row=2, column=2, sticky = N+S+E+W)

        #lets make a ( button
        #load an image from our machine
        img = PhotoImage(file="images/lpr.gif")
        #create a button object with that image on it
        button = Button(self, bg="white", image = img,\
                        command = lambda:self.process("("))
        #assign the img object to the button.image mem
        button.image = img
        #shove this thing into the grid
        button.grid(row=1, column=0, sticky = N+S+E+W)

        #lets make a ) button
        #load an image from our machine
        img = PhotoImage(file="images/rpr.gif")
        #create a button object with that image on it
        button = Button(self, bg="white", image = img,\
                        command = lambda:self.process(")"))
        #assign the img object to the button.image mem
        button.image = img
        #shove this thing into the grid
        button.grid(row=1, column=1, sticky = N+S+E+W)

        #lets make a AC button
        #load an image from our machine
        img = PhotoImage(file="images/clr.gif")
        #create a button object with that image on it
        button = Button(self, bg="white", image=img, command=self.clear_display)
        #assign the img object to the button.image mem
        button.image = img
        #shove this thing into the grid
        button.grid(row=1, column=2, sticky = N+S+E+W)

        #lets make a = button
        #load an image from our machine
        img = PhotoImage(file="images/eql-wide.gif")
        #create a button object with that image on it
        button = Button(self, bg="white", image = img,\
                        command = lambda:self.process("="))
        #assign the img object to the button.image mem
        button.image = img
        #shove this thing into the grid
        button.grid(row=7, column=0, columnspan=2, sticky=N+S+E+W)

        #lets make a ** button
        #load an image from our machine
        img = PhotoImage(file="images/pow.gif")
        #create a button object with that image on it
        button = Button(self, bg="white", image = img,\
                        command = lambda:self.process("**"))
        #assign the img object to the button.image mem
        button.image = img
        #shove this thing into the grid
        button.grid(row=7, column=2, sticky = N+S+E+W)

        #lets make a % button
        #load an image from our machine
        img = PhotoImage(file="images/mod.gif")
        #create a button object with that image on it
        button = Button(self, bg="white", image = img,\
                        command = lambda:self.process("%"))
        #assign the img object to the button.image mem
        button.image = img
        #shove this thing into the grid
        button.grid(row=7, column=3, sticky = N+S+E+W)

        #lets make a 0 button
        #load an image from our machine
        img = PhotoImage(file="images/0.gif")
        #create a button object with that image on it
        button = Button(self, bg="white", image = img,\
                        command = lambda:self.process("0"))
        #assign the img object to the button.image mem
        button.image = img
        #shove this thing into the grid
        button.grid(row=6, column=0, sticky = N+S+E+W)

        #lets make a . button
        #load an image from our machine
        img = PhotoImage(file="images/dot.gif")
        #create a button object with that image on it
        button = Button(self, bg="white", image = img,\
                        command = lambda:self.process("."))
        #assign the img object to the button.image mem
        button.image = img
        #shove this thing into the grid
        button.grid(row=6, column=1, sticky = N+S+E+W)

        #lets make a + button
        #load an image from our machine
        img = PhotoImage(file="images/add.gif")
        #create a button object with that image on it
        button = Button(self, bg="white", image = img,\
                        command = lambda:self.process("+"))
        #assign the img object to the button.image mem
        button.image = img
        #shove this thing into the grid
        button.grid(row=6, column=3, sticky = N+S+E+W)

        #lets make a - button
        #load an image from our machine
        img = PhotoImage(file="images/sub.gif")
        #create a button object with that image on it
        button = Button(self, bg="white", image = img,\
                        command = lambda:self.process("-"))
        #assign the img object to the button.image mem
        button.image = img
        #shove this thing into the grid
        button.grid(row=4, column=3, sticky = N+S+E+W)

        #lets make a * button
        #load an image from our machine
        img = PhotoImage(file="images/mul.gif")
        #create a button object with that image on it
        button = Button(self, bg="white", image = img,\
                        command = lambda:self.process("*"))
        #assign the img object to the button.image mem
        button.image = img
        #shove this thing into the grid
        button.grid(row=3, column=3, sticky = N+S+E+W)

        #lets make a / button
        #load an image from our machine
        img = PhotoImage(file="images/div.gif")
        #create a button object with that image on it
        button = Button(self, bg="white", image = img,\
                        command = lambda:self.process("/"))
        #assign the img object to the button.image mem
        button.image = img
        #shove this thing into the grid
        button.grid(row=2, column=3, sticky = N+S+E+W)

        #lets make a <- button
        #load an image from our machine
        img = PhotoImage(file="images/bak.gif")
        #create a button object with that image on it
        button = Button(self, bg="white", image=img, command=self.backspace)
        #assign the img object to the button.image mem
        button.image = img
        #shove this thing into the grid
        button.grid(row=1, column=3, sticky = N+S+E+W)

        #error handle
        #clear the screen if result published

        #process any button calls from the layout
        def process(self,buttonName):
            if(shouldClear==True):
                self.display["text"]=""
                

    def process(self,value):
        self.display["text"]+=value

window = Tk()
c = Calculon(window)
