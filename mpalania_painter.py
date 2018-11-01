import tkinter as tk
from tkinter.colorchooser import askcolor
from tkinter.messagebox import *

class GetPointsDialog(tk.Toplevel):
    def __init__(self,root,value):
        #This is toplevel window and take input of coordinates
        self.painter = root
        tk.Toplevel.__init__(self,root)
        self.x1=tk.StringVar()
        self.x2=tk.StringVar()
        self.y1=tk.StringVar()
        self.y2=tk.StringVar()
        self.radius=tk.StringVar()
        tk.Label(self,text="X1").grid(column=0,row=0,sticky=tk.E)
        tk.Entry(self,width=25, textvariable=self.x1).grid(column=1,row=0,sticky=tk.E)
        tk.Label(self,text="Y1").grid(column=2,row=0,sticky=tk.E)
        tk.Entry(self,width=25, textvariable=self.y1).grid(column=3,row=0,sticky=tk.E)
        tk.Button(self,text="Color",command=self.choose_color).grid(column=2,row=2,sticky=tk.E)
        self.options=["Dashed","Undashed"]
        self.choice= tk.IntVar()
        self.choice.set(-1)
        tk.Radiobutton(self,text=self.options[0],variable=self.choice,value=0).grid(column=0,row=2,sticky=tk.E)
        tk.Radiobutton(self,text=self.options[1],variable=self.choice,value=1).grid(column=1,row=2,sticky=tk.E)
        if value == "Circle":
            tk.Label(self,text="Radius").grid(column=0,row=1,sticky=tk.E)
            tk.Entry(self,width=25, textvariable=self.radius).grid(column=1,row=1,sticky=tk.E)
        elif value == "Line" or value == "Rectangle":
            tk.Label(self,text="X2").grid(column=0,row=1,sticky=tk.E)
            tk.Entry(self,width=25, textvariable=self.x2).grid(column=1,row=1,sticky=tk.E)
            tk.Label(self,text="Y2").grid(column=2,row=1,sticky=tk.E)
            tk.Entry(self,width=25, textvariable=self.y2).grid(column=3,row=1,sticky=tk.E)
        tk.Button(self,text="Submit",command=lambda *args:self.submit(value)).grid(column=1,row=3)
        tk.Button(self,text="Reset",command=self.reset).grid(column=4,row=3)

    def choose_color(self):
        #select color from color available
        self.color= askcolor(parent=self)

    def submit(self,value):
        #check the all values entered
        if value == "Circle":
            try:
                self.painter.X1_CORD=int(self.x1.get())
            except:
                showerror("Value Error","Coefficient's of X1 can't be character or a Null",parent=self)
            try:
                self.painter.Y1_CORD=int(self.y1.get())
            except:
                showerror("Value Error","Coefficient's of Y1 can't be character or a Null",parent=self)
            try:
                self.painter.Radius=int(self.radius.get())
            except:
                showerror("Value Error","Coefficient's of Radius can't be character or a Null",parent=self)
            try:
                self.painter.Option=self.options[self.choice.get()]
            except:
                showerror("Value Error","You must select the format of line",parent=self)
            try:
                self.painter.Color=self.color
            except:
                showerror("Value Error","You must select a color",parent=self)
            if self.painter.Radius <= 0:
                showinfo("Error","Radius cannot be 0 or less than 0",parent=self)
            elif self.painter.X1_CORD< 50 or self.painter.Y1_CORD< 50:
                showinfo("Error","Coefficient's of X1 or Y1 can't be less than 50",parent=self)
            else:
                self.painter.Create_Circle(self.painter.X1_CORD,self.painter.Y1_CORD,self.painter.Radius,self.painter.Option,self.painter.Color)
        elif value == "Rectangle" or value=="Line":
            try:
                self.painter.X1_CORD=int(self.x1.get())
            except:
                showerror("Value Error","Coefficient's of X1 can't be character or a Null",parent=self)
            try:
                self.painter.Y1_CORD=int(self.y1.get())
            except:
                showerror("Value Error","Coefficient's of Y1 can't be character or a Null",parent=self)
            try:
                self.painter.X2_CORD=int(self.x2.get())
            except:
                showerror("Value Error","Coefficient's of X2 can't be character or a Null",parent=self)
            try:
                self.painter.Y2_CORD=int(self.y2.get())
            except:
                showerror("Value Error","Coefficient's of Y2 can't be character or a Null",parent=self)
            try:
                self.painter.Option=self.options[self.choice.get()]
            except:
                showerror("Value Error","You must select the format of line",parent=self)
            try:
                self.painter.Color=self.color
            except:
                showerror("Value Error","You must select a color",parent=self)
            if self.painter.X1_CORD< 50 or self.painter.X2_CORD< 50 or self.painter.X2_CORD<self.painter.X1_CORD or self.painter.Y2_CORD<self.painter.Y1_CORD:
                showinfo("Error"," Coefficient's of X1 or X2 can't be less than 50 or X2<X1 or Y2<Y1",parent=self)
            elif value == "Rectangle":
                self.painter.Create_Rectangle(self.painter.X1_CORD,self.painter.Y1_CORD,self.painter.X2_CORD,self.painter.Y2_CORD,self.painter.Option,self.painter.Color)
            elif value=="Line":
                self.painter.Create_Line(self.painter.X1_CORD,self.painter.Y1_CORD,self.painter.X2_CORD,self.painter.Y2_CORD,self.painter.Option,self.painter.Color)

    def reset(self):
        #reset all the dialog values
        self.x1.set("")
        self.x2.set("")
        self.y1.set("")
        self.y2.set("")
        self.radius.set("")
        self.choice.set(-1)

class Painter(tk.Frame):
    def __init__(self,root):
        tk.Frame.__init__(self,root)
        self.X=0
        self.Y=0
        self.X1_CORD=0
        self.X2_CORD=0
        self.Y1_CORD=0
        self.Y2_CORD=0
        self.Radius=0
        self.Option = "undashed"
        self.Color = "black"

        self.init_widgets()

    def init_widgets(self):
        #add menu to base windows,add buttons
        self.menubar = tk.Menu()
        self.filemenu=tk.Menu(tearoff=0)
        self.optionmenu=tk.Menu(tearoff=0)
        self.helpmenu=tk.Menu()
        self.menubar.add_cascade(label="File",menu=self.filemenu)
        self.menubar.add_cascade(label="Options",menu=self.optionmenu,state="disabled")
        self.menubar.add_command(label="Help",command=self.Show_help_about)
        self.filemenu.add_command(label="New",command=self.create_New_Canvas)
        self.filemenu.add_command(label="Save",command=self.save_canvas)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit",command=self.exit)
        self.optionmenu.add_command(label="Circle",command=lambda *args:self.get_Cordinate_Points("Circle"))
        self.optionmenu.add_command(label="Line",command=lambda *args:self.get_Cordinate_Points("Line"))
        self.optionmenu.add_command(label="Rectangle",command=lambda *args:self.get_Cordinate_Points("Rectangle"))
        self.optionmenu.add_separator()
        self.optionmenu.add_command(label="Clear All",command=self.clear_canvas)
        root.configure(menu=self.menubar)
        self.penbutton=tk.Button(text="Pen",state="disabled",command=lambda *args:self.activate_button("pen"))
        self.penbutton.grid(column=0,row=0,sticky=tk.E)
        self.circlebutton=tk.Button(text="Circle",state="disabled",command=lambda *args:self.activate_button("circle"))
        self.circlebutton.grid(column=1,row=0,sticky=tk.E)
        self.linebutton=tk.Button(text="Line",state="disabled",command=lambda *args:self.activate_button("line"))
        self.linebutton.grid(column=2,row=0,sticky=tk.E)
        self.active_button = self.penbutton
        self.circlelist=[]
        self.linelist=[]

    def create_New_Canvas(self):
        #new canvas of size 600x600
        self.canvs=tk.Canvas(root,width=600,height=600, bg='white')
        self.canvs.grid(column=5,row =7)
        self.enable_menu()
        self.va='pen'

    def enable_menu(self):
        #enable_menu when new canvas is created
        self.menubar.entryconfig("Options",state="normal")
        self.penbutton['state'] = 'normal'
        self.circlebutton['state'] = 'normal'
        self.linebutton['state'] = 'normal'

    def get_Cordinate_Points(self,value):
        #call the GetPointDialog for getting coordinates
        self.cordinate=GetPointsDialog(self,value)
        self.cordinate.wm_title("Enter Co-ordinates Points")

    def Create_Circle(self,X1,Y1,Rad,Opt,Col):
        if Opt == 'Undashed':
            self.canvs.create_oval(X1-Rad,Y1-Rad,X1+Rad,Y1+Rad,outline=Col[1])
        elif Opt == 'Dashed':
            self.canvs.create_oval(X1-Rad,Y1-Rad,X1+Rad,Y1+Rad,outline=Col[1],dash=(4,2))

    def Create_Line(self,X1,Y1,X2,Y2,Opt,Col):
        if Opt == 'Undashed':
            self.canvs.create_line(X1,Y1,X2,Y2,fill=Col[1])
        elif Opt == 'Dashed':
            self.canvs.create_line(X1,Y1,X2,Y2,fill=Col[1],dash=(4,2))

    def Create_Rectangle(self,X1,Y1,X2,Y2,Opt,Col):
        if Opt == 'Undashed':
            self.canvs.create_rectangle(X1,Y1,X2,Y2,outline=Col[1])
        elif Opt == 'Dashed':
            self.canvs.create_rectangle(X1,Y1,X2,Y2,outline=Col[1],dash=(4,2))

    def activate_button(self, some_button):
        #activate buttons depending upon user selection
        if some_button=="pen":
            some_button = self.penbutton
            self.active_button.config(relief='raised')
            some_button.config(relief='sunken')
            self.active_button = some_button
            self.va = 'pen'
            self.canvs.bind('<B1-Motion>',self.Brush)
            self.canvs.bind('<ButtonRelease-1>',self.button_released)
        elif some_button == "line":
            some_button = self.linebutton
            self.active_button.config(relief='raised')
            some_button.config(relief='sunken')
            self.active_button = some_button
            self.va = 'line'
            self.canvs.bind('<Button-1>',self.line_click)
            self.canvs.bind('<ButtonRelease-1>',self.button_released)
        elif some_button == "circle":
            some_button = self.circlebutton
            self.active_button.config(relief='raised')
            some_button.config(relief='sunken')
            self.active_button = some_button
            self.va = 'circle'
            self.canvs.bind('<Button-1>',self.Circle_Click)
            self.canvs.bind('<ButtonRelease-1>',self.button_released)
        self.old_x = None
        self.old_y = None
        self.line_width = 1
        self.color = 'black'

    def line_click(self,event):
        #self.activate_button(self.linebutton)
        if self.va =='line':
            self.old_x = event.x
            self.old_y = event.y
            self.linelist.append(event.x)
            self.linelist.append(event.y)

    def Circle_Click(self,event):
        #self.activate_button(self.circlebutton)
        if self.va =='circle':
            self.old_x = event.x
            self.old_y = event.y
            self.circlelist.append(event.x)
            self.circlelist.append(event.y)


    def Brush(self,event):
        #self.active_button = self.penbutton
        if self.va =='pen':
            if self.old_x and self.old_y:
                self.canvs.create_line(self.old_x, self.old_y, event.x, event.y)
            self.old_x = event.x
            self.old_y = event.y

    def button_released(self, event):
        if self.va == 'line':
            self.canvs.create_line(self.old_x, self.old_y, event.x, event.y)
            self.linelist.append(event.x)
            self.linelist.append(event.y)
        elif self.va == 'circle':
            self.canvs.create_oval(self.old_x, self.old_y, event.x, event.y)
            self.circlelist.append(event.x)
            self.circlelist.append(event.y)
        self.old_x, self.old_y = None, None


    def redraw(self):
        for i in range(0,len(self.circlelist),4):
            self.canvs.create_oval(self.circlelist[i],self.circlelist[i+1],self.circlelist[i+2],self.circlelist[i+3])
        for j in range(0,len(self.linelist),4):
            self.canvs.create_line(self.linelist[j],self.linelist[j+1],self.linelist[j+2],self.linelist[j+3])


    def save_canvas(self):
        self.canvs.postscript(file="1005760.ps")


    def clear_canvas(self):
        self.canvs.delete("all")

    def Show_help_about(self):
        showinfo("About PY paint", '''\
        Created by : Muthuraman
        ID : 1005760''')

    def exit(self):
        answer=askquestion("Exit","Are You Sure?",icon='warning')
        if answer == "yes":
            root.destroy()
        else:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Python Paint")
    Painter(root)
    root.geometry("800x800")
    root.mainloop()
