#------------------------------LIBRERIAS--------------------------------------
import tkinter
import tkinter.font as tkFont
from tkinter import*
from tkinter import messagebox
from tkinter import filedialog
import time
import ast


#--------------------------VENTANAS---------------------------------------------------

NewWindow=Tk()
menu=Menu(NewWindow)
NewWindow.config(menu=menu)
NewWindow.title("PATITO 1.0.0")
NewWindow.resizable(1,1)
NewWindow.iconbitmap("Logo.ico")
NewWindow.geometry("800x465")
#fondo color = raiz.configure(bg="DarkRed")

fondo=PhotoImage(file='Fondo.gif')
fondo1 = Label(NewWindow, image=fondo).place(x=0,y=0,relwidth=1,relheight=1)
#---------------------------------------------------FUNCIONES------------------
#-----------------------------------------------------FUNCION SALIR--------------------------------------

def SALIR():
    salir=messagebox.askquestion("Salir","Desea salir de la interfaz?")
    if salir == 'yes':
        NewWindow.quit()
        NewWindow.destroy()

#----------------------------------------------FUNCION ANALIZAR LA CABEZERA ETHERNET------------------------------------------------           
def CABEZERA_ETHERNET():
    archivo = filedialog.askopenfilename(title="Abrir un paquete de red",filetypes=(("Archivos de texto","*.txt"),("Archivos pdf","*.pdf"),
    ("Archivos python","*.py"),("Todos los archivos","*.*")))
   
    v = Toplevel()
    v.geometry = ("400x400")
    v.resizable(1,1)
    v.title("Paquete de red")
    v.iconbitmap("Logo.ico")
    v.configure(bg="black")
    
    fontStyle1 = tkFont.Font(family="Lucida Grande", size=28)
    fontStyle2 = tkFont.Font(family="Lucida Grande", size=25)
    a=open(archivo)
    T=a.read()
    i = 0
    j = 3
    E = "                                       "
    x=0
    while x < 1:
        if j<4:

            etiqueta=tkinter.Label(v,text="PAQUETE DE DATOS A ANALIZAR o_O",font=fontStyle1)
            etiqueta.config(bg="lemon chiffon")
           
            etiqueta.pack()
            
            j=j+4
        elif j<8:
            j=j+400
            T1=T[i:j]
            T1 = T1.replace(' ',':')
            etiqueta=tkinter.Label(v,text=T1,font=fontStyle1)
            etiqueta.config(bg="alice blue")
           
            etiqueta.pack()
            
            j=j-399
        elif j<10:
            j=j+33
            """etiqueta=tkinter.Label(v,text="\n",font=fontStyle1)
            T1=T[i:j]
            T1 = T1.replace(' ', '.').replace('\n', '.').replace('\r','.')
            etiqueta=tkinter.Label(v,text="Cabecera de ethernet:     "+T1,font=fontStyle2)
            j=j+400
            T1=T[i:j]
            T1 = T1.replace(' ',':')
            etiqueta=tkinter.Label(v,text=T1,font=fontStyle1)
            etiqueta.config(bg="alice blue")
            etiqueta.config(bg="coral1")
            etiqueta.pack()
            etiqueta.config(bg="gray1")"""
            T1=T[i:j]
            T1 = T1.replace(' ', '.').replace('\n', '.').replace('\r','.')
            etiqueta=tkinter.Label(v,text="         Cabecera de ethernet:     "+T1+" ",font=fontStyle2)
            etiqueta.config(bg="gold")
            #etiqueta.config(bg="coral1")
            etiqueta.pack()
            j=j-24
        elif j<18:
            T1=T[i:j]
            T1 = T1.replace(' ', '.').replace('\n', '.').replace('\r','.')
            etiqueta=tkinter.Label(v,text="       Direccion MAC destino:     "+T1+E+"   ",font=fontStyle2)
            etiqueta.config(bg="lawn green")
            etiqueta.pack()
            i=i+18
            j=j+18
        elif j<36:
            T1=T[i:j]
       
            T1 = T1.replace(' ', '.').replace('\n', '.').replace('\r','.')
            etiqueta=tkinter.Label(v,text="        Direccion MAC origen:     "+T1+E+"  ",font=fontStyle2)
            etiqueta.config(bg="sky blue")
            #etiqueta.config(bg="lavender")
            #etiqueta.config(bg="ivory")
            etiqueta.pack()
            i=i+18
            j=j+3
        elif j<40:
            j=j+3
            
        elif j<43:
            T1=T[i:j]
          
            T1 = T1.replace('.','').replace('\n','').replace('\r','').replace(':','').replace(' ','')
            j=j+4 
            etiqueta=tkinter.Label(v,text="                  Tipo de servicio:     "+"0x"+T1+E+"                     ",font=fontStyle2)
            etiqueta.config(bg="lavender")
            etiqueta.pack()
            if T1=='0800':
                etiqueta=tkinter.Label(v,text="                                Ineternet Protocol Version 4(IPV4)                                  ",font=fontStyle2)
                etiqueta.config(bg="salmon")
                etiqueta.pack()
            else:
                etiqueta=tkinter.Label(v,text="                                PROTOCOLO EN DESARROLLO                                ",font=fontStyle2)
                etiqueta.config(bg="salmon")
                etiqueta.pack()
                
            #etiqueta.config(bg="LightSteelBlue3")
           
            j=j+12
            #NUMERO SUPERIMPORTANTE
            x = x+1
        """elif j<70:
            print(i)
            etiqueta=tkinter.Label(v,text="  Tipo de servicio:     ",font=fontStyle2)
            etiqueta.config(bg="lavender")
            etiqueta.pack()
            i=i+18
            j=j+3
            #NUMERO SUPERIMPORTANTE
            x = x+1"""
            
#------------------------------------------------FUNCION CABECERA IPV4---------------------------------------
def CABEZERA_IPV4():
    archivo = filedialog.askopenfilename(title="Abrir un paquete de red",filetypes=(("Archivos de texto","*.txt"),("Archivos pdf","*.pdf"),
    ("Archivos python","*.py"),("Todos los archivos","*.*")))
    

    v = Toplevel()
    v.geometry = ("400x400")
    v.resizable(1,1)

    
    v.title("Paquete de red")
    v.iconbitmap("Logo.ico")
    v.configure(bg="black")
    fontStyle1 = tkFont.Font(family="Lucida Grande", size=26)
    fontStyle2 = tkFont.Font(family="Lucida Grande", size=23)
    a=open(archivo)
################
    AreaLabelFrame = LabelFrame(v, bg='gray1') #Área de la capa

    CanvasWidget = Canvas(AreaLabelFrame, bg='gray1', width=1050,height=500) #El área donde se va a desplazar el widget
    CanvasWidget.pack(side='left',fill='both')

    ScrollbarWidget = tkinter.Scrollbar(AreaLabelFrame, orient='vertical', command=CanvasWidget.yview) #Barra de desplazamiento
    ScrollbarWidget.pack(side='right', fill='y')

    CanvasWidget.config(yscrollcommand=ScrollbarWidget.set) 
    CanvasWidget.bind('<Configure>', lambda e: CanvasWidget.config(scrollregion = CanvasWidget.bbox('all'))) #Configurara el evento de la barra de desplazamiento

    """def _on_mousewheel(event):
        CanvasWidget.yview_scroll(-1 * (event.delta // 120), "units") # Evento del mouse

    CanvasWidget.bind('<MouseWheel>', _on_mousewheel) #Evento de movimiento de mouse."""

    FramaVentana = Frame(CanvasWidget, bg='gray1') #Frame para mover los widgets.
    CanvasWidget.create_window((0,0), window=FramaVentana) #Crea la capa para poder mover los widgets

    AreaLabelFrame.pack(fill='y', expand='yes', padx=0, pady=0)

######################
    T=a.read()

    E = "                             "
    EE="              "
    i = 0
    j = 3
    x=0
    while x < 1:
        if j<4:
            etiqueta=tkinter.Label(FramaVentana,text="PAQUETE DE DATOS A ANALIZAR o_O",font=fontStyle2)
            etiqueta.config(bg="lemon chiffon")
            etiqueta.place(x=50, y=0)
           
            etiqueta.pack()
            j=j+4

        elif j<8:
            j=j+400
            T1=T[i:j]
            T1 = T1.replace(' ',':')
            etiqueta=tkinter.Label(FramaVentana,text=T1,font=fontStyle2)
            etiqueta.config(bg="alice blue")
            etiqueta.pack()
            """ etiqueta0=tkinter.Label(v,text="",font=fontStyle1)
            etiqueta0.config(bg="gray1")
            etiqueta0.pack()""" 
            j=j-399

        elif j<10:
            j=j+33
            T1=T[i:j]
            T1 = T1.replace(' ', '.').replace('\n', '.').replace('\r','.')
            etiqueta=tkinter.Label(FramaVentana,text="     Cabecera de ethernet:     "+T1+"     ",font=fontStyle2)
            etiqueta.config(bg="gold")
            #etiqueta.config(bg="coral1")
            etiqueta.pack()
            j=j-24
             
        elif j<18:
            T1=T[i:j]
            T1 = T1.replace(' ', '.').replace('\n', '.').replace('\r','.')
            etiqueta=tkinter.Label(FramaVentana,text="   Direccion MAC destino:     "+T1+E+"                ",font=fontStyle2)
            etiqueta.config(bg="lawn green")
            etiqueta.pack()
            i=i+18
            j=j+18
            
        elif j<36:
            T1=T[i:j]
       
            T1 = T1.replace(' ', '.').replace('\n', '.').replace('\r','.')
            etiqueta=tkinter.Label(FramaVentana,text="    Direccion MAC origen:     "+T1+E+"               ",font=fontStyle2)
            etiqueta.config(bg="sky blue")
            #etiqueta.config(bg="lavender")
            #etiqueta.config(bg="ivory")
            etiqueta.pack()
            i=i+18
            j=j+3
        elif j<40:
            j=j+3
            
        elif j<43:
            T1=T[i:j]
          
            T1 = T1.replace('.','').replace('\n','').replace('\r','').replace(':','').replace(' ','')
            j=j+4 
            etiqueta=tkinter.Label(FramaVentana,text="             Tipo de servicio:     "+"0x"+T1+E+"                                 ",font=fontStyle2)
            etiqueta.config(bg="lavender")
            etiqueta.pack()
            if T1=='0800':
                etiqueta=tkinter.Label(FramaVentana,text="                                Ineternet Protocol Version 4(IPV4)                                ",font=fontStyle2)
                etiqueta.config(bg="salmon")
                etiqueta.pack()
                k=9
                i=0
                if k<10:
                    i=i+42
                    k=k+62
                    T1=T[i:k]
                    T1 = T1.replace(':', '.').replace(' ', '.').replace('\n', '.').replace('\r', '.')
                    etiqueta=tkinter.Label(FramaVentana,text=" Cabecera IPv4 (parte 1):     "+T1+"                          ",font=fontStyle2)
                    etiqueta.config(bg="LawnGreen")
                    etiqueta.pack()
                    k=k-27

                    #LONGITUD DE LA CABECERA
    
                    T1=T[i:k]
                    #@primer auxiliar
                    T3=T[i]
                    #@segundo auxiliar
                    T4=T[i+1]
                    op0 = int(T3)
                    op1 = int(T4)
                    res = (op0*op1)
                    etiqueta0=tkinter.Label(FramaVentana,text="                          Version:     "+str(op0)+E+"                                          ",font=fontStyle2)
                    etiqueta0.config(bg="turquoise3")
                    etiqueta0.pack()
                    #SIN OPERACION
                    #etiqueta=tkinter.Label(FramaVentana,text="          Longitud de la cabecera:     "+str(res)+" bytes"+E+"   ",font=fontStyle2)
                    #CON OPERACION EN LONGITUD 
                    etiqueta=tkinter.Label(FramaVentana,text=" Longitud de la cabecera:     "+str(op0)+" * "+str(op1)+" = "+str(res)+" bytes                                                 ",font=fontStyle2)
                    etiqueta.config(bg="tomato")
                    etiqueta.pack()
                    k=k+3

                    i=i+3
                    T1=T[i:k]
          
                    T1 = T1.replace(':', '.').replace(' ', '.').replace('\n', '.').replace('\r', '.')
                    #CADENA A HEXADECIMAL A ENTERO A BINARIO
                    TA = T1
                    PP = int(TA, 16)
                    hex_valu = hex(PP)
                    ss=ast.literal_eval(hex_valu)
                    temp = format(ss, "b")
                    ####
                    temp=temp.zfill(8)
                    str(temp)
            
            
                    #######################
                    #COMPARA EL NUMERO EN BINARIO PARA SABER 
                    if temp[0:3]=='000':
                        T2=" (Rutina) "
                    elif temp[0:3]=='001':
                        T2=" (Prioritario)               "

                    elif temp[0:3]=='100':
                        T2=" (Invalidacion relampago)               "
            
                    T3=" Retardo: "
                    T4=" RENDIMIENTO: "
                    T5=" Fiabilidad: "
                    T6=" Costo: "

                
                    etiqueta=tkinter.Label(FramaVentana,text="           Campo de servicios diferenciados:     "+T1+"   ",font=fontStyle2)
                    etiqueta.config(bg="gold")
                    etiqueta.pack()
    
                    etiqueta1=tkinter.Label(FramaVentana,text=T2+T3+temp[3]+T4+temp[4],font=fontStyle2)
                    etiqueta1.config(bg="coral1")
                    etiqueta1.pack()
            
                    etiqueta2=tkinter.Label(FramaVentana,text=T5+temp[5]+T6+temp[6],font=fontStyle2)
                    etiqueta2.config(bg="ivory1")
                    etiqueta2.pack()
            
                    k=k+6

                    i=i+3
                    T1=T[i:k]
                    T1 = T1.replace(':','').replace(' ', '').replace('\n','').replace('\r','').replace('.', '')

              
                    #CONVERTIR CADENA A HEXADECIMAL Y LUEGO A DECIMAL
                    PPP = int(T1, 16)
                    hex_value = hex(PPP)
          
          
                    s=ast.literal_eval(hex_value)
         
                    etiqueta=tkinter.Label(FramaVentana,text="                         Longitud total:     "+str(s)+" bytes                                 ",font=fontStyle2)
                    #FIN DE LA CONVERSION
           
                    etiqueta.config(bg="light sea green")
                    etiqueta.pack()

                    k=k+6
                    i=i+6
                    
                    T1=T[i:k]
                    T1 = T1.replace(':', '.').replace(' ', '.').replace('\n', '.').replace('\r', '.')
    
                    TAUX=T1
                    TAUX = TAUX.replace('.','').replace(' ','').replace('\n','').replace('\r','').replace(':','')
                    print(TAUX)
                    HA = int(TAUX, 16)
                    HEX = hex(HA)
                    NV=ast.literal_eval(HEX)
                    #CON VALOR DECIMAL
                    etiqueta=tkinter.Label(FramaVentana,text="                         Identificacion:     "+T1+" ("+str(NV)+")                          ",font=fontStyle2)
                    #SIN VALOR EN DECIMAL
                    #etiqueta=tkinter.Label(v,text="                        Identificacion:     "+T1+"                                     ",font=fontStyle2)

                    etiqueta.config(bg="plum3")
                    etiqueta.pack()
                    k=k+4

                    i=i+6
                    T1=T[i:k]
                    ########CONVERSIONES
                    TT = T1
                    N = int(TT, 16)
                    EHH = hex(N)
                    VN=ast.literal_eval(EHH)
                    tem = format(VN, "b")
                    tem=tem.zfill(8)
                    str(tem)
                    ###CONDICIONALES PARA LAS BANDERAS
                    if tem[1]=='1':
                        TXC="                         (1) No permite fragmentar                                 "
                
                    else:
                        TXC="                           (0) Permite fragmentar                                    " 
                    if tem[2]=='0':
                        TXD="                              (0) Ultimo fragmento                                    "
  
                    else:
               
                        TXD="                       (1) No es el ultimo fragmento                              "
             
                    etiqueta=tkinter.Label(FramaVentana,text="                               Banderas:     "+T1+E+"            ",font=fontStyle2) 
                    etiqueta.config(bg="lime green")
                    etiqueta.pack()
            

                    etiqueta1=tkinter.Label(FramaVentana,text=TXC,font=fontStyle2) 
                    etiqueta1.config(bg="ivory2")
                    etiqueta1.pack()
                    etiqueta2=tkinter.Label(FramaVentana,text=TXD,font=fontStyle2) 
                    etiqueta2.config(bg="orange red")
                    etiqueta2.pack()
                    k=k+5
                    i=i+6
                    
                    T1=T[i:k]
                    TIEMPOV = int(T1, 16)
                    TVH = hex(TIEMPOV)
                    TVHE=ast.literal_eval(TVH)
                    T1 = T1.replace(':', '.').replace(' ', '.').replace('\n', '.').replace('\r', '.')
                    etiqueta=tkinter.Label(FramaVentana,text="                        Tiempo de vida:     "+T1+" ( "+str(TVHE)+" segundos )",font=fontStyle2)
                    etiqueta.config(bg="LawnGreen")
                    etiqueta.pack()
                    k=k+3

                    i=i+3
                    T1=T[i:k]
                    if T1=='06':
                        etiqueta=tkinter.Label(FramaVentana,text="Protocolo: "+T1+"              TCP                                 ",font=fontStyle2)
                        etiqueta.config(bg="salmon")
                        etiqueta.pack()
                    elif T1=='08':
                        etiqueta=tkinter.Label(FramaVentana,text="Protocolo: "+T1+"              EGP                                 ",font=fontStyle2)
                        etiqueta.config(bg="salmon")
                        etiqueta.pack()
                    else:
                        etiqueta=tkinter.Label(FramaVentana,text="Protocolo: "+T1+"           PROTOCOLO EN DESARROLLO                                ",font=fontStyle2)
                        etiqueta.config(bg="salmon")
                        etiqueta.pack()
                    k=k+6
                    #IP PARTE 2

                    k=101
                    i=i+3
                    T1=T[i:k]
                    T1 = T1.replace(':', '.').replace(' ', '.').replace('\n', '.').replace('\r', '.')
                    etiqueta=tkinter.Label(FramaVentana,text="Cabecera IPv4(parte 2):     "+T1+"       ",font=fontStyle2)
                    etiqueta.config(bg="LawnGreen")
                    etiqueta.pack()

  


                    #########gdg


                    i=72
                    k=77
                   
                    T1=T[i:k]
                    T_AUXI = T
                    T_AUXI  = T_AUXI.replace('.','').replace(' ','').replace('\n','').replace('\r','').replace(':','')


                    """
                    *******************************
                    *******************************
                    *******************************
                    *******************************
                    *******************************
                    """
                    #TERMINAR CHECK SUM
                    #*******************************
                    #*******************************
                    #*******************************
                    #*******************************
                    #*******************************
                    #*******************************
                    #CALCULO PARA EL CHECK SUM

                    #UNA VEZ TERMINADO IMPLEMENTAR UNA ESTRUCTURA ITERATIVA
                    
                    #NUMERO 4   
                    b1 = T_AUXI[28:29]
                    bb1 = int(b1,16)
                    bh1 = hex(bb1)
                    br1=ast.literal_eval(bh1)
                    bf1 = format(br1, "b")
                    bf1=bf1.zfill(4)
                    bf1 = bf1.replace('0', '2')
                    bf1 = bf1.replace('1', '0')
                    bf1 = bf1.replace('2', '1')
                    #NUMERO 5
                    b2 = T_AUXI[29:30]
                    bb2 = int(b2,16)
                    bh2 = hex(bb2)
                    br2=ast.literal_eval(bh2)
                    bf2 = format(br2, "b")
                    bf2=bf2.zfill(4)
                    bf2 = bf2.replace('0', '2')
                    bf2 = bf2.replace('1', '0')
                    bf2 = bf2.replace('2', '1')
                    #NUMERO 0 
                    b3 = T_AUXI[30:31]
                    bb3 = int(b3,16)
                    bh3 = hex(bb3)
                    br3=ast.literal_eval(bh3)
                    bf3 = format(br3, "b")
                    bf3=bf3.zfill(4)
                    bf3 = bf3.replace('0', '2')
                    bf3 = bf3.replace('1', '0')
                    bf3 = bf3.replace('2', '1')
                    #NUMERO 0 
                    b4 = T_AUXI[31:32]
                    bb4 = int(b4,16)
                    bh4 = hex(bb4)
                    br4=ast.literal_eval(bh4)
                    bf4 = format(br4, "b")
                    bf4=bf4.zfill(4)
                    bf4 = bf4.replace('0', '2')
                    bf4 = bf4.replace('1', '0')
                    bf4 = bf4.replace('2', '1')
                    #NUMERO 0
                    b5 = T_AUXI[32:33]
                    bb5 = int(b5,16)
                    bh5 = hex(bb5)
                    br5=ast.literal_eval(bh5)
                    bf5 = format(br5, "b")
                    bf5=bf5.zfill(4)
                    bf5 = bf5.replace('0','2')
                    bf5 = bf5.replace('1', '0')
                    bf5 = bf5.replace('2', '1')
                    #NUMERO 0
                    b6 = T_AUXI[33:34]
                    bb6 = int(b6,16)
                    bh6 = hex(bb6)
                    br6=ast.literal_eval(bh6)
                    bf6 = format(br6, "b")
                    bf6=bf6.zfill(4)
                    bf6 = bf6.replace('0', '2')
                    bf6 = bf6.replace('1', '0')
                    bf6 = bf6.replace('2', '1')
                    #NUMERO 6
                    b7 = T_AUXI[34:35]
                    bb7 = int(b7,16)
                    bh7 = hex(bb7)
                    br7=ast.literal_eval(bh7)
                    bf7 = format(br7, "b")
                    bf7=bf7.zfill(4)
                    bf7 = bf7.replace('0', '2')
                    bf7 = bf7.replace('1', '0')
                    bf7 = bf7.replace('2', '1')
                    #NUMERO 0 
                    b8 = T_AUXI[35:36]
                    bb8 = int(b8,16)
                    bh8 = hex(bb8)
                    br8=ast.literal_eval(bh8)
                    bf8 = format(br8, "b")
                    bf8=bf8.zfill(4)
                    bf8 = bf8.replace('0', '2')
                    bf8 = bf8.replace('1', '0')
                    bf8 = bf8.replace('2', '1')
                    #NUMERO 2
                    b9 = T_AUXI[36:37]
                    bb9 = int(b9,16)
                    bh9 = hex(bb9)
                    br9=ast.literal_eval(bh9)
                    bf9 = format(br9, "b")
                    bf9=bf9.zfill(4)
                    bf9 = bf9.replace('0','2')
                    bf9 = bf9.replace('1', '0')
                    bf9 = bf9.replace('2', '1')
                    #NUMERO 1
                    b10 = T_AUXI[37:38]
                    bb10 = int(b10,16)
                    bh10 = hex(bb10)
                    br10=ast.literal_eval(bh10)
                    bf10 = format(br10, "b")
                    bf10=bf10.zfill(4)
                    bf10 = bf10.replace('0', '2')
                    bf10 = bf10.replace('1', '0')
                    bf10 = bf10.replace('2', '1')
                    #NUMERO 0
                    b11 = T_AUXI[38:39]
                    bb11 = int(b11,16)
                    bh11 = hex(bb11)
                    br11=ast.literal_eval(bh11)
                    bf11 = format(br11, "b")
                    bf11=bf11.zfill(4)
                    bf11 = bf11.replace('0', '2')
                    bf11 = bf11.replace('1', '0')
                    bf11 = bf11.replace('2', '1')
                    #NUMERO 8
                    b12= T_AUXI[39:40]
                    bb12 = int(b12,16)
                    bh12 = hex(bb12)
                    br12=ast.literal_eval(bh12)
                    bf12 = format(br12, "b")
                    bf12=bf12.zfill(4)
                    bf12 = bf12.replace('0', '2')
                    bf12 = bf12.replace('1', '0')
                    bf12 = bf12.replace('2', '1')
                    #NUMERO 4
                    b13= T_AUXI[40:41]
                    bb13 = int(b13,16)
                    bh13 = hex(bb13)
                    br13=ast.literal_eval(bh13)
                    bf13 = format(br13, "b")
                    bf13=bf13.zfill(4)
                    bf13 = bf13.replace('0', '2')
                    bf13 = bf13.replace('1', '0')
                    bf13 = bf13.replace('2', '1')
                    #NUMERO 0
                    b14= T_AUXI[41:42]
                    bb14 = int(b14,16)
                    bh14 = hex(bb14)
                    br14=ast.literal_eval(bh14)
                    bf14 = format(br14, "b")
                    bf14=bf14.zfill(4)
                    bf14 = bf14.replace('0', '2')
                    bf14 = bf14.replace('1', '0')
                    bf14 = bf14.replace('2', '1')
                    #NUMERO 0
                    b15= T_AUXI[42:43]
                    bb15 = int(b15,16)
                    bh15 = hex(bb15)
                    br15=ast.literal_eval(bh15)
                    bf15 = format(br15, "b")
                    bf15=bf15.zfill(4)
                    bf15 = bf15.replace('0', '2')
                    bf15 = bf15.replace('1', '0')
                    bf15 = bf15.replace('2', '1')
                    #NUMERO 0
                    b16= T_AUXI[43:44]
                    bb16 = int(b16,16)
                    bh16 = hex(bb16)
                    br16=ast.literal_eval(bh16)
                    bf16 = format(br16, "b")
                    bf16=bf16.zfill(4)
                    bf16 = bf16.replace('0', '2')
                    bf16 = bf16.replace('1', '0')
                    bf16 = bf16.replace('2', '1')
                    #NUMERO 2
                    b17= T_AUXI[44:45]
                    bb17 = int(b17,16)
                    bh17 = hex(bb17)
                    br17=ast.literal_eval(bh17)
                    bf17 = format(br17, "b")
                    bf17=bf17.zfill(4)
                    bf17 = bf17.replace('0', '2')
                    bf17 = bf17.replace('1', '0')
                    bf17 = bf17.replace('2', '1')
                    #NUMERO 0
                    b18= T_AUXI[45:46]
                    bb18 = int(b18,16)
                    bh18 = hex(bb18)
                    br18=ast.literal_eval(bh18)
                    bf18 = format(br18, "b")
                    bf18=bf18.zfill(4)
                    bf18 = bf18.replace('0', '2')
                    bf18 = bf18.replace('1', '0')
                    bf18 = bf18.replace('2', '1')
                    #NUMERO 0
                    b19= T_AUXI[46:47]
                    bb19 = int(b19,16)
                    bh19 = hex(bb19)
                    br19=ast.literal_eval(bh19)
                    bf19 = format(br19, "b")
                    bf19=bf19.zfill(4)
                    bf19 = bf19.replace('0', '2')
                    bf19 = bf19.replace('1', '0')
                    bf19 = bf19.replace('2', '1')
                    #NUMERO 6
                    b20= T_AUXI[47:48]
                    bb20 = int(b20,16)
                    bh20 = hex(bb20)
                    br20=ast.literal_eval(bh20)
                    bf20 = format(br20, "b")
                    bf20=bf20.zfill(4)
                    bf20 = bf20.replace('0', '2')
                    bf20 = bf20.replace('1', '0')
                    bf20 = bf20.replace('2', '1')
                    
                    #####NUMREO VERIFICADOR

                    #NUMERO 3
                    Verificador0= T_AUXI[48:49]
                    Verificador_a0 = int(Verificador0,16)
                    Verificador_b0 = hex(Verificador_a0)
                    Verificador_c0 = ast.literal_eval(Verificador_b0)
                    Verificador_d0 = format(Verificador_c0, "b")
                    Verificador_d0=Verificador_d0.zfill(4)
                    Verificador_d0 = Verificador_d0.replace('0', '2')
                    Verificador_d0 = Verificador_d0.replace('1', '0')
                    Verificador_d0 = Verificador_d0.replace('2', '1')
                    #NUMERO 2
                    Verificador1= T_AUXI[49:50]
                    Verificador_a1 = int(Verificador1,16)
                    Verificador_b1 = hex(Verificador_a1)
                    Verificador_c1 = ast.literal_eval(Verificador_b1)
                    Verificador_d1 = format(Verificador_c1, "b")
                    Verificador_d1=Verificador_d1.zfill(4)
                    Verificador_d1 = Verificador_d1.replace('0', '2')
                    Verificador_d1 = Verificador_d1.replace('1', '0')
                    Verificador_d1 = Verificador_d1.replace('2', '1')
                    #NUMERO 3
                    Verificador2= T_AUXI[50:51]
                    Verificador_a2 = int(Verificador2,16)
                    Verificador_b2 = hex(Verificador_a2)
                    Verificador_c2 = ast.literal_eval(Verificador_b2)
                    Verificador_d2 = format(Verificador_c2, "b")
                    Verificador_d2=Verificador_d2.zfill(4)
                    Verificador_d2 = Verificador_d2.replace('0', '2')
                    Verificador_d2 = Verificador_d2.replace('1', '0')
                    Verificador_d2 = Verificador_d2.replace('2', '1')
                    #NUMERO 2
                    Verificador3= T_AUXI[51:52]
                    Verificador_a3 = int(Verificador3,16)
                    Verificador_b3 = hex(Verificador_a3)
                    Verificador_c3 = ast.literal_eval(Verificador_b3)
                    Verificador_d3 = format(Verificador_c3, "b")
                    Verificador_d3=Verificador_d3.zfill(4)
                    Verificador_d3 = Verificador_d3.replace('0', '2')
                    Verificador_d3 = Verificador_d3.replace('1', '0')
                    Verificador_d3 = Verificador_d3.replace('2', '1')

                    ###3FIN DE NUMERO VERIFICADOR
                    
                    #NUMERO 8
                    b21= T_AUXI[52:53]
                    bb21 = int(b21,16)
                    bh21 = hex(bb21)
                    br21=ast.literal_eval(bh21)
                    bf21 = format(br21, "b")
                    bf21=bf21.zfill(4)
                    bf21 = bf21.replace('0', '2')
                    bf21 = bf21.replace('1', '0')
                    bf21 = bf21.replace('2', '1')
                    #NUMERO 2
                    b22= T_AUXI[53:54]
                    bb22 = int(b22,16)
                    bh22 = hex(bb22)
                    br22=ast.literal_eval(bh22)
                    bf22 = format(br22, "b")
                    bf22=bf22.zfill(4)
                    bf22 = bf22.replace('0', '2')
                    bf22 = bf22.replace('1', '0')
                    bf22 = bf22.replace('2', '1')
                    #NUMERO 8
                    b23= T_AUXI[54:55]
                    bb23 = int(b23,16)
                    bh23 = hex(bb23)
                    br23=ast.literal_eval(bh23)
                    bf23 = format(br23, "b")
                    bf23=bf23.zfill(4)
                    bf23 = bf23.replace('0', '2')
                    bf23 = bf23.replace('1', '0')
                    bf23 = bf23.replace('2', '1')
                    #NUMERO 2
                    b24= T_AUXI[55:56]
                    bb24 = int(b24,16)
                    bh24 = hex(bb24)
                    br24=ast.literal_eval(bh24)
                    bf24 = format(br24, "b")
                    bf24=bf24.zfill(4)
                    bf24 = bf24.replace('0', '2')
                    bf24 = bf24.replace('1', '0')
                    bf24 = bf24.replace('2', '1')
                    #NUMERO 0
                    b25= T_AUXI[56:57]
                    bb25 = int(b25,16)
                    bh25 = hex(bb25)
                    br25=ast.literal_eval(bh25)
                    bf25 = format(br25, "b")
                    bf25=bf25.zfill(4)
                    bf25 = bf25.replace('0', '2')
                    bf25 = bf25.replace('1', '0')
                    bf25 = bf25.replace('2', '1')
                    #NUMERO 1
                    b26= T_AUXI[57:58]
                    bb26 = int(b26,16)
                    bh26 = hex(bb26)
                    br26=ast.literal_eval(bh26)
                    bf26 = format(br26, "b")
                    bf26=bf26.zfill(4)
                    bf26 = bf26.replace('0', '2')
                    bf26 = bf26.replace('1', '0')
                    bf26 = bf26.replace('2', '1')
                    #NUMERO 3
                    b27= T_AUXI[58:59]
                    bb27 = int(b27,16)
                    bh27 = hex(bb27)
                    br27=ast.literal_eval(bh27)
                    bf27 = format(br27, "b")
                    bf27=bf27.zfill(4)
                    bf27 = bf27.replace('0', '2')
                    bf27 = bf27.replace('1', '0')
                    bf27 = bf27.replace('2', '1')
                    #NUMERO 7
                    b28= T_AUXI[59:60]
                    bb28 = int(b28,16)
                    bh28 = hex(bb28)
                    br28=ast.literal_eval(bh28)
                    bf28 = format(br28, "b")
                    bf28=bf28.zfill(4)
                    bf28 = bf28.replace('0', '2')
                    bf28 = bf28.replace('1', '0')
                    bf28 = bf28.replace('2', '1')

                    bf35 = bf1
                    bf34 = bf1
                    bf33 = bf1
                    bf32 = bf1
                    bf31 = bf1
                    bf30 = bf1
                    bf29 = bf1
                    bf28 = bf1
                    bf27 = bf1
                    bf26 = bf1
                    bf25 = bf1
                    bf24 = bf1






                    #CONCATENAR
                    digito1=bf1+bf2+bf3+bf4
                    digito2=bf5+bf6+bf7+bf8
                    digito3=bf9+bf10+bf11+bf12
                    digito4=bf13+bf14+bf15+bf16
                    digito5=bf17+bf18+bf19+bf20
                    

                    digito6=bf21+bf22+bf23+bf24
                    digito7=bf25+bf26+bf27+bf28
                    digito8=bf29+bf30+bf31+bf32
                    digito9=bf33+bf34+bf35+bf36

                    check_sum = Verificador_d0+Verificador_d1+Verificador_d2+Verificador_d3
                    

                    
                    
                    sum1 = bin(int(digito1, 2) + int(digito2, 2))
                    suma1=sum1[2:]

                    if len(suma1)>16:
                        v1=suma1[0:1]
                        v2=suma1[1:]
          
                        sum1 = bin(int(v1, 2) + int(v2, 2))
                        suma1=sum1[2:]
                        res1=suma1
                        if len(sum1)<16:
                            res1=res1.zfill(16)
                        else:
                            res1=res1
                            

                    else:
                        res1=suma1



                    sum2 = bin(int(res1, 2) + int(digito3, 2))
                    suma2=sum2[2:]
                    if len(suma2)>16:
                        va1=suma2[0:1]
                        va2=suma2[1:]
                        sum2 = bin(int(va1, 2) + int(va2, 2))
                        suma2=sum2[2:]
                        res2=suma2
                        if len(res2)<16:
                            res2=res2.zfill(16)
                        else:
                            res2=res2
                            

                    else:
                        res2=suma2

        #checar desde aqui
                    
                    sum3 = bin(int(res2, 2) + int(digito4, 2))
                    suma3=sum3[2:]
                    if len(suma3)>16:
                        v1=suma3[0:1]
         
                        v2=suma3[1:]
                        sum3 = bin(int(v1, 2) + int(v2, 2))
                        suma3=sum3[2:]
                        if len(suma3)<16:
                            suma3=suma3.zfill(16)
                        else:
                            suma3=suma3            
                        res3=suma3
                    else:
                        res3=suma3
                        
                    #OPERACION NUMERO 5
                    sum4 = bin(int(res3, 2) + int(digito5, 2))
                    suma4=sum4[2:]
                    if len(suma4)>16:
                        v1=suma4[0:1]
         
                        v2=suma4[1:]
                        sum4 = bin(int(v1, 2) + int(v2, 2))
                        suma4=sum4[2:]
                        if len(suma4)<16:
                            suma4=suma4.zfill(16)
                        else:
                            suma4=suma4            
                        res4=suma4
                    else:
                        res4=suma4
                   
                    #OPERACION NUMERO 8282
                    sum5 = bin(int(res4, 2) + int(digito6, 2))
                    suma5=sum5[2:]
                    if len(suma5)>16:
                        v1=suma5[0:1]
         
                        v2=suma5[1:]
                        sum5 = bin(int(v1, 2) + int(v2, 2))
                        suma5=sum5[2:]
                        if len(suma5)<16:
                            suma5=suma5.zfill(16)
                        else:
                            suma5=suma5            
                        res5=suma5
                    else:
                        res5=suma5


                    #OPERACION 0137
                    sum6 = bin(int(res5, 2) + int(digito7, 2))
                    suma6=sum6[2:]
                    if len(suma6)>16:
                        v1=suma6[0:1]
         
                        v2=suma6[1:]
                        sum6 = bin(int(v1, 2) + int(v2, 2))
                        suma6=sum6[2:]
                        if len(suma6)<16:
                            suma6=suma6.zfill(16)
                        else:
                            suma6=suma6            
                        res6=suma6
                    else:
                        res6=suma6


                    #OPERACION 8282
                    sum7 = bin(int(res6, 2) + int(digito8, 2))
                    suma7=sum7[2:]
                    if len(suma7)>16:
                        v1=suma7[0:1]
         
                        v2=suma7[1:]
                        sum7 = bin(int(v1, 2) + int(v2, 2))
                        suma7=sum7[2:]
                        if len(suma7)<16:
                            suma7=suma7.zfill(16)
                        else:
                            suma7=suma7            
                        res7=suma7
                    else:
                        res7=suma7

                    #OPERACION 0132
                    sum8 = bin(int(res7, 2) + int(digito9, 2))
                    suma8=sum8[2:]
                    if len(suma8)>16:
                        v1=suma8[0:1]
         
                        v2=suma8[1:]
                        sum8 = bin(int(v1, 2) + int(v2, 2))
                        suma8=sum8[2:]
                        if len(suma8)<16:
                            suma8=suma8.zfill(16)
                        else:
                            suma8=suma8            
                        res8=suma8
                    else:
                        res8=suma8
              

                    #OPERACION CHECKSUM
                    CHECK = bin(int(res8, 2) + int(check_sum, 2))
                    CHECK1=CHECK[2:]
                    if len(CHECK1)>16:
                        v1=CHECK1[0:1]
         
                        v2=CHECK1[1:]
                        CHECK = bin(int(v1, 2) + int(v2, 2))
                        CHECK1=CHECK[2:]
                        if len(CHECK1)<16:
                            CHECK1=CHECK1.zfill(16)
                        else:
                            CHECK1=CHECK1         
                        CHECK_SUM=CHECK1
                    else:
                        CHECK_SUM=CHECK1


                    
                    esp0=(hex(int(res8[0:4], 2)))


                    esp1=(hex(int(res8[4:8], 2)))

                    esp2=(hex(int(res8[8:12], 2)))
            

                    esp3=(hex(int(res8[12:], 2)))
           

                    obtenido = esp0[2:]+esp1[2:]+"."+esp2[2:]+esp3[2:]
           

                    #FIN CALCULO
                    T1 = T1.replace(':', '.').replace(' ', '.').replace('\n', '.').replace('\r', '.')
                    
                    etiqueta=tkinter.Label(FramaVentana,text="Checksum esperado: "+T1,font=fontStyle2)
                    etiqueta.config(bg="ghost white")
                    etiqueta.pack()
                    
                    etiqueta1=tkinter.Label(FramaVentana,text="Checksum obtenido: "+obtenido,font=fontStyle2)
                    etiqueta1.config(bg="plum3")
                    etiqueta1.pack()

                    #CHECK SUM
                    if CHECK_SUM=='1111111111111111':
                        etiqueta=tkinter.Label(FramaVentana,text="Checksum correcto ",font=fontStyle2)
                        etiqueta.config(bg="green yellow")
                        etiqueta.pack()
                    else:
                        etiqueta=tkinter.Label(FramaVentana,text="Checksum incorrecto ",font=fontStyle2)
                        etiqueta.config(bg="red")
                        etiqueta.pack()
                        
                    i=78
                    k=89
                    T1=T[i:k]
                    T1 = T1.replace(':', '.').replace(' ', '.').replace('\n', '.').replace('\r', '.')
                    etiqueta=tkinter.Label(FramaVentana,text=" Direccion IP origen:     "+T1+"       ",font=fontStyle2)
                    etiqueta.config(bg="Cyan")
                    etiqueta.pack()

                    i=90
                    k=101
                    
                    T1=T[i:k]
                    T1 = T1.replace(':', '.').replace(' ', '.').replace('\n', '.').replace('\r', '.')
                    etiqueta=tkinter.Label(FramaVentana,text=" Direccion IP destino:     "+T1+"       ",font=fontStyle2)
                    etiqueta.config(bg="GhostWhite")
                    etiqueta.pack()


                    
                    
                    
            
               
            
           
            else:
                etiqueta=tkinter.Label(FramaVentana,text="                                PROTOCOLO EN DESARROLLO                                ",font=fontStyle2)
                etiqueta.config(bg="salmon")
                etiqueta.pack()
            x=x+1
            



    
            
            


            
            
#-----------------------------------------------OPCIONES-------------------------------------------

ayuda = Menu(menu, tearoff=0)
menu.add_cascade(label="ANALIZAR DESDE PC", menu=ayuda)
ayuda.add_command(label = "ANALIZAR CABECERA ETHERNET",command = CABEZERA_ETHERNET)


ayuda.add_command(label = "ANALIZAR CABEZERA IPV4",command = CABEZERA_IPV4)



wifi = Menu(menu, tearoff=0)
menu.add_cascade(label="WI-FI", menu=wifi)

salir = Menu(menu, tearoff=0)
menu.add_cascade(label="SALIR", menu=salir)
salir.add_command(label = "FINALIZAR",command = SALIR)

NewWindow.mainloop()
