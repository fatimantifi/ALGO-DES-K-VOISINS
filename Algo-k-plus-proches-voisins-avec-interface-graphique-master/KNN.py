""" Presentation Du Projet : Simulation de réfrigérateur a l'aide d'un algorithme style 'k plus proches voisins'//
Cette algo a pour but de comparer les réfrigérateurs d'une population par rapport a la votre, votre frigo etant la liste nommé: témoin[]// Pour afficher les réfrigérateurs qui sont comparés au votre pressez f5 puis appelez la liste prsn[], ces réfrigérateurs seront numérotés selon le nombre de 'gens' que vous avez choisi a la ligne 94 dans la fonction gens(x) (choisissez un nombre entre 1 et 10 car seulemnt cette tranche est represntable avec tkinter)et en deuxieme arguments de la ligne 258 le nombre de k voisins voulu (en fonction de celui entré dans gens())
"""

import random
from tkinter import *


ingredient=['sauces','yaourts','fruits','legumes','viandes','eau','soda','glace','fromage','lait']

temoin=['sauces','yaourts','fruits']

prsn=[]

path=r"C:/Users/maroc/Desktop/KNN"

def gens(num):
    if num>10:
        print("nombres de frigo non supportés")
    var = 1
    secu=[]
    prsn.clear()
    for i in range(num):
        a = random.randint(0,len(ingredient)-1)
        while a == 0:
            a = random.randint(0,len(ingredient)-1)
        b=frigo(a)
        if b in secu:
            b=frigo(a)
        b.append(var)
        var = var +1
        prsn.append(b)
        secu.append(b)


def frigo(num):
    L=[]
    cuse=[]
    for i in range (num):
        a=random.randint(0,len(ingredient)-1)
        b=ingredient[a]
        if b in L:
            a=random.randint(0,len(ingredient)-1)
            b=ingredient[a]
        else:
            L.append(b)
    return L


def knn(temoin):
    vide=[]
    for elt in temoin:
        for i in range (len(prsn) - 1):
            a = prsn[i]
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


def autre(prsn,vide):
    zzz= []
    for item in prsn:
        if item not in vide:
            zzz.append(item)
    return zzz


def voisin(vide,K):
    if K > len(vide):
        print("vous avez dépassé le nombre d'element de la liste")
    else:
        T=vide[:K]
    beto=''
    for elt in T:
        q = elt[-1]
        beto = beto + str(q) + ','
    print("les "+ " " + str(K)+" "+" plus proches voisins sont les numeros " + beto)


gens(10)
vide = knn(temoin)
sss = autre(prsn,vide)
vide.extend(sss)


app = Tk()
app.title("KNN")
screen_x=int(app.winfo_screenwidth())
screen_y=int(app.winfo_screenheight())
window_x=1920
window_y=1080
posX= ( screen_x // 2) - (window_x // 2)
posY= ( screen_y // 2) - (window_y // 2)
geo="{}x{}+{}+{}".format(window_x,window_y,posX,posY)
app.geometry(geo)
app.configure(bg="#8c7ae6")


xteille=[130,430,730,1030,1330,130,430,730,1030,1330]
yteille=[120,120,120,120,120,630,630,630,630,630]
eau=PhotoImage(file=path+"/eau.png")



xcheese=[130,430,730,1030,1330,130,430,730,1030,1330]
ycheese=[170,170,170,170,170,700,700,700,700,700]
fromage=PhotoImage(file=path+"/fromage.png")



xfru=[185,485,785,1085,1385,185,485,785,1085,1385]
yfru=[120,120,120,120,120,635,635,635,635,635]
fruits=PhotoImage(file=path+"/fruits.png")



xhagen=[235,535,835,1135,1435,235,535,835,1135,1435]
yhagen=[120,120,120,120,120,635,635,635,635,635]
glace=PhotoImage(file=path+"/glace.png")



xmilk=[185,485,785,1085,1385,185,485,785,1085,1385]
ymilk=[170,170,170,170,703,703,703,703,703,703]
lait=PhotoImage(file=path+"/lait.png")



xvegetal=[140, 440,740,1040,1340,140,440,740,1040,1340]
yvegetal=[280,280,280,280,280,780,780,780,780,780]
legumes=PhotoImage(file=path+"/legumes.png")


sauces=PhotoImage(file=path+"/sauces.png")
xketchup=[250,550,850,1150,1450,250,550,850,1150,1450]
yketchup=[290,290,290,290,290,790,790,790,790,790]


xcoca=[200,500,800,1100,1400,200,500,800,1100,1400]
ycoca=[290,290,290,290,290,790,790,790,790,790]
soda=PhotoImage(file=path+"/soda.png")



xviande=[135, 435,735,1035,1335,135,435,735,1035,1335]
yviande=[330,330,330,330,330,830,830,830,830,830]
steak=PhotoImage(file=path+"/steak.png")



xyogurt=[230, 530,830,1130,1430,230,530,830,1030,1330]
yyogurt=[330, 330,330,330,330,830,830,830,830,830]
yaourt=PhotoImage(file=path+"/yaourt.png")


def test(vide):
    if len(vide) >10:
        print()
    elif len(vide)<=10:
        for a in range(len(vide)):
            for o in range (len(vide[a])):
                if vide[a][o]=='legumes':
                    leg= Button(app,image=legumes)
                    leg.pack()
                    leg.place(x=xvegetal[a],y=yvegetal[a])
                if vide[a][o]=='sauces':
                    sauc= Button(app,image=sauces)
                    sauc.pack()
                    sauc.place(x=xketchup[a],y=yketchup[a])
                if vide[a][o]=='viandes':
                    stak=Button(app,image=steak)
                    stak.pack()
                    stak.place(x=xviande[a],y=yviande[a])
                if vide[a][o]=='yaourts':
                    yaa = Button(app,image=yaourt)
                    yaa.pack()
                    yaa.place(x=xyogurt[a],y=yyogurt[a])
                if vide[a][o]=='soda':
                    sod= Button(app,image=soda)
                    sod.pack()
                    sod.place(x=xcoca[a],y=ycoca[a])
                if vide[a][o]=="eau":
                    teille = Button(app,image=eau)
                    teille.pack()
                    teille.place(x=xteille[a],y=yteille[a])
                if vide[a][o] =='fromage':
                    cheese = Button(app,image=fromage)
                    cheese.pack()
                    cheese.place(x=xcheese[a],y=ycheese[a])
                if vide[a][o] =='fruits':
                    fru= Button(app,image=fruits)
                    fru.pack()
                    fru.place(x=xfru[a],y=yfru[a])
                if vide[a][o] == 'glace':
                    hagen=Button(app,image=glace)
                    hagen.pack()
                    hagen.place(x=xhagen[a],y=yhagen[a])
                if vide[a][o] =='lait':
                    milk=Button(app,image=lait)
                    milk.pack()
                    milk.place(x=xmilk[a],y=ymilk[a])
    vide.pop(-1)

image= PhotoImage(file=path+"/frigo.png")
X=[100,400,700,1000,1300,100,400,700,1000,1300,]
Y=[100,100,100,100,100,600,600,600,600,600,]


def affiche(o):
    if o > 10:
        print()
    elif o <= 10:
        for i in range (o):
            btn = Button(app,image=image)
            btn.pack()
            btn.place(x=X[i],y=Y[i])


def classification(vide):
    i=1
    for item in vide:
        item[-1]=i
        i+=1


xmot=[200,500,800,1100,1400,200,500,800,1100,1400,]
ymot=[70,70,70,70,70,570,570,570,570,570]
def mot(vide):
    if len(vide) >10:
        print()
    elif len(vide)<=10:
        for i in range (len(vide)+1):
            mot=Button(app,text=str(i+1))
            mot.pack()
            mot.place(x=xmot[i],y=ymot[i])






affiche(len(prsn))
test(vide)
voisin(vide,3)
mot(vide)
app.mainloop()