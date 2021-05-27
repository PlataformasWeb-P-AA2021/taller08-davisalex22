from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and
import csv
# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import MundialFootball

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()

# Crear un archivo que permita presentar todos los jugadores, ordenados por el número de goles.

jugadores = session.query(MundialFootball).order_by(MundialFootball.goals).all()
print(jugadores)

