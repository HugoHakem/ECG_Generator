import argparse
from distutils.log import error
import wfdb
import numpy as np
from méthode1 import coordonnéesECG, ajoute_bruit


# Configuration du passeur d'argument afin d'utiliser le générateur dans le terminal
parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter, description="""
Générateur d'ECG par la Team ECG de CentraleSupélec réalisé lors d'un projet avec Implicity :
\n
Étudiants\n
	Sarah Wu\n
	Marie Cubaynes\n
	Guillaume Gerony\n
	Séléna Jean-Mactoux\n
	Hugo Hakem\n
	Virgile Rapegno\n
\n
Encadrants\n
    Micheal Kirkpatrick\n
    Cristian Puentes\n
    Trungdung Le\n
\n
Implicity\n
    David Perlmutter\n
    Eliot Crespin\n
\n
Le format de sortie des ECG est le standard MIT-BIH
""")

parser.add_argument('maladie', type=str, default="normal", help="""
Maladie dont on souhaite tracer l'ECG parmi les suivantes : \n
normal,\n
vtachy,\n
sintachy,\n
assystolie,\n
brady,\n
artflutter,\n
atrfib,\n
atrachy,\n
vflutter\n
vfib
""")

parser.add_argument('nombre', type=int, default=1, help="""
Nombre d'ECG à générer
""")

parser.add_argument('emplacement', type=str, default=".", help="""
Emplacement des fichiers après leur générations
""")

parser.add_argument('--PLI', type=float, default=0, help="""
Probabilité d'avoir un bruit Power Line Interference, en tant que nombre entre 0 et 1
""")

parser.add_argument('--MA', type=float, default=0, help="""
Probabilité d'avoir un bruit Muscle Artifact, en tant que nombre entre 0 et 1
""")

args = parser.parse_args()


# Exportation des données stockées sous forme d'array au format MIT-BIH
def exporter(nom, fréquence, données, emplacement, commentaires):
    """
    exporter a la signature suivante
    (string, float, np.array, str, [str]) -> ()
    nom est une chaine de caratère qui permet d'identifier l'ECG
    fréquences est une flotant donnant la fréquence d'échentillonage
    données est un vecteur avec qui à chaque temps associe une valeur en mV de l'ECG
    emplacement est une chaine de caratère indiquant où enregistrer l'ECG
    commentaires est une liste de chaine de caratère avec les informations sur l'ECG comme l'âge, le sexe, et la pathologie
    """

    wfdb.io.wrsamp(
        nom,
        fréquence,
        ["mV"],
        ['I'],
        p_signal=données,
        comments=commentaires,
        write_dir=emplacement
    )


# Excécution du programme

def main(maladie=args.maladie, nombre=args.nombre, emplacement=args.emplacement, PLI=args.PLI, MA=args.MA):
    for i in range(nombre):
        nom = "ECG_{}_{}".format(maladie, i)
        Y, _ = coordonnéesECG(maladie)
        Y = ajoute_bruit(Y, PLI, MA)
        données = np.array(Y[1000:3000], ndmin=2).T
        exporter(nom, 200, données, emplacement, [maladie])


if __name__ == "__main__":

    if (args.maladie not in ["normal", "vtachy", "sintachy", "assystolie", "brady", "artflutter", "atrfib", "atrachy", "vflutte", "vfib"] or
        args.nombre <= 0 or
        args.PLI < 0 or
        args.PLI > 1 or
        args.MA < 0 or
            args.MA > 1):
        raise Exception("vérifier les valeurs saisies")

    main()
