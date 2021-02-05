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




#   FORSE E MEGLIO FARE UNA MINI LISTA CHE SI RESETTA




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
            raise ExamException('ATTENZIONE: Errore nella lettura del file')
            
            # Esco dalla funzione tornando "niente".
            return None


        # Ora inizio a leggere il file linea per linea
        for line in my_file:
            
            # Faccio lo split di ogni linea sulla virgola
            elements = line.split(',')
            

            #controllo se nel file ci sono solo 2 valori a riga
            #----------------------------------------------------------

            if len(elements != 2):
                raise ExamException('ATTENZIONE: Il nel file ci dovrebbero essere solo due valori a riga, ovvero l` epoch e la temperatura') 

                continue      
            
            ####           CONTINUE E` OK? O E` MEGLIO UN ELSE????
            #---------------------------------------------------------------




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
                    raise ExamException('ATTENZIONE: Errore nela conversione di epoch a float')
                    continue
                #adesso lo convertiamo in int, non potevo fare if isistance(epoch,float), perche all'inizio non e` di tipo float ma e` una stringa
                try:                           
                    epoch = int(epoch)
                except:
                    raise ExamException('ATTENZIONE: Errore nela conversione di epoch a int')
                    continue

                #-----------------------------------------------------



                try:
                    temperature= float(temperature)
                except:
                    raise ExamException('ATTENZIONE: Errore nella conversione di temperature a float')
                    continue

                if(temperature>60):
                    raise ExamException('ATTENZIONE: Temperatura troppo alta')
                    continue

                if(temperature<-20):
                    raise ExamException('ATTENZIONE: Temperatura troppo bassa')
                    continue

                if epoch<0:
                    raise ExamException('ATTENZIONE: Non esiste il tempo negativo')
                    continue

           
                
                # Infine aggiungo alla lista dei valori questo valore
                time_series.append(epoch,temperature)

        
        # Chiudo il file
        my_file.close()


        #adesso controllo se la lista e` ordinata e di conseguenza se ci sono duplicati

        x=len(time_series)

        for i in range(1, x):
            if time_series[i][0]<=time_series[i-1][0]:
                raise ExamException('ATTENZIONE: C`e` un problema con la lista(duplicati/lista non ordinata)')

        # Quando ho processato tutte le righe, ritorno i valori
        return time_series

##------------------------FINE PRIMA PARTE-----------------------------##

##inizio seconda parte
def daily_stats(time_series):

#   COSE DA FARE;
#   1. lista per giorni che iniziano alle 00;00
#   2. MODEL per calcolare quando inizia il giorno
#   3. fare una lista con tutte le temperature
#   4. creare lista dei risultati
#   5. fare le piccole funzioni (min,max,media ecc)