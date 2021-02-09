#Martin Carli
#Esame - Laboratorio di Programmazione - 09/02/2021


# Definisco la classe che usero` per alzare le eccezioni
class ExamException(Exception):
    pass

# Creo la classe CSVTimeSeriesFile con cui stampero` le informazioni del file "data.csv"

class CSVTimeSeriesFile:
    def __init__(self, name):
        # Setto il nome del file
        self.name = name
        # Adesso alzo qualche eccezione
        if not isinstance(name,str):
            raise ExamException('\nATTENZIONE: Il nome del file deve essere di tipo stringa')
        if(name== ''):
            raise ExamException('\nATTENZIONE: Il file deve avere un nome')


    def get_data(self):

        # Inizializzo una lista vuota per salvare i valori
        time_series = []

        # Per prima cosa provo ad aprire il file per estrare i dati. Nel caso in cui non riesca allora alzo un eccezione che informera` all'utente che c'e`stato un errore all'apertura del file

        try:
            # Apro il file (leggendolo)
            my_file = open(self.name, 'r')
        except:
            raise ExamException('\nATTENZIONE: Errore nella lettura del file')
 

        # Ora inizio a leggere il file linea per linea
        for line in my_file:
            
            # Faccio lo split di ogni linea sulla virgola
            elements = line.split(',')
            
            # Controllo se nel file ci sono solo 2 valori a riga
            if len(elements) != 2:
                raise ExamException('\nATTENZIONE: Il nel file ci dovrebbero essere solo due valori a riga, ovvero l` epoch e la temperatura') 


            if elements[0] != 'epoch':
                    
                # Setto l epoch ed il valore della temperatura
                epoch  = elements[0]
                temperature = elements[1]
                
                # Le variabili "epoch" e "temperature" al momento sono ancora una stringa, poiche' ho letto da file di testo, quindi devo convertire i valore in int/float e se nel farlo ho un errore avverto

                try:                           
                    epoch = int(epoch)
                except:
                    print('\nATTENZIONE: Errore nela conversione di epoch a int')

                # Converto il valore della temperatura in float
                try:
                    temperature= float(temperature)
                except:
                    print('\nATTENZIONE: Errore nella conversione di temperature a float')
                
                # Infine aggiungo alla lista dei valori questo valore
                try:
                    time_series.append([epoch,temperature])
                except:
                    print('\nATTENZIONE: Ho avuto un problema nell`appendere i valori in time_series')
        
        # Chiudo il file
        my_file.close()


        length_time_series=len(time_series)

        # Controllo se la lista contiene almeno 28 elementi (une per giorno)
        if length_time_series<=27:
            raise ExamException('\nATTENZIONE: La lista time_series deve contenere almeno 28 informazioni (una informazione per giorno')
            
        # Adesso controllo se la lista e` ordinata e di conseguenza se ci sono duplicati         
        # Controllo riga per riga se c'e`qualche valore di epoch che e` minoreo uguale del precedente
        for i in range(1, length_time_series):
            if time_series[i][0]<=time_series[i-1][0]:
                raise ExamException('\nATTENZIONE: C`e` un problema con la lista(duplicati/lista non ordinata)')

        # Quando ho processato tutte le righe, ritorno i valori
        return time_series

##------------------------FINE PRIMA PARTE-----------------------------##

# Inizio seconda parte

def daily_stats(time_series):

    # Qui verranno messi le "prime" informazioni del giorno
    giorno_inizio=[]

    # Per prima cosa devo capire quali sono le prime informazioni del giorno
    # Per le informazioni nella lista "time_series"
    for informazioni in time_series:
        # Uso l' operazione modulo (ps. informazioni[0] == epoch)
        day_start_epoch = informazioni[0] - (informazioni[0] % 86400)
        # Controllo se c'e` effetivamente il valore nella lista giorno_inizio
        if day_start_epoch not in giorno_inizio:
            # Se non c'e` allora aggiungo il valore
            giorno_inizio.append(day_start_epoch)


#--------------------- FUNZIONE PRINCIPALE ---------------------   

    # Creo una lista dove verranno salvate tutte le informazioni dei giorni (min,max,media) ovvero le  soluzioni dell'esercizio
    statistiche_giornagliere= []   

    # Definisco la lughezza dei primi valori dei giorni
    length_giorno_inizio= len(giorno_inizio)

    # Definisco la lunghezza della lista time_series
    length_time_series= len(time_series)

    # Nel primo for definiamo i giorni in cui faremo i calcoli
    # Ovvero da 0 fino al numero di giorni del mese
    for i in range(0,length_giorno_inizio):
        # Definisco la lista giorno, che verra` riscritta ogni volta
        giorno=[]

        # Passiamo al secondo for dove definiremo i valori di ogni giorno
        for p in range(0,length_time_series):
            # controlliamo se il valore e` nel giorno (usando sempre l operazione modulo)
            if(giorno_inizio[i]== time_series[p][0] - (time_series[p][0] % 86400)):
                # Se  fa parte del giorno allora nella lista "giorno" mettiamo il valore della temperatura
                giorno.append(time_series[p][1])
        # Facciamo i calcoli e li mettiamo nella lista "statistiche_giornagliere"
        statistiche_giornagliere.append([min(giorno), max(giorno), sum(giorno)/len(giorno)])
    # Ritorniamo il risultato
    return statistiche_giornagliere