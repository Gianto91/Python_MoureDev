
nombre = input('¿Tu nombre?')
apellido = input('¿Tu Apellido?')
edad = input('¿Tu Edad?')
correo = input('¿Tu correo?')
if not correo:
    correo = 'No ingreso correo'

usuario = {
    "nombre": nombre,
    "apellido": apellido,
    "edad": edad,
    "correo": correo

}

print("\nDatos del usuario almacenados:")
print(f"Nombre: {usuario['nombre']}")
print(f"Apellido: {usuario['apellido']}")
print(f"Edad: {usuario['edad']}")
print(f"Correo: {usuario['correo']}")
