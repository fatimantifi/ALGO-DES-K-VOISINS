import random
from tkinter import *

ingredient=['sauces','yaourts','fruits','legumes','viandes','eau','soda','glace','fromage','lait']

temoin=['sauces','yaourts','fruits']

prsn=[]

path=r"C:/Users/maroc/Desktop/KNN"

def gens(num):
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
    if len(dede) > 2:
        print('les frigos similaires ont le numero:'+dede)
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


gens(18)
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


image= PhotoImage(file=path+"/frigo.png")
btn = Button(app,image=image)
btn.pack()
btn.place(x=400,y=100)
X=[100,400,700,1000,1300,100,400,700,1000,1300,]
Y=[100,100,100,100,100,600,600,600,600,600,]
for i in range (10):
    btn = Button(app,image=image)
    btn.pack()
    btn.place(x=X[i],y=Y[i])


xteille=[130,430,730,1030,1330,130,430,730,1030,1330]
yteille=[120,120,120,120,120,630,630,630,630,630]
eau=PhotoImage(file=path+"/eau.png")
teille = Button(app,image=eau)
teille.pack()
teille.place(x=1330,y=630)


xcheese=[130,430,730,1030,1330,130,430,730,1030,1330]
ycheese=[170,170,170,170,170,700,700,700,700,700]
fromage=PhotoImage(file=path+"/fromage.png")
cheese = Button(app,image=fromage)
cheese.pack()
cheese.place(x=1330,y=700)


xfru=[185,485,785,1085,1385,185,485,785,1085,1385]
yfru=[120,120,120,120,120,635,635,635,635]
fruits=PhotoImage(file=path+"/fruits.png")
fru= Button(app,image=fruits)
fru.pack()
fru.place(x=1385,y=635)


xhagen=[235,535,835,1135,1435,235,535,835,1135,1435]
yhagen=[120,120,120,120,120,635,635,635,635,635]
glace=PhotoImage(file=path+"/glace.png")
hagen=Button(app,image=glace)
hagen.pack()
hagen.place(x=1435,y=635)


xmilk=[185,485,785,1085,1385,185,485,785,1085,1385]
ymilk=[170,170,170,170,670,703,703,703,703]
lait=PhotoImage(file=path+"/lait.png")
milk=Button(app,image=lait)
milk.pack()
milk.place(x=1385,y=703)


xvegetal=[140, 440,740,1040,1340,140,440,740,1040,1340]
yvegetal=[280,280,280,280,280,780,780,780,780,780]
legumes=PhotoImage(file=path+"/legumes.png")
vegetal=Button(app,image=legumes)
vegetal.pack
vegetal.place(x=1340,y=780)


xketchup=[250,550,850,1150,1450,250,550,850,1150,1450]
yketchup=[290,290,290,290,290,790,790,790,790,790]
sauces=PhotoImage(file=path+"/sauces.png")
ketchup=Button(app,image=sauces)
ketchup.pack()
ketchup.place(x=1450,y=790)


xcoca=[200,500,800,1100,1400,200,500,800,1100,1400]
ycoca=[290,290,290,290,290,790,790,790,790,790]
soda=PhotoImage(file=path+"/soda.png")
coca=Button(app,image=soda)
coca.pack()
coca.place(x=1400,y=790)


xviande=[135, 435,735,1035,1335,135,435,735,1035,1335]
yviande=[330,330,330,330,330,830,830,830,830,830]
steak=PhotoImage(file=path+"/steak.png")
viande=Button(app,image=steak)
viande.pack()
viande.place(x=13535,y=830)


xyogurt=[230, 530,830,1130,1430,230,530,830,1030,1330]
yyogurt=[330, 330,330,330,330,830,830,830,830,830]
yaourt=PhotoImage(file=path+"/yaourt.png")
yogurt=Button(app,image=yaourt)
yogurt.pack()
yogurt.place(x=1330,y=830)


app.mainloop()