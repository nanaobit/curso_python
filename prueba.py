def cifrar(msj):
  s = ""
  for i in msj:
    s += chr(ord(i)+1)
  return s
def decifrar(msj):
  s =""
  for j in msj:
    s += chr(ord(j)-1)

e = input("ingrese el mensaje a cifrar:")
print(f"el mensaje cifrado es: {cifrar(e)}")
print(f"el mensaje decifrado es:{decifrar(cifrar(e))}")
