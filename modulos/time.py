import time
hora = time.localtime().tm_hour
minutos= time.localtime().tm_min
if ((hora - 19 ) *-1 >=8):
	print("aun te faltan",11-hora ,"para entrar",60 - minutos)
elif((hora - 19) *-1 <=8):
	print("te faltan ",19-hora,"hrs con", 60 - minutos, "para salir")
else:
	print("nos vemos mañana")
