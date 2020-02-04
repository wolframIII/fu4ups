#start
import tkinter as tk
#Head
app = tk.Tk()
app.title ('Useless counter')
app.geometry("300x80")
#Neck
app.i=1
#body
def BC():
    app.i += 1
    l['text'] = app.i
    
    if app.i >= 4:
        g = tk.Label(app, text="I can only count to Four")
        g.pack()
        
        b.config(command = YG)
def YG():
    l['text'] ='You are Gay'
    
    b.config(text='Exit',command=app.destroy)
#Legs
l = tk.Label(app,text = app.i)
l.pack()
b = tk.Button(app, text='Next', width=10, command=BC)
b.pack()
#Feet
app.mainloop()
#end
