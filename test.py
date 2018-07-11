#-*- coding: utf-8 -*-
#class resistance
class resistance(object):
        def __init__(self):
                self.root = Tk()
                self.root.title('code des couleurs')
                self.dessineresistance()
                Label(self.root, text='entre un valeur:').grid(row =2, column =1, columnspan =3)
                Button(self.root, text='montrer', command=self.changecouleurs).grid(row=3, column=1)
                Button(self.root, text='quitter', command=self.root.destroy).grid(row=3, column=3)
                self.entree = Entry(self.root, width=14)
                self.entree.grid(row=3, column=2)
                self.cc = ['black','brown','red','orange','yellow','green','blue','purple','grey','white']
                self.root.mainloop()
        def dessineresistance(self):
                self.can = Canvas(self.root, width=250, height =100, bg='ivory')
                self.can.grid(row=1, column=1, columnspan=3, padx=5,pady=5)
                self.can.create_line(10, 50, 240, 50, width =5)
                self.can.create_rectangle(65, 30, 185, 70, fill ='lightgrey', width =2)
                self.ligne = []
                for x in range(85,150,24):
                        self.ligne.append(self.can.create_rectangle(x,30,x+12,70,fill='black',width=0))
        def changecouleurs(self):
                self.vlch = self.entree.get()
                try:
                        self.v = float(self.vlch)
                except ValueError:
                        err = 1
                else:
                        err = 0
                if self.v<9 or self.v>1e11 or err == 1:
                        self.signalerreur()
                else:
                        self.li = [0]*3
                        logv = int(log10(self.v))
                        ordr = 10**logv
                        self.li[0] = int(self.v/ordr)
                        de = self.v/ordr - self.li[0]
                        self.li[1] = int(de*10+0.5)
                        self.li[2] = logv -1
                for n in range(3):
                        self.can.itemconfigure(self.ligne[n], fill=self.cc[self.li[n]])
        def signalerreur(self):
                self.entree.configure(bg ='red')
                self.root.after(1000, self.videntree)
        def videntree(self):
                self.entree.configure(bg ='white')
                self.entree.delete(0, END)
#execution
if __name__ == '__main__':
        from tkinter import *
        from math import log10
        f = resistance()
