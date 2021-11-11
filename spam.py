import pyautogui
from time import sleep
from os import system
import win32api
import requests
from bs4 import BeautifulSoup
import pyperclip

while True:
    try:
        menu = int(input("1- Kelime yazdır\n2- Atasözü yazdır\n3- Çıkış\n\nSeçim: "))
    except ValueError:
        system("cls")
        print("Lütfen sayı giriniz.")
        sleep(2)
        system("cls")
        continue
    
    if menu == 1:
        system("cls")
        kelime = input("Yazdırmak istediğiniz kelimeyi veya cümleyi yazınız: ")
        system("cls")
        try:
            adet = int(input("Girdiğiniz kelime veya cümleyi kaç kere yazdırmak istiyorsunuz: "))
        except ValueError:
            system("cls")
            print("Lütfen sayı giriniz.")
            sleep(2)
            system("cls")
            continue
        system("cls")
        aralik = input("Girdiğiniz kelimeleri veya cümleleri kaç saniye aralıkla yazdırmak istiyorsunuz(varsayılan -> 1): ")
        if len(aralik) == 0:
            aralik = 1
        system("cls")
        try:
            aralik = int(aralik)
        except ValueError:
            print("Lütfen sayı giriniz.")
            sleep(2)
            system("cls")
            continue
        print("Kelime veya cümleyi yazdırmak istediğiniz yere tıklayın..")
        sleep(2)
        system("cls")
        state_left = win32api.GetKeyState(0x01)  
        while True:
            a = win32api.GetKeyState(0x01)
            if a != state_left:  
                if a < state_left:
                    system("cls")
                    while adet>0:
                        sleep(0.2)
                        pyperclip.copy(kelime) 
                        pyautogui.hotkey("ctrl", "v")
                        sleep(0.2)
                        pyautogui.press("enter")
                        adet-=1
                        sleep(int(aralik))    
                    break
        
    elif menu == 2:
        system("cls")
        harf = str(input("Atasözü hangi harf ile başlasın: ")).upper()
        soup = BeautifulSoup((requests.get(f"https://tr.wikiquote.org/wiki/T%C3%BCrk%C3%A7e_atas%C3%B6zleri/{harf}").content), "html.parser")
        div = soup.find("div", {"class":"mw-parser-output"}).find("ul").find_all("li")
        liste = []
        for li in div:
            atasoz= ((li.text).split("."))
            liste.append(atasoz[0])
        system("cls")
        aralik = (input("Girdiğiniz kelimeleri veya cümleleri kaç saniye aralıkla yazdırmak istiyorsunuz(varsayılan -> 1): "))
        if len(aralik) == 0:
            aralik = 1
        system("cls")
        try:
            aralik = int(aralik)
        except ValueError:
            print("Lütfen sayı giriniz.")
            sleep(2)
            system("cls")
            continue
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
                        sleep(int(aralik))
                    break
    
    elif menu == 3:
        break
    else:
        system("cls")
        print("Lütfen doğru bir seçim yapınız..")
        sleep(4)
        system("cls")
        continue
