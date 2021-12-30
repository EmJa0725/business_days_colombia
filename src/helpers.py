from datetime import datetime

#Initial variables
start_date = datetime.strptime("01-08-2021", "%d-%m-%Y")
end_date = datetime.strptime("31-08-2022", "%d-%m-%Y")


def is_valid_date(date):
    """Valida que la fecha se encuentra en el rango definido"""
    input_date = datetime.strptime(date, "%d-%m-%Y")
    return start_date <= input_date <= end_date