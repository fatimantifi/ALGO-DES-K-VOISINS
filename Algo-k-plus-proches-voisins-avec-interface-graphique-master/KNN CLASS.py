"""Presentation Du Projet : Simulation de réfrigérateur a l'aide d'un algorithme style 'k plus proches voisins'.
Cette algo a pour but de comparer les réfrigérateurs d'une population par rapport a la votre, votre frigo etant la liste que vous entrerez.
Pour lancer la class veuillez entrer en argument :
-Le nombre de k voisins voulu (entre 1,10)
-Une liste avec les ingredients voulu qui servira de comparé (ingredient=['sauces','yaourts','fruits','legumes','viandes','eau','soda','glace','fromage','lait'])
-Le nombre de frigo demandé (max 10)
Puis lancer la fonction stockage()
"""


import random

from tkinter import *

path=r"C:/Users/maroc/Desktop/KNN"

class KNN:


    def __init__(self,k,temoin,num):
        self.num=num
        self.ingredient=['sauces','yaourts','fruits','legumes','viandes','eau','soda','glace','fromage','lait']
        self.prsn=[]
        self.temoin=temoin
        self.xvegetal=[140, 440,740,1040,1340,140,440,740,1040,1340]
        self.yvegetal=[280,280,280,280,280,780,780,780,780,780]
        self.xketchup=[250,550,850,1150,1450,250,550,850,1150,1450]
        self.yketchup=[290,290,290,290,290,790,790,790,790,790]
        self.xcoca=[200,500,800,1100,1400,200,500,800,1100,1400]
        self.ycoca=[290,290,290,290,290,790,790,790,790,790]
        self.xviande=[135,435,735,1035,1335,135,435,735,1035,1335]
        self.yviande=[330,330,330,330,330,830,830,830,830,830]
        self.xyogurt=[230,530,830,1130,1430,230,530,830,1030,1330]
        self.yyogurt=[330,330,330,330,330,830,830,830,830,830]
        self.X=[100,400,700,1000,1300,100,400,700,1000,1300]
        self.Y=[100,100,100,100,100,600,600,600,600,600]
        self.xmot=[200,500,800,1100,1400,200,500,800,1100,1400]
        self.ymot=[70,70,70,70,70,570,570,570,570,570]
        self.xmilk=[185,485,785,1085,1385,185,485,785,1085,1385]
        self.ymilk=[170,170,170,170,703,703,703,703,703,703]
        self.xhagen=[235,535,835,1135,1435,235,535,835,1135,1435]
        self.yhagen=[120,120,120,120,120,635,635,635,635,635]
        self.xcheese=[130,430,730,1030,1330,130,430,730,1030,1330]
        self.ycheese=[170,170,170,170,170,700,700,700,700,700]
        self.xfru=[185,485,785,1085,1385,185,485,785,1085,1385]
        self.yfru=[120,120,120,120,120,635,635,635,635,635]
        self.xteille=[130,430,730,1030,1330,130,430,730,1030,1330]
        self.yteille=[120,120,120,120,120,630,630,630,630,630]
        self.vide=[]
        self.legumes=''
        self.sauces=''
        self.soda=''
        self.steak=''
        self.yaourt= ''
        self.image= ''
        self.app = Tk()
        self.k=k
        self.eau=''
        self.fromage=''
        self.glace=''
        self.fruits=''
        self.lait=''
        self.image=''



    def gens(self):
        if self.num>10:
            print("nombres de frigo non supportés")
        var = 1
        secu=[]
        self.prsn.clear()
        for i in range(self.num):
            a = random.randint(0,len(self.ingredient)-1)
            while a == 0:
                a = random.randint(0,len(self.ingredient)-1)
            b=self.frigo(a)
            if b in secu:
                b=self.frigo(a)
            b.append(var)
            var = var +1
            self.prsn.append(b)
            secu.append(b)


    def frigo(self,num):
        L=[]
        cuse=[]
        for i in range (num):
            a=random.randint(0,len(self.ingredient)-1)
            b=self.ingredient[a]
            if b in L:
                a=random.randint(0,len(self.ingredient)-1)
                b=self.ingredient[a]
            else:
                L.append(b)
        return L


    def knn(self):
        vide=[]
        for elt in self.temoin:
            for i in range (len(self.prsn) - 1):
                a = self.prsn[i]
                for elts in a:
                    if  elt == elts:
                        if a not in vide:
                            vide.append(a)
        c=len(vide)
        dede=''
        for i in range(c):
            d=vide[i]
            x=d[-1]
            dede=dede+str(x)+","
        if len(dede) == 2:
            print("le frigo similaire est le numero: "+dede)
        if len(dede) > 2 and len(dede)<10:
            print('les frigos similaires ont le numero:'+dede+"(ordre du plus proches au plus éloignés )")
        if vide==[]:
            print('aucun frigo similaire')
        return vide


    def autre(self):
        zzz= []
        for item in self.prsn:
            if item not in self.vide:
                zzz.append(item)
        return zzz


    def voisin(self):
        if self.k > len(self.vide):
            print("vous avez dépassé le nombre d'element de la liste")
        else:
            T=self.vide[:self.k]
            beto=''
            for elt in T:
                q = elt[-1]
                beto = beto + str(q) + ','
            print("les "+ " " + str(self.k)+" "+" plus proches voisins sont les numeros " + beto)


    def affiche(self):
        if len(self.prsn) > 10:
            print()
        elif len(self.prsn) <= 10:
            for i in range (len(self.prsn)):
                btn = Button(self.app,image=self.image)
                btn.pack()
                btn.place(x=self.X[i],y=self.Y[i])


    def test(self):
        if len(self.vide) >10:
            print()
        elif len(self.vide)<=10:
            for a in range(len(self.vide)):
                for o in range (len(self.vide[a])):
                    if self.vide[a][o]=='legumes':
                        leg= Button(self.app,image=self.legumes)
                        leg.pack()
                        leg.place(x=self.xvegetal[a],y=self.yvegetal[a])
                    if self.vide[a][o]=='sauces':
                        sauc= Button(self.app,image=self.sauces)
                        sauc.pack()
                        sauc.place(x=self.xketchup[a],y=self.yketchup[a])
                    if self.vide[a][o]=='viandes':
                        stak=Button(self.app,image=self.steak)
                        stak.pack()
                        stak.place(x=self.xviande[a],y=self.yviande[a])
                    if self.vide[a][o]=='yaourts':
                        yaa = Button(self.app,image=self.yaourt)
                        yaa.pack()
                        yaa.place(x=self.xyogurt[a],y=self.yyogurt[a])
                    if self.vide[a][o]=='soda':
                        sod= Button(self.app,image=self.soda)
                        sod.pack()
                        sod.place(x=self.xcoca[a],y=self.ycoca[a])
                    if self.vide[a][o]=="eau":
                        teille = Button(self.app,image=self.eau)
                        teille.pack()
                        teille.place(x=self.xteille[a],y=self.yteille[a])
                    if self.vide[a][o] =='fromage':
                        cheese = Button(self.app,image=self.fromage)
                        cheese.pack()
                        cheese.place(x=self.xcheese[a],y=self.ycheese[a])
                    if self.vide[a][o] =='fruits':
                        fru= Button(self.app,image=self.fruits)
                        fru.pack()
                        fru.place(x=self.xfru[a],y=self.yfru[a])
                    if self.vide[a][o] == 'glace':
                        hagen=Button(self.app,image=self.glace)
                        hagen.pack()
                        hagen.place(x=self.xhagen[a],y=self.yhagen[a])
                    if self.vide[a][o] =='lait':
                        milk=Button(self.app,image=self.lait)
                        milk.pack()
                        milk.place(x=self.xmilk[a],y=self.ymilk[a])
        self.vide.pop(-1)


    def mot(self):
        if len(self.vide) >10:
            print()
        elif len(self.vide)<=10:
            for i in range (len(self.vide)+1):
                mot=Button(self.app,text=str(i+1))
                mot.pack()
                mot.place(x=self.xmot[i],y=self.ymot[i])

    def stockage(self):
        self.app.title("KNN")
        screen_x=int(self.app.winfo_screenwidth())
        screen_y=int(self.app.winfo_screenheight())
        window_x=1920
        window_y=1080
        posX= ( screen_x // 2) - (window_x // 2)
        posY= ( screen_y // 2) - (window_y // 2)
        geo="{}x{}+{}+{}".format(window_x,window_y,posX,posY)
        self.app.geometry(geo)
        self.app.configure(bg="#8c7ae6")
        self.eau=PhotoImage(file=path+"/eau.png")
        self.fromage=PhotoImage(file=path+"/fromage.png")
        self.fruits=PhotoImage(file=path+"/fruits.png")
        self.glace=PhotoImage(file=path+"/glace.png")
        self.lait=PhotoImage(file=path+"/lait.png")
        self.legumes=PhotoImage(file=path+"/legumes.png")
        self.sauces=PhotoImage(file=path+"/sauces.png")
        self.soda=PhotoImage(file=path+"/soda.png")
        self.steak=PhotoImage(file=path+"/steak.png")
        self.yaourt=PhotoImage(file=path+"/yaourt.png")
        self.image= PhotoImage(file=path+"/frigo.png")
        self.gens()
        self.vide = self.knn()
        sss = self.autre()
        self.vide.extend(sss)
        self.affiche()
        self.test()
        self.voisin()
        self.mot()
        self.app.mainloop()





























