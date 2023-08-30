class Persona:

    def __init__(self,ID,Nombre,Apellido):
        self.ID=ID
        self.Nombre=Nombre
        self.Apellido=Apellido


        class Hombre(Persona):
            def casado(self):
             print("esta persona esta casada")

             def soltero(self):
             print("esta persona esta soltera")

        class Mujer(Persona):
            def casado(self):
             print("esta persona esta casada")

            def soltero(self):
             print("esta persona esta soltera")


    Nombre=input("Ingrese nombre ")
    Apellido=input("Ingrese apellido ")
    ID=input("ingrese ID ")

    print("el nombre de esta persona es",Nombre)
    print("el apellido de esta persona es", Apellido)
    print("El numero de ID de",Nombre , Apellido ,"es",ID)





