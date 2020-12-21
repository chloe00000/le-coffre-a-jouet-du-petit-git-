# Créé par charr, le 12/11/2020 en Python 3.7
#importation d'une bibliothèque graphique
#test
from graphics import *

#ouverture de la fenêtre graphique de 600 pixels par 400
f=init_graphics(600,400)

#exercice 1
def draw_quadrilatère(p1,p2,p3,p4,coul,f):
    draw_line(p1,p2,coul,f)
    draw_line(p2,p3,coul,f)
    draw_line(p3,p4,coul,f)
    draw_line(p4,p1,coul,f)


#draw_quadrilatère((0,0),(400,200),(400,300),(200,200),rouge,f)


#exercice2
def draw_circle_color(rayon,f):
    centre=wait_clic()
    draw_fill_circle(centre,rayon,rouge,f)
    p=wait_clic()
    while distance(centre,p)<rayon:
        if distance(centre,p)<rayon:
            draw_fill_circle(centre,rayon,blanc,f)
            p=wait_clic()
            if distance(centre,p)<rayon:
                draw_fill_circle(centre,rayon,bleu,f)
                p=wait_clic()
                if distance(centre,p)<rayon:
                    draw_fill_circle(centre,rayon,rouge,f)
                    p=wait_clic()
        else:
            wait_escape(f)







draw_circle_color(100,f)

#exercice3
def draw_line_H(delta,coul,f):
    y=0
    while y<=400:
        p1=(0,y)
        p2=(600,y)
        draw_line(p1,p2,coul,f)
        y=y+delta


#draw_line_H(100,rouge,f)

def draw_line_V(delta, coul, f):
    x=0
    while x<=600:
        p1=(x,0)
        p2=(x,400)
        draw_line(p1,p2,coul,f)
        x=x+delta

#draw_line_V(100,rouge,f)

def draw_quadrillage(delta,coul,f):
    draw_line_H(delta,coul,f)
    draw_line_V(delta,coul,f)


#draw_quadrillage(100,rouge,f)

#exercice4
def dessine_couleurs(f):
    draw_fill_rectangle((0,350),(50,400),rouge,f)
    draw_fill_rectangle((100,350),(150,400),vert,f)
    draw_fill_rectangle((200,350),(250,400),bleu,f)
    draw_fill_rectangle((300,350),(350,400),blanc,f)

#dessine_couleurs(f)


#on attend un appui sur echap pour terminer
wait_escape(f)

#fermeture de la fenêtre graphique
quit_graphics()