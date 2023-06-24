import os

import re


def dosyalari_bul(aranankelimeler, dizin):

    files = []

    for root, directories, filenames in os.walk(dizin):

        for filename in filenames:

            if any(word in filename for word in aranankelimeler):
                files.append(os.path.join(root, filename))

    return files


def main():
    aranankelimeler = ["contracts","geth","node-modules","nodes", "genesis","clef","truffle","hardhat","ganache"]

    dizin = "C:\\OrnekDizin"

    files = dosyalari_bul(aranankelimeler, dizin)

    for file in files:
        print(file)


if __name__ == "__main__":
    print ("Özel ağlar olabilecek dizin ve dosyalar:")
    main()
    print("\n Bilgisayarda D dizininde bulunan adres bilgileri:")
    powerShell()
