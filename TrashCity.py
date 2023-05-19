from datetime import datetime

class PuntoGeografico:
    def __init__(self, latitud, longitud):
        #Representa un punto geográfico definido por latitud y longitud.
        self.latitud = latitud
        self.longitud = longitud

class Persona:
    def __init__(self, identificacion, nombre, apellido):
        #Representa una persona con identificación, nombre y apellido.
        self.identificacion = identificacion
        self.nombre = nombre
        self.apellido = apellido

class Camion:
    def __init__(self, conductor, asistentes):
        #Representa un camión con su conductor y asistentes.
        self.conductor = conductor
        self.asistentes = asistentes
        self.turnos = []

    def agregar_turno(self, turno):
        #Agrega un turno a la lista de turnos del camión.
        self.turnos.append(turno)

    def calcular_carga_por_dia(self, fecha, tipo_residuo):
        #Calcula la carga total de un tipo de residuo para una fecha específica.
        total_carga = 0
        for turno in self.turnos:
            if turno.inicio.date() == fecha:
                total_carga += turno.carga[tipo_residuo]
        return total_carga

class Turno:
    def __init__(self, ruta, inicio, fin):
        #Representa un turno de recolección de residuos.
        self.ruta = ruta
        self.inicio = inicio
        self.fin = fin
        self.localizaciones = []
        self.carga = {}
        self.observadores = []

    def agregar_localizacion(self, localizacion, tiempo):
        #Agrega una localización y tiempo al turno y notifica a los observadores.
        self.localizaciones.append((localizacion, tiempo))
        self.notificar_observadores()

    def agregar_carga(self, tipo_residuo, cantidad):
        #Agrega una carga de residuo al turno y notifica a los observadores.
        if tipo_residuo not in self.carga:
            self.carga[tipo_residuo] = 0
        self.carga[tipo_residuo] += cantidad
        self.notificar_observadores()

    def notificar_observadores(self):
        #Notifica a los observadores sobre los cambios en el turno.
        for observador in self.observadores:
            observador.actualizar(self)

    def suscribir_observador(self, observador):
        #Suscribe un observador al turno.
        self.observadores.append(observador)

    def desuscribir_observador(self, observador):
        #Desuscribe un observador del turno.
        self.observadores.remove(observador)

class Observador:
    def actualizar(self, turno):
        #Método abstracto para que los observadores implementen la actualización.
        pass

class GeneradorInformes(Observador):
    def actualizar(self, turno):
        #Genera informes o realiza acciones adicionales con el turno actualizado.
        print(f"Informe generado para el turno {turno}")

# Ejemplo de uso

# Creación de puntos geográficos
punto1 = PuntoGeografico(12.345, -67.890)
punto2 = PuntoGeografico(98.765, -43.210)

# Definición de la ruta con los puntos geográficos
ruta = [punto1, punto2]

# Creación de personas (conductor y asistentes)
conductor = Persona("ID-Conductor", "John", "Doe")
asistente1 = Persona("ID-Asistente1", "Jane", "Smith")
asistente2 = Persona("ID-Asistente2", "Mike", "Johnson")

# Creación de turnos
turno1 = Turno(ruta, datetime(2023, 5, 19, 8, 0, 0), datetime(2023, 5, 19, 12, 0, 0))
turno1.agregar_localizacion(punto1, datetime(2023, 5, 19, 8, 0, 0))
turno1.agregar_localizacion(punto2, datetime(2023, 5, 19, 9, 0, 0))
turno1.agregar_localizacion(punto1, datetime(2023, 5, 19, 10, 0, 0))
turno1.agregar_localizacion(punto2, datetime(2023, 5, 19, 11, 0, 0))
turno1.agregar_carga('vidrio', 10)
turno1.agregar_carga('papel', 20)
turno1.agregar_carga('plastico', 30)
turno1.agregar_carga('metal', 40)
turno1.agregar_carga('organicos', 50)

turno2 = Turno(ruta, datetime(2023, 5, 19, 13, 0, 0), datetime(2023, 5, 19, 17, 0, 0))
turno2.agregar_localizacion(punto1, datetime(2023, 5, 19, 13, 0, 0))
turno2.agregar_localizacion(punto2, datetime(2023, 5, 19, 14, 0, 0))
turno2.agregar_localizacion(punto1, datetime(2023, 5, 19, 15, 0, 0))
turno2.agregar_localizacion(punto2, datetime(2023, 5, 19, 16, 0, 0))
turno2.agregar_carga('vidrio', 5)
turno2.agregar_carga('papel', 10)
turno2.agregar_carga('plastico', 15)
turno2.agregar_carga('metal', 20)
turno2.agregar_carga('organicos', 25)

# Creación de un camión con su conductor y asistentes
camion = Camion(conductor, [asistente1, asistente2])
camion.agregar_turno(turno1)
camion.agregar_turno(turno2)

# Búsqueda de la cantidad total de vidrio recogida en una fecha específica
fecha_busqueda = datetime(2023, 5, 19).date()
total_vidrio = camion.calcular_carga_por_dia(fecha_busqueda, 'vidrio')

# Impreime el resultado
print(f"La cantidad total de vidrio recogida el 19 de mayo de 2023 fue: {total_vidrio} toneladas.")
