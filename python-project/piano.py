import pygame
#pygame is a cross-platform set of python modules designed for writing video games. 
# It includes computer graphics and sound libraries dessigned to be used with the python programming lanuage.
import sys
#It let us access system-specific parameters and functionc.
from tkinter import*
#Tk widgets can be used to construct buttons, menus, data fields, etc. in a Python application.
#Tkinter is the name of that library. Import * means everything.
pygame.init()     #pygameinit() initializes all imported pygame modules
def clear(): 
    txtDisplay.delete(0,END)
    num1.set(0)
    return   

def value_Cs():
    num1.set("C#")
    
    sound = pygame.mixer.Sound('C:\\Users\\hp\\python-project\\203459__tesabob2001__a-5.mp3')
    
    sound.play()
    return
def value_Ds():
    num1.set("D#")
    sound = pygame.mixer.Sound("C:\\Users\\hp\\python-project\\203460__tesabob2001__a-4.mp3")
    sound.play()
    return
def value_Fs():
    num1.set("F#")
    sound = pygame.mixer.Sound("C:\\Users\\hp\\python-project\\203466__tesabob2001__c-3.mp3")
    sound.play()
    return
def value_Gs():
    num1.set("G#")
    sound = pygame.mixer.Sound("C:\\Users\\hp\\python-project\\203471__tesabob2001__e4.mp3")
    sound.play()
    return
def value_Bb():
    num1.set("Bb")
    sound = pygame.mixer.Sound("C:\\Users\\hp\\python-project\\203473__tesabob2001__d5.mp3")
    sound.play()
    return
def value_Cs1():
    num1.set("C#1")
    sound = pygame.mixer.Sound("C:\\Users\\hp\\python-project\\203480__tesabob2001__c-5.mp3")
    sound.play()
    return
def value_Ds1():
    num1.set("D#1")
    sound = pygame.mixer.Sound("C:\\Users\\hp\\python-project\\203472__tesabob2001__d4.mp3")
    sound.play()
    return
def value_C():
    num1.set("C")
    sound = pygame.mixer.Sound("C:\\Users\\hp\\python-project\\203462__tesabob2001__b4.mp3")
    sound.play()
    return
def value_D():
    num1.set("D")
    sound = pygame.mixer.Sound("C:\\Users\\hp\\python-project\\203463__tesabob2001__b3.mp3")
    sound.play()
    return
def value_E():
    num1.set("E")
    sound = pygame.mixer.Sound("C:\\Users\\hp\\python-project\\203467__tesabob2001__b5.mp3")
    sound.play()
    return
def value_F():
    num1.set("F")
    sound = pygame.mixer.Sound("C:\\Users\\hp\\python-project\\203468__tesabob2001__f3.mp3")
    sound.play()
    return 
def value_G():
    num1.set("G")
    sound = pygame.mixer.Sound("C:\\Users\\hp\\python-project\\203476__tesabob2001__e5.mp3")
    sound.play()
    return 
def value_A():
    num1.set("A")
    sound = pygame.mixer.Sound("C:\\Users\\hp\\python-project\\203483__tesabob2001__d-3.mp3")
    sound.play()
    return
def value_B():
    num1.set("B")
    sound = pygame.mixer.Sound("C:\\Users\\hp\\python-project\\203484__tesabob2001__c6.mp3")
    sound.play()
    return 
def value_C1():
    num1.set("C1")
    sound = pygame.mixer.Sound("C:\\Users\\hp\\python-project\\203488__tesabob2001__g-3.mp3")
    sound.play()
    return 
def value_D1():
    num1.set("D1")
    sound = pygame.mixer.Sound("C:\\Users\\hp\\python-project\\203491__tesabob2001__g-4.mp3")
    sound.play()
    return
def value_E1():
    num1.set("E1")
    sound = pygame.mixer.Sound("C:\\Users\\hp\\python-project\\203493__tesabob2001__g3.mp3")
    sound.play()
    return
def value_F1():
    num1.set("F1")
    sound = pygame.mixer.Sound("C:\\Users\\hp\\python-project\\203499__tesabob2001__f-5.mp3")
    sound.play()
    return   
root = Tk()  #It helps to display the root window and manages all the other components of the tkinter application.
frame = Frame(root)

frame.pack()

root.title('PIANO')

num1=StringVar()
num1.set(0)
num2=StringVar()
operator=StringVar()


topframe = Frame(root)
topframe.pack(side = TOP)
txtDisplay=Entry(frame,textvariable = num1,bd=20,insertwidth =1,font =30 ,justify= 'right',width=4)
txtDisplay.pack( side = TOP)


button1 = Button(topframe,padx=8, height = 6, pady=8, bd=8, text="C# ",  bg="black",fg="white", command=value_Cs)
button1.pack(side =LEFT)
button22 = Button(topframe, state=DISABLED, height = 7, width=1, padx=0, pady=0, relief=RIDGE)
button22.pack(side =LEFT)
button2 = Button(topframe,padx=8, height = 6, pady=8, bd=8, text="D# ", bg="black",fg="white", command=value_Ds)
button2.pack(side =LEFT)
button22 = Button(topframe, state=DISABLED, height = 7, width=1, padx=0, pady=0, relief=RIDGE)
button22.pack(side =LEFT)
button3 = Button(topframe,padx=8, height = 6, pady=8, bd=8, text="F# ", bg="black",fg="white", command=value_Fs)
button3.pack(side =LEFT)
button22 = Button(topframe, state=DISABLED, height = 7, width=1, padx=0, pady=0, relief=RIDGE)
button22.pack(side =LEFT)
button4 = Button(topframe,padx=8, height = 6, pady=8, bd=8, text="G# ", bg="black",fg="white", command=value_Gs)
button4.pack(side =LEFT)
button22 = Button(topframe, state=DISABLED, height = 7, width=1, padx=0, pady=0, relief=RIDGE)
button22.pack(side =LEFT)

button2 = Button(topframe,padx=8, height = 6, pady=8, bd=8, text="Bb ", bg="black",fg="white", command=value_Bb)
button2.pack(side =LEFT)
button22 = Button(topframe, state=DISABLED, height = 7, width=1, padx=0, pady=0, relief=RIDGE)
button22.pack(side =LEFT)
button3 = Button(topframe,padx=8, height = 6, pady=8, bd=8, text="C#1 ", bg="black",fg="white", command=value_Cs1)
button3.pack(side =LEFT)
button22 = Button(topframe, state=DISABLED, height = 7, width=1, padx=0, pady=0, relief=RIDGE)
button22.pack(side =LEFT)
button4 = Button(topframe,padx=8, height = 6, pady=8, bd=8, text="D#1 ", bg="black",fg="white", command=value_Ds1)
button4.pack(side =LEFT)

frame1 = Frame(root)
frame1.pack( side = TOP)

button1 = Button(frame1,padx=16, height = 8, pady=16, bd=8, text="C", bg="white",fg="black", command=value_C)
button1.pack(side =LEFT)
button2 = Button(frame1,padx=16, height = 8, pady=16, bd=8, text="D", bg="white",fg="black", command=value_D)
button2.pack(side =LEFT)
button3 = Button(frame1,padx=16, height = 8, pady=16, bd=8, text="E", bg="white",fg="black", command=value_E)
button3.pack(side =LEFT)
button4 = Button(frame1,padx=16, height = 8, pady=16, bd=8, text="F", bg="white",fg="black", command=value_F)
button4.pack(side =LEFT)

button5 = Button(frame1,padx=16, height = 8, pady=16, bd=8, text="G", bg="white",fg="black", command=value_G)
button5.pack(side =LEFT)
button6 = Button(frame1,padx=16, height = 8, pady=16, bd=8, text="A", bg="white",fg="black", command=value_A)
button6.pack(side =LEFT)
button7 = Button(frame1,padx=16, height = 8, pady=16, bd=8, text="B", bg="white",fg="black", command=value_B)
button7.pack(side =LEFT)
button8 = Button(frame1,padx=16, height = 8, pady=16, bd=8, text="C1", bg="white",fg="black", command=value_C1)
button8.pack(side =LEFT)

button9 = Button(frame1,padx=16, height = 8, pady=16, bd=8, text="D1", bg="white",fg="black", command=value_D1)
button9.pack(side =LEFT)
button10 = Button(frame1,padx=16, height = 8, pady=16, bd=8, text="E1", bg="white",fg="black", command=value_E1)
button10.pack(side =LEFT)
button11 = Button(frame1,padx=16, height = 8, pady=16, bd=8, text="F1", bg="white",fg="black", command=value_F1)
button11.pack(side =LEFT)

root.mainloop()
#Root. mainloop() is simply a method in the main window 
# that executes what we wish to execute in an application
#What are the 12 piano keys?
#There are 12 possible keys any particular song can be played in. This is because of the 12 notes on the piano keyboard, A, A#/Bb, B, C, C#/Db, D, D#/Eb, E, F, F#/Gb, G, and G#/Ab. A song can be played so that any one of these twelve notes will be the tonal center or home base.