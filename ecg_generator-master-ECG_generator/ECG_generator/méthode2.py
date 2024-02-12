import numpy as np
import matplotlib.pyplot as plt

# on travaille plutôt sur l'EGM, on a déjà fait :
# création du tableau
# création de la sphère
# transmition du signal 
# faut faire :
# delai pour que s'éteigne 
# delai pour que ça se réactive
# différents types de cellules (coefficient à multiplier par 1 si c'est activé et ajouter à amplitude totale)
# géométrie du coeur
#tableau[i][j][k][0] : 1 si c'est une cellule du myocarde (donc activable)
#tableau[i][j][k][1] : 1 si tau vaut 1
#tableau[i][j][k][1] : 2 si tau vaut 1,5
#tableau[i][j][k][2] : 1 si la cellule est activée  


theta =np.pi/9
### création tableau ###
tableau = [[0 for i in range(100)]for i in range(100)]
for i in range(len(tableau)):
    for j in range(len(tableau[0])):
        tableau[i][j] = [[0,0,0] for i in range(100)]
        #tableau[i][j] = [0 for i in range(10)]

for i in range(len(tableau)):
    for j in range(len(tableau[0])):
        for k in range(len(tableau[1])):
            #oreillette droite
            if (i-33)**2 + (j-66)**2 + (k-50)**2 >= 12**2 and (i-33)**2 + (j-66)**2 + (k-50)**2 <= 17**2:
                tableau[i][j][k][0] = 1
                tableau[i][j][k][1] = 1

            #oreillette gauche
            if (i-66)**2 + (j-66)**2 + (k-50)**2 >= 12**2 and (i-66)**2 + (j-66)**2 + (k-50)**2 <= 17**2:
                tableau[i][j][k][0] = 1
                tableau[i][j][k][1] = 1
            #ventricule droit imbriqué dans oreillette droite 
            #if ((i-33)/12)**2 + ((j-34)/20)**2 + ((k-50)/12)**2 >= 1 and ((i-33)/17)**2 + ((j-34)/25)**2 + ((k-50)/17)**2 <= 1 and (i-33)**2 + (j-66)**2 + (k-50)**2 >= 17**2:
            if ((np.sin(theta)*(j-34)+np.cos(theta)*(i-33))/12)**2 + ((np.cos(theta)*(j-34)-np.sin(theta)*(i-33))/20)**2 +((k-50)/12)**2 >=1 and (((np.sin(theta)*(j-34)+np.cos(theta)*(i-33)))/17)**2 +(((np.cos(theta)*(j-34)-np.sin(theta)*(i-33)))/25)**2 +((k-50)/17)**2 <=1 : 
                tableau[i][j][k][0] = 1
                tableau[i][j][k][1] = 2
            #ventricule gauche imbriqué dans oreillette gauche
            #if ((i-66)/12)**2 + ((j-34)/20)**2 + ((k-50)/12)**2 >= 1 and ((i-66)/17)**2 + ((j-34)/25)**2 + ((k-50)/17)**2 <= 1 and (i-66)**2 + (j-66)**2 + (k-50)**2 >= 17**2:
            if (((np.sin(-theta)*(j-34)+np.cos(-theta)*(i-66)))/12)**2 + (((np.cos(-theta)*(j-34)-np.sin(-theta)*(i-66)))/20)**2 +((k-50)/12)**2 >= 1 and (((np.sin(-theta)*(j-34)+np.cos(-theta)*(i-66)))/17)**2 +(((np.cos(-theta)*(j-34)-np.sin(-theta)*(i-66)))/24)**2 +((k-50)/17)**2 <=1 :
                tableau[i][j][k][0] = 1
                tableau[i][j][k][1] = 2
            #bloc oreillette / ventricule droit pour que l'influx aillent bien au milieu des ventricules et pas sur le côté
            #if (i-33)**2 + (j-66)**2 + (k-50)**2 >= 12**2 and (i-33)**2 + (j-66)**2 + (k-50)**2 <= 17**2 and ((i-33)/12)**2 + ((j-34)/20)**2 + ((k-50)/12)**2 >= 1 and ((i-33)/17)**2 + ((j-34)/25)**2 + ((k-50)/17)**2 <= 1 and i < 33 :
            if (((np.sin(theta)*(j-34)+np.cos(theta)*(i-33)))/12)**2 + (((np.cos(theta)*(j-34)-np.sin(theta)*(i-33)))/20)**2 +((k-50)/12)**2 >=1 and (((np.sin(theta)*(j-34)+np.cos(theta)*(i-33)))/17)**2 +(((np.cos(theta)*(j-34)-np.sin(theta)*(i-33)))/25)**2 +((k-50)/17)**2 <=1 and (i-33)**2 + (j-66)**2 + (k-50)**2 >= 12**2 and (i-33)**2 + (j-66)**2 + (k-50)**2 <= 17**2 and i<33:
                tableau[i][j][k][0] = 0
            #bloc oreillette / ventricule gauche pour que l'influx aillent bien au milieu des ventricules et pas sur le côté
            #if (i-66)**2 + (j-66)**2 + (k-50)**2 >= 12**2 and (i-66)**2 + (j-66)**2 + (k-50)**2 <= 17**2 and ((i-66)/12)**2 + ((j-34)/20)**2 + ((k-50)/12)**2 >= 1 and ((i-66)/17)**2 + ((j-34)/25)**2 + ((k-50)/17)**2 <= 1 and (i-66)**2 + (j-66)**2 + (k-50)**2 <= 17**2 and i > 66 :
            if (((np.sin(-theta)*(j-34)+np.cos(-theta)*(i-66)))/12)**2 + (((np.cos(-theta)*(j-34)-np.sin(-theta)*(i-66)))/20)**2 +((k-50)/12)**2 >= 1 and (((np.sin(-theta)*(j-34)+np.cos(-theta)*(i-66)))/17)**2 +(((np.cos(-theta)*(j-34)-np.sin(-theta)*(i-66)))/25)**2 +((k-15)/5)**2 <=1 and (i-66)**2 + (j-66)**2 + (k-50)**2 >= 12**2 and (i-66)**2 + (j-66)**2 + (k-50)**2 <= 17**2 and i>66:
                tableau[i][j][k][0] = 0

### initialisation de la première valeur du tableau : début de l'influx nerveux ###
tableau[18][66][50][2] = 1


### mise à jour des cellules alentours à une cellule activée ###
def propagation(tableau, i, j, k):
    ampl = 0
    cellules_vent_actives = 0
    cellules_oreillettes_actives = 0
    tabl = tableau.copy()
    if tableau[i][j][k][2] == 1:
        if tableau[i-1][j][k][0] == 1:
            tabl[i-1][j][k][2] = 1
            ampl += 1
            if tableau[i-1][j][k][1] == 1 :
               cellules_oreillettes_actives += 1 
            else :
                cellules_vent_actives += 1
        if tableau[i][j-1][k][0] == 1:
            tabl[i][j-1][k][2] = 1
            ampl += 1
            if tableau[i][j-1][k][1] == 1:
                cellules_oreillettes_actives += 1
            else :
                cellules_vent_actives += 1
        if tableau[i][j][k-1][0] == 1:
            tabl[i][j][k-1][2] = 1
            ampl += 1
            if tableau[i][j][k-1][1] == 1:
                cellules_oreillettes_actives += 1
            else :
                cellules_vent_actives += 1
        if tableau[i+1][j][k][0] == 1:
            tabl[i+1][j][k][2] = 1
            ampl += 1
            if tableau[i+1][j][k][1] == 1:
                cellules_oreillettes_actives += 1
            else :
                cellules_vent_actives += 1
        if tableau[i][j+1][k][0] == 1:
            tabl[i][j+1][k][2] = 1
            ampl += 1
            if tableau[i][j+1][k][1] == 1:
                cellules_oreillettes_actives += 1
            else :
                cellules_vent_actives += 1
        if tableau[i][j][k+1][0] == 1:
            tabl[i][j][k+1][2] = 1
            ampl += 1
            if tableau[i][j][k+1][1] == 1:
                cellules_oreillettes_actives += 1
            else :
                cellules_vent_actives += 1
    return tabl, ampl, cellules_oreillettes_actives, cellules_vent_actives


### mise à jour du tableau entier pour une simulation ###
def update(tableau):
    ampl = 0
    cellules_vent_actives = 0
    cellules_oreillettes_actives = 0
    tabl = tableau.copy()
    for i in range(len(tableau)):
        for j in range(len(tableau[0])):
            for k in range(len(tableau[1])):
                prop = propagation(tableau, i, j, k)
                tabl = prop[0]
                ampl += prop[1]
                cellules_oreillettes_actives += prop[2]
                cellules_vent_actives += prop[3]
    return tabl, ampl, cellules_oreillettes_actives, cellules_vent_actives


### amplitude (nombre cellules activées) en une simulation ###
def ampl_simulation(tableau,n):
    l_ampl = [1]
    l_cellules_oreillettes_actives = [1]
    l_cellules_vent_actives = [0]
    for i in range(1,n+1):
        up = update(tableau)
        tableau = up[0]
        l_ampl += [up[1]]
        l_cellules_oreillettes_actives += [up[2]]
        l_cellules_vent_actives += [up[3]]
    return l_ampl, l_cellules_oreillettes_actives, l_cellules_vent_actives

tau = 3
nb_simulations = 100
y = ampl_simulation(tableau, nb_simulations)
yr1 = y[1].copy()
yr2 = y[2].copy()
#l_ampl_finale = [y[0][i]  for i in range(tau)] + [y[0][i] - yr[0][i-tau] for i in range(tau, len(y))] + [y[0][-1] - yr[0][i] for i in range(len(y)-tau, len(y))]
#l_ampl_finale += l_ampl_finale


#on fait 2 simulations par unité de temps --> tau = nombre d'unité de temps après lequel les cellules se désactivent
l_ampl_finale = []
for i in range(2*tau):
    l_ampl_finale += [y[0][i]]
l_ampl_finale += [y[0][2*tau] - yr1[0]]
for i in range(2*tau + 1, len(y[0])):
    l_ampl_finale += [y[0][i] - yr1[i-2*tau] - yr2[i - 2*tau - 1]]
for i in range(len(y[0]) - 2*tau, len(y[0])):
    l_ampl_finale += [y[0][-1] - yr1[i] - yr2[i - 1]]

print(l_ampl_finale)

X = [k for k in range(len(l_ampl_finale))]
Y = l_ampl_finale

plt.plot(X,Y)
plt.show()
