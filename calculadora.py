class Calculadora:
	def __init__(self):
		self.numero = 0.0
		self.entrada = 0.0
		self.tip_oper = ""
	
	def iniciar(self):
		self.numero = 0.0
		self.entrada = 0.0
	
	def capturarInicial(self, valor):
		self.numero = valor
	
	def operacion(self, entrada):
		if self.tip_oper == "S":
			self.numero = self.numero + entrada
		if self.tip_oper == "R":
			self.numero = self.numero - entrada
		if self.tip_oper == "M":
			self.numero = self.numero * entrada
		if self.tip_oper == "D":
			self.numero = self.numero / entrada
		
		return self.numero