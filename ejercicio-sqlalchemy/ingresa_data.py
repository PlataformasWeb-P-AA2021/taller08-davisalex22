  
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del
# archivo genera_tablas
from genera_tablas import MundialFootball

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
import csv
import itertools
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()


jugadores = open("data/mundial2018.csv", "r", encoding= 'utf-8')    

# Ingreso de datos Jugadores
# Uso de itertools.islice para saltar el encabezado del csv
 
for j in  itertools.islice(jugadores, 1, None):   
    cadenaJugadores = j.split("|")
    cadenaJugadores[-1] = cadenaJugadores[-1].strip()
    #print(cadenaJugadores)          
    session.add(MundialFootball(fifa_display_name= cadenaJugadores[1], country=cadenaJugadores[2],  
                               last_name=cadenaJugadores[3], first_name= cadenaJugadores[4], shirt_name= cadenaJugadores[5],
                               pos= cadenaJugadores[6], height= cadenaJugadores[7], caps= cadenaJugadores[8],
                               goals= cadenaJugadores[9]))

# se confirma las transacciones       
session.commit()