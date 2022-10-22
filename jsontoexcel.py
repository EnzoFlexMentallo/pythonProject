from pprint import pprint
import pandas as pd


def transformar_decimales(monto):
     
     valor_2dec = '{:.2f}'.format(monto)
     #print("monto origen: ", monto, "\n monto transformado", valor_2dec)
     return valor_2dec


# 0, 1, 2 = MP, LC, MP + Combinado
# 18E4

datos = pd.read_json('./data.json')

df1 = pd.DataFrame(datos)

print("**///////////////////////** DataFrame original")
print(df1)


#new_df=df1.assign(Profit=6)
#df1.insert(2, "fecha", '20-04-2021', allow_duplicates=False)
#df1.insert(2, "fecha", nuevaColDf, allow_duplicates=False)

nuevaColDf = df1['email']


solicitud_fecha = {'fecha_solicitud'}

df1.insert(2, "fecha", [{'fechadia: 13-10-2022', 'fechaAprobado: 13-10-2022'}], allow_duplicates=False)
print("**///////////////////////** DataFrame agregar campo")
pprint(df1)

##print(df1.info())
##print(df1['email'][0])
##print(df1['email'][1])

#to replace into pd 
#email_origen = df1['email'][0]
#nuevodf = df1.replace(email_origen,'gatogordo@gato.cl')
#print(nuevodf['email'])

#filtrar por contenido del texto 
#busquedaemail= nuevodf[nuevodf['email'].str.contains("gatogordo")]
#print("encontre el correo del gato gordo\n", busquedaemail)

#  modificamos los montos a decimales (2) 
for mo in df1['amounts']:

     #nuevoMontodf = df1.replace(mo['TC'],transformar_decimales(mo['TC'])), df1.replace(mo['MP'],transformar_decimales(mo['MP'])), df1.replace(mo['LC'],transformar_decimales(mo['LC']))
     LCMontoDecimal = transformar_decimales(mo['LC'])
     TCMontoDecimal = transformar_decimales(mo['TC'])
     MPMontoDecimal = transformar_decimales(mo['MP'])

     #valor_LC = '{:.2f}'.format(mo['LC'])
     #print(valor_LC) 
     #monto_df = df1.replace(mo['LC'], MontoDecimal)
     mo['LC'] = LCMontoDecimal
     mo['TC'] = TCMontoDecimal
     mo['MP'] = MPMontoDecimal
     #print(monto_df['amounts'][0]['LC'])
   

     ##print(mo['email'])
     #nuevoMontoMPdf = df1.replace(mo['MP'],transformar_decimales(mo['MP']))
     #nuevoMontoLCdf = df1.replace(mo['LC'],transformar_decimales(mo['LC']))
    

#print(df1['amounts'])
#for m in df1['amounts']:
#     print(m['TC'])
#nuevomonto = pd.DataFrame(df1)
#print (monto_df['amounts'][0]['TC'])
#for json_data in nuevoMontodf:
#   pprint(json_data['amounts'])



#print(montos_origen)
#print(transformar_decimales(valor))
#valor_transformado = transformar_decimales(valor)
#print(valor_transformado)
#print(nuevodf)
#pprint(nuevodf['email'][0])
#print(nuevodf['profile'][0])
#print(df1['profile'][1]['dob'],df1['profile'][1]['name'])

# cambiar formato numeros
# latitud_formateada = '{:.0f}'.format(df1['profile'][1]['location']['lat'])
#print(latitud_formateada)

#print(nuevodf['id'])
#for json_objects in df1:
#    print(json_objects)
#    for json2 in json_objects:
#        print(json2)


#for json_data in df1.values:
#   pprint(json_data)
#df1.to_excel("./data_en_excel1.xlsx", sheet_name = "pagina1", engine ='openpyxl')
#print(datos.head())

# filtrar por condicion en pandas (dataframe)
# df = [df['id'] > 1 & df[profile] != null]


