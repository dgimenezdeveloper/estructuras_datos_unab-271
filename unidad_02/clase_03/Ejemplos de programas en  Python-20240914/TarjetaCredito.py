class TarjetaCredito():
	
	def __init__(self, nombre, banco, numeroTarjeta, limite, balance):
		# variables de la TarjetaCredito
		self.nombre=nombre
		self.banco=banco
		self.numeroTarjeta= numeroTarjeta
		self.limite=limite              # limite de mi tarjeta de crédito
		self.balance= balance           #monto q me permitirá ver cuanto va utilizando en la tarjeta
		
	def dar_nombre(self):
		return self.nombre
		
	def dar_banco (self):
		return self.banco
		
	def dar_numeroTarjeta (self):
		return self.numeroTarjeta
		
	def dar_limite(self):
		return self.limite
		
	def dar_balance(self):
		return self.balance
		
	def tiene_credito(self, monto):
		#vamos a verificar que tenga credito, si tiene credito devuelve True y actualiza el balance
		if monto+self.balance > self.limite:
			return False
		else:
			return True
	
	def actualizar_credito(self, monto):
		#Cuando paga su tarjeta de crédito se actualiza el balance
		self.balance = self.balance + monto
		
	def presentar(self):
		datos= "El cliente " + self.nombre + " Tiene una linea de Crédito de: "+ str (self.limite) + "$  " + " y solo puede utilizar :" + str(self.limite - self.balance) 
		print (datos)
	
		
# programa principal

cliente23=TarjetaCredito("Pérez", "Banco Provincia", "123456789876", 500000, 0)
print ("Los datos del cliente nuevo son: ")
cliente23.presentar()
gasto=float (input ("ingrese el monto a utilizar en su Tarjeta de Drédito: "))
if cliente23.tiene_credito(gasto):
	print("Su Tarjeta tiene crédito disponible para efectuar ese gasto: ")
	cliente23.actualizar_credito(gasto)
	print()
	print("Se procedio a actualizar la disponibilidad de su Tarjeta: " , cliente23.dar_limite() - cliente23.dar_balance())
else:
	print ("su Tarjeta no tiene crédito")
	


