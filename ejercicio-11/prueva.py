import practica

carro = practica.Veiculo("for","verde")

archivo = practica.Conversor("./test1")

archivo.WriteFileJson(carro)

texto = practica.Veiculo(**archivo.ReadFileJson())

print(texto.color)
