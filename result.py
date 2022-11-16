class Result:
    '''név,idő,nehézség,elkészítés,hozzávalók'''
    def __init__(self, row: str):
        data = row.split(';')
        self.name = data[0]
        self.time = data[1]
        self.difficult = data[2]
        self.preparation = data[3]
        self.ingredients = data[4]

