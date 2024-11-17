import random


zasieg = range(1,100)

def draw_random_characteristics():
    dobroc_wys = 0
    rzuty_wys ={}
    zasieg = range(1,10)
    for i in zasieg:
        waga = ["WW", "Wt", "Zw", "I", "S", "Int", "Ogd", "SW", "US", "Zr"]
        rzuty = []
        a = 10
        while a>0:
            b = random.randint(1,10) + random.randint(1,10) 
            rzuty.append(b)
            a = a -1
            
            
        slownik_cech_i_rzutow_w_kolejnosci_wagi = {}
        rzuty.sort()
        rzuty.reverse()
        #print (rzuty)
        a = 0
        while a<10:
            slownik_cech_i_rzutow_w_kolejnosci_wagi[waga[a]]=rzuty[a]
            a = a + 1

        characteristics = slownik_cech_i_rzutow_w_kolejnosci_wagi
        dobroc = 0
        for key, value in characteristics.items():
            dobroc = dobroc + int(value)
        
        if dobroc > dobroc_wys:
            dobroc_wys = dobroc
            rzuty_wys = characteristics
        
    print(f"Twoje rzuty to {(rzuty_wys)} \n")
    print(f"Razem {dobroc_wys} Współczynnik dobroci Twoich rzutów to {dobroc_wys/110}")
        






draw_random_characteristics()
