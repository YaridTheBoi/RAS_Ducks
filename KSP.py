import pandas as pd

#Kaczka
class Duck():
    def __init__(self,  h, w ):
        self.height = h
        self.width = w

#Rekurencyjne KSP
def KSP(backpack_capacity, ducks, ducks_amount):

    #jezeli przejrzalemjuz wszystkie kaczki lub plecak jest pelen to koniec
    if ducks_amount == 0 or backpack_capacity==0:
        return 0
    

    #jezeli nie moge wcisnac aktualnej kaczki do plecaka to przegladaj dalej
    if (ducks[ducks_amount-1].width > backpack_capacity):
        return KSP(backpack_capacity, ducks, ducks_amount-1)
    

    #jezeli moge wsadzic kaczke do plecaka
    else:
        #zwroc co jest wieksze: sytuacja gdy wsadze te kaczke i polece do konca czy jak jej nie wsadze i polece dalej
        return max(
            ducks[ducks_amount-1].height + KSP(
                backpack_capacity- ducks[ducks_amount-1].width,
                ducks,
                ducks_amount-1
            ), KSP(backpack_capacity, ducks, ducks_amount-1)
            
        )



def main():
    #Wczytanie danych z pliku
    data = pd.read_excel("zadanie-rekrutacyjne.xlsx", header=None)

    #Pobierz ile kaczek i jaki duzy plecak
    ducks_count = data.at[0,0]
    backpack_capacity = data.at[0,1]

    #Wsadz wszystkie kaczki do tablicy
    ducks=[]
    for i in range (1, ducks_count+1):
        duck = Duck(data.at[i,0], data.at[i,1])
        ducks.append(duck)
    
    #Rozwiaz KSP
    print(KSP(backpack_capacity, ducks, ducks_count))




#uruchom
if __name__ == '__main__':
    main()