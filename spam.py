import pyautogui
from time import sleep
from os import system
import win32api
import time
import requests
from bs4 import BeautifulSoup
import pyperclip

while True:
    try:
        menu = int(input("1- Kelime yazdır\n2- Atasözü yazdır\n3- Çıkış\n\nSeçim: "))
    except ValueError:
        system("cls")
        print("Lütfen sayı giriniz.")
        sleep(4)
        system("cls")
        continue
    if menu == 1:
        system("cls")
        kelime = input("Yazdırmak istediğiniz kelimeyi veya cümleyi giriniz: ")
        system("cls")
        try:
            adet = int(input("Girdiğiniz kelime veya cümleyi kaç kere yazdırmak istiyorsunuz: "))
        except ValueError:
            system("cls")
            print("Lütfen sayı giriniz.")
            sleep(4)
            system("cls")
            continue
        system("cls")
        print("Kelime veya cümleyi yazdırmak istediğiniz yere tıklayın..")
        sleep(2)
        system("cls")
        state_left = win32api.GetKeyState(0x01)  
        while True:
            a = win32api.GetKeyState(0x01)

            if a != state_left:  
                if a < state_left:
                    while adet>0:
                        sleep(0.2)
                        pyperclip.copy(kelime) 
                        pyautogui.hotkey("ctrl", "v")
                        sleep(0.2)
                        pyautogui.press("enter")
                        adet-=1
                    break
        
    elif menu == 2:
        system("cls")
        try:
            harf = str(input("Atasözü hangi harf ile başlasın(küçük karekter giriniz): "))
        except ValueError:
            system("cls")
            print("Lütfen harf giriniz.")
            sleep(4)
            system("cls")
            continue
        if harf == "ü":
            harf = "u2"
        if harf == "ş":
            harf = "s2"
        if harf == "ö":
            harf = "o2"
        if harf == "ı":
            harf = "i2"
        if harf == "ç":
            harf = "c2"
        soup = BeautifulSoup((requests.get(f"https://www.dilbilgisi.net/{harf}-harfi-atasozleri-sozlugu/").content), "html.parser")

        div = soup.find("div", {"class":"td-post-content tagdiv-type"}).find_all("p")

        liste = []
        for p in div:
            atasoz = p.find("strong").text
            atasoz1 = atasoz.strip(":")
            liste.append(atasoz1)
        liste.remove('ANLAMINI ÖĞRENMEK İSTEDİĞİNİZ ATASÖZÜNÜN İLK HARFİNİ AŞAĞIDAKİ LİSTEDEN SEÇİNİZ!')
        system("cls")
        print("Atasözlerini yazdırmak istediğiniz yere tıklayın..")
        sleep(2)
        system("cls")
        state_left = win32api.GetKeyState(0x01)  
        while True:
            a = win32api.GetKeyState(0x01)
            

            if a != state_left:  
                if a < state_left:
                    for i in liste:
                        sleep(0.2)
                        pyperclip.copy(i) 
                        pyautogui.hotkey("ctrl", "v")
                        sleep(0.2)
                        pyautogui.press("enter")
                    break
    
    
    elif menu == 3:
        break
    else:
        system("cls")
        print("Lütfen doğru bir seçim yapınız..")
        sleep(4)
        system("cls")
        continue
    