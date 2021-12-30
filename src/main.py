from datetime import datetime, date, timedelta
import pandas as pd
import numpy as np
from helpers import is_valid_date
from utils import colombia_holidays

"""Construya el código fuente de un algoritmo que, dadas dos fechas entre agosto de 2020 y agosto de 2021,
calcule el número de días hábiles entre dichas fechas teniendo en cuenta el calendario de Colombia"""

def get_dates():
    """Función que captura la fecha inicial y la fecha final comprendida"""    
    valid_input_date = {
        'inicial': False,
        'final': False
    }
    input_date = {
        'inicial': '',
        'final': ''
    }
    #Valida cada entrada del usuario
    for field in valid_input_date.keys():
        while not valid_input_date[field]:
            try:
                input_date[field] = str(input(f'Ingrese fecha {field} (dd-mm-yyyy): '))
                valid_input_date[field] = is_valid_date(input_date[field])
                if not valid_input_date[field]:
                    print('fecha invalida, intente de nuevo')
            except Exception as e:
                print(f'Error: {str(e)}')
    
    return input_date['inicial'], input_date['final']

def get_business_days(start_date, end_date):
    """Función que retorna el numero de dias habiles entre dos fechas teniendo en cuenta feriados de Colombia"""
    try:
        holiday_date = None
        date_count = 0
        #Conversion a tipo fecha 
        start_date = datetime.strptime(start_date, "%d-%m-%Y")
        end_date = datetime.strptime(end_date, "%d-%m-%Y")
        #Valicación fechas ingresadas
        if start_date > end_date:
            print("La Fecha final no puede ser menor a la fecha inicial")
            return 0
        #Calculo dias calendario
        days = pd.bdate_range(start_date, end_date)
        res = len(days)
        #Obtiene la cantidad de festivos de colombia que existen entre las fechas ingresadas
        for date in colombia_holidays:
            holiday_date = datetime.strptime(date[1], "%d-%m-%Y")
            today = datetime.strftime(holiday_date,"%Y-%m-%d")
            if start_date <= holiday_date <= end_date and np.is_busday(today):
                date_count += 1
        business_days = res - date_count
        return business_days
    except Exception as e:
        print(f'Error: {str(e)}')
        
if __name__ == "__main__":
    while True:
        start_date, end_date = get_dates()
        business_days = get_business_days(start_date, end_date)
        print(f'La cantidad de días hábiles en Colombia entre las fechas ingresadas es: {business_days}')