#----------------------------------Librerias-------------------------------
from tkinter import * ; from datetime import datetime
from time import strftime
from tkinter import messagebox ;from PIL import ImageTk,Image
from tkinter import ttk ; from pygame import mixer
#--------------------------------------------------------------------------

#creacion del display
t=Tk()
t.geometry('1280x720')
t.minsize(1280,720)
t.maxsize(1280,720)
t.title("Reloj Personal")
mixer.init()

#formato para extraer el dia de la libreria
a=datetime.today().strftime('%A')
b=(a.upper())
c=(b[0:2]) 

#imagen de fondo de la aplicacion
img1=Image.open("01.png")
img2= ImageTk.PhotoImage(img1)
Label(t,image=img2).place(x=-2,y=0)

#se crea el cuadro para el reloj digital
f1=Frame(t,width=750, height=200,bg='#0e1013')
f1.place(x=265,y=200)
#--------------------------------------------------------------
#entrada: entra el formato del tiempo y se crean las labels en las que ira
#salida: se retorna en texto para mostrarlo en la interfaz
#--------------------------------------------------------------
def home():   
    
    #label principal Frame,Fuente,Background,foreground
    l1=Label(f1, font=('Open Sans',60), bg='#0e1013', fg='#d3d3d3')
    l1.place(x=275,y=35)
    #formato del tiempo 
    a=strftime('%H : %M : %S')  
    l1.config(text=a)
    l1.after(1000,home)
    #label del separador entre dia y horas
    l2=Label(f1, font=('Open Sans',60), bg='#0e1013', fg='#d3d3d3')
    l2.config(text=c+" |")
    l2.place(x=75,y=35)
    #label del dia
    l3=Label(f1, font=('Open Sans',8),bg='#0e1013',fg='#7f7f7f',text='Dia')
    l3.place(x=122,y=130)
    #label de las horas
    l4=Label(f1, font=('Open Sans',8),bg='#0e1013',fg='#7f7f7f',text='Horas')
    l4.place(x=305,y=130)
    #label de los minutos
    l5=Label(f1, font=('Open Sans',8),bg='#0e1013',fg='#7f7f7f',text='Minutos')
    l5.place(x=445,y=130)
    #label de los segundos
    l3=Label(f1, font=('Open Sans',8),bg='#0e1013',fg='#7f7f7f',text='Segundos')
    l3.place(x=445+145+5,y=130)
    return
#--------------------------------------------------------------
#listas con el rango de unidades que tiene cada tiempo
#--------------------------------------------------------------
lista_horas = []
lista_minutos = []
lista_segundos = []

for  i in range(0,24):
	lista_horas.append(i)

for  i in range(0,60):
	lista_minutos.append(i)

for  i in range(0,60):
	lista_segundos.append(i)

#--------------------------------------------------------------
#se crean los textos para hora,minutos y segundos
#--------------------------------------------------------------
t1 = Label(t, font= ('Open Sans',12), bg= '#0e1013', fg= '#d3d3d3', text= 'Hora')
t1.place(x=400,y=420)
t2 = Label(t, font= ('Open Sans',12), bg= '#0e1013', fg= '#d3d3d3', text= 'Minutos')
t2.place(x=600,y=420)
t3 = Label(t, font= ('Open Sans',12), bg= '#0e1013', fg= '#d3d3d3',  text= 'Segundos')
t3.place(x=800,y=420)

#--------------------------------------------------------------
#se crean las boxes con el rango de los arrays ya definidos
#y se les da un diseño
#--------------------------------------------------------------
combobox1 = ttk.Combobox(t, values = lista_horas , style = "TCombobox", justify='center',width='12', font='Arial')
combobox1.place(x=355,y=480)
combobox1.current(0)
combobox2 = ttk.Combobox(t, values = lista_minutos , style = "TCombobox", justify='center',width='12', font='Arial')
combobox2.place(x=568,y=480)
combobox2.current(0)
combobox3 = ttk.Combobox(t, values = lista_segundos , style = "TCombobox", justify='center',width='12', font='Arial')
combobox3.place(x=775,y=480)
combobox3.current(0)


style = ttk.Style()
style.theme_create('combostyle', parent='alt',settings = {'TCombobox':
                                     {'configure':
                                      {'selectbackground': 'red',
                                       'fieldbackground': '#d3d3d3',
                                       'background': 'blue'
                                       }}})
style.theme_use('combostyle')

t.option_add('*TCombobox*Listbox*Background', 'white')
t.option_add('*TCombobox*Listbox*Foreground', 'black')
t.option_add('*TCombobox*Listbox*selectBackground', 'green2')
t.option_add('*TCombobox*Listbox*selectForeground', 'black')

#--------------------------------------------------------------
#textos de la alarma, repetir y el box de x veces que se repite
#--------------------------------------------------------------
alarma = Label(t,font = ('Open Sans', 20), bg='#0e1013', fg = '#d3d3d3' )
alarma.place(x=355,y=550)
repetir = Label(t, font='Arial', bg='#0e1013', text = 'Repetir', fg = '#d3d3d3')
repetir.place(x=670,y=550)
cantidad = ttk.Combobox(t, values = (1,2,3,4,5), justify='center',width='8', font='Arial')
cantidad.place(x=775,y=550)
cantidad.current(0)

#--------------------------------------------------------------
#entrada: entra el formato de las boxes en hora, min. y seg. y el sistema
#tiempo actual
#salida: se retornasi el tiempo de las boxes es igual al 
#tiempo actual entonces que se muestre una ventana con que la hora de la alarma
#y que comienze a sonar el audio
#--------------------------------------------------------------
def obtener_tiempo():
    x_hora = combobox1.get()
    x_minutos = combobox2.get()
    x_segundos = combobox3.get()

    hora =  strftime('%H')
    minutos = strftime('%M')
    segundos = strftime('%S')
    

    hora_alarma = x_hora +' : '+ x_minutos +' : '+ x_segundos
    alarma['text']= hora_alarma

	#condicion:
    if int(hora) == int(x_hora):
	    if int(minutos) == int(x_minutos):
	        if int(segundos) == int(x_segundos):								
	            (mixer.music.load("audio.mp3"),
                mixer.music.play(loops=int(cantidad.get())),
                messagebox.showinfo(message=hora_alarma,title="Alarma"))
             
    texto_hora.after(100, obtener_tiempo)
    return
texto_hora = Label(t,  fg = 'green2', bg='black')


#--------------------------------------------------------------
#llamado de las funciones
#--------------------------------------------------------------
home() ; obtener_tiempo() ; t.mainloop() 