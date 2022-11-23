import ifcopenshell

ifc=ifcopenshell.open('Archivo.ifc')

for p in ifc.by_type('IfcPropertySingleValue'):
  #print(p.NominalValue)
  if p.NominalValue == None:
    ifc.remove(p)

ifc.write('NuevoArchivo.ifc')
print('fin')
