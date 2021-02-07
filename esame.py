#Martin Carli


#       ----------------------------------------------------------------

###         CONTROLLA  PER I RAISE SE FARE CONTINUE, OPPURE  NONE, OPPURE ELSE ECC


#forse nellaparte doveapro il file devo mettere il None


#       ----------------------------------------------------------------


#definisco la classe che usero` per alzare le eccezioni
class ExamException(Exception):
    pass

#creo la classe CSVTimeSeriesFile con cui stampero` le informazioni del del file "data.csv"

class CSVTimeSeriesFile:
    def __init__(self, name):
        # Setto il nome del file
        self.name = name
        #adesso alzo qualche eccezione
        if not isinstance(name,str):
            raise ExamException('\nATTENZIONE: Il nome del file deve essere di tipo stringa')
        if(name== ''):
            raise ExamException('\nATTENZIONE: Il file deve avere un nome')


    def get_data(self):

        # Inizializzo una lista vuota per salvare i valori
        time_series = []

        #Per prima cosa provo ad aprire il file per estrare i dati. Nel caso in cui non riesca allora alzo un eccezione che informera` all'utente che c'e`stato un errore all'apertura del file. Essendo un errore "un-recovable" non potro` esseguire il file e quindi ritorno None

        try:
            #apro il file (leggendolo)
            my_file = open(self.name, 'r')
        except:
            raise ExamException('\nATTENZIONE: Errore nella lettura del file')
 


        # Ora inizio a leggere il file linea per linea
        for line in my_file:
            
            # Faccio lo split di ogni linea sulla virgola
            elements = line.split(',')
            

            #controllo se nel file ci sono solo 2 valori a riga
            #----------------------------------------------------------

            if len(elements) != 2:
                raise ExamException('\nATTENZIONE: Il nel file ci dovrebbero essere solo due valori a riga, ovvero l` epoch e la temperatura') 


            #              FORSE SE NON E GIUSTO DEVO CHIUDERE IL file

            #---------------------------------------------------------------




            if elements[0] != 'epoch':
                    
                # Setto l epoch ed il valore della temperatura
                epoch  = elements[0]
                temperature = elements[1]
                
                # Le variabili "epoch" e "temperature" al momento sono ancora una stringa, poiche' ho letto da file di testo, quindi devo convertire i valore in int/float e se nel farlo ho un errore avverto
                #In questo caso sarebbe un errore "recoverable" e posso proseguire (semplicemente salto la linea)






                # CONTROLLA QUESTA PARTE --------E GIUSTO????----------



                #converto il valore di epoch in float 
                try:
                    epoch = float(epoch)
                except:
                    raise ExamException('\nATTENZIONE: Errore nela conversione di epoch a float')

                #adesso lo convertiamo in int, non potevo fare if isistance(epoch,float), perche all'inizio non e` di tipo float ma e` una stringa
                try:                           
                    epoch = int(epoch)
                except:
                    raise ExamException('\nATTENZIONE: Errore nela conversione di epoch a int')


                #-----------------------------------------------------






                #converto il valore della temperatura in float
                try:
                    temperature= float(temperature)
                except:
                    raise ExamException('\nATTENZIONE: Errore nella conversione di temperature a float')






#                  SI USA IL TEMPO NEGATIVO IN QUESTO CASO???/? COTNROLLA
                if epoch<0:
                    raise ExamException('\nATTENZIONE: Non esiste il tempo negativo')

#----------------------------------------------------------------------------





                
                # Infine aggiungo alla lista dei valori questo valore
                time_series.append([epoch,temperature])

        
        # Chiudo il file
        my_file.close()


        #adesso controllo se la lista e` ordinata e di conseguenza se ci sono duplicati

        length_time_series=len(time_series)

        for i in range(1, length_time_series):
            if time_series[i][0]<=time_series[i-1][0]:
                raise ExamException('\nATTENZIONE: C`e` un problema con la lista(duplicati/lista non ordinata)')

        # Quando ho processato tutte le righe, ritorno i valori
        return time_series

##------------------------FINE PRIMA PARTE-----------------------------##


#inizio seconda parte

def daily_stats(time_series):


    # NOTAZIONE IMPORTANTE: Queste eccezioni non sono fondamentali, perche ci sono gia` nella funzione precendente, le ho aggiunte perche potrebbe esserci il caso in cui l'utente non usa la prima funzione (CSVTimeSeriesFile) ma passa subito alla seconda
    

    #time_series DEVE essere di tipo lista
    if not isinstance(time_series,list):
        raise ExamException('\nATTENZIONE: non e` di tipo lista')

    
    #ricontrolliamo se c'e` qualche duplicato
    length_time_series=len(time_series)

    for i in range(1, length_time_series):
        if time_series[i][0]<=time_series[i-1][0]:
            raise ExamException('\nATTENZIONE: C`e` un problema con la lista(duplicati/lista non ordinata)')

    #adesso guardiamo le sottoliste che sono in "time_series"

    for sottolista in time_series:
        if not isinstance(sottolista,list):
            raise ExamException('\nATTENZIONE: Le sottoliste non sono di tipo lista')
        if len(sottolista)!=2:
            raise ExamException('\nATTENZIONE: ogni sottolista deve avere due valori')

    
    #  ~~~~~~~~~~~~~         fine delle eccezioni iniziai         ~~~~~~~~~~~~~~~


    #   creo una lista dove verranno salvate tutte le informazioni dei giorni (min,max,media) ovvero le  soluzioni dell'esercizio
    statistiche_giornagliere= []   

    #qui verranno messi le "prime" informazioni del giorno
    giorno_inizio=[]


    #per prima cosa devo capire quali sono le prime informazioni del giorno
    #informazioni[0] == epoch
    #uso l'operazione "modulo"

    #per le informazioni nella lista "time_series"
    for informazioni in time_series:
        #uso l' operazione modulo
        day_start_epoch = informazioni[0] - (informazioni[0] % 86400)
        #controllo se c'e` effetivamente il valore nella lista giorno_inizio
        if day_start_epoch not in giorno_inizio:
            #se non c'e` allora aggiungo il valore
            giorno_inizio.append(day_start_epoch)
    
    

    #definisco la lughezza dei primi valori dei giorni
    length_giorno_inizio= len(giorno_inizio)

    #controlliamo se la lunghezza della lista ingiorni e` lunga dai 28 ai 31 giorni
    if length_giorno_inizio not in [28,29,30,31]:
        raise ExamException('\nATTENZIONE: Un mese deve avere dai 28 ai 31 giorni')


#--------------------- FUNZIONE PRINCIPALE ---------------------   

    #nel primo for definiamo i giorni in cui faremo i calcoli
    #ovvero da 0 fino al numero di giorni del mese
    for i in range(0,length_giorno_inizio):
        #definisco la lista giorno, che verra` riscritta ogni volta
        giorno=[]

        #passiamo al secondo for dove definiremo i valori di ogni giorno
        for p in range(0,length_time_series):
            #facciamo il valero sia nel giorno
            if(giorno_inizio[i]== time_series[p][0] - (time_series[p][0] % 86400)):
                #se  fa parte del giorno allora nella lista "giorno" mettiamo il valore della temperatura
                giorno.append(time_series[p][1])
        #facciamo i calcoli e li mettiamo nella lista "statistiche_giornagliere"
        statistiche_giornagliere.append([min(giorno), max(giorno), sum(giorno)/len(giorno)])
    #ritorniamo il risultato
    return statistiche_giornagliere




        
