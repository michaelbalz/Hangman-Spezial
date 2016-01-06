#Bibliothek für Zufallsentscheidungen wird importiert
import random


print ("Willkommen bei Hangman-Spezial! Der Galgen spielt hier aus Jugendschutzgründen keine Rolle aber das Prinzip bleibt das Gleiche: Entweder das Wort vom Computer oder das deines Mitspielers zu erraten.\n")
print("Entscheide dich für Einzelspieler (1) oder Mehrspieler, wenn ihr zu zweit seid (2):\n") 

#Die Auswahl, ob man "Einzelspieler" oder "Mehrspieler" spielen möchte, erfolgt  durch die Variable: Figuren 
figuren = ("Einzelspieler?", "Mehrspieler?")
spielen = True

while spielen:
    #Spielerfigur auswählen
    spielerauswahl = 0

    #Es wird gesichert, dass nur die "1" für Einzelspieler oder die "2" für Mehrspieler eingegeben wird
    while True:
        try:
            spielerauswahl = int(input("[1]Einzelspieler? [2]Mehrspieler?\n"))
            if spielerauswahl != 1 and spielerauswahl!= 2:
                print("Das habe ich nicht verstanden. Bitte nur Zahlen (1 oder 2) eingeben")
            else:
                break
        except:
            print("Das habe ich nicht verstanden. Bitte nur Zahlen (1 oder 2) eingeben")

    #Da bei einem String das erste Element = 0 ist muss also von der eigentlichen Spielerauswahl 1 abgezogen werden
    spielerfigur = figuren[spielerauswahl - 1]
    


    #Nachfolgend der Quellcode für Mehrspieler (wird durch Spielerauswahl == 1 eingeleitet)
    if spielerauswahl == 2:
            print("***********")
            print("* HANGMAN *")
            print("***********\n\n")
            print("Einige dich mit deinem Mitspieler wer sich das Wort ausdenken soll, dass der Andere dann erraten muss.\nNachfolgend muss das Wort oder die Buchstaben, die man vermutet, in GROßBUCHSTABEN geschrieben werden (gilt nur für den Mehrspielermodus).\nDer Mitspieler, der das Wort raten soll, dreht sich jetzt um.\n")

            while True:
                richtigesWort = str(input("Schreibe das Hangmanwort in Großbuchstaben: "))

                #Überprüfung, ob der String Zahlen enthält
                if str.isalpha(richtigesWort)!= True:
                    print("Bitte gebe nur Buchstaben ein!")

                #Überprüfung, ob der String Kleinbuchstaben enthält
                elif str.isupper(richtigesWort)!= True:
                    print("Bitte gebe nur Großbuchstaben ein!")
                else:
                    break


            angezeigtesWort = ["_"] * len(richtigesWort)

            #Eingabe des Spielers
            eingabe = ""

            #Man hat 10 Fehlversuche 
            falscheVersuche = 10

            #Den Buchstaben werden Nummern zugeordnet, um diese später besser vergleichen zu können. Beispiel: Michael --> 1234567 
            buchstabenNummer = 0

            richtigeVersuche = 0

            print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("Willkommen bei Hangman! Das Wort deines Mitspielers wurde nach oben verschoben. Scrolle also nicht nach oben, um den Spielwitz zu erhalten!\nDu hast 10 Fehlversuche zur Verfügung, um das gesuchte Wort zu erraten.\n Wenn du einen Buchstaben richtig rätst, wird dir kein Versuch abgezogen.\nWenn du jedoch einen Buchstaben, der im Wort mehrmals vorkommt, errätst, bekommst du die jeweilige Anzahl an Versuchen gutgeschrieben(Beispiel 3*A --> 2 Versuche plus)")
            print("Wenn du jedoch schon vorher aufhören möchtest, dann schreibe 'ENDE'")


            #Solange nicht "Ende" eingegeben wurde oder Fehlversuche nicht 0 sind läuft diese while-Schleife die 
            while (eingabe != "ENDE") and (falscheVersuche != 0):

                #Die Länge des Wortes wird angezeigt
                print ("Das Wort,das du suchst passt genau hier rein: " + str(angezeigtesWort))

                #Das nächste zeigt an wieviel Versuche man noch hat
                print("Du hast noch: " + str(falscheVersuche) +" Fehlversuche übrig")
                while True:
                    eingabe = input("Schreibe einen Großbuchstaben, von dem du denkst, dass er im Wort vorkommt: ")

                    #Überprüfung, ob die Eingabe Zahlen enthält
                    if str.isalpha(eingabe)!= True:
                        print("Bitte gebe Buchstaben ein!")

                    #Überprüfung, ob der String Kleinbuchstaben enthält
                    elif str.isupper(eingabe)!= True:
                        print("Bitte gebe nur Großbuchstaben ein!")
                    else:
                        break

                #Wenn der Spieler das richtige Wort eingibt, wird die Schleife beendet
                if eingabe == richtigesWort:
                    print("Herzlichen Glückwunsch, du hast das richtige Wort eingegeben! \nDu hast gewonnen!")
                    break
                #Die folgende While-Schleife läuft, so lange die buchstabenNummer kleiner ist als die Länge des Wortes 
                while (buchstabenNummer < len(richtigesWort)):
                    if(richtigesWort[buchstabenNummer] == eingabe):

                            #vergleicht die Länge des  richtigen Wortes mit der eingabe
                            angezeigtesWort[buchstabenNummer] = eingabe
                            richtigeVersuche += 1
                            falscheVersuche += 1
                    buchstabenNummer += 1
                    
                
                falscheVersuche -= 1
                buchstabenNummer = 0

                #Hier wird geschaut ob die Versuche zu der Länge des richtigen/gesuchten Wortes passen
                if(richtigeVersuche == len(richtigesWort)):
                    print("Glückwunsch, du hast gewonnen! Das gesuchte Wort war '" + richtigesWort +"'!")
                    break

                #Wenn die erlaubten Versuche jedoch 0 sind (Man hat es inerhalb der 10 Versuche nicht geschafft das Wort zu erraten) hat man verloren.
                if(falscheVersuche == 0):
                    print("Du hast leider keinen Versuch mehr. Du hast verloren! :(")



    





    #Nachfolgend der Quellcode für Einzelspieler (wird durch Spielerauswahl == 1 eingeleitet)
    elif spielerauswahl == 1:
        print("\n") 
        print("***********")
        print("* HANGMAN *")
        print("***********\n")
        print("Du musst alleine das Wort erraten. Dir stehen zwar unendlich viele Versuche zur Verfügung, jedoch ist dein Ziel es mit so wenigen Versuchen wie möglich zu erraten.\n Danach siehst du nämlich eine Tabelle, wo du dir anschauen kannst, wie gut du warst.\n")




        #mögliche Wörter, die zur Verfügung stehen
        def möglicheWörter():
            wörter = ["Himmel",
                      "Traum",
                      "Mond",
                      "Tasse",
                      "Pferd",
                      "Stein",
                      "Schulferien",
                      "Stift",
                      "Auto",
                      "Flugzeug",
                      "Wohnzimmer",
                      "Schreibtisch",
                      "Telefon",
                      "Kopfhörer",
                      "Fussball",
                      "Handtasche",
                      "Weihnachtsbaum",
                      "Stuhl",
                      "Tastatur",
                      "Fenster",
                      "Parkplatz",
                      "Sandsturm",
                      "Schiffsfahrt",
                      "Mikroskop",
                      "Mauer",
                      "Kugelschreiber",
                      "Lenkrad",
                      "Schwimmbad",
                      "Wasserfall",
                      "Heizung",
                      "Luftballon",
                      "Weihnachtsmann",
                      "Geschenke",
                      "Corvinianum",
                      "Informatik"
                      ]
            #wählt ein zufälliges Wort aus
            return random.choice(wörter).upper()

        #Hier wird überprüft, ob der eingegebene Buchstabe/Wort im gesuchten Wort vorkommt oder nicht
        def Überprüfung(wort,vermutungen,vermutung):
            vermutung = vermutung.upper()
    
            status = ""
            versuche = 0
            for buchstabe in wort:
                if buchstabe in vermutungen:
                    status += buchstabe
                else:
                    status += "['_']"
            

                if buchstabe == vermutung:
                    versuche += 1

            #Hier wird festgelegt was als Antwort zu den eingegeben Buchstaben kommen soll

            if versuche > 1:
                print ("\nJa! Das Wort hat",versuche, "'" + vermutung+"'"+"s")
            elif versuche == 1:
                print("\nJa! Das Word besitzt den Buchstaben'" + vermutung + "'")
            else:
                print("\nSorry aber das gesuchte Wort hat nicht den Buchstaben'" + vermutung + "'")

            return status


        def Hauptteil():
            #das Wort wird ausgewählt aus der oberen Liste
            wort = möglicheWörter()

            #die vermutungen bekommen eine eigene Liste um nachher zu überprüfen, ob manche Buchstaben schon eingegeben wurden
            vermutungen = []

            #vermutet wird auf "False" gesetzt da noch nicht das richtige Wort vermutet wurde. Das ändert sich zu "True" wenn das Wort herausgefunden wurde.
            vermutet = False

            #die Länge des Wortes wird angegeben
            print ("\nDas Wort hat",len(wort), "buchstaben.")
            while not vermutet:
                text="\nBitte gib einen Buchstaben oder das gesuchte Wort, das {} Buchstaben lang ist, ein.".format(len(wort))
                vermutung = input(text)
                vermutung = vermutung.upper()

                #hier wird überprüft ob ein Buchstabe schonmal vermutet wurde
                if vermutung in vermutungen:
                    print("\nUps, du hast schon den Buchstaben'" + vermutung + "' vermutet")
                elif len(vermutung) == len(wort):
                    vermutungen.append(vermutung)
                    if vermutung == wort:
                        vermutet = True
                    else:
                        print("\nSorry da ist was falsch gelaufen. Bitte nur einen Buchstaben oder das gesuchte Wort eingeben.")
                elif len(vermutung) == 1:
                    vermutungen.append(vermutung)
                    ergebnis = Überprüfung(wort,vermutungen,vermutung)
                    if ergebnis == wort:
                        vermutet = True

                    else:
                        print(ergebnis)
                else:
                    print("\nFalsche Eingabe!")

            #Nachfolgend wird die Tabelle angezeigt, in der man ablesen kann, wie gut/schlecht man war 
            print(" Richtig, das Wort ist'", wort + "'! Du hast es in ", len(vermutungen), " Versuchen geschafft. Schau dir unten in der Tabelle an, wie gut du warst!\n")
            print("|Wörter mit 3-5 Buchstaben --> PROFI= 5-8 Versuche; NORMALERSPIELER= 9-12; LOOSER= 13-unendlich        | ")
            print("|Wörter mit 6-10 Buchstaben --> PROFI= 5-12 Versuche; NORMALERSPIELER= 13-16; LOOSER= 17-unendlich     | ")
            print("|Wörter mit 11-mehr Buchstaben --> PROFI= 5-15 Versuche; NORMALERSPIELER= 16-19; LOOSER= 20-unendlich  | ")
        Hauptteil()
    
    
  









   

  
