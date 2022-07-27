from numpy import save
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime


engine = create_engine("mysql+pymysql://root:@localhost/datosdesalud")   ## Conectarse a DB

my_dict = { 
'sintomas':['Dolor de cabeza', 'Dolor de estómago', 'Fiebre', 'Dolor muscular' , 'Dolor de garganta'],
'paciente':['Jose Carlos', 'Juan Carlos', 'Pedro Alejandro', 'Jorge Manuel', 'Mario Rodrigo']
}
claves = my_dict.keys()
#len(my_dict)


tipo_1 =  {'Fechas': [],
'Ciudad_de_origen': [],
'Cantidad_de_personas': [],
'Sintoma': []
}
claves_1 = tipo_1.keys()
#len(tipo_1)

tipo_2 = {'sintomas': [],
'paciente': [],
'fecha': [] 
}
claves_2 = tipo_2.keys()
#len(tipo_2)



def save_to_bd(my_dict):    ## Convertir a DataFrame y guardar en DB
    if claves == claves_1:
        df = pd.DataFrame.from_dict(my_dict)
        df.to_sql('datosdepaciente', con = engine, if_exists = 'append', chunksize = 1000, index= False)
    
    elif claves == claves_2:
        df_2 = pd.DataFrame.from_dict(my_dict) 
        df_2.to_sql('sintomas_paciente', con = engine, if_exists = 'append', chunksize = 1000, index= False)


#save_to_bd(my_dict)

if __name__ == "__main__":
    save_to_bd()

