from datetime import date

class Data:
    def __init__(self):
        self.dia = date.today().day
        self.mes = date.today().month
        self.ano = date.today().year