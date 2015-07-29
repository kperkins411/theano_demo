__author__ = 'Keith'

import numpy as np
import theanotest

from Tkinter import *
from Tkinter import StringVar

class Application(Frame):
    def __init__(self,parent):
        Frame.__init__(self, parent)
        self.parent = parent

        self.grid()
        self.create_widgets()

    def create_widgets(self):
        #general instructions
        Label(self,text="This application uses neural nets",justify=LEFT, pady=15).grid(row=0,column=0,columnspan=4,sticky=W)

        Label(self,text="Number of Layers:",justify=LEFT).grid(row=1,column=0,columnspan=3, sticky=W)
        self._numb_layer = Entry(self)
        self._numb_layer.insert(0,"1")
        self._numb_layer.grid(row=1,column=3,sticky=W)

        Label(self,text="Neurons per Layer:",justify=LEFT).grid(row=2,column=0,columnspan=3,sticky=W)
        self._numb_neuron = Entry(self)
        self._numb_neuron.insert(0,"10")
        self._numb_neuron.grid(row=2,column=3,sticky=W)

        Label(self,text="Number of points:",justify=LEFT).grid(row=3,column=0,columnspan=3,sticky=W)
        self._numb_points = Entry(self)
        self._numb_points.insert(0,"40")
        self._numb_points.grid(row=3,column=3,sticky=W)

        Label(self,text="training iterations:",justify=LEFT).grid(row=4,column=0,columnspan=3,sticky=W)
        self._numb_iterations = Entry(self)
        self._numb_iterations.insert(0,"20")
        self._numb_iterations.grid(row=4,column=3,sticky=W)

        #placeholder for format
        Label(self, pady=15).grid(row=5,column=0)


        #create a start button
        self._start_network=Button(self,text="Start",command = self.start_network)
        self._start_network.grid(row=5,column=3,sticky=W)

    def verify_inputs(self):
        return True

    def start_network(self):
        if self.verify_inputs() == False:
            return


        theanotest.main(int(self._numb_points.get()), int(self._numb_layer.get()),int(self._numb_iterations.get()) )

        #TODO start network

#main
root = Tk()
root.title("Theano Demo")
#root.geometry("300x500")
app=Application(root)
root.mainloop()
