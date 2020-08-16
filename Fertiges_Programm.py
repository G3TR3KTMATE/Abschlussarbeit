# Tkinter wird für das GUI importiert - Einfachere Funktionen, um ein GUI zu programmieren
# Bei RSA_Verschluesslung wird der Code für die Umformung von Buchstaben zu Bytes importiert - Um auch Buchstaben zu Verschlüsseln

from tkinter import *
import tkinter as tk
from Buchstaben_zu_bytes import convert_to_num, convert_to_text
from math import gcd
from math import *
import random
from hashlib import blake2b
from Blockchain_V1 import *

# import hashlip

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

Primelist = [
    945002999839, 999999699709, 949999699331, 825034358893, 825034358903, 785037358619, 785037358543, 785037358571,
    785537358371, 845054959421, 825034359103, 825034359157, 825034358767, 825034358699, 785037358639, 785037358561,
    785537358341, 945003000143, 945002999923, 825034959103, 825034959113, 785037358667, 785537358553, 785537358563,
    785537358607, 945002959837, 825054959423, 825054959383, 825054959387, 825034959467, 785537358647, 945052959713,
    845054959733, 845054959663, 945052959703, 945052959817, 775537358303, 775537358333, 775537358381, 775537358437,
    777537358531, 777537358541, 777537358487, 777537358177, 777537358097, 777537358099, 777537358079, 777537357937
]

numberlist = 1
Numberlist = []
while numberlist < 100:
    Numberlist.append(numberlist)
    numberlist += 1

Namelist = ["Adam", "Alex", "Alexander", "Andreas", "Adrian", "Antoine", "Daniel", "David", "Dominik", "Fiona",
            "Franziska", "Florin", "Kai", "Karla", "Katharina", "Kim", "Maria", "Michelle", "Marion", "Patrick",
            "Peter", "Paul", "Philipp", "Ramin", "Richard", "Robert", "Roman"]

Kosch_Coin = BlockChain()


def getLCM(a, b):
    return a * b // gcd(a, b)


# Quelle:https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python

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
    def random_Prime1():
        #        eingabe_seite2_primzahl1.insert(tk.INSERT, random.choice(Primelist))
        entry1.delete(first=0, last=20)
        entry1.insert(tk.INSERT, random.choice(Primelist))

    def random_Prime2():
        #        eingabe_seite2_primzahl2.insert(tk.INSERT, random.choice(Primelist))
        entry2.delete(first=0, last=20)
        entry2.insert(tk.INSERT, random.choice(Primelist))

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

    #    frame_site_startpunkt = tk.Frame(root, bg="white", bd=2)
    #    frame_site_startpunkt.place(relx=0.5, rely=0.7, relwidth=0.5, relheight=0.1, anchor="n")

    frame_button_weiter = tk.Frame(root, bg="white", bd=2)
    frame_button_weiter.place(relx=0.5, rely=0.85, relwidth=0.3, relheight=0.1, anchor="n")

    frame_for_random_prime1 = tk.Frame(root, bg="white", bd=2)
    frame_for_random_prime1.place(relx=0.8, rely=0.3, relwidth=0.1, relheight=0.1)

    frame_for_random_prime2 = tk.Frame(root, bg="white", bd=2)
    frame_for_random_prime2.place(relx=0.8, rely=0.5, relwidth=0.1, relheight=0.1)

    button_for_random_prime1 = tk.Button(frame_for_random_prime1, text="Auto", bg="#00001a", fg="white",
                                         font=("Alegra", 30), bd=1,
                                         command=random_Prime1)
    button_for_random_prime1.place(relwidth=1, relheight=1)

    button_for_random_prime2 = tk.Button(frame_for_random_prime2, text="Auto", bg="#00001a", fg="white",
                                         font=("Alegra", 30), bd=1,
                                         command=random_Prime2)
    button_for_random_prime2.place(relwidth=1, relheight=1)

    label_seite2 = tk.Label(frame_site_titel, text="Geben sie nun 2 verschiedene Primzahlen ein.", bg="#00001a",
                            fg="white",
                            font=("Alegra", 28))
    label_seite2.place(relwidth=1, relheight=1)

    label_seite2 = tk.Label(frame_site_primzahl, text="Primzahl 1:", bg="#00001a", fg="white",
                            font=("Alegra", 28))
    label_seite2.place(relwidth=0.4, relheight=1)

    label_seite2_primzahl1 = tk.Label(frame_site_primzahl2, text="Primzahl 2:", bg="#00001a", fg="white",
                                      font=("Alegra", 28))
    label_seite2_primzahl1.place(relwidth=0.4, relheight=1)

    #    label_seite2_startpunkt = tk.Label(frame_site_startpunkt, text="Startzahl :", bg="#00001a", fg="white",
    #                                       font=("Alegra", 28))
    #    label_seite2_startpunkt.place(relwidth=0.4, relheight=1)

    # Die 3 global's werden zusaetzlich in anderen Funktionen gebraucht - Zwischenspeicher für andere Funktionen

    global eingabe_seite2_primzahl1
    eingabe_seite2_primzahl1 = StringVar()
    entry1 = tk.Entry(frame_site_primzahl, bg="#00001a", font=("Alegra", 30), fg="white",
                      textvariable=eingabe_seite2_primzahl1)
    entry1.place(relx=0.4, relwidth=0.6, relheight=1)

    global eingabe_seite2_primzahl2
    eingabe_seite2_primzahl2 = StringVar()
    entry2 = tk.Entry(frame_site_primzahl2, bg="#00001a", font=("Alegra", 30), fg="white",
                      textvariable=eingabe_seite2_primzahl2)
    entry2.place(relx=0.4, relwidth=0.6, relheight=1)

    # global eingabe_seite2_startpunkt
    # eingabe_seite2_startpunkt = StringVar()
    # entry = tk.Entry(frame_site_startpunkt, bg="#00001a", font=("Alegra", 30), fg="white",
    #                 textvariable=eingabe_seite2_startpunkt)
    # entry.place(relx=0.4, relwidth=0.6, relheight=1)

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

    label2 = tk.Label(frame, bg="#00001a", fg="white", font=("Alegra", 30), text="Geben Sie hier ihre Nachricht ein.")
    label2.place(relwidth=1, relheight=1)

    # Die Informationen von diesen 2 global's werden in unteren Funtionen gebraucht - Informationsspeicher

    global eingabe_nachricht
    eingabe_nachricht = StringVar()
    entry_seite_3 = tk.Entry(frame1, textvariable=eingabe_nachricht, bg="#00001a", fg="white", font=("Alegra", 30))
    entry_seite_3.place(relwidth=1, relheight=1)

    # Verschluesslungsknopf - Wenn er gedrueckt wird verweist er auf die Verschluesslungsfunktion mit command=

    button_weiter = tk.Button(frame2, text="Verschlüsseln", bg="#00001a", fg="white", font=("Alegra", 30), bd=1,
                              command=Verschluesseln)
    button_weiter.place(relwidth=1, relheight=1)

    # Entschluesslungsknopf - Verweist auf Entschluesslungfunktion mit command=

    button_weiter = tk.Button(frame3, text="Entschlüsseln", bg="#00001a", fg="white", font=("Alegra", 30), bd=1,
                              command=Entschluesseln)
    button_weiter.place(relwidth=1, relheight=1)

    global label_nachrichten
    label_nachrichten = tk.Text(frame4, fg="white", bg="#00001a", font=("Alegra", 22), bd=3)
    label_nachrichten.place(relwidth=1, relheight=1)

    # Button um das Programm nicht jedes Mal neu starten zu muessen, wenn man die Angaben der Primzahlen und des Startpunktes ändern moechte
    # Man kommt direkt auf das Menue Fenster - Neuspeicherung der Daten

    button_menue = tk.Button(frame5, image=menue_pic, bg="#00001a", fg="white", font=("Alegra", 30), bd=1, command=open)
    button_menue.place(relwidth=1, relheight=1)

    frame_for_random_prime1 = tk.Frame(root, bg="white", bd=2)
    frame_for_random_prime1.place(relx=0.89, rely=0.2, relwidth=0.1, relheight=0.1)

    def CopyPaste_message():
        entry_seite_3.delete(first=0, last=50)
        entry_seite_3.insert(tk.INSERT, verschlüsselte_nachricht)

    button_for_random_prime1 = tk.Button(frame_for_random_prime1, text="Auto", bg="#00001a", fg="white",
                                         font=("Alegra", 30), bd=1,
                                         command=CopyPaste_message)
    button_for_random_prime1.place(relwidth=1, relheight=1)

    #    scrollbar = Scrollbar(label_nachrichten)
    #    scrollbar.pack(side=RIGHT, fill=Y)

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


def Verschluesseln():
    # Die Globla's werden hier aufgenommen und in die jeweiligen variablen aufgeteilt
    # Sie liegen jedoch in Strings vor weshalb alle noch zu einer Int zahl umgewandelt werden müssen

    q = eingabe_seite2_primzahl1.get()
    p = eingabe_seite2_primzahl2.get()
    message = eingabe_nachricht.get()

    # Convert to num ist eine Funktion von "Buchstabe zu bytes"
    # Die message m wird dabei nach zu der multipliziertes Zahl der jeweiligen Zahlen von 1-256 umgeformt

    m = convert_to_num(message)
    q = int(q)
    p = int(p)
    m = int(m)
    #    e = int(e)

    # ueberpruefung von moelichen Fehlern , ein Error mit dem Text wird direkt im GUI anzeigt - der Error geht jedoch durch und somit stoppt das Programm
    # Ich weiss leider nicht wieso aber verschiedene Kombinationen mit Primzahlen unter 30 funktionieren nicht richtig und somit habe ich sie im Error File dazugefuegt
    # Ich gehe von einem mathematischen Fehler aus aber kann es mir nicht ganz erklaeren
    # Das gleiche gilt, wenn die Message = m groesser ist als die Multiplikation der 2 Primzahlen
    # Dies ist jedoch momentan auf grau, da die Zahl m durchs umwandeltn mit utf-8 viel groesser wird als p*q

    if not primzahl(p) or not primzahl(q):
        label_nachrichten.insert(tk.INSERT, "Sie haben für p oder q keine Primzahlen gewählt..\n")
        label_nachrichten.insert(tk.INSERT, "Geben Sie bitte echte Primzahlen ein.\n")
        raise (ValueError)
        # if p < 32 or q < 32:
        #    label_nachrichten.insert(tk.INSERT, "Die Primzahlen müssen grösser als 31 sein.\n")
        #    raise (ValueError)
    if m > (q * p):
        label_nachrichten.insert(tk.INSERT, "Die Nachricht ist grösser als n und somit ungültig.\n")
        label_nachrichten.insert(tk.INSERT, "Geben Sie dafür höhere Primzahlen ein.\n")
        raise (ValueError)
    if p == q:
        label_nachrichten.insert(tk.INSERT, "Sie haben für p und q die gleiche Primzahl angegeben.\n")
        label_nachrichten.insert(tk.INSERT, "Geben Sie 2 unterschiedliche Primzahlen ein.\n")
        raise (ValueError)

    # Berechnung von den Schluesseln mit Hilfe des Startpunktes x

    n = p * q

    # Carmichael’s totient function
    icm = getLCM(p - 1, q - 1)
    # In unserem Fall wird e gleichbleiben - um die gleichen Resultate zu erhalten

    global e

    #Achtung - mit output of e wird das erstbesate e bestimmt was logischerweise immer 1 ist.
    # Dies dient als Demonstrationzweck - Automatische Funktion der Primzahlen erleichtert die Anwendung
    # Weil e aber 1 ist ist d automatisch auch 1 und somit findet keine "richtige" oder sinnvolle verschlüsslung statt
    # Bei einer richigen Verschlüsslung können sie die untere Zahl von 1 auf 2 verändern, damit e und folglich auch d zu
    # sinnvollen Zahlen werden. (Mit einer 2 funktionieren Primzahlen bis knapp 10'000)
    # e = output_of_e(2, icm)

    e = output_of_e(1, icm)
    #    e = 17

    # e = 16
    #    e = random.randint(1, icm)
    #    print("Das ist e1: ", e,)

    # print(e)
    # e = 23
    global d
    d = modinv(e, icm)
    print("Das sollte d sein", d)

    global verschluesselte_nachricht
    verschluesselte_nachricht = (m ** e) % n
    print(verschluesselte_nachricht)
    # Diese print() Funktionen wollte ich den Fehler mit der Umrechnung mit utf-8 herausfinden -

    # Berechnete Zahl wird auf die 3 Seite geprinted

    label_nachrichten.insert(tk.INSERT,
                             "Ihre Verschlüsselte Nachricht lautet: " + (str(verschluesselte_nachricht) + "\n"))

    message = str.encode(message)
    h = blake2b(digest_size=1)
    h.update(message)
    digest = h.hexdigest()
    digest1 = convert_to_num(digest)
    global digital_signature
    digital_signature = (digest1 ** d) % n

    if digest1 > n:
        label_nachrichten.insert(tk.INSERT, "Die Digest der Digitaler Signatur ist zu Gross\n")
        label_nachrichten.insert(tk.INSERT, "Erhöhen Sie die 2 Primzahlen\n")
        raise (ValueError)



def Entschluesseln():
    print("das ist used_m vorher")
    print(verschluesselte_nachricht)

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

    #    if not primzahl(p) or not primzahl(q):
    #        label_nachrichten.insert(tk.INSERT, "Geben Sie bitte echte Primzahlen ein\n")
    #        raise (ValueError)
    # if p < 32 or q < 32:
    #    label_nachrichten.insert(tk.INSERT, "Die Primzahlen müssen grösser als 31 sein.\n")
    #    raise (ValueError)
    #    if m1 > (q * p):
    #        label_nachrichten.insert(tk.INSERT, "Geben Sie dafür hoehere Primzahlen ein.\n")
    #        raise (ValueError)
    #    if p == q:
    #        label_nachrichten.insert(tk.INSERT, "Geben Sie 2 unterschiedliche Primzahlen ein.\n")
    #        raise (ValueError)

    n = p * q

    # Carmichael’s totient function

    icm = getLCM(p - 1, q - 1)
    print("Das ist das icm: ", icm, )

    print("e2", e)

    #    e = 3
    #    e = random.randint(1, icm)
    #    print("Das ist e2: ", e,)

    newm = (c ** d) % n
    print("Das ist newm ", newm, )

    # Hier kommt die eigentliche Entschlüsslungs ins Spiel - Umwandlung und danach die utf-8 Umformung zurueck zum Ursprung

    # Hier kommt die Funktion von Buchtstaben zu bytes ins Spiel

    decrypted_message = convert_to_text(newm)
    label_nachrichten.insert(tk.INSERT, "Ihre Entschlüsselte Nachricht lautet: " + (str(decrypted_message) + "\n"))

    decrypted_message = str.encode(decrypted_message)
    h = blake2b(digest_size=1)
    h.update(decrypted_message)
    digest = h.hexdigest()
    digest1 = convert_to_num(digest)
    decrypted_digital_signature = (digital_signature ** e) % n

    if digest1 == decrypted_digital_signature:
        label_nachrichten.insert(tk.INSERT, "Diese Nachricht ist Valid!" + "\n" "\n")

    else:
        label_nachrichten.insert(tk.INSERT, "Diese Nachricht ist Invalid!" + "\n" + "\n")

    mainloop()


def open3():
    canvas.pack()
    background_image = tk.PhotoImage(file="Sunset.png")
    background_label_huch = tk.Label(root, image=background_image)
    background_label_huch.place(relx=0, rely=0, relwidth=1, relheight=1)

    frame = tk.Frame(root, bg="white", bd=2)
    frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

    frame1 = tk.Frame(root, bg="white", bd=2)
    frame1.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.1, anchor="n")

    frame_site_primzahl = tk.Frame(root, bg="white", bd=2)
    frame_site_primzahl.place(relx=0.5, rely=0.35, relwidth=0.5, relheight=0.1, anchor="n")

    frame_site_primzahl2 = tk.Frame(root, bg="white", bd=2)
    frame_site_primzahl2.place(relx=0.5, rely=0.65, relwidth=0.5, relheight=0.1, anchor="n")

    frame_site_primzahl3 = tk.Frame(root, bg="white", bd=2)
    frame_site_primzahl3.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.1, anchor="n")

    label2 = tk.Label(frame, text="Erstellen Sie die Blöcke der Blockchain.", bg="#00001a", fg="white",
                      font=("Alegra", 30))
    label2.place(relwidth=1, relheight=1)

    label3 = tk.Label(frame1, text="Geben Sie dazu die benötigten Daten ein.", bg="#00001a", fg="white",
                      font=("Alegra", 30))
    label3.place(relwidth=1, relheight=1)

    global input_Glaeubiger
    input_Glaeubiger = StringVar()
    entry = tk.Entry(frame_site_primzahl, bg="#00001a", font=("Alegra", 30), fg="white",
                     textvariable=input_Glaeubiger)
    entry.place(relx=0.4, relwidth=0.6, relheight=1)

    global input_Schuldner
    input_Schuldner = StringVar()
    entry1 = tk.Entry(frame_site_primzahl3, bg="#00001a", font=("Alegra", 30), fg="white",
                      textvariable=input_Schuldner)
    entry1.place(relx=0.4, relwidth=0.6, relheight=1)

    global input_Geldbetrag
    input_Geldbetrag = StringVar()
    entry2 = tk.Entry(frame_site_primzahl2, bg="#00001a", font=("Alegra", 30), fg="white",
                      textvariable=input_Geldbetrag)
    entry2.place(relx=0.4, relwidth=0.6, relheight=1)

    label_seite1 = tk.Label(frame_site_primzahl, text="Schuldner :", bg="#00001a", fg="white",
                            font=("Alegra", 28))
    label_seite1.place(relwidth=0.4, relheight=1)

    label_seite2 = tk.Label(frame_site_primzahl3, text="Gläubiger :", bg="#00001a", fg="white",
                            font=("Alegra", 28))
    label_seite2.place(relwidth=0.4, relheight=1)

    label_seite3 = tk.Label(frame_site_primzahl2, text="Geldbetrag:", bg="#00001a", fg="white",
                            font=("Alegra", 28))
    label_seite3.place(relwidth=0.4, relheight=1)

    frame_button_uebersicht = tk.Frame(root, bg="white", bd=2)
    frame_button_uebersicht.place(relx=0.2, rely=0.85, relwidth=0.3, relheight=0.1, anchor="n")

    button_weiter = tk.Button(frame_button_uebersicht, text="Übersicht", bg="#00001a", fg="white", font=("Alegra", 30),
                              bd=1,
                              command=open5)
    button_weiter.place(relwidth=1, relheight=1)

    frame_button_weitern_block = tk.Frame(root, bg="white", bd=2)
    frame_button_weitern_block.place(relx=0.5, rely=0.85, relwidth=0.3, relheight=0.1, anchor="n")

    button_weiter = tk.Button(frame_button_weitern_block, text="Neuer Block", bg="#00001a", fg="white",
                              font=("Alegra", 30), bd=1,
                              command=open4)
    button_weiter.place(relwidth=1, relheight=1)

    frame_button_manipulation = tk.Frame(root, bg="white", bd=2)
    frame_button_manipulation.place(relx=0.8, rely=0.85, relwidth=0.3, relheight=0.1, anchor="n")

    button_weiter = tk.Button(frame_button_manipulation, text="Manipulation", bg="#00001a", fg="white",
                              font=("Alegra", 30), bd=1,
                              command=manipulation)
    button_weiter.place(relwidth=1, relheight=1)

    frame_for_random_prime1 = tk.Frame(root, bg="white", bd=2)
    frame_for_random_prime1.place(relx=0.77, rely=0.5, relwidth=0.1, relheight=0.1)

    def CopyPaste_message_for_blockchain():
        entry.delete(first=0, last=50)
        entry1.delete(first=0, last=50)
        entry2.delete(first=0, last=50)
        entry.insert(tk.INSERT, random.choice(Namelist))
        entry1.insert(tk.INSERT, random.choice(Namelist))
        entry2.insert(tk.INSERT, random.choice(Numberlist))

    button_for_random_prime1 = tk.Button(frame_for_random_prime1, text="Auto", bg="#00001a", fg="white",
                                         font=("Alegra", 30), bd=1,
                                         command=CopyPaste_message_for_blockchain)
    button_for_random_prime1.place(relwidth=1, relheight=1)

    mainloop()


variable_i = 0


def open4():
    global variable_i
    variable_i += 1

    Geldbetrag = input_Geldbetrag.get()
    Schuldner = input_Schuldner.get()
    Glaeubiger = input_Glaeubiger.get()

    Kosch_Coin.addBlock(
        Block(variable_i, variable_i, time.asctime(time.localtime(time.time())), Geldbetrag, Schuldner, Glaeubiger))

    mainloop()

    return variable_i


def open5():
    canvas.pack()
    background_image = tk.PhotoImage(file="Sunset.png")
    background_label_huch = tk.Label(root, image=background_image)
    background_label_huch.place(relx=0, rely=0, relwidth=1, relheight=1)

    frame = tk.Frame(root, bg="white", bd=2)
    frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

    label2 = tk.Label(frame, text="Hier erhalten Sie eine Übersicht der Blockchain.", bg="#00001a", fg="white",
                      font=("Alegra", 30))
    label2.place(relwidth=1, relheight=1)

    frame_for_Blockchain = tk.Frame(root, bg="white", bd=2)
    frame_for_Blockchain.place(relx=0.075, rely=0.225, relwidth=0.85, relheight=0.6)

    label_for_Blockchain = tk.Text(frame_for_Blockchain, fg="white", bg="#00001a", font=("Alegra", 19), bd=3)
    label_for_Blockchain.place(relwidth=1, relheight=1)

    frame_button_manipulation = tk.Frame(root, bg="white", bd=2)
    frame_button_manipulation.place(relx=0.8, rely=0.85, relwidth=0.3, relheight=0.1, anchor="n")

    button_weiter = tk.Button(frame_button_manipulation, text="Manipulation", bg="#00001a", fg="white",
                              font=("Alegra", 30), bd=1,
                              command=manipulation)
    button_weiter.place(relwidth=1, relheight=1)

    frame_button_zurueck = tk.Frame(root, bg="white", bd=2)
    frame_button_zurueck.place(relx=0.5, rely=0.85, relwidth=0.3, relheight=0.1, anchor="n")

    button_zurueck = tk.Button(frame_button_zurueck, text="Zurück", bg="#00001a", fg="white",
                               font=("Alegra", 30), bd=1,
                               command=open3)
    button_zurueck.place(relwidth=1, relheight=1)

    frame_button_wallet = tk.Frame(root, bg="white", bd=2)
    frame_button_wallet.place(relx=0.2, rely=0.85, relwidth=0.3, relheight=0.1, anchor="n")

    button_wallet = tk.Button(frame_button_wallet, text="Wallet", bg="#00001a", fg="white",
                              font=("Alegra", 30), bd=1,
                              command=wallet_opener)
    button_wallet.place(relwidth=1, relheight=1)

    for b in Kosch_Coin.chain:
        print(b)
        label_for_Blockchain.insert(tk.INSERT, str(b) + "\n")

    if str(Kosch_Coin.validate_Chain()) == "True":
        label_for_Blockchain.insert(tk.INSERT, "Diese Blockchain ist valid!" + "\n")

    if str(Kosch_Coin.validate_Chain()) == "False":
        label_for_Blockchain.insert(tk.INSERT, "Der Block " + str(input_Block.get()) + " der Chain ist invalid!" + "\n")

    if str(Kosch_Coin.validate_Chain()) == "None":
        label_for_Blockchain.insert(tk.INSERT, "Die chain ist invalid!" + "\n")

    mainloop()


def wallet_opener():
    canvas.pack()
    background_image = tk.PhotoImage(file="Sunset.png")
    background_label_huch = tk.Label(root, image=background_image)
    background_label_huch.place(relx=0, rely=0, relwidth=1, relheight=1)

    frame = tk.Frame(root, bg="white", bd=2)
    frame.place(relx=0.5, rely=0.1, relwidth=0.85, relheight=0.1, anchor="n")

    frame1 = tk.Frame(root, bg="white", bd=2)
    frame1.place(relx=0.5, rely=0.2, relwidth=0.85, relheight=0.1, anchor="n")

    frame_site_primzahl3 = tk.Frame(root, bg="white", bd=2)
    frame_site_primzahl3.place(relx=0.5, rely=0.5, relwidth=0.7, relheight=0.1, anchor="n")

    label2 = tk.Label(frame, text="Hier bekommen Sie einen Einblick auf ihr Guthaben.", bg="#00001a", fg="white",
                      font=("Alegra", 30))
    label2.place(relwidth=1, relheight=1)

    label3 = tk.Label(frame1, text="Dieses Guthaben erzielten Sie durch ihr Mining.", bg="#00001a", fg="white",
                      font=("Alegra", 30))
    label3.place(relwidth=1, relheight=1)

    label4 = tk.Text(frame_site_primzahl3, bg="#00001a", font=("Alegra", 30), fg="white", )
    label4.place(relx=0.4, relwidth=0.6, relheight=1)

    label_seite3 = tk.Label(frame_site_primzahl3, text="Ihr Guthaben :", bg="#00001a", fg="white",
                            font=("Alegra", 28))
    label_seite3.place(relwidth=0.4, relheight=1)

    frame_button_uebersicht = tk.Frame(root, bg="white", bd=2)
    frame_button_uebersicht.place(relx=0.35, rely=0.85, relwidth=0.3, relheight=0.1, anchor="n")

    button_weiter = tk.Button(frame_button_uebersicht, text="Übersicht", bg="#00001a", fg="white", font=("Alegra", 30),
                              bd=1,
                              command=open5)
    button_weiter.place(relwidth=1, relheight=1)

    frame_button_weitern_block = tk.Frame(root, bg="white", bd=2)
    frame_button_weitern_block.place(relx=0.65, rely=0.85, relwidth=0.3, relheight=0.1, anchor="n")

    button_weiter = tk.Button(frame_button_weitern_block, text="Neuer Block", bg="#00001a", fg="white",
                              font=("Alegra", 30), bd=1,
                              command=open3)
    button_weiter.place(relwidth=1, relheight=1)

    Guthaben_Coin = variable_i * 6.25

    label4.insert(tk.INSERT, "      " + str(Guthaben_Coin) + " Kosch Coins")

    mainloop()


def manipulation():
    canvas.pack()
    background_image = tk.PhotoImage(file="Sunset.png")
    background_label_huch = tk.Label(root, image=background_image)
    background_label_huch.place(relx=0, rely=0, relwidth=1, relheight=1)

    frame = tk.Frame(root, bg="white", bd=2)
    frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

    frame1 = tk.Frame(root, bg="white", bd=2)
    frame1.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.1, anchor="n")

    frame2 = tk.Frame(root, bg="white", bd=2)
    frame2.place(relx=0.5, rely=0.3, relwidth=0.75, relheight=0.1, anchor="n")

    frame_site_primzahl3 = tk.Frame(root, bg="white", bd=2)
    frame_site_primzahl3.place(relx=0.5, rely=0.57, relwidth=0.5, relheight=0.1, anchor="n")

    label2 = tk.Label(frame, text="Welchen Block möchten Sie verändern?", bg="#00001a", fg="white",
                      font=("Alegra", 30))
    label2.place(relwidth=1, relheight=1)

    label3 = tk.Label(frame1, text="Geben Sie dazu die Blocknummer an.", bg="#00001a", fg="white",
                      font=("Alegra", 30))
    label3.place(relwidth=1, relheight=1)

    label3 = tk.Label(frame2, text="Beachten Sie, dass es nicht der letzte Block ist.", bg="#00001a", fg="white",
                      font=("Alegra", 30))
    label3.place(relwidth=1, relheight=1)

    global input_Block
    input_Block = StringVar()
    entry1 = tk.Entry(frame_site_primzahl3, bg="#00001a", font=("Alegra", 30), fg="white",
                      textvariable=input_Block)
    entry1.place(relx=0.4, relwidth=0.6, relheight=1)

    label_seite3 = tk.Label(frame_site_primzahl3, text="Block :", bg="#00001a", fg="white",
                            font=("Alegra", 28))
    label_seite3.place(relwidth=0.4, relheight=1)

    frame_button_uebersicht = tk.Frame(root, bg="white", bd=2)
    frame_button_uebersicht.place(relx=0.2, rely=0.85, relwidth=0.3, relheight=0.1, anchor="n")

    button_weiter = tk.Button(frame_button_uebersicht, text="Übersicht", bg="#00001a", fg="white", font=("Alegra", 30),
                              bd=1,
                              command=open5)
    button_weiter.place(relwidth=1, relheight=1)

    frame_button_weitern_block = tk.Frame(root, bg="white", bd=2)
    frame_button_weitern_block.place(relx=0.5, rely=0.85, relwidth=0.3, relheight=0.1, anchor="n")

    button_weiter = tk.Button(frame_button_weitern_block, text="Weiter", bg="#00001a", fg="white",
                              font=("Alegra", 30), bd=1,
                              command=selection_variable)
    button_weiter.place(relwidth=1, relheight=1)

    frame_button_manipulation = tk.Frame(root, bg="white", bd=2)
    frame_button_manipulation.place(relx=0.8, rely=0.85, relwidth=0.3, relheight=0.1, anchor="n")

    button_weiter = tk.Button(frame_button_manipulation, text="Zurück", bg="#00001a", fg="white",
                              font=("Alegra", 30), bd=1,
                              command=open3)
    button_weiter.place(relwidth=1, relheight=1)

    mainloop()


def selection_variable():
    canvas.pack()
    background_image = tk.PhotoImage(file="Sunset.png")
    background_label_huch = tk.Label(root, image=background_image)
    background_label_huch.place(relx=0, rely=0, relwidth=1, relheight=1)

    frame = tk.Frame(root, bg="white", bd=2)
    frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

    frame_site_primzahl3 = tk.Frame(root, bg="white", bd=2)
    frame_site_primzahl3.place(relx=0.5, rely=0.3, relwidth=0.5, relheight=0.1, anchor="n")

    frame_site_primzahl2 = tk.Frame(root, bg="white", bd=2)
    frame_site_primzahl2.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.1, anchor="n")

    frame_site_primzahl1 = tk.Frame(root, bg="white", bd=2)
    frame_site_primzahl1.place(relx=0.5, rely=0.7, relwidth=0.5, relheight=0.1, anchor="n")

    label2 = tk.Label(frame, text="Welche Variable möchten Sie verändern?", bg="#00001a", fg="white",
                      font=("Alegra", 30))
    label2.place(relwidth=1, relheight=1)

    button_3 = tk.Button(frame_site_primzahl3, text="Schuldner", bg="#00001a", fg="white", font=("Alegra", 30), bd=1,
                         command=change_Sender)

    button_3.place(relwidth=1, relheight=1)

    button_2 = tk.Button(frame_site_primzahl2, text="Gläubiger", bg="#00001a", fg="white", font=("Alegra", 30), bd=1,
                         command=change_Receiver)

    button_2.place(relwidth=1, relheight=1)

    button_1 = tk.Button(frame_site_primzahl1, text="Geldbetrag", bg="#00001a", fg="white", font=("Alegra", 30), bd=1,
                         command=change_Geldbetrag)

    button_1.place(relwidth=1, relheight=1)

    mainloop()


def change_Sender():
    canvas.pack()
    background_image = tk.PhotoImage(file="Sunset.png")
    background_label_huch = tk.Label(root, image=background_image)
    background_label_huch.place(relx=0, rely=0, relwidth=1, relheight=1)

    frame = tk.Frame(root, bg="white", bd=2)
    frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

    frame_site_primzahl3 = tk.Frame(root, bg="white", bd=2)
    frame_site_primzahl3.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.1, anchor="n")

    label2 = tk.Label(frame, text="Geben Sie den neuen Schuldner ein.", bg="#00001a", fg="white",
                      font=("Alegra", 30))
    label2.place(relwidth=1, relheight=1)

    global input_new_Sender
    input_new_Sender = StringVar()
    entry1 = tk.Entry(frame_site_primzahl3, bg="#00001a", font=("Alegra", 30), fg="white",
                      textvariable=input_new_Sender)
    entry1.place(relx=0.4, relwidth=0.6, relheight=1)

    label_seite3 = tk.Label(frame_site_primzahl3, text="Schuldner :", bg="#00001a", fg="white",
                            font=("Alegra", 25))
    label_seite3.place(relwidth=0.4, relheight=1)

    frame_button_weitern_block = tk.Frame(root, bg="white", bd=2)
    frame_button_weitern_block.place(relx=0.5, rely=0.85, relwidth=0.3, relheight=0.1, anchor="n")

    button_weiter = tk.Button(frame_button_weitern_block, text="Verändern", bg="#00001a", fg="white",
                              font=("Alegra", 30), bd=1,
                              command=change_sender1)
    button_weiter.place(relwidth=1, relheight=1)

    Kosch_Coin.chain[int(input_Block.get())].schuldner = input_new_Sender.get()

    mainloop()


def change_sender1():
    Kosch_Coin.chain[int(input_Block.get())].schuldner = input_new_Sender.get()
    recalculate_hash()


def change_Receiver():
    canvas.pack()
    background_image = tk.PhotoImage(file="Sunset.png")
    background_label_huch = tk.Label(root, image=background_image)
    background_label_huch.place(relx=0, rely=0, relwidth=1, relheight=1)

    frame = tk.Frame(root, bg="white", bd=2)
    frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

    frame_site_primzahl3 = tk.Frame(root, bg="white", bd=2)
    frame_site_primzahl3.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.1, anchor="n")

    label2 = tk.Label(frame, text="Geben Sie den neuen Gläubiger ein.", bg="#00001a", fg="white",
                      font=("Alegra", 30))
    label2.place(relwidth=1, relheight=1)

    global input_new_Receiver
    input_new_Receiver = StringVar()
    entry1 = tk.Entry(frame_site_primzahl3, bg="#00001a", font=("Alegra", 30), fg="white",
                      textvariable=input_new_Receiver)
    entry1.place(relx=0.4, relwidth=0.6, relheight=1)

    label_seite3 = tk.Label(frame_site_primzahl3, text="Gläubiger:", bg="#00001a", fg="white",
                            font=("Alegra", 25))
    label_seite3.place(relwidth=0.4, relheight=1)

    frame_button_weitern_block = tk.Frame(root, bg="white", bd=2)
    frame_button_weitern_block.place(relx=0.5, rely=0.85, relwidth=0.3, relheight=0.1, anchor="n")

    button_weiter = tk.Button(frame_button_weitern_block, text="Verändern", bg="#00001a", fg="white",
                              font=("Alegra", 30), bd=1,
                              command=change_receiver1)
    button_weiter.place(relwidth=1, relheight=1)

    mainloop()


def change_receiver1():
    Kosch_Coin.chain[int(input_Block.get())].glaeubiger = input_new_Receiver.get()
    recalculate_hash()


def change_Geldbetrag():
    canvas.pack()
    background_image = tk.PhotoImage(file="Sunset.png")
    background_label_huch = tk.Label(root, image=background_image)
    background_label_huch.place(relx=0, rely=0, relwidth=1, relheight=1)

    frame = tk.Frame(root, bg="white", bd=2)
    frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

    frame_site_primzahl3 = tk.Frame(root, bg="white", bd=2)
    frame_site_primzahl3.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.1, anchor="n")

    label2 = tk.Label(frame, text="Geben Sie den neuen Geldbetrag ein.", bg="#00001a", fg="white",
                      font=("Alegra", 30))
    label2.place(relwidth=1, relheight=1)

    global input_new_Geldbetrag
    input_new_Geldbetrag = StringVar()
    entry1 = tk.Entry(frame_site_primzahl3, bg="#00001a", font=("Alegra", 30), fg="white",
                      textvariable=input_new_Geldbetrag)
    entry1.place(relx=0.4, relwidth=0.6, relheight=1)

    label_seite3 = tk.Label(frame_site_primzahl3, text="Geldbetrag :", bg="#00001a", fg="white",
                            font=("Alegra", 25))
    label_seite3.place(relwidth=0.4, relheight=1)

    frame_button_weitern_block = tk.Frame(root, bg="white", bd=2)
    frame_button_weitern_block.place(relx=0.5, rely=0.85, relwidth=0.3, relheight=0.1, anchor="n")

    button_weiter = tk.Button(frame_button_weitern_block, text="Verändern", bg="#00001a", fg="white",
                              font=("Alegra", 30), bd=1,
                              command=change_Geldbetrag1)
    button_weiter.place(relwidth=1, relheight=1)

    mainloop()


def change_Geldbetrag1():
    Kosch_Coin.chain[int(input_Block.get())].transaction = input_new_Geldbetrag.get()
    recalculate_hash()


def recalculate_hash():
    canvas.pack()
    background_image = tk.PhotoImage(file="Sunset.png")
    background_label_huch = tk.Label(root, image=background_image)
    background_label_huch.place(relx=0, rely=0, relwidth=1, relheight=1)

    frame = tk.Frame(root, bg="white", bd=2)
    frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

    frame_site_primzahl3 = tk.Frame(root, bg="white", bd=2)
    frame_site_primzahl3.place(relx=0.5, rely=0.3, relwidth=0.5, relheight=0.1, anchor="n")

    frame_site_primzahl2 = tk.Frame(root, bg="white", bd=2)
    frame_site_primzahl2.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.1, anchor="n")

    label2 = tk.Label(frame, text="Wollen Sie den Hash des Blockes nachberechnen?", bg="#00001a", fg="white",
                      font=("Alegra", 30))
    label2.place(relwidth=1, relheight=1)

    button_3 = tk.Button(frame_site_primzahl3, text="Ja", bg="#00001a", fg="white", font=("Alegra", 30), bd=1,
                         command=recalculate_hash_yes)

    button_3.place(relwidth=1, relheight=1)

    button_2 = tk.Button(frame_site_primzahl2, text="Nein", bg="#00001a", fg="white", font=("Alegra", 30), bd=1,
                         command=Go_Back)

    button_2.place(relwidth=1, relheight=1)

    mainloop()


def recalculate_hash_yes():
    Kosch_Coin.chain[int(input_Block.get())].hash = Kosch_Coin.chain[int(input_Block.get())].calcHash()
    open3()


def Go_Back():
    open3()


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

label3 = tk.Label(frame1, text="Zu welchem Bereich wollen Sie?", bg="#00001a", fg="white",
                  font=("Alegra", 30))
label3.place(relwidth=1, relheight=1)

# Hier wird beim druecken des Knopfes die 2 Seite aufgerufen

button = tk.Button(frame_button_yes, text="Verschlüsslung", bg="#00001a", fg="white", font=("Alegra", 30), bd=2,
                   command=open)
button.place(relwidth=1, relheight=1)

button_no = tk.Button(frame_button_no, text="Blockchain", bg="#00001a", fg="white", font=("Alegra", 30), bd=1,
                      command=open3)
button_no.place(relwidth=1, relheight=1)

root.mainloop()
