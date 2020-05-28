# Tkinter wird für das GUI importiert - Einfachere Funktionen, um ein GUI zu programmieren
# Bei RSA_Verschluesslung wird der Code für die Umformung von Buchstaben zu Bytes importiert - Um auch Buchstaben zu Verschlüsseln

from tkinter import *
import tkinter as tk
import math
from Buchstaben_zu_bytes import convert_to_num, convert_to_text
from math import gcd
from math import *
import random

# Grundsätzliches Einnrichten des GUI
# Diese Informationen werden bei jeder Neuer Seite wieder von hier entnommen
# Gleichbleibendes Schema

root = tk.Tk()
Height = 600
Width = 800
root.title("EnkryptenAPP")

# Wird eingefuehrt, um das GUI bei Vergroesserung und Verkleinerung automatisch der Grösse der Fenster innerhalb des GUI's anzupassen

canvas = tk.Canvas(root, height=Height, width=Width)
canvas.pack()


def getLCM(a, b):
    return a * b // gcd(a, b)


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x % m


def ggt(a, icm):
    while icm > 0:
        a, icm = icm, a % icm
    return a


def output_of_e(a, icm):
    while ggt(a, icm) != 1:
        a = a + 1
    else:
        return a


# Nur für das Introfenster - Funktion für den Nein Knopf auf Seite 1

def close():
    root.destroy()


# Für das Fenster wenn man auf den Ja Knopf der Introfolie drueckt - Neues Fenster

def open():
    canvas.pack()

    # Hintergrundbild - Ich habe keine Funktion gefunden, welche das Hintergrundbild automatisch mit der Veränderung des Fensters anpasst (Wie es z.B der Fall ist bei den labels, buttons)

    # Fuer jeden Button, Text und Eingabefenster wird ein frame erstellt - Hilft beim Veraendern der groesse des Fensters - Automatische anpassung mit der funktion "place"

    background_image = tk.PhotoImage(file="Sunset.png")
    background_label = tk.Label(root, image=background_image)
    background_label.place(relx=0, rely=0, relwidth=1, relheight=1)

    frame_site_titel = tk.Frame(root, bg="white", bd=2)
    frame_site_titel.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

    frame_site_primzahl = tk.Frame(root, bg="white", bd=2)
    frame_site_primzahl.place(relx=0.5, rely=0.3, relwidth=0.5, relheight=0.1, anchor="n")

    frame_site_primzahl2 = tk.Frame(root, bg="white", bd=2)
    frame_site_primzahl2.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.1, anchor="n")

    frame_site_startpunkt = tk.Frame(root, bg="white", bd=2)
    frame_site_startpunkt.place(relx=0.5, rely=0.7, relwidth=0.5, relheight=0.1, anchor="n")

    frame_button_weiter = tk.Frame(root, bg="white", bd=2)
    frame_button_weiter.place(relx=0.5, rely=0.85, relwidth=0.3, relheight=0.1, anchor="n")

    label_seite2 = tk.Label(frame_site_titel, text="Geben sie nun 2 Primzahlen und 1 Startpunkt ein", bg="#00001a",
                            fg="white",
                            font=("Alegra", 28))
    label_seite2.place(relwidth=1, relheight=1)

    label_seite2 = tk.Label(frame_site_primzahl, text="Primzahl 1:", bg="#00001a", fg="white",
                            font=("Alegra", 28))
    label_seite2.place(relwidth=0.4, relheight=1)

    label_seite2_primzahl1 = tk.Label(frame_site_primzahl2, text="Primzahl 2:", bg="#00001a", fg="white",
                                      font=("Alegra", 28))
    label_seite2_primzahl1.place(relwidth=0.4, relheight=1)

    label_seite2_startpunkt = tk.Label(frame_site_startpunkt, text="Startzahl :", bg="#00001a", fg="white",
                                       font=("Alegra", 28))
    label_seite2_startpunkt.place(relwidth=0.4, relheight=1)

    # Die 3 global's werden zusaetzlich in anderen Funktionen gebraucht - Zwischenspeicher für andere Funktionen

    global eingabe_seite2_primzahl1
    eingabe_seite2_primzahl1 = StringVar()
    entry = tk.Entry(frame_site_primzahl, bg="#00001a", font=("Alegra", 30), fg="white",
                     textvariable=eingabe_seite2_primzahl1)
    entry.place(relx=0.4, relwidth=0.6, relheight=1)

    global eingabe_seite2_primzahl2
    eingabe_seite2_primzahl2 = StringVar()
    entry = tk.Entry(frame_site_primzahl2, bg="#00001a", font=("Alegra", 30), fg="white",
                     textvariable=eingabe_seite2_primzahl2)
    entry.place(relx=0.4, relwidth=0.6, relheight=1)

    global eingabe_seite2_startpunkt
    eingabe_seite2_startpunkt = StringVar()
    entry = tk.Entry(frame_site_startpunkt, bg="#00001a", font=("Alegra", 30), fg="white",
                     textvariable=eingabe_seite2_startpunkt)
    entry.place(relx=0.4, relwidth=0.6, relheight=1)

    # Mit dem Button werden die 3 (global's) Eingaben abgespeichert und (command) ruft die Funktion open 1 auf - Neue Seite wird geoeffnet

    button_weiter = tk.Button(frame_button_weiter, text="Weiter", bg="#00001a", fg="white", font=("Alegra", 30), bd=1,
                              command=open1)
    button_weiter.place(relwidth=1, relheight=1)

    mainloop()


# Messengerfenster wird beim oberen Button erstellt - Schlussfenster

def open1():
    canvas.pack()

    # Menue pic für einen Button, welcher einem zurueck zum Einstellungfenster bringt

    menue_pic = PhotoImage(file="menue.png")
    background_image = tk.PhotoImage(file="Sunset.png")
    background_label_huch = tk.Label(root, image=background_image)
    background_label_huch.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Neue Frames für GUI, welches aufgerufen wird (Seite 3)

    frame = tk.Frame(root, bg="white", bd=2)
    frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

    frame1 = tk.Frame(root, bg="white", bd=2)
    frame1.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.1, anchor="n")

    frame2 = tk.Frame(root, bg="white", bd=2)
    frame2.place(relx=0.35, rely=0.35, relwidth=0.3, relheight=0.1, anchor="n")

    frame3 = tk.Frame(root, bg="white", bd=2)
    frame3.place(relx=0.65, rely=0.35, relwidth=0.3, relheight=0.1, anchor="n")

    frame4 = tk.Frame(root, bg="white", bd=2)
    frame4.place(relx=0.125, rely=0.5, relwidth=0.75, relheight=0.4)

    frame5 = tk.Frame(root, bg="white", bd=2)
    frame5.place(relx=0.92, rely=0.9, relwidth=0.08, relheight=0.1)

    label2 = tk.Label(frame, bg="#00001a", fg="white", font=("Alegra", 30), text="Geben sie hier ihre Nachricht ein")
    label2.place(relwidth=1, relheight=1)

    label_for_validation = tk.Frame(root, bg="white", bd=2)
    label_for_validation.place(relx=0, rely=0.9, relwidth=0.08, relheight=0.1)

    # Die Informationen von diesen 2 global's werden in unteren Funtionen gebraucht - Informationsspeicher

    global eingabe_nachricht
    eingabe_nachricht = StringVar()
    entry_seite_3 = tk.Entry(frame1, textvariable=eingabe_nachricht, bg="#00001a", fg="white", font=("Alegra", 30))
    entry_seite_3.place(relwidth=1, relheight=1)

    # Verschluesslungsknopf - Wenn er gedrueckt wird verweist er auf die Verschluesslungsfunktion mit command=

    button_weiter = tk.Button(frame2, text="Verschlüsseln", bg="#00001a", fg="white", font=("Alegra", 30), bd=1,
                              command=Verschlüsseln)
    button_weiter.place(relwidth=1, relheight=1)

    # Entschluesslungsknopf - Verweist auf Entschluesslungfunktion mit command=

    button_weiter = tk.Button(frame3, text="Entschlüsseln", bg="#00001a", fg="white", font=("Alegra", 30), bd=1,
                              command=Entschlüsseln)
    button_weiter.place(relwidth=1, relheight=1)

    global label_nachrichten
    label_nachrichten = tk.Text(frame4, fg="white", bg="#00001a", font=("Alegra", 25), bd=3)
    label_nachrichten.place(relwidth=1, relheight=1)

    # Button um das Programm nicht jedes Mal neu starten zu muessen, wenn man die Angaben der Primzahlen und des Startpunktes ändern moechte
    # Man kommt direkt auf das Menue Fenster - Neuspeicherung der Daten

    button_menue = tk.Button(frame5, image=menue_pic, bg="#00001a", fg="white", font=("Alegra", 30), bd=1, command=open)
    button_menue.place(relwidth=1, relheight=1)

    global validation_entry
    validation_entry = tk.Text(label_for_validation, bg="#00001a", fg="white", font=("Alegra", 30), bd=1)
    validation_entry.place(relwidth=1, relheight=1)

    mainloop()


# Pruefung ob es sich auch um eine Primzahl handelt
# Nicht, dass man einfach random Zahlen im Programm eingeben kann


def primzahl(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    quadratzahl = int(math.sqrt(n)) + 1

    # Von 3 bis zur Quadratzahl werden alle Teiler überprüft
    # Dies in 2er Schritten, da man die 2er Zahlen schon oben rausgenommen hat

    for teiler in range(3, quadratzahl, 2):
        if n % teiler == 0:
            return False
    return True


def Verschlüsseln():
    # Die Globla's werden hier aufgenommen und in die jeweiligen variablen aufgeteilt
    # Sie liegen jedoch in Strings vor weshalb alle noch zu einer Int zahl umgewandelt werden müssen

    q = eingabe_seite2_primzahl1.get()
    p = eingabe_seite2_primzahl2.get()
    #    e = eingabe_seite2_startpunkt.get()
    m = eingabe_nachricht.get()

    # Convert to num ist eine Funktion von "Buchstabe zu bytes"
    # Die message m wird dabei nach zu der multipliziertes Zahl der jeweiligen Zahlen von 1-256 umgeformt

    m = convert_to_num(m)
    q = int(q)
    p = int(p)
    #    e = int(e)
    m = int(m)

    # ueberpruefung von moelichen Fehlern , ein Error mit dem Text wird direkt im GUI anzeigt - der Error geht jedoch durch und somit stoppt das Programm
    # Ich weiss leider nicht wieso aber verschiedene Kombinationen mit Primzahlen unter 30 funktionieren nicht richtig und somit habe ich sie im Error File dazugefuegt
    # Ich gehe von einem mathematischen Fehler aus aber kann es mir nicht ganz erklaeren
    # Das gleiche gilt, wenn die Message = m groesser ist als die Multiplikation der 2 Primzahlen
    # Dies ist jedoch momentan auf grau, da die Zahl m durchs umwandeltn mit utf-8 viel groesser wird als p*q

    if not primzahl(p) or not primzahl(q):
        label_nachrichten.insert(tk.INSERT, "Geben Sie bitte echte Primzahlen ein\n")
        raise (ValueError)
        # if p < 32 or q < 32:
        #    label_nachrichten.insert(tk.INSERT, "Die Primzahlen müssen grösser als 31 sein.\n")
        #    raise (ValueError)
        if m > (q * p):
            label_nachrichten.insert(tk.INSERT, "Geben Sie dafür hoehere Primzahlen ein.\n")
            raise (ValueError)
    if p == q:
        label_nachrichten.insert(tk.INSERT, "Geben Sie 2 unterschiedliche Primzahlen ein.\n")
        raise (ValueError)

    # Berechnung von den Schluesseln mit Hilfe des Startpunktes x

    n = p * q

    # Carmichael’s totient function
    icm = getLCM(p - 1, q - 1)
    # In unserem Fall wird e gleichbleiben - um die gleichen Resultate zu erhalten

    global e
    e = output_of_e(1, icm)

    #e = 16
    #    e = random.randint(1, icm)
    #    print("Das ist e1: ", e,)

    # print(e)
    # e = 23

    global verschlüsselte_nachricht
    verschlüsselte_nachricht = (m ** e) % n
    print(verschlüsselte_nachricht)
    # Diese print() Funktionen wollte ich den Fehler mit der Umrechnung mit utf-8 herausfinden -

    # Berechnete Zahl wird auf die 3 Seite geprinted

    label_nachrichten.insert(tk.INSERT,
                             "Ihre Verschlüsselte Nachricht lautet: " + (str(verschlüsselte_nachricht) + "\n"))


def Entschlüsseln():
    checker = bool()
    checker = False

    print("das ist used_m vorher")
    print(verschlüsselte_nachricht)

    # Gleiches Prozedere wie bei Verschluesseln - Die neue Eingabe wird mit m1 abgespeichert

    q = eingabe_seite2_primzahl1.get()
    p = eingabe_seite2_primzahl2.get()
    #    e = eingabe_seite2_startpunkt.get()
    c = eingabe_nachricht.get()
    q = int(q)
    p = int(p)
    #    e = int(e)
    c = int(c)
    print("Das ist c: ", c, )

    # ueberpruefung der Gleichen Problemen wie Oben
    # Falls jemands nur mit der Verschluesung arbeiten würde ohne zuerst die Verschluesslugsfunktion ausgeloest zu haben

    if not primzahl(p) or not primzahl(q):
        label_nachrichten.insert(tk.INSERT, "Geben Sie bitte echte Primzahlen ein\n")
        raise (ValueError)
        # if p < 32 or q < 32:
        #    label_nachrichten.insert(tk.INSERT, "Die Primzahlen müssen grösser als 31 sein.\n")
        #    raise (ValueError)
        if m1 > (q * p):
            label_nachrichten.insert(tk.INSERT, "Geben Sie dafür hoehere Primzahlen ein.\n")
            raise (ValueError)
    if p == q:
        label_nachrichten.insert(tk.INSERT, "Geben Sie 2 unterschiedliche Primzahlen ein.\n")
        raise (ValueError)

    n = p * q

    # Carmichael’s totient function

    icm = getLCM(p - 1, q - 1)
    print("Das ist das icm: ", icm, )

    #    e = 3
    #    e = random.randint(1, icm)
    #    print("Das ist e2: ", e,)

    d = modinv(e, icm)
    print("Das ist das modinv: ", d, )

    newm = (c ** d) % n
    print("Das ist newm ", newm, )

    global the_signature
    the_signature = ((newm ** e) % n)

    print("das hier müsse das gleiche sein ", the_signature, )

    # Hier kommt die eigentliche Entschlüsslungs ins Spiel - Umwandlung und danach die utf-8 Umformung zurueck zum Ursprung

    # Hier kommt die Funktion von Buchtstaben zu bytes ins Spiel

    converted_message = convert_to_text(newm)
    label_nachrichten.insert(tk.INSERT, "Ihre Entschlüsselte Nachricht lautet: " + (str(converted_message) + "\n"))

    #Bestimmung der Signature - Valid oder invalid - Im jetzigen Programm ist es unmöglich m zu verändern

    if the_signature == verschlüsselte_nachricht:
        checker = True
    if checker:
        validation_entry.insert(tk.INSERT, "  V")
    else:
        validation_entry.insert(tk.INSERT, "  I")


# Das GUI für den Anfangscreen
# Ich weiss es wäre nicht umbedingt eine noetige Seite des Programms, aber ich finde eine Startseite macht einen guten ersten Eindruck für das gesammte Programm


background_image = tk.PhotoImage(file="Sunset.png")
background_label_huch = tk.Label(root, image=background_image)
background_label_huch.place(relx=0, rely=0, relwidth=1, relheight=1)

frame = tk.Frame(root, bg="white", bd=2)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

frame1 = tk.Frame(root, bg="white", bd=2)
frame1.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.1, anchor="n")

frame_button_yes = tk.Frame(root, bg="white", bd=2)
frame_button_yes.place(relx=0.2, rely=0.6, relwidth=0.3, relheight=0.1)

frame_button_no = tk.Frame(root, bg="white", bd=2)
frame_button_no.place(relx=0.5, rely=0.6, relwidth=0.3, relheight=0.1)

label2 = tk.Label(frame, text="Ich begrüsse Sie zu meiner Abschlussarbeit!", bg="#00001a", fg="white",
                  font=("Alegra", 30))
label2.place(relwidth=1, relheight=1)

label3 = tk.Label(frame1, text="Wollen sie mit dem Verschlüsseln beginnen?", bg="#00001a", fg="white",
                  font=("Alegra", 30))
label3.place(relwidth=1, relheight=1)

# Hier wird beim druecken des Knopfes die 2 Seite aufgerufen

button = tk.Button(frame_button_yes, text="Ja", bg="#00001a", fg="white", font=("Alegra", 30), bd=2, command=open)
button.place(relwidth=1, relheight=1)

button_no = tk.Button(frame_button_no, text="Nein", bg="#00001a", fg="white", font=("Alegra", 30), bd=1, command=close)
button_no.place(relwidth=1, relheight=1)

root.mainloop()
