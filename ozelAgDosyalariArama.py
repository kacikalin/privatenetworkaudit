import os
import re


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
    
if __name__ == "__main__":
    print ("Özel ağlar olabilecek dizin ve dosyalar:")
    main()
    print("\n Bilgisayarda D dizininde bulunan adres bilgileri:")
    powerShell()
