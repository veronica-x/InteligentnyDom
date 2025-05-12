from abc import ABC, abstractmethod

class IPrzelaczalne(ABC):
    @abstractmethod
    def wlacz(self) -> None:  # Wlącza/wyłącza urządzenie
        pass

    @abstractmethod
    def wylacz(self) -> None:
        pass

class IRegulowalne(ABC):
    @abstractmethod
    def ustawPoziom(self, wartosc: int) -> None:  # Ustawia poziom urządzenia
            pass

class Urzadzenie(ABC):
    def __init__(self, id_urzadzenia: str, nazwa_przyjazna: str, lokalizacja: str):
        self._id_urzadzenia = id_urzadzenia
        self._nazwa_przyjazna = nazwa_przyjazna
        self._lokalizacja = lokalizacja
        self.status = False  # Urządzenie domyślnie wyłącznone


    @abstractmethod
    def wyswietlStatus(self) -> str:  # Wyświetla aktualny status urządzenie
        pass

    @abstractmethod

    def wyswietlSzczegolowyOpis(self) -> str:  # Wyświetla szczegółowy opis urządzenia
        pass

    @abstractmethod
    def zmienStatus (self, nowy_status: bool) -> None:  # Zmienia status urządzenia
        pass


class Glosnik(Urzadzenie, IPrzelaczalne, IRegulowalne):
    def __init__(self, id_urzadzenia, nazwa_przyjazna, lokalizacja, glosnosc=0):
            super().__init__(id_urzadzenia, nazwa_przyjazna, lokalizacja)
            self._glosnosc = glosnosc
        
    def wyswietlStatus(self) -> str:
            return "Włączony" if self.status else "Wyłączony"
        
    def wyswietlSzczegolowyOpis(self) -> str:
            return (f"Głośnik - {self._nazwa_przyjazna}, Lokalizacja: {self._lokalizacja}, "
                    f"Głośność: {self._glosnosc}, Status: {self.wyswietlStatus()}")
        
    def zmienStatus(self, nowy_status: bool) -> None:
            self.status = nowy_status

    def wlacz(self) -> None:
            self.status = True
        
    def wylacz(self) -> None:
            self.status = False

    def ustawPoziom(self, wartosc: int) -> None:
            if 0 <= wartosc <= 100:
                self._glosnosc = wartosc
            else:
                print("Nieprawidłowa wartość głośności. Wpisz wartość z zakresu 0-100.")

class SmartTV (Urzadzenie, IPrzelaczalne, IRegulowalne):
        
    KANALY = {
             1: "TVP1",
             2: "TVP2",
             3: "Polsat",
             4: "TVN",
             5: "TV 4",
             6: "TV 6",
             7: "TV Puls",
             8: "TVP Kultura",
             9: "TVP Historia",
             10: "MTV",
             11: "TVN Style",
             12: "TVP Seriale"

        }

    def __init__(self, id_urzadzenia, nazwa_przyjazna, lokalizacja, kanal=1, glosnosc=10):
            super().__init__(id_urzadzenia, nazwa_przyjazna, lokalizacja)
            self._kanal = kanal
            self._glosnosc = glosnosc

    def wyswietlStatus(self) -> str:
             return "Włączony" if self.status else "Wyłaczony"

    def wyswietlSzczegolowyOpis(self) -> str:
             nazwa_kanalu = SmartTV.KANALY.get(self._kanal, "Kanał niedostępny. W celu uzyskania dostępu, wykup dodatkowy pakiet.")
             return (f"Smart TV - {self._nazwa_przyjazna}, Lokalizacja: {self._lokalizacja}, "
                    f"Kanał: {self._kanal} ({nazwa_kanalu}), Głośność: {self._glosnosc}, Status: {self.wyswietlStatus()}")

    def zmienStatus(self, nowy_status: bool) -> None:
             self.status = nowy_status

    def wlacz(self) -> None:
             self.status = True

    def wylacz(self) -> None:
             self.status = False

    def ustawPoziom(self, wartosc: int) -> None:
             if 0 <= wartosc <= 100:
                  self._glosnosc = wartosc
             else:
                print ("Nieprawidłowa głośność. Wpisz wartość z zakresu 0-100.")

    def zmienKanal(self, nowy_kanal: int) -> None:
             if nowy_kanal in SmartTV.KANALY:
                  self._kanal = nowy_kanal
                  print(f"{SmartTV.KANALY[nowy_kanal]} ({nowy_kanal})")
             else:
                  print(f"Nieprawidłowy numer kanału. W celu uzyskania dostępu, wykup dodatkowy pakiet. Dostępne kanały: {list(SmartTV.KANALY.keys())}")

    def nastepnyKanal(self) -> None:  # Przełącza na kolejny kanał. Jeśli ostatni, wraca na pierwszy.
             numery_kanalow = sorted(SmartTV.KANALY.keys())
             current_index = numery_kanalow.index(self._kanal)
             next_index = (current_index + 1) % len(numery_kanalow)
             self._kanal = numery_kanalow[next_index]
             print(f"Przełączono na kanał: {SmartTV.KANALY[self._kanal]} ({self._kanal})")

    def wyswietlAktualnyKanal(self) -> None:
             print(f"Przełączono na kanał: {SmartTV.KANALY[self._kanal]} ({self._kanal})") 

    def poprzedniKanal(self) -> None:  # Przełącza na poprzedni kanał. Jeśli pierwszy, wraca na ostatni.
             numery_kanalow = sorted(SmartTV.KANALY.keys())
             current_index = numery_kanalow.index(self._kanal)
             prev_index = (current_index - 1) % len(numery_kanalow)
             self._kanal = numery_kanalow[prev_index]
             print(f"Przełączono na kanał: {SmartTV.KANALY[self._kanal]} ({self._kanal})")

    def wyswietlAktualnyKanal(self) -> None:
          print(f"\nAktualny kanał: {SmartTV.KANALY[self._kanal]} ({self._kanal})")
        
        
class Rolety(Urzadzenie, IPrzelaczalne, IRegulowalne):

    def __init__(self, id_urzadzenia, nazwa_przyjazna, lokalizacja, poziom=0):
            super().__init__(id_urzadzenia, nazwa_przyjazna, lokalizacja)
            self._poziom = poziom

    def wyswietlStatus(self) -> str:
           return "Włączone" if self.status else "Wyłączone"
      
    def wyswietlSzczegolowyOpis(self) -> str:
           return (f"Rolety - {self._nazwa_przyjazna}, Lokalizacja: {self._lokalizacja}, "
                   f"Poziom zasłonięcia: {self._poziom}%, Status: {self.wyswietlStatus()}")
      
    def zmienStatus(self, nowy_status: bool) -> None:
            self.status = nowy_status

    def wlacz(self) -> None:
            self.status = True

    def wylacz(self) -> None:
            self.status = False

    def ustawPoziom(self, wartosc: int) -> None:  # Ustawia poziom zasłonięcia rolet (0 - całkowicie otwarte, 100 - całkowicie zasłonięte).
             
            if 0 <= wartosc <= 100:
                  self._poziom = wartosc
            else:
                print("Nieprawidłowa wartość. Wpisz wartość z zakresu 0-100.")
        
    def podniesRolety(self, procent: int = 10) -> None:  #Podnosi rolety o podaną wartość procentową.
            nowy_poziom = max(0, self._poziom - procent)
            self._poziom = nowy_poziom
            print(f"Rolety podniesione. Aktualny poziom zasłonięcia: {self._poziom}%")
        
    def opuscRolety(self, procent: int = 10) -> None:  #Opuszcza rolety o podaną wartość procentową.
            nowy_poziom = min(100, self._poziom + procent)
            self._poziom = nowy_poziom
            print(f"Rolety opuszczone. Aktualny poziom zasłonięcia: {self._poziom}%")
             
class InteligentnyDom:
     
    def __init__(self, nazwa_domu: str):
            self.nazwa_domu = nazwa_domu
            self.lista_urzadzen = []
    
    def dodajUrzadzenie(self, urzadzenie: Urzadzenie) -> None:  # Dodaje urządzenie do listy urządzeń.
            self.lista_urzadzen.append(urzadzenie)
            print(f"Dodano urządzenie: {urzadzenie._nazwa_przyjazna}")

    def usunUrzadzenie(self, id_urzadzenia: str) -> None:  # Usuwa urządzenie.
            self.lista_urzadzen = [
                 urzadzenie for urzadzenie in self.lista_urzadzen
                 if urzadzenie._id_urzadzenia != id_urzadzenia
            ]
            print(f"Usunięto urządzenie o ID: {id_urzadzenia}")
        
    def wyswietlWszystkieUrzadzenia(self) -> None:
            print(f"\n Urządzenia w domu '{self.nazwa_domu}':")
            for urzadzenie in self.lista_urzadzen:
                 print(urzadzenie.wyswietlSzczegolowyOpis())

    def wlaczWszystkiePrzelaczalne(self) -> None:
            print ("\n Włączono urządzenia:")
            for urzadzenie in self.lista_urzadzen:
                  if isinstance(urzadzenie, IPrzelaczalne):
                        urzadzenie.wlacz()
                        print(f"Urządzenie '{urzadzenie._nazwa_przyjazna}' zostało włączone.")

    def wylaczWszystkiePrzelaczalne(self) -> None:
            print ("\n Wyłączono urządzenia:")
            for urzadzenie in self.lista_urzadzen:
                  if isinstance(urzadzenie, IPrzelaczalne) and urzadzenie.status:
                        urzadzenie.wylacz()
                        print(f"Urządzenie '{urzadzenie._nazwa_przyjazna}' zostało wyłączone.")

    def znajdzUrzadzenie(self, id_urzadzenia: str) -> Urzadzenie:
            for urzadzenie in self.lista_urzadzen:
                if urzadzenie._id_urzadzenia == id_urzadzenia:
                    return urzadzenie
            print(f"Nie znaleziono urządzenia o podanym ID: {id_urzadzenia}")
            return None

    def zarzadzajUrzadzeniem(self, id_urzadzenia: str, akcja: str, wartosc=None):
            urzadzenie = self.znajdzUrzadzenie(id_urzadzenia)
            if urzadzenie is not None:
                if akcja == "wlacz":
                     urzadzenie.wlacz()
                     print(f"Urządzenie '{urzadzenie._nazwa_przyjazna}' zostało włączone.")
                elif akcja == "wylacz":
                     urzadzenie.wylacz()
                     print(f"Urządzenie '{urzadzenie._nazwa_przyjazna}' zostało wyłączone.")
                elif akcja == "ustaw" and wartosc is not None:
                     urzadzenie.ustawPoziom(wartosc)
                     print(f"Ustawiono wartość dla urządzenia: '{urzadzenie._nazwa_przyjazna}' na {wartosc}.")
                else:
                     print ("Nieprawidłowe działanie!")

    def raportWszystkichUrzadzen(self) -> None:
          
          print("\nRaport wszystkich urządzeń w domu:")
          print(f"{'ID':<10} {'Nazwa':<20} {'Lokalizacja':<15} {'Status':<10}")
          print ("-" * 60)

          for urzadzenie in self.lista_urzadzen:
                status = "Włączone" if urzadzenie.status else "Wyłączone"
                print(f"{urzadzenie._id_urzadzenia:<10} {urzadzenie._nazwa_przyjazna:<20} {urzadzenie._lokalizacja:<15} {status:<10}")
        

# Demonstacja

# Tworzę Inteligentny Dom
dom = InteligentnyDom("Mi Casa")

# Tworzę urządzenia
glosnik = Glosnik(id_urzadzenia="G1", nazwa_przyjazna="Głośnik w salonie", lokalizacja="Salon", glosnosc=30)
smart_tv = SmartTV(id_urzadzenia="TV1", nazwa_przyjazna="Telewizor w salonie", lokalizacja="Salon", kanal=4, glosnosc=20)
rolety = Rolety(id_urzadzenia="R1", nazwa_przyjazna="Rolety w sypialni", lokalizacja="Sypialnia", poziom=80)

# Dodaję urządzenia do domu

dom.dodajUrzadzenie(glosnik)
dom.dodajUrzadzenie(smart_tv)
dom.dodajUrzadzenie(rolety)

# 1. Wyświetlam status wszystkich urządzeń

dom.wyswietlWszystkieUrzadzenia()

# 2. Włączam wszystkie urządzenia

dom.wlaczWszystkiePrzelaczalne()

# 2.1. Sprawdzam status urządzeń po włączeniu

dom.wyswietlWszystkieUrzadzenia()

# 3. Zmiana poziomu dla urządzeń regulowanych
dom.zarzadzajUrzadzeniem("G1", "ustaw", 50) #Zmieniam poziom głośnika na 50
dom.zarzadzajUrzadzeniem("R1", "ustaw", 100) #Zmieniam poziom zasłonięcia rolet na 100%

# 4. Zmiana kanału w telewizorze
dom.zarzadzajUrzadzeniem("TV1", "ustaw", 10) #Zmieniam kanał na 10
smart_tv.wyswietlAktualnyKanal()

# 5. Przełączam kanał w telewizorze
smart_tv.nastepnyKanal()
smart_tv.poprzedniKanal()

# 6. Wyświetlam status wszystkich urządzeń po zmianiach
dom.wyswietlWszystkieUrzadzenia()