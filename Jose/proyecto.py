import pandas as pd
import matplotlib.pyplot as plt

file_path = r'C:\Users\Villa5050G\Desktop\curso de python\Pandas\database.xlsx'



df = pd.read_excel(file_path)

#print(df.head())

hydrological_disasters = df[df['Disaster Subgroup'] == 'Hydrological']
años_de_interes = [2013, 2014, 2015] #modificar con el rango de años 
#####################################################################

filtro_disasters = hydrological_disasters[hydrological_disasters['Start Year'].isin(años_de_interes)]

desastres_por_mes = filtro_disasters['Start Month'].value_counts().sort_index()
print(desastres_por_mes )
desastres_por_region = filtro_disasters['Region'].value_counts()

cantidad_de_datos = len(filtro_disasters)
print(f"Cantidad de datos disponibles: {cantidad_de_datos}")

total_danos_por_año = filtro_disasters.groupby('Start Year')['Total Damage'].sum()

promedio_afectados_por_año = filtro_disasters.groupby('Start Year')['Total Affected'].mean()

desastres_por_año = filtro_disasters['Start Year'].value_counts()


# Crear un gráfico de barras para mostrar el número de desastres por año
desastres_por_region.plot(kind='bar')
plt.title('Número de Desastres Hidrológicos por Región (2013-2015)')
plt.xlabel('Region')
plt.ylabel('Número de Desastres')
plt.xticks(rotation=45)
plt.show()
