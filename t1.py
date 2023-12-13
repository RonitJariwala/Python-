"""
from tkinter import *
window=Tk()
label=Label(window,text='Hello World',bg='Red',relief=RAISED,bd=10)
label.pack()
def click():
    print('You click the button')
def submit():
    username=entry.get()
    print('Hello '+username)
button=Button(window,text='click me',command=click)
button.pack()
entry=Entry(window,)
entry.pack()
submit_button=Button(window,text='submit',command=submit)
submit_button.pack()
check_button=Checkbutton(window,text='I agree to something')
check_button.pack()
r=Radiobutton(text='hi')
r.pack()

mainloop()
"""
from tkinter import *
window=Tk()
canvas=Canvas(window,height=500,width=500)
canvas.create_line(0,0,500,500,fill='blue',width=5)
canvas.create_rectangle(50,50,250,250,fill='black')
canvas.create_polygon(250,0,500,500,0,500,fill='yellow')


canvas.pack()




window.mainloop()