#Martin Carli


#       ----------------------------------------------------------------

###         CONTROLLA  PER I RAISE SE FARE CONTINUE, OPPURE  NONE, OPPURE ELSE ECC





#       ----------------------------------------------------------------


#definisco la classe che usero` per alzare le eccezioni
class ExamException(Exception):
    pass

#creo la classe CSVTimeSeriesFile con cui stampero` le informazioni del del file "data.csv"



#         -----PROBABILMENTE NON VA BENE SE LASCIO L VARIABILE FUORI----

#-----------------------------------------------------------------------




#   FORSE E MEGLIO FARE UNA MINI LISTA CHE SI RESETTA ////// ho aggiunto le parentesi quadre




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

        #Per prima cosa provo ad aprire il file per estrare i dati. Nel caso in cui non riesca allora alzo un eccezione che informera` all'utente che c'e`stato un errore all'apertura del file. Essendo un errore "un-recovable" non potro` esseguire il file equindi ritorno None
        
        # Inizializzo una lista vuota per salvare i valori

        time_series = []


        try:
            my_file = open(self.name, 'r')
        except:
            raise ExamException('\nATTENZIONE: Errore nella lettura del file')
            
            # Esco dalla funzione tornando "niente".
            return None


        # Ora inizio a leggere il file linea per linea
        for line in my_file:
            
            # Faccio lo split di ogni linea sulla virgola
            elements = line.split(',')
            

            #controllo se nel file ci sono solo 2 valori a riga
            #----------------------------------------------------------

            if len(elements != 2):
                raise ExamException('\nATTENZIONE: Il nel file ci dovrebbero essere solo due valori a riga, ovvero l` epoch e la temperatura') 

                continue      
            
            ####           CONTINUE E` OK? O E` MEGLIO UN ELSE????
            #---------------------------------------------------------------




            #FORSE NEL 'IF ELEMENTS[0]!= EPOCH' DOVREI METTERE UN ECCEZIONE??

            # Se NON sto processando l'intestazione...
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
                    continue
                #adesso lo convertiamo in int, non potevo fare if isistance(epoch,float), perche all'inizio non e` di tipo float ma e` una stringa
                try:                           
                    epoch = int(epoch)
                except:
                    raise ExamException('\nATTENZIONE: Errore nela conversione di epoch a int')
                    continue

                #-----------------------------------------------------



                try:
                    temperature= float(temperature)
                except:
                    raise ExamException('\nATTENZIONE: Errore nella conversione di temperature a float')
                    continue


#   ------------     VANNO BENE LE ECCEZIONI PERLA TEMPERATURA???? ----------
#                 forse no perche non per forza si tratta di una casa

                if(temperature>60):
                    raise ExamException('\nATTENZIONE: Temperatura troppo alta')
                    continue

                if(temperature<-20):
                    raise ExamException('\nATTENZIONE: Temperatura troppo bassa')
                    continue

#-----------------------------------------------------------------------------


#                  SI USA IL TEMPO NEGATIVO IN QUESTO CASO???/? COTNROLLA
                if epoch<0:
                    raise ExamException('\nATTENZIONE: Non esiste il tempo negativo')
                    continue
#----------------------------------------------------------------------------
           
                
                # Infine aggiungo alla lista dei valori questo valore
                time_series.append([epoch,temperature])

        
        # Chiudo il file
        my_file.close()


        #adesso controllo se la lista e` ordinata e di conseguenza se ci sono duplicati

        x=len(time_series)

        for i in range(1, x):
            if time_series[i][0]<=time_series[i-1][0]:
                raise ExamException('\nATTENZIONE: C`e` un problema con la lista(duplicati/lista non ordinata)')

        # Quando ho processato tutte le righe, ritorno i valori
        return time_series

##------------------------FINE PRIMA PARTE-----------------------------##


#           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#                   CONTROLLA LA QUESTIONE DEI GIORNI
#                       -sia nella eccezione che dopo per la funzione

#           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##inizio seconda parte
def daily_stats(time_series):
    #per sicurezza inizio ad alzare qualche eccezione

    #time_series DEVE ESSERE DI TIPO LISTA
    if not isinstance(time_series,list):
        raise ExamException('\nATTENZIONE: non e` di tipo lista')

    #un mese ha almeno 28 giorni, quindi alziamo questa eccezione
    if len(time_series) <=27:
        raise ExamException('\nATTENZIONE: la lista deve avere almeno 28 informazioni')
    
    #ricontrolliamo se c'e` qualche duplicato
    x=len(time_series)

    for i in range(1, x):
        if time_series[i][0]<=time_series[i-1][0]:
            raise ExamException('\nATTENZIONE: C`e` un problema con la lista(duplicati/lista non ordinata)')

    #adesso guardiamo le mini liste che sono in "time_series"

    for sottolista in time_series:
        if not isinstance(sottolista,list):
            raise ExamException('\nATTENZIONE: Le sottoliste non sono di tipo lista')
        if len(sottolista)!=2:
            raise ExamException('\nATTENZIONE: ogni sottolista deve avere due valori')

 #  ~~~~~~~~~~~~~         fine delle eccezioni iniziai         ~~~~~~~~~~~~~~~

    #   creo una lista dove verranno salvate tutte le informazioni dei giorni (min,max,media) - le  soluzioni dell'esercizio
    statistiche= []   

    #qui verranno messi i giorni 
    ingiorni=[]

    #per prima cosa devo capire quali sono le prime informazioni del giorno
    #informazioni[0] == epoch
    #uso l'operazione "modulo"
    for informazioni in time_series:
        day_start_epoch = informazioni[0] - (informazioni[0] % 86400)
        #controllo se effetivamente c'e` il valore nella lista ingiorni
        if day_start_epoch is not in ingiorni:
            #se non c'e` allora aggiungo il valore
            ingiorni.append(day_start_epoch)
    #ricontrolliamo se la lunghezza della lista ingiorni e` lunga dai 28 ai 31 giorni

    #--------  SONO GIUSTI QUEI OR?? E QUEI ==? RICONTROLLA ------------

    if not len(ingiorni) == 28 or 29 or  30 or 31:
        raise ExamException('\nATTENZIONE: Un mese deve avere dai 28 ai 31 giorni')

    #-------------------------------------------------------------------
    
    #usero k per definire i giorni iniziali
    k=1
    #ricordiamo che x = len(time_list)

    giorno=[]
        
    
    for i in range(1,x):
   
        if time_series[i][0]>=ingiorni[k] and time_series[i][0]<ingiorni[k+1]:
            giorno.append(time_series[i][1]) #aggiungo il valore  della temperatura

        if time_series[i][0]>ingiorni[k] and time_series[i][0]>=ingiorni[k+1]:
            statistiche.append([min(giorno), max(giorno), sum(giorno)/len(giorno)])
            giorno=[]
            giorno.append(time_series[i][1]) #aggiungo il valore  della temperatura
            k++ #passo al prossimo ingiorno

        if time_series[i][0]==time_series[x][0]:
            statistiche.append([min(giorno), max(giorno), sum(giorno)/len(giorno)])

    return statistiche


        
