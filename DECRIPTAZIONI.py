from time import sleep
import pyAesCrypt
import sys


bufferSize = 64 * 1024

print("DECRIPTAZIONI")
print("-------------------------------\n")
print("(digita il numero corrispondente per scegliere)\n")
print("1. Cripta un file")
print("2. Decripta un file")
print("99. Esci")
sleep(0.2)
a = input(">>> ")

if a == "1":
    print("Inserisci il nome del file da criptare:")
    sleep(0.2)
    file = input(">>> ")
    finale = str(file + ".aes")
    print("Inserisci la password con la quale criptare il file. Ricordala bene!")
    sleep(0.2)
    pw = input(">>> ")
    pw = str(pw)
    print("Il file da criptare è: " + file)
    print("La pw è: " + pw)
    sleep(2)
    
    try:
        pyAesCrypt.encryptFile(file, finale, pw, bufferSize)
    except:
        print("Controlla il percorso del file che devi criptare.")
    sleep(0.2)
    print("Il file è stato criptato con sussesso.")
    print("Puoi tanquillamente condividerlo su Google Drive.")
    print("Ricordati di eliminare il file originale. Quello criptato si chiama " + finale)
    sleep(2)
    exit()

    sleep(1)
    print("Qualcosa è andato storto.")
    exit()
        
elif a == "2":
    print("Inserisci il nome del file da decriptare SENZA includere l'estensione .aes:")
    sleep(0.2)
    file = input(">>> ")
    finale = file
    file = finale + ".aes"
    print("Inserisci la password per decifrare il file. Attenzione ad eventuali maiuscole!:")
    sleep(0.2)
    pw = input(">>> ")
    pw = str(pw)
    print("Il file da decriptare è: " + file)
    print("La pw è: " + pw)
    sleep(2)

    try:
        pyAesCrypt.decryptFile(file, finale, pw, bufferSize)
    except:
        sleep(1)
        print("Qualcosa è andato storto. Il file può essere danneggito, puoi aver inserito un nome sbagliato o forse hai messo una password errata. Riprova!")
        exit()

    sleep(0.2)
    print("Il file è stato decriptato con sussesso.")
    print("Puoi utilizzarlo e modificarlo in locale per poi ri prittarlo per metterlo su Google Drive.")
    print("Ricordati di eliminare il file criptato o farai confusione. Quello decriptato si chiama " + finale)
