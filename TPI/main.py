from abc import ABC, abstractmethod
from datetime import datetime as dt

###  ---------------------------------------------------------------- ###

class Ciudad:
    def __init__(self, codigo: str, nombre: str, provincia: str):
        self._codigo = codigo
        self._nombre = nombre
        self._provincia = provincia

    def get_nombre(self) -> str:
        return f'{self._nombre}, {self._provincia}'
    
    
###  ---------------------------------------------------------------- ###

class Itinerario:
    def __init__(self,ciudad_partida: Ciudad,ciudad_llegada: Ciudad, ciudades_paradas: list['Ciudad'] ):
        self._ciudad_partida = ciudad_partida
        self._ciudad_llegada = ciudad_llegada
        self._paradas = ciudades_paradas
        
    def consultar_itinerario(self):
        print(f'Ciudad partida: {self._ciudad_partida.get_nombre()} \n Ciudad llegada: {self._ciudad_llegada.get_nombre()} \n Paradas: ')
        cont_paradas = 1
        for ciudad in self._paradas:
            print(f'{cont_paradas}. {ciudad.get_nombre()}')
            cont_paradas += 1

    def obtener_destino(self)->str:
        return self._ciudad_llegada.get_nombre()

###  ---------------------------------------------------------------- ###

class Pasajero:
    def __init__(self, nombre,email,dni):
        self._nombre = nombre
        self._email = email
        self._dni = dni

    def get_Nombre(self):
        return self._nombre

###  ---------------------------------------------------------------- ###

class Unidad:
    def __init__(self, patente, asientos : list['Asiento']):
        self._patente = patente
        self._asientos = asientos

    def consultar_unidad(self):
        print(f"Patente: {self._patente}")

    def _buscar_asiento(self,nro_asiento): 
        asiento_buscado = None
        for a in self._asientos:
            if a.tiene_numero(nro_asiento):
                asiento_buscado = a
                break
        return asiento_buscado

    def reservar_asiento(self,nro_asiento)->'Asiento':
        asien = self._buscar_asiento(nro_asiento)
        
        asiento_reservado = None
        if asien != None:
            asiento_reservado = asien.reservar()    
            
        return asiento_reservado

    def get_asientos(self) -> list['Asiento']:
        return self._asientos             

    def consulta_asientos_disponibles(self):
        for asiento in self._asientos:
            asiento.consultar_asiento()

    def vender_asiento(self,nro_asiento) -> 'Asiento':
        asien = self._buscar_asiento(nro_asiento)
        asiento_vendido = None
        if asien != None:
            asiento_vendido = asien.vender()    
            
        return asiento_vendido
        
        
###  ---------------------------------------------------------------- ###

class Asiento:
    def __init__(self, numero):
        self._numero = numero
        self._ocupado = False
    
    def get_numero(self):
        return self._numero

    def esta_ocupado(self):
        return self._ocupado

    def reservar(self)->'Asiento':
        asiento_reserva = None
        if not self._ocupado:
            self._ocupado = True
            asiento_reserva = self
        else: 
            print("Error, asiento no disponible")
            
        return asiento_reserva

    def vender(self) -> 'Asiento':
        asiento_venta = None
        if not self._ocupado:
            self._ocupado = True
            asiento_venta = self
        else: 
            print("Error, asiento no disponible")
            
        return asiento_venta


    def consultar_asiento(self):
        if not self._ocupado:
            print(f"{self._numero},", end="")

    def tiene_numero(self, nro):
        return self._numero == nro
###  ---------------------------------------------------------------- ###

class Reserva:
    def __init__(self,fechaHora, pasajero: Pasajero, asiento: Asiento):
        self._fechaHora = fechaHora
        self._pasajero = pasajero
        self._asiento = asiento

    def get_numero_asiento(self):
        return self._asiento.get_numero()

###  ---------------------------------------------------------------- ###

class Venta:
    def __init__(self, fechaHora : dt, asiento:Asiento,pasajero:Pasajero,medioPago:'IMedioPago'):
        self._fecha = fechaHora
        self._asiento = asiento
        self._pasajero = pasajero
        self._medioPago = medioPago

    def get_numero_asiento(self):
        return self._asiento.get_numero()

    def get_medio_de_pago(self):
        return  self._medioPago.tipo()
###  ---------------------------------------------------------------- ###

class Servicio: 
    def __init__(self, unidad: Unidad, itine: Itinerario, fechaPartida: dt, fechaLlegada: dt, calidad: str, precio: float, cod: int):
        self._cod = cod
        self._fechaPartida = fechaPartida
        self._fechaLlegada = fechaLlegada
        self._calidad = calidad
        self._precio = precio
        self._unidad = unidad
        self._itinerario = itine
        self._ventas: list['Venta'] = []
        self._reservas: list[Reserva] = []


    def tiene_codigo(self, codigo: int):
        return self._cod == codigo

    def consultar_servicio(self):
        print(f"Servicio {self._cod}: \n") 
        print(f"  Itinerario:")
        self._itinerario.consultar_itinerario()
        print(f"Fecha de partida: {self._fechaPartida.strftime('%d/%m/%Y %H:%M')}")
        print(f"Fecha de llegada: {self._fechaLlegada.strftime('%d/%m/%Y %H:%M')}")
        print(f"Calidad del servicio: {self._calidad}")
        print(f"Precio: ${self._precio:.2f}")
        print(f"Unidad asignada:")
        self._unidad.consultar_unidad()

    def mostrar_asientos_disponibles(self):
        print("Asientos libres: ", end="")
        self._unidad.consulta_asientos_disponibles()

    def mostrar_todos_los_asientos(self):
        self.mostrar_asientos_disponibles()
        ##VENDIDOS
        asientos_vendidos = []
        for v in self._ventas:
            asientos_vendidos.append(v.get_numero_asiento())
        asientos_vendidos.sort()
        ##RESERVADOS
        asientos_reservados = []
        for r in self._reservas:
            asientos_reservados.append(r.get_numero_asiento())
        asientos_reservados.sort()

            # Armar strings
        #str_libres = ", ".join(map(str, libres)) if libres else "ninguno"
        str_reservados = ", ".join(map(str, asientos_reservados)) if asientos_reservados else "ninguno"
        str_vendidos = ", ".join(map(str, asientos_vendidos)) if asientos_vendidos else "ninguno"

        # Mostrar con el formato deseado
        print(f"\nOcupado: {str_reservados} (reservado) / Vendido: {str_vendidos}\n")

   
    def reservar_asiento_servicio(self,nro_asiento: int, pasajero: Pasajero):
        asiento = self._unidad.reservar_asiento(nro_asiento)
        if asiento != None:
            self._reservas.append( Reserva(dt.now(),pasajero,asiento ))
            print(f"Reserva realizada: Pasajero {pasajero.get_Nombre()}, asiento {nro_asiento}, servicio del {self._fechaPartida.strftime('%d/%m/%Y')}\n")
            self.mostrar_todos_los_asientos()

    def esta_dentro_fecha(self, f_desde : dt, f_hasta : dt ) -> bool:
        return f_desde <= self._fechaPartida <= f_hasta     

    def calcular_total_vendido(self) -> float:
        return self._precio * len(self._ventas)
        
    def obtener_ciudad_destino(self) -> str:
        return self._itinerario.obtener_destino()

    def obtener_codigo(self)->int:
        return self._cod

    def mostrar_ventas_medio_de_pago(self,conteo:dict): 
    
        for venta in self._ventas:
            medio = venta.get_medio_de_pago()
            if medio in conteo:
                conteo[medio] += 1
            else:
                conteo[medio] = 1

        return conteo

    def vender_asiento_servicio(self,nro_asiento: int, pasajero: Pasajero, medioPago: 'IMedioPago'):
        asiento = self._unidad.vender_asiento(nro_asiento)
        if asiento != None:
            self._ventas.append( Venta(dt.now(),asiento,pasajero,medioPago) )
            print(f"Venta realizada: Pasajero {pasajero.get_Nombre()}, asiento {nro_asiento}, servicio del {self._fechaPartida.strftime('%d/%m/%Y')}, pago: {medioPago.tipo()}\n")
            self.mostrar_todos_los_asientos()

            
###  ---------------------------------------------------------------- ###

# todo: implement
class IMedioPago(ABC):
    @abstractmethod
    def Pagar():
        pass
    @abstractmethod
    def tipo(self):
        pass


class MercadoPago(IMedioPago):
    def __init__(self, celular: str, email: str):
        self._celular = celular
        self._email = email
    def Pagar():
        pass
    def tipo(self):
        return "MercadoPago"


class Uala(IMedioPago):
    def __init__(self, email: str, nombreTitular: str):
        self._nombreTitular = nombreTitular
        self._email = email
    def Pagar():
        pass
    def tipo(self):
        return "UALA"


class TarjetaCredito(IMedioPago):
    def __init__(self, numero: str, dniTitular: int, nombre: str, fechaVenc: dt):
        self._numero = numero
        self._dniTitular = dniTitular
        self._nomber = nombre
        self._fechaVenc = fechaVenc
    def Pagar():
        pass
    def tipo(self):
        return "Tarjeta de Credito"
        
###  ---------------------------------------------------------------- ###

class Argentur:
    def __init__(self):
        self._servicios : list[Servicio] = []
        self._pasajeros : list[Pasajero] = []
        self._itinerarios : list[Itinerario] = []


    def consultar_servicios(self):
        for servicio in self._servicios:
            servicio.consultar_servicio()
    
    def _seleccionar_servicio(self, cod_serv: int)->Servicio:
        serv_busc = None
        for servicio in self._servicios:
            if servicio.tiene_codigo(cod_serv):
                serv_busc = servicio
                break
        return serv_busc 
                
    def consultar_asientos_servicio(self, cod_serv: int):
        servicio = self._seleccionar_servicio(cod_serv)
        if servicio != None:
            servicio.mostrar_asientos_disponibles()
                
    def crearServicio(self, unidad: Unidad, itine: Itinerario, fechaPartida:dt, fechaLlegada:dt, calidad:str, precio:float, cod: int):
        self._servicios.append( Servicio(unidad,itine,fechaPartida,fechaLlegada,calidad,precio,cod) )

    def realizar_reserva(self,cod: int,nro_asiento:int, pasajero: Pasajero):
        servicio = self._seleccionar_servicio(cod)
        if servicio != None:
            servicio.reservar_asiento_servicio(nro_asiento, pasajero)
    
    def realizar_venta(self, cod: int, nro_asiento: int, pasajero: Pasajero, medio: IMedioPago):
        servicio = self._seleccionar_servicio(cod)
        if servicio != None:
            servicio.vender_asiento_servicio(nro_asiento, pasajero, medio)

    def _consultar_total_servicio(self,serv: Servicio, mapa:dict):
        cod = serv.obtener_codigo()
        mapa[cod] = serv.calcular_total_vendido()

    def _contar_viaje_a_localidades_destino(self,serv:Servicio,mapa:dict):
        ciudad = serv.obtener_ciudad_destino()
        if ciudad in mapa:
            mapa[ciudad] += 1
        else:
            mapa[ciudad] = 1
        

    def generar_informe(self,f_desde : dt, f_hasta : dt):
        total_vendido = 0.0
        mapa_ciudades_destino = dict()
        mapa_ventas_medio_pago =  dict()
        mapa_ventas_totales = dict()

        for s in self._servicios:
            
            if s.esta_dentro_fecha(f_desde,f_hasta):
                
                total_vendido += s.calcular_total_vendido()
                self._consultar_total_servicio(s,mapa_ventas_totales)

                self._contar_viaje_a_localidades_destino(s,mapa_ciudades_destino)
            
                s.mostrar_ventas_medio_de_pago(mapa_ventas_medio_pago)

        ### Forma resumen ###
        print(f"Informe periodo {f_desde} al {f_hasta}")
        print(f'Total facturado: {total_vendido}')
        print(f'Totales por servicio facturado:')
        for servicio,monto in mapa_ventas_totales.items():
            print(f"Servicio {servicio}: ${monto}")
        print(f'Cantidad de viajes a cada localidad destino:')
        for ciudad, cantidad in mapa_ciudades_destino.items():
            print(f"{ciudad}: {cantidad} veces")
        
        print(f'Cantidades de pagos discriminados por medio de pago:')
        for medio_pago, cant in mapa_ventas_medio_pago.items():
            print(f"Medio de pago: {medio_pago}: {cant}")



if __name__ == "__main__":
    ###  CIUDADES ###
    c1_SF = Ciudad(3000, "Santa Fe","Santa Fe")
    c2_R = Ciudad(1231, "Rosario","Santa Fe")
    c3_Tost = Ciudad(3000, "Tostado","Santa Fe")
    c4_Vt = Ciudad(1232,"Venado Tuerto","Santa Fe")
    
    ### ITINERARIOS ###
    It1 = Itinerario(c4_Vt, c3_Tost, [c2_R,c1_SF])
    
    It2 = Itinerario(c1_SF,c3_Tost,[])

    ### ASIENTOS ###
    asientos = []
    for i in range(1, 10):
        asientos.append(Asiento(i))

    asientos_2 = []
    for i in range(1, 10):
        asientos_2.append(Asiento(i))

    ### UNIDADES ###
    u1 = Unidad("AB312HS",asientos)
    u2 = Unidad("AA346GG",asientos_2)

 ### PASAJERO ###
    ps1 = Pasajero("Tito Calderon","momorelojero@gmail.com",12312332)
    ### Ventas ###

    #venta_1 = Venta( dt.now(), Asiento(1),ps1,MercadoPago("6546654","juan@gmail.com"))
    #venta_2 = Venta( dt.now(), Asiento(2),ps1,TarjetaCredito("34255555",4565465,"nombre",dt.now()))
    #venta_3 = Venta( dt.now(), Asiento(3),ps1,Uala("juan@gmail.com","nombre"))
    #venta_4 = Venta( dt.now(), Asiento(4),ps1,MercadoPago("6546654","juan@gmail.com"))
    #venta_5 = Venta( dt.now(), Asiento(6),ps1,TarjetaCredito("34255555",4565465,"nombre",dt.now()))
    #venta_6 = Venta( dt.now(), Asiento(6),ps1,TarjetaCredito("34255555",4565465,"nombre",dt.now()))

    ### SERVICIOS ###
    #serv1 = Servicio(u1,It1,dt.now(),dt.now(),"Primiun",12312312,1)
 
    
    ### AGENCIA ###
    agencia = Argentur()
    agencia.crearServicio(u1,It1,dt.now(),dt.now(),"Primiun",300000,1)
    agencia.crearServicio(u2,It2,dt.now(),dt.now(),"Estandar",50000,2)
    agencia.consultar_servicios()
    #agencia.consultar_asientos_servicio(1)
    agencia.realizar_reserva(1,4,ps1)
    #agencia.realizar_reserva(1,4,ps1)
    agencia.realizar_venta(1,1,ps1,Uala("juan@gmail.com","nombre"))
    #agencia.realizar_venta(1,1,ps1,Uala("juan@gmail.com","nombre"))
    agencia.realizar_venta(1,2,ps1,TarjetaCredito(4447555999,12312332,"tito",dt(2028,12,1)))
    agencia.realizar_venta(1,6,ps1,MercadoPago(3491555666,"example@example.com"))
    agencia.realizar_venta(1,8,ps1,Uala("juan@gmail.com","nombre"))

    agencia.realizar_reserva(2,1,ps1)
    agencia.realizar_venta(2,8,ps1,Uala("example@gmail","Tito"))


    agencia.generar_informe(dt(2024,5,20),dt(2025,6,20))