#definisco la classe che usero` per alzare le eccezioni
class ExamException(Exception):
    pass

#creo la classe CSVTimeSeriesFile con cui stampero` le informazioni del del file "data.csv"


# Inizializzo una lista vuota per salvare i valori
#questa lista verra` utilizzata piu volte nel nostro programma non solo in get_data

time_series = []


class CSVTimeSeriesFile:
    def __init__(self, name):
        # Setto il nome del file
        self.name = name


    def get_data(self):

        #Per prima cosa provo ad aprire il file per estrare i dati. Nel caso in cui non riesca allora alzo un eccezione che informera` all'utente che c'e`stato un errore all'apertura del file. Essendo un errore "un-recovable" non potro` esseguire il file equindi ritorno None
        
        #creo una lista piccola che contarra' solo 2 elementi
        lista_piccola= [] 
        try:
            my_file = open(self.name, 'r')
        except:
            raise ExamException('Errore nella lettura del file')
            
            # Esco dalla funzione tornando "niente".
            return None
        


#-------------------------------------------------------

#           fai un rise che ti dece,che se sono piu di 3 elementi, esempio
            #epoch,temperature, televisione
            #oppure 23123443,24, 1023

#-------------------------------------------------------
            





        # Ora inizio a leggere il file linea per linea
        for line in my_file:
            
            # Faccio lo split di ogni linea sulla virgola
            elements = line.split(',')

            # Se NON sto processando l'intestazione...
            if elements[0] != 'epoch':
                    
                # Setto l epoch ed il valore della temperatura
                epoch  = elements[0]
                temperature = elements[1]
                
                # Le variabili "epoch" e "temperature" al momento sono ancora una stringa, poiche' ho letto da file di testo, quindi devo convertire i valore in int/float e se nel farlo ho un errore avverto
                #In questo caso sarebbe un errore "recoverable" e posso proseguire (semplicemente salto la linea)

                #converto il valore di epoch in int
                try:                           
                    epoch = int(epoch)
                except:
                    raise ExamException('Errore nela conversione di epoch a int')
                    continue

                try:
                    temperature= float(temperature)
                except:
                    raise ExamException('Errore nella conversione di temperature a float')
                    continue

                lista_piccola= [epoch,temperature]                
                
                # Infine aggiungo alla lista dei valori questo valore
                time_series.append(lista_piccola)

                #"resetto" la lista_piccola
                lista_piccola=[0]
        
        # Chiudo il file
        my_file.close()
        
        # Quando ho processato tutte le righe, ritorno i valori
        return time_series

