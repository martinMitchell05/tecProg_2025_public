from datetime import datetime as dt


class Cliente:
    def __init__(self, nom, cuit):
        self.nom = nom
        self.cuit = cuit

class Factura:
    def __init__(self, cod_factura: int, fecha_emision: dt.date, cliente, empresa):
        self.cod = cod_factura
        self.fecha = fecha_emision
        self.cliente = cliente
        self.empresa = empresa
        self.detalles = {}
    
    def agregarDetalle(self, detalle: {str,()}):
        for k, v in detalle.items():
            self.detalles[k] = v
    
    def getTotal(self):
        sum = 0
        for v in self.detalles.values():
            sum += v[1]
        
        return sum


class Empresa:
    def __init__(self, nom, cond_iva):
        self.nom = nom
        self.iva = cond_iva
        self.facturas = []

    def getTotalFacturas(self):
        sum = 0
        for f in self.facturas:
            sum += f.getTotal()
        
        return sum
    
    def agregarFactura(self, f: Factura):
        self.facturas.append(f)


emp1 = Empresa("Mayorista S.A", "Monotributo")
cli1 = Cliente("Gilcomat SRL", 30123456781)

f1 = Factura(1000,dt.now(),cli1,emp1)
det1 = {"Porcelanato 45x45":(100,600), "Griferia FV 6 piezas":(1,400)}

f1.agregarDetalle(det1)
emp1.agregarFactura(f1)
print(f"Empresa: {emp1.nom}, IVA: {emp1.iva}\n")
print(f"Nro factura: {f1.cod}\n")
print(f"Cliente: {cli1.nom}, CUIT: {cli1.cuit}\n")
print(f"Fecha: {f1.fecha}\n")
print(f"Total: {f1.getTotal()}\n")

i = 1
for k, v in f1.detalles.items():
    print(f"Detalle {i}: {k}, {v[0]} unidades, Total item: {v[1]}\n")
    i += 1

f2 = Factura(1001,dt.now(),cli1,emp1)
det2 = {"Porcelanato 45x45":(1000,6000), "Griferia FV 6 piezas":(10,40000)}
f2.agregarDetalle(det2)
emp1.agregarFactura(f2)

print(f"Empresa: {emp1.nom}, IVA: {emp1.iva}\n")
print(f"Nro factura: {f2.cod}\n")
print(f"Cliente: {cli1.nom}, CUIT: {cli1.cuit}\n")
print(f"Fecha: {f2.fecha}\n")
print(f"Total: {f2.getTotal()}\n")

i = 1
for k, v in f2.detalles.items():
    print(f"Detalle {i}: {k}, {v[0]} unidades, Total item: {v[1]}\n")
    i += 1

f3 = Factura(1002,dt.now(),cli1,emp1)
det3 = {"Porcelanato 25x35":(10,400), "Griferia FV 4 piezas":(5,3500)}
det4 = {"Inodoro FV c/mochila":(4,120000), "Bidet FV":(4,80000)}
f3.agregarDetalle(det3)
f3.agregarDetalle(det4)
emp1.agregarFactura(f3)

print(f"Empresa: {emp1.nom}, IVA: {emp1.iva}\n")
print(f"Nro factura: {f3.cod}\n")
print(f"Cliente: {cli1.nom}, CUIT: {cli1.cuit}\n")
print(f"Fecha: {f3.fecha}\n")
print(f"Total: {f3.getTotal()}\n")

i = 1
for k, v in f3.detalles.items():
    print(f"Detalle {i}: {k}, {v[0]} unidades, Total item: {v[1]}\n")
    i += 1

print(f"Total emitido por {len(emp1.facturas)} facturas: ${emp1.getTotalFacturas()}\n")
