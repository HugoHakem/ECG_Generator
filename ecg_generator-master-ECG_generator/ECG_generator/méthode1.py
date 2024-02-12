import numpy as np
from scipy.integrate import odeint
import random


def constantes(maladie):
    """retourne les constantes nécessaires à la résolution du système 
    au format [eta,alpha1,alpha2,alpha3,alpha4,beta,a,b,H,C,bpm]"""
    # maladies parmi normal, atrflutter,vfib...
    # pour VF bpm=190 env.
    h = 0.08804
    if maladie == "normal":
        return [1, -0.024, 0.0216, -0.0012, 0.12, 4, -1, -3, 3, 1.35, 80]
    if maladie == "vtachy":
        return [1, -0.024, 0.0216, -0.0012, 0.12, 4, -1, -3, 6, 1.35, 80]
    if maladie == "sintachy":
        return [1, -0.024, 0.0216, -0.0012, 0.12, 4, -1, -3, 3, 1.35, 140]
    if maladie == "asystolie":
        return [1, -0.024, 0.0216, -0.0012, 0.12, 4, -1, -3, 3, 1.35, 80]
    if maladie == "brady":
        return [1, -0.024, 0.0216, -0.0012, 0.12, 4, -1, -3, 3, 1.35, 40]
    if maladie == "atrflutter":
        return [1, -0.068, 0.028, -0.024, 0.12, 4, -1, -3, 2.848, 1.52, 13/h]
    if maladie == "atrfib":
        return [1, -0.024, 0.0216, -0.0012, 0.12, 4, -1, -3, 2.164, 1.35, 193.2]
    if maladie == "atrtachy":
        return [1, 0, -0.1, 0, 0, 4, -1, -3, 2.848, 1.35, 21/h]
    if maladie == "vflutter":
        return [1, 0.1, -0.02, -0.01, 0, 4, -1, -3, 2.178, 1.35, 280]
    if maladie == "vfib":
        return [1, 0, 0, 0, -0.1, 4, -1, -3, 2.178, 1.35, 21/h]


def ajout_bruit_gauss(Y, variance=1):
    """ajoute le bruit blanc gaussien à l'ECG brut Y"""
    for i in range(len(Y)):
        Y[i] += (2*np.random.normal(scale=variance)-1)*0.0075
    return Y


def ajout_bruit_ma(Y, proba_MA, variance2=1, amp=0.03):
    """ajoute le bruit de type motion artefact à l'ECG brut Y"""
    existe = random.uniform(0, 1)
    # le bruit sera ajouté avec la probabilité proba_MA
    proba_MA = float(proba_MA)
    if existe < proba_MA:
        start = random.randint(0, 2000)  # entre 0 et 10s
        duration = random.randint(100, 500)  # entre 0.5 et 2.5s
        for i in range(len(Y)):
            # même motif de bruit répété toutes les 10s
            if i % 2000 > start and i % 2000 < min(start+duration, 2000):
                Y[i] += (2*np.random.normal(scale=variance2)-1)*amp
    return Y


def ajout_bruit_bw(Y, a0=0.1, a1=0.05, phi0=3, phi1=5, omega1=0.01, omega0=0.01, présence=True):
    """ajoute le bruit de type Baseline Wander à l'ECG brut Y"""
    if présence:  # dans l'état le bruit sera toujours ajouté
        for i in range(len(Y)):
            Y[i] = Y[i]+np.cos(omega0*i+phi0)*a0+a1*np.cos(omega1*i+phi1)
    return Y


def ajout_bruit_pli(Y, proba_PLI, omega=1.57, ampli=0.05):  # omega=2*pi*50Hz*0.005
    """ajoute le bruit de type Power Line Interference à l'ECG brut Y"""
    existe = random.uniform(0, 1)
    # le bruit sera ajouté avec la probabilité proba_PLI
    proba = float(proba_PLI)
    if existe < proba:
        for i in range(len(Y)):
            Y[i] = Y[i]+np.cos(omega*i)*ampli
    return Y


def traitement_post(maladie, Y):
    """fonction créée pour simuler l'asystolie : récupère un ECG simulé avec les mêmes constantes
    que pour un individu sain et élimine des battements aléatoirement"""
    if maladie == "asystolie":
        start = random.randint(200, 1800)  # entre 1 et 9s
        duration = random.randint(200, 601)  # durée du vide entre 1 et 3s
        for i in range(1000, len(Y)):
            if (i-1000) % 2000 > start and (i-1000) % 2000 <= start+duration:
                Y[i] = 0


def coordonnéesECG(maladie):
    """résout le système avec les constantes correspondant à la maladie en entrée"""
    [eta, alpha1, alpha2, alpha3, alpha4, beta,
        a, b, H, C, bpm] = constantes(maladie)
    # le bpm est tiré aléatoirement autour d'une valeur de référence
    bpm = bpm+random.uniform(-0.2*bpm, 0.2*bpm)
    # idem pour le paramètre H qui définit la maladie
    H = random.gauss(H, 0.001)
    x0 = [0, 0] + [random.uniform(0, 4)] + [0]  # idem pour x3(0)
    time = 45  # durée de la simulation en secondes
    # delta_t=0.005s comme dans l'article
    t = np.linspace(0, time, int(time/0.005))

    def odes(x, t):  # x = [x1, x2, x3, x4]
        """définit le système à résoudre"""
        gama = 0.08804*bpm-0.06754
        x1, x2, x3, x4 = x
        d_x1 = x1 - x2 - C * x1 * x2 - x1 * x2**2
        d_x2 = H * x1 - 3 * x2 + C * x1 * x2 + x1 * x2**2 + beta * (x4 - x2)
        d_x3 = x3 - x4 - C*x3*x4 - x3*x4**2
        d_x4 = H * x3 - 3*x4 + C*x3*x4 + x3*x4**2 + 2 * beta * (x2-x4)
        return gama*np.array([d_x1, d_x2, d_x3, d_x4])
    x = odeint(odes, x0, t)
    Y = [(alpha1 * x[i][0] + alpha2 * x[i][1] + alpha3 * x[i][2] +
          alpha4 * x[i][3]) for i in range(0, int(time/0.005), 2)]
    # dupplique l'ECG pour diviser par deux la résolution en temps
    Y = [item for sublist in zip(Y, Y) for item in sublist]
    traitement_post(maladie, Y)
    # Y=ajout_bruit_gauss(Y)
    # Y=ajout_bruit_bw(Y)
    # Y=ajout_bruit_pli(Y,proba_PLI)
    #Y=ajout_bruit_ma(Y, proba_MA)
    return Y, bpm


def ajoute_bruit(Y, proba_PLI, proba_MA):
    """ajoute les bruits à l'ECG brut"""
    Y = ajout_bruit_gauss(Y)
    Y = ajout_bruit_bw(Y)
    Y = ajout_bruit_pli(Y, proba_PLI)
    Y = ajout_bruit_ma(Y, proba_MA)
    return Y


def mix_ecg(maladies):  # maladies est une liste
    """prend en entrée une liste de maladies, et retrourne un ECG de 10s(2000 points) construit 
    par succession de périodes égales correspondant à chacune des maladies"""
    A = []
    for i in range(len(maladies)):
        A.append(coordonnéesECG(maladies[i])[0])
    # nb de points par maladie, correspont à une durée totale de 10s
    n = 2000//len(maladies)
    Y = []
    for i in range(len(maladies)):
        for j in range(n):
            # +2000 pour ne pas prendre les valeurs du régime transitoire
            Y[j+i*n] = A[i][j+2000]
    return np.array(Y)


def detect_R(Y, t, bpm):
    """détecte les ondes R : retourne les instants correspondant aux pics des ondes R"""
    M = max(Y)
    Z = []  # Liste des [temps t, voltage(t)]
    for i in range(len(Y)):
        Z.append([t[i], Y[i]])
    liste_R = []
    var = 0
    for [temps, volt] in Z:
        if volt > 0.6*M and temps > var + (30/bpm):  # comment trouve le 0.6
            liste_R.append(temps)
            var = temps
    return(liste_R)
