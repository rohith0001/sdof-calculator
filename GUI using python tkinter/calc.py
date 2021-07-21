from tkinter import *
import numpy as np
import math as mt
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  NavigationToolbar2Tk)
import matplotlib.pyplot as plt

def mainfunc2():

    def mainfunc():
        def func():
            mylabel=Label(root,text="Cicular frequency [wn] =")
            mylabel.grid(row=14,column=0)
            mylabel=Label(root,text=round(wn,3))
            mylabel.grid(row=14,column=1)
            mylabel=Label(root,text=" rad/s ")
            mylabel.grid(row=14,column=2)

            mylabel=Label(root,text="Natural frequency [fn] =")
            mylabel.grid(row=15,column=0)
            mylabel=Label(root,text=round(fn,3))
            mylabel.grid(row=15,column=1)
            mylabel=Label(root,text=" Hz ")
            mylabel.grid(row=15,column=2)

            mylabel=Label(root,text="Period of oscilattion [T] =")
            mylabel.grid(row=16,column=0)
            mylabel=Label(root,text=round(ti,3))
            mylabel.grid(row=16,column=1)
            mylabel=Label(root,text=" seconds ")
            mylabel.grid(row=16,column=2)

            mylabel=Label(root,text="Critical damping [cc] =")
            mylabel.grid(row=17,column=0)
            mylabel=Label(root,text=round(Cc,3))
            mylabel.grid(row=17,column=1)
            mylabel=Label(root,text=" N s/m ")
            mylabel.grid(row=17,column=2)

            mylabel=Label(root,text="Damping factor [c] =")
            mylabel.grid(row=18,column=0)
            mylabel=Label(root,text=round(C,3))
            mylabel.grid(row=18,column=1)
            mylabel=Label(root,text=" N s/m")
            mylabel.grid(row=18,column=2)

            mylabel=Label(root,text="Damped natural angular frequency [wd] =")
            mylabel.grid(row=19,column=0)
            mylabel=Label(root,text=round(wd,3))
            mylabel.grid(row=19,column=1)
            mylabel=Label(root,text=" rad/s ")
            mylabel.grid(row=19,column=2)

            mylabel=Label(root,text="Damped natural frequency [fd]  =")
            mylabel.grid(row=20,column=0)
            mylabel=Label(root,text=round(fd,3))
            mylabel.grid(row=20,column=1)
            mylabel=Label(root,text=" Hz ")
            mylabel.grid(row=20,column=2)

            mylabel=Label(root,text="Quality factor [Q]  =")
            mylabel.grid(row=21,column=0)
            mylabel=Label(root,text=round(q,3))
            mylabel.grid(row=21,column=1)
            mylabel=Label(root,text="--")
            mylabel.grid(row=21,column=2)

            mylabel=Label(root,text="Transmissiblity [TR]  =")
            mylabel.grid(row=22,column=0)
            mylabel=Label(root,text=round(tr,3))
            mylabel.grid(row=22,column=1)
            mylabel=Label(root,text="--")
            mylabel.grid(row=22,column=2)



        mass=(entr_m.get())
        try:
            mass= float(mass)
        except:
            mass=1
        if m_clicked.get()=='g':
            mass=mass/1000
        elif m_clicked.get()=='lb':
            mass=mass/2.20462

        stif=(entr_k.get())
        try:
            stif=float(stif)
        except:
            stif=3600

        damr=(entr_dr.get())
        try:
            damr=float(damr)
        except:
            damr=0.1

        if k_clicked.get()=='N/mm':
            stif=stif*1000
        elif k_clicked.get()=='lbf/in':
            stif = stif*100*4.44822/2.54

        try:
            freq=(entr_h.get())
            freq=float(freq)*2*mt.pi
        except:
            freq=10

        wn=mt.sqrt(stif/mass)
        fn=1/(2*mt.pi)*wn
        ti=(1/fn)
        Cc=2*mt.sqrt(mass*stif)
        C=damr*Cc
        if damr<=1:
            wd=wn*mt.sqrt(1-mt.pow(damr,2))
            fd=wd/(2*mt.pi)
        else:
            wd=np.nan
            fd=np.nan

        if damr == 0:
            q = 'Infinity'
        else:
            q = 1/(2*damr)

        if aaaa==1:
            a = 1+(np.power(2*damr*freq/wn,2))
            b = np.power((1-(np.power((freq/wn),2))),2)
            c1 = np.power(2*damr*freq/wn,2)
            tr = np.power(a/(b+c1),0.5)
            freqratioreal=freq/fn
            m11=np.power((1-(freqratioreal*freqratioreal)),2)
            m22=np.power((2*freqratioreal*damr),2)
            M22=1/(np.power((m11+m22),0.5))
            p22=mt.degrees(np.arctan(2*freqratioreal*damr/(1-(freqratioreal*freqratioreal))))
            if p22<=0:
                p22=p22+180
        else:
            tr = 0.00





        func()
        if aaaa == 0:
            fig = Figure(figsize = (5,3))
            plot1 = fig.add_subplot()
            plot1.loglog(5, 3)
            plot1.set_title('Transmissiblity vs Frequency Ratio Graph(log-log)',fontsize=8)
            plot1.set_ylabel('Transmissiblity [TR]',fontsize=8)
            canvas = FigureCanvasTkAgg(fig,master = root)
            canvas.get_tk_widget().grid(row =36,column=0)
            samp2.grid(row =37,column=0)

            fig = Figure(figsize = (5,3))
            plot2 = fig.add_subplot()
            plot2.loglog(5,3)
            plot2.set_title('Magnification Factor vs Frequency Ratio Graph(log-log)',fontsize=8)
            plot2.set_ylabel('Magnification Factor (M)',fontsize=8)
            canvas = FigureCanvasTkAgg(fig,master = root)
            canvas.get_tk_widget().grid(row =36,column=1)
            samp3.grid(row =37,column=1)

            fig = Figure(figsize = (5,3))
            plot3 = fig.add_subplot()
            plot3.plot(5,3)
            plot3.set_title('Phase angle vs Frequency Ratio Graph',fontsize=8)
            plot3.set_ylabel(' phase angle ϕ',fontsize=8)
            canvas = FigureCanvasTkAgg(fig,master = root)
            canvas.get_tk_widget().grid(row =36,column=2)
            samp4.grid(row =37,column=2)

        elif aaaa==1:
            freq1=[]
            freq4=[]
            tr1=[]
            M1=[]
            p1=[]
            freq3 = 0.01
            for i in range(1,10000000):
                freqratio=freq3/wn
                if freqratio >= 0.099:
                    freq1.append(freqratio)
                a = 1+(np.power(2*damr*freq3/wn,2))
                b = np.power((1-(np.power((freq3/wn),2))),2)
                c1 = np.power(2*damr*freq3/wn,2)
                tr2 = np.power(a/(b+c1),0.5)

                m1=np.power((1-(freqratio*freqratio)),2)
                m2=np.power((2*freqratio*damr),2)
                M2=1/(np.power((m1+m2),0.5))

                p2=mt.degrees(np.arctan(2*freqratio*damr/(1-(freqratio*freqratio))))

                if p2<=0:
                    p1.append(p2+180)
                else:
                    p1.append(p2)

                if freqratio >= 0.099:
                    M1.append(M2)
                    tr1.append(tr2)


                freq3 = 0.01+freq3
                freq4.append(freqratio)
                if int(freqratio) >= 3:
                    break



            fig = Figure(figsize = (5,3))
            plot1 = fig.add_subplot()
            plot1.loglog(freq1, tr1,c='r')
            plot1.grid(which='major', linestyle='-', linewidth='0.5')
            plot1.grid(which='minor', linestyle='-', linewidth='0.5')
            plot1.set_title('Transmissiblity vs Frequency Ratio Graph(log-log)',fontsize=8)
            plot1.set_ylabel('Transmissiblity [TR]',fontsize=8)
            canvas = FigureCanvasTkAgg(fig,master = root)
            canvas.get_tk_widget().grid(row =36,column=0)
            samp2.grid(row =37,column=0)

            fig = Figure(figsize = (5,3))
            plot2 = fig.add_subplot()
            plot2.plot(freq1, M1,c='b')
            if freqratioreal<=3:
                plot2.plot(freqratioreal,M22,'+',color='black')
                plot2.annotate("  operating value of f/fn", (freqratioreal,M22))
            plot2.grid(which='major', linestyle='-', linewidth='0.5')
            plot2.grid(which='minor', linestyle='-', linewidth='0.5')
            plot2.set_title('Magnification Factor vs Frequency Ratio Graph',fontsize=8)
            plot2.set_ylabel('Magnification Factor (M)',fontsize=8)
            canvas = FigureCanvasTkAgg(fig,master = root)
            canvas.get_tk_widget().grid(row =36,column=1)
            samp3.grid(row =37,column=1)

            fig = Figure(figsize = (5,3))
            plot3 = fig.add_subplot()
            plot3.plot(freq4, p1,c='g')
            if freqratioreal<=3:
                plot3.plot(freqratioreal,p22,'+',color='black')
                plot3.annotate("  operating value of f/fn", (freqratioreal,p22))
            plot3.grid(which='major', linestyle='-', linewidth='0.5')
            plot3.grid(which='minor', linestyle='-', linewidth='0.5')
            plot3.set_xticks([0,0.5,1,1.5,2,2.5,3])
            plot3.set_yticks([0,30,60,90,120,150,180])
            plot3.set_title('Phase angle vs Frequency Ratio Graph',fontsize=8)
            plot3.set_ylabel(' phase angle ϕ',fontsize=8)
            canvas = FigureCanvasTkAgg(fig,master = root)
            canvas.get_tk_widget().grid(row =36,column=2)
            samp4.grid(row =37,column=2)



    select=int(r.get())

    if select == 1:

        mylabel=Label(root,text="Parameters:......................",font =("Courier", 13))
        mylabel.grid(row=2,column=0)

        mylabel_m=Label(root,text="* Mass [m]:\n(Default value = 1 unit)")
        mylabel_m.grid(row=3,column=0)
        entr_m=Entry(root)
        entr_m.grid(row=3,column=1)

        m_options=['kg','g','lb']
        m_clicked=StringVar()
        m_clicked.set(m_options[0])
        drop=OptionMenu(root,m_clicked,*m_options)
        drop.grid(row=3,column=2)

        mylabel_k=Label(root,text="* Spring rate (Stiffness) [k]:\n(Default value = 3600 unitS)" )
        mylabel_k.grid(row=4,column=0)
        entr_k=Entry(root)
        entr_k.grid(row=4,column=1)

        k_options=['N/m','N/mm','lbf/in']
        k_clicked=StringVar()
        k_clicked.set(k_options[0])
        drop=OptionMenu(root,k_clicked,*k_options)
        drop.grid(row=4,column=2)

        mylabel_dr=Label(root,text="* Damping ratio (coefficient) [ζ]:\n(Default value = 0.1)" )
        mylabel_dr.grid(row=5,column=0)
        entr_dr=Entry(root)
        entr_dr.grid(row=5,column=1)

        freqst1=Label(root,text = "...............Harmonic input..............\n ...........frequency...........")
        freqst1.grid(row =6,column=0)
        freqst2=Label(root,text = "input frequency = 0",bg="white")
        freqst2.grid(row =6,column=1)
        freqst3=Label(root,text = "---------------------")
        #freqst3.grid(row =6,column=2)



        mylabel=Label(root,text="Result:.....................give calculate>>>>",font =("Courier", 13))
        mylabel.grid(row=7,column=0)
        aaaa=0
        bbbb=0
        samp2=Label(root,text = "Frequency ratio (Ω/fn)")
        samp3=Label(root,text = "Frequency ratio (Ω/fn)")
        samp4=Label(root,text = "Frequency ratio (Ω/fn)")

        mybutton2=Button(root,text="Calculate ", fg="red",command=mainfunc)
        mybutton2.grid(row=7,column=1)
        return

    elif select == 2:

        mylabel=Label(root,text="Parameters:......................",font =("Courier", 13))
        mylabel.grid(row=2,column=0)

        mylabel_m=Label(root,text="* Mass [m]:\n(Default value = 1 unit)")
        mylabel_m.grid(row=3,column=0)
        entr_m=Entry(root)
        entr_m.grid(row=3,column=1)

        m_options=['kg','g','lb']
        m_clicked=StringVar()
        m_clicked.set(m_options[0])
        drop=OptionMenu(root,m_clicked,*m_options)
        drop.grid(row=3,column=2)

        mylabel_k=Label(root,text="* Spring rate (Stiffness) [k]:\n(Default value = 3600 unit)" )
        mylabel_k.grid(row=4,column=0)
        entr_k=Entry(root)
        entr_k.grid(row=4,column=1)

        k_options=['N/m','N/mm','lbf/in']
        k_clicked=StringVar()
        k_clicked.set(k_options[0])
        drop=OptionMenu(root,k_clicked,*k_options)
        drop.grid(row=4,column=2)

        mylabel_dr=Label(root,text="* Damping ratio (coefficient) [ζ]:\n(Default value = 0.1)" )
        mylabel_dr.grid(row=5,column=0)
        entr_dr=Entry(root)
        entr_dr.grid(row=5,column=1)

        mylabel_h=Label(root,text="* Harmonic input frequency [Ω]:\n(Default value = 10 Hz)")
        mylabel_h.grid(row=6,column=0)
        entr_h=Entry(root)
        entr_h.grid(row=6,column=1)

        h_options=['Hz']
        h_clicked=StringVar()
        h_clicked.set(h_options[0])
        drop=OptionMenu(root,h_clicked,*h_options)
        drop.grid(row=6,column=2)

        mylabel=Label(root,text="Result:.....................give calculate>>>>",font =("Courier", 13))
        mylabel.grid(row=7,column=0)

        aaaa=1
        bbbb=0

        mybutton=Button(root,text="Calculate ", fg="red",command=mainfunc)
        mybutton.grid(row=7,column=1)
        samp2=Label(root,text = "Frequency ratio (Ω/fn)")
        samp3=Label(root,text = "Frequency ratio (Ω/fn)")
        samp4=Label(root,text = "Frequency ratio (Ω/fn)")
        return

root=Tk()
root.geometry("3000x2300")
root.title("SDOF calculator")

mylabel=Label(root,text="Single Degree of Freedom Vibration Calculator:",font =("Courier", 16),bg="beige")
mylabel.grid(row=0,column=1)

samp=Label(root).grid(row =6,column=0)

r=IntVar()
R1=Radiobutton(root,text="Free vibration",font =("Courier", 13),variable=r,value=1).grid(row =1,column=0)
R2=Radiobutton(root,text="Forced vibration",font =("Courier", 13),variable=r,value=2).grid(row =1,column=1)

mybutton=Button(root,text="<----SUBMIT", fg="red",command=mainfunc2)
mybutton.grid(row=1,column=2)

root.mainloop()
