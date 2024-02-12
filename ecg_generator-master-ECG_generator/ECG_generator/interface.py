from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # NavigationToolbar2Tk
from matplotlib.figure import Figure
from tkinter import *
from méthode1 import ajoute_bruit, coordonnéesECG, detect_R
import numpy as np
import matplotlib.image as mpimg


class testme:
    def __init__(self, frame1):
        self.frame1 = frame1

        self.ECG = []
        self.R = []

        self.MNU_OngletA = Menubutton(
            aframe, text="type de pathologie cardiaque")
        self.MNU_OptionA = Menu(self.MNU_OngletA)

        self.MNU_OptionA.add_command(label="normal", command=self.plot_normal)
        self.MNU_OptionA.add_command(
            label="tachycardie ventriculaire", command=self.plot_vtachy)
        self.MNU_OptionA.add_command(
            label="tachycardie sinusale", command=self.plot_sintachy)
        self.MNU_OptionA.add_command(
            label="flutter ventriculaire", command=self.plot_vflutter)
        self.MNU_OptionA.add_command(
            label="flutter atrial", command=self.plot_atrflutter)
        self.MNU_OptionA.add_command(
            label="fibrillation ventriculaire", command=self.plot_vfib)
        self.MNU_OptionA.add_command(
            label="fibrillation atriale", command=self.plot_atrfib)
        self.MNU_OptionA.add_command(
            label="asystolie", command=self.plot_asystolie)
        self.MNU_OptionA.add_command(
            label="bradycardie", command=self.plot_brady)

        self.MNU_OngletA["menu"] = self.MNU_OptionA
        self.MNU_OngletA.pack(side=TOP)

        self.text_PLI = Label(text="probabilité du bruit PLI :")
        self.text_PLI.pack()
        self.proba_PLI = Entry()
        self.proba_PLI.pack()

        self.text_MA = Label(text="probabilité du bruit MA :")
        self.text_MA.pack()
        self.proba_MA = Entry()
        self.proba_MA.pack()

        # crée un objet entier pour récupérer la valeur de la case à cocher,
        # 0 pour non cochée, 1 pour cochée
        self.v = IntVar()
        self.case = Checkbutton(variable=self.v)
        self.case.pack()
        self.case.config(text="afficher les ondes R ?")

        self.valider = Button(
            master=frame1, text="Valider", command=self.valider)
        self.valider.pack()

        # self.button1=Button(self.frame1,text="CLEARME",command=self._clear)
        # self.button1.pack()

        self.BUT_Quitter = Button(
            master=frame1, text="Quitter", command=root.destroy)
        self.BUT_Quitter.pack(padx=5, pady=20)

    def valider(self):
        trace = self.v.get()
        try:
            self.wierdobject.get_tk_widget().pack_forget()
        except AttributeError:
            pass
        self.fig = Figure(figsize=(655, 2), dpi=100)
        self.plot = self.fig.add_subplot(111)
        time = 45  # time in s
        t = np.linspace(0, time, int(time/0.005))
        self.plot.imshow(img, extent=[5, 15, -1.2, 1.2])
        self.plot.plot(t[1000:3000], self.ECG)
        if trace == 1:  # bouton coché
            self.plot = self.plot
            for temps in self.R:
                if temps <= 15 and temps >= 5:
                    self.plot.axvline(temps, color='g')
        self.wierdobject = FigureCanvasTkAgg(self.fig, master=self.frame1)
        self.wierdobject.get_tk_widget().pack()
        self.wierdobject.draw()

    def plot_normal(self):
        try:
            self.wierdobject.get_tk_widget().pack_forget()
        except AttributeError:
            pass
        proba_PLI = self.proba_PLI.get()
        proba_MA = self.proba_MA.get()
        Y, bpm = coordonnéesECG("normal")
        Y = ajoute_bruit(Y, proba_PLI, proba_MA)
        time = 45  # time in s
        # delta_t=0.005s comme dans l'article
        t = np.linspace(0, time, int(time/0.005))
        R = detect_R(Y, t, bpm)
        self.ECG = Y[1000:3000]
        self.R = R

    def plot_vtachy(self):
        try:
            self.wierdobject.get_tk_widget().pack_forget()
        except AttributeError:
            pass
        proba_PLI = self.proba_PLI.get()
        proba_MA = self.proba_MA.get()
        Y, bpm = coordonnéesECG("vtachy")
        Y = ajoute_bruit(Y, proba_PLI, proba_MA)
        time = 45  # time in s
        # delta_t=0.005s comme dans l'article
        t = np.linspace(0, time, int(time/0.005))
        R = detect_R(Y, t, bpm)
        self.ECG = Y[1000:3000]
        self.R = R

    def plot_atrflutter(self):
        try:
            self.wierdobject.get_tk_widget().pack_forget()
        except AttributeError:
            pass
        proba_PLI = self.proba_PLI.get()
        proba_MA = self.proba_MA.get()
        Y, bpm = coordonnéesECG("atrflutter")
        Y = ajoute_bruit(Y, proba_PLI, proba_MA)
        time = 45  # time in s
        # delta_t=0.005s comme dans l'article
        t = np.linspace(0, time, int(time/0.005))
        R = detect_R(Y, t, bpm)
        self.ECG = Y[1000:3000]
        self.R = R

    def plot_sintachy(self):
        try:
            self.wierdobject.get_tk_widget().pack_forget()
        except AttributeError:
            pass
        proba_PLI = self.proba_PLI.get()
        proba_MA = self.proba_MA.get()
        Y, bpm = coordonnéesECG("sintachy")
        Y = ajoute_bruit(Y, proba_PLI, proba_MA)
        time = 45  # time in s
        # delta_t=0.005s comme dans l'article
        t = np.linspace(0, time, int(time/0.005))
        R = detect_R(Y, t, bpm)
        self.ECG = Y[1000:3000]
        self.R = R

    def plot_vfib(self):
        try:
            self.wierdobject.get_tk_widget().pack_forget()
        except AttributeError:
            pass
        proba_PLI = self.proba_PLI.get()
        proba_MA = self.proba_MA.get()
        Y, bpm = coordonnéesECG("vfib")
        Y = ajoute_bruit(Y, proba_PLI, proba_MA)
        time = 45  # time in s
        # delta_t=0.005s comme dans l'article
        t = np.linspace(0, time, int(time/0.005))
        R = detect_R(Y, t, bpm)
        self.ECG = Y[1000:3000]
        self.R = R

    def plot_vflutter(self):
        try:
            self.wierdobject.get_tk_widget().pack_forget()
        except AttributeError:
            pass
        proba_PLI = self.proba_PLI.get()
        proba_MA = self.proba_MA.get()
        Y, bpm = coordonnéesECG("vflutter")
        Y = ajoute_bruit(Y, proba_PLI, proba_MA)
        time = 45  # time in s
        # delta_t=0.005s comme dans l'article
        t = np.linspace(0, time, int(time/0.005))
        R = detect_R(Y, t, bpm)
        self.ECG = Y[1000:3000]
        self.R = R

    def plot_asystolie(self):
        try:
            self.wierdobject.get_tk_widget().pack_forget()
        except AttributeError:
            pass
        proba_PLI = self.proba_PLI.get()
        proba_MA = self.proba_MA.get()
        Y, bpm = coordonnéesECG("asystolie")
        Y = ajoute_bruit(Y, proba_PLI, proba_MA)
        time = 45  # time in s
        # delta_t=0.005s comme dans l'article
        t = np.linspace(0, time, int(time/0.005))
        R = detect_R(Y, t, bpm)
        self.ECG = Y[1000:3000]
        self.R = R

    def plot_brady(self):
        try:
            self.wierdobject.get_tk_widget().pack_forget()
        except AttributeError:
            pass
        proba_PLI = self.proba_PLI.get()
        proba_MA = self.proba_MA.get()
        Y, bpm = coordonnéesECG("brady")
        Y = ajoute_bruit(Y, proba_PLI, proba_MA)
        time = 45  # time in s
        # delta_t=0.005s comme dans l'article
        t = np.linspace(0, time, int(time/0.005))
        R = detect_R(Y, t, bpm)
        self.ECG = Y[1000:3000]
        self.R = R

    def plot_atrfib(self):
        try:
            self.wierdobject.get_tk_widget().pack_forget()
        except AttributeError:
            pass
        proba_PLI = self.proba_PLI.get()
        proba_MA = self.proba_MA.get()
        Y, bpm = coordonnéesECG("atrfib")
        Y = ajoute_bruit(Y, proba_PLI, proba_MA)
        time = 45  # time in s
        # delta_t=0.005s comme dans l'article
        t = np.linspace(0, time, int(time/0.005))
        R = detect_R(Y, t, bpm)
        self.ECG = Y[1000:3000]
        self.R = R

    def _clear(self):
        for item in self.wierdobject.get_tk_widget().find_all():
            self.wierdobject.get_tk_widget().delete(item)


if __name__ == "__main__":
    root = Tk()
    root.geometry("1200x800")
    background_image = PhotoImage(file="ECGcoeur.png")
    background_label = Label(image=background_image)
    background_label.place(x=0, y=100, relwidth=1, relheight=1)
    aframe = Frame(root)
    img = mpimg.imread("grille.png")
    testme(aframe)
    aframe.pack()  # packs a frame which given testme packs frame 1 in testme
    root.mainloop()
