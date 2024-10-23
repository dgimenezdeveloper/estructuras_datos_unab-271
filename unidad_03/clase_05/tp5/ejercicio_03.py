""" Utilizando TADs se deberá representar y programar un Juzgado de faltas. Del juzgado 
se conoce nro de juzgado, direccion, juez a cargo y las multas pertenecientes a ese juzgado. De cada multa se conoce nro de acta, dominio, fecha emision, importe, fecha vencimiento, codigo QR. """

class Juzgado:
    def __init__(self, num_juzgado, direccion, juez, multas = []):
        self.num_juzgado = num_juzgado
        self.direccion = direccion
        self.juez = juez
        self.multas = multas

    def __str__(self):
        return f'Juzgado N° {self.num_juzgado}, Direccion: {self.direccion}, Juez: {self.juez}'
    
    #Metodo que agrega multas al juzgado
    def agregar_multa(self, multa):
        self.multas.append(multa)
    
    def buscar_multa(self, dominio):
        multas_por_dominio = []
        for multa in self.multas:
            if multa.dominio == dominio:
                multas_por_dominio.append(multa)
        return multas_por_dominio

    def imprimir_multas(self, dominio):
        for multa in self.buscar_multa(dominio):
            print(multa)

class Multa:
    def __init__(self, num_acta, dominio, fecha_emision, importe, fecha_vencimiento, codigo_qr):
        self.num_acta = num_acta
        self.dominio = dominio
        self.fecha_emision = fecha_emision
        self.importe = importe
        self.fecha_vencimiento = fecha_vencimiento
        self.codigo_qr = codigo_qr

    def __str__(self):
        return f'Número de acta: {self.num_acta}, Dominio: {self.dominio}, Fecha de emisión: {self.fecha_emision}, Importe: {self.importe}, Fecha de vencimiento: {self.fecha_vencimiento}, Código QR: {self.codigo_qr}'
    

def main():
    juzgado1 = Juzgado(1, 'Av. Siempre Viva 123', 'Dr. House')
    multa = Multa(1, 'AAA123', '12/12/2021', 2000, '12/01/2022', '123456789')
    multa1 = Multa(2, 'AAA123', '12/12/2021', 2000, '12/01/2022', '123456789')
    multa2 = Multa(3, 'BBB123', '12/12/2021', 2000, '12/01/2022', '123456789')
    juzgado1.agregar_multa(multa)
    juzgado1.agregar_multa(multa1)
    juzgado1.agregar_multa(multa2)
    juzgado1.imprimir_multas('AAA123')
    juzgado1.imprimir_multas('BBB123')

main()