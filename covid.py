#coding: utf-8
import requests, json, sys, os 

h = "\33[0;32m"
hm = "\33[32;1m"
b = "\33[0;36m"
bm = "\33[36;1m"
m = "\33[31;1m"
mg = "\33[0;31m"
p = "\33[37;1m"
pg = "\33[37;0m"
hit = "\33[30;1m"
o = "\33[33;1m"
km = "\33[1;33m"
k = "\33[0;33m"

def banner() :
  os.system("clear")
  r = requests.get("https://api.kawalcorona.com/positif")
  j = json.loads(r.text)
  re = requests.get("https://api.kawalcorona.com/sembuh")
  js = json.loads(re.text)
  req = requests.get("https://api.kawalcorona.com/meninggal")
  jsn = json.loads(req.text)
  print p + '''

 ██████  ██████  ██    ██ ██ ██████         ██  █████  
██      ██    ██ ██    ██ ██ ██   ██       ███ ██   ██ 
██      ██    ██ ██    ██ ██ ██   ██ █████  ██  ██████ 
██      ██    ██  ██  ██  ██ ██   ██        ██      ██ 
 ██████  ██████    ████   ██ ██████         ██  █████  
                                                       '''
  print m + "         Data API : https://kawalcorona.com"
  print 50 * '\x1b[1;37m\xe2\x95\x90'
  print pg +"Total positif "+ bm +">"+ m +" " + j["value"] + " "+ pg +"orang"
  print pg +"Total sembuh "+ bm +">"+ hm +" " + js["value"] + " "+ pg +"orang"
  print pg +"Total meninggal "+ bm +">"+ km +" " + jsn["value"] + " "+ pg +"orang"
  print 50 * '\x1b[1;37m\xe2\x95\x90' + p


def indonesia() : 
  r = requests.get("https://api.kawalcorona.com/indonesia")
  j = json.loads(r.text)
  for i in j :
    print pg + "Positif "+ bm +">"+ m +" " + i["positif"] + " "+ pg +"orang"
    print pg + "Sembuh "+ bm +">"+ hm +" " + i["sembuh"] + " "+ pg +"orang"
    print pg + "Meninggal "+ bm +">"+ km +" " + i["meninggal"] + " "+ p +"orang"
    print pg + "Dirawat "+ bm +">"+ bm +" " + i["dirawat"] + " "+ pg +"orang"
    
def provinsi() :
  r = requests.get("https://api.kawalcorona.com/indonesia/provinsi")
  j = json.loads(r.text)
  for i in j :
    print pg + "\nProvinsi \33[36;1m>\33[37;0m",i["attributes"]["Provinsi"]
    print pg + "Positif \33[36;1m>\33[31;1m",i["attributes"]["Kasus_Posi"],"\33[37;0morang"
    print pg + "Sembuh \33[36;1m>\33[32;1m",i["attributes"]["Kasus_Semb"],"\33[37;0morang"
    print pg + "Meninggal \33[36;1m>\33[33;1m",i["attributes"]["Kasus_Meni"],"\33[37;0morang"
    print 37 * '\x1b[1;97m\xe2\x95\x90'
  raw_input("Kembali")
  menu()
  choose()


def negara() :
  r = requests.get("https://api.kawalcorona.com/")
  j = json.loads(r.text)
  for i in j :
    print pg + "\nNegara \33[36;1m>\33[37;0m",i["attributes"]["Country_Region"]
    print pg + "Positif \33[36;1m>\33[31;1m",i["attributes"]["Confirmed"], "\33[37;0morang"
    print pg + "Sembuh \33[36;1m>\33[32;1m",i["attributes"]["Recovered"], "\33[37;0morang"
    print pg + "Meninggal \33[36;1m>\33[33;1m",i["attributes"]["Deaths"], "\33[37;0morang"
    print pg + "Dirawat \33[36;1m>",i["attributes"]["Active"], "\33[37;0morang"
    print 37 * '\x1b[1;97m\xe2\x95\x90' 
    
def menu() :
  banner()
  print "1. Indonesia"
  print "2. Seluruh dunia"
  print m + "3. Keluar.."
  
def choose2() :
  pi = raw_input("\nTampilkan data provinsi? Y/N +> ")
  if pi.lower() == "y" :
    provinsi()
  else:
    raw_input("Kembali")
    banner()
    choose()
  
def choose() :
  pil = raw_input(p + "Pilih "+ hm +"+"+ bm +"> " + p)
  if pil == "1" :
    indonesia()
    choose2()
  elif pil == "2" :
    negara()
    raw_input("Kembali")
    menu()
    choose()
  elif pil == "3" :
    sys.exit(1)
  else:
    print "pilihan salah"
    raw_input("Kembali")
    menu()
    choose()
    

if __name__ == '__main__':
  menu()
  choose()
    


