import os
import re

#Parametre olarak gonderilen kelimeleri dizinde arar. Gonderilen kelimeler private blokchain olustururken olusan klasor ve dosyalar icin
#ozel olarak olusturulmustur.
def dosyalari_bul(aranankelimeler, dizin):

    files = []

    for root, directories, filenames in os.walk(dizin):

        for filename in filenames:

            if any(word in filename for word in aranankelimeler):
                files.append(os.path.join(root, filename))

    return files


def powerShell():
    p=subprocess.Popen('powershell.exe Get-ChildItem –Path D:\ -Recurse –File | Where-Object {$_.Name –match \'[a-fA-F0-9]{40}\'}' ,stdout=sys.stdout)
    p.communicate()
    
def main():
    aranankelimeler = ["contracts","geth","node-modules","nodes", "genesis","clef","truffle","hardhat","ganache"]

    dizin = "C:\\OrnekDizin"

    files = dosyalari_bul(aranankelimeler, dizin)

    for file in files:
        print(file)
##Powershell komutu calistirabilmak icin powershell.exe nin oldugu C:\Windows\System32\WindowsPowerShell\v1.0\ dizininin Path'e eklenmesi gerekiyor.
def powerShell():
    p=subprocess.Popen('powershell.exe Get-ChildItem –Path D:\ -Recurse –File | Where-Object {$_.Name –match \'[a-fA-F0-9]{40}\'}' ,stdout=sys.stdout)
    p.communicate()
    
def getConnections():
    port="8545" #Buraya 1. adımda elde edilen konfigurasyon dosyasında bulunan port bilgileri girilir.
    c = subprocess.Popen('powershell.exe netstat -ano | findstr :'+port,stdout=sys.stdout)
    c.communicate()    
    
if __name__ == "__main__":
    print ("Özel ağlar olabilecek dizin ve dosyalar:")
    main()
    print("\n Bilgisayarda D dizininde bulunan adres bilgileri:")
    powerShell()
    print("\n 3. Bilgisayar ile özel portlar üzerinden iletişim kuran bilgisayarlar")
    getConnections()
    print("\n 4.Remix IDE uzerinden akıllı sözleşme geliştirildiğinin kontrolü için tarayıcıdan https://remix.ethereum.org/ açıp contracts klasörünün altında eklenen sözleşme var mı diye kontrol ediniz.")
    print("\n 5. Ganache UI üzerinden transaction input verisi alınarak kullanılacak yönteme parametre olarak verilir. ÖR: https://ethervm.io/decompile adresinde bulunan alana yapıştırılarak decompile edilir.")

