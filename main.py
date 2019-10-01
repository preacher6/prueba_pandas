#%%
import pandas as pd
import matplotlib.pyplot as plt

#%%
ri = pd.read_csv('police.csv')
ted = pd.read_csv('ted.csv')

#%%
ri.head()

#%%
ri.shape
ri.dtypes
#%%  Suma de cada columna que contenga datos NaN
ri.isnull().sum()

#%% Eliminar columna que contiene todos NaN
ri.dropna(axis='columns', how='all', inplace=True)

#%%  Filtrar por violacion = exceso de velocidad
speeding_violation = ri[ri.violation=='Speeding']

#%%  Filtrar por mujeres
speeding_violation[speeding_violation['driver_gender']=='F']

#%%  Convertir variable categorica en numerica
pd.get_dummies(speeding_violation, columns=['driver_gender'], drop_first=True)

#%%  Contar cantidad de hombres y mujeres que cometieron ese tipo de infraccion
speeding_violation.driver_gender.value_counts(normalize=True)

#%% Value counts enseña la cantidad de valores que hay por cada categoria
ri.search_conducted.value_counts() 

#%% Con dropna false se cuentan hasta los Nan
ri.search_type.value_counts(dropna=False)

#%%  Porcentaje de violaciones por hombres
ri[ri.driver_gender=='M'].violation.value_counts(normalize=True)

#%%  Porcentaje de violaciones por mujeres
ri[ri.driver_gender=='F'].violation.value_counts(normalize=True)

#%% Agrupar violaciones por genero
ri.groupby('driver_gender').violation.value_counts(normalize=True).unstack()

#%% tomar solo velocidades de la Agrupacion violaciones por genero
ri.groupby('driver_gender').violation.value_counts(normalize=True).loc[:, 'Speeding']

#%%  Con mean se saca el promedio de valores que sean verdadero
ri.search_conducted.mean()

#%%  Agrupar por genero el promedio de busquedas forzadas
ri.groupby('driver_gender').search_conducted.mean()

#%%  Agrupar por genero el promedio de busquedas forzadas
ri.groupby(['violation', 'driver_gender']).search_conducted.mean().unstack()

#%% Bsuqueda con strings
ri['frisk'] = ri.search_type.str.contains('Protective Frisk')
ri.frisk.value_counts()  # Cantidad de cada valor
ri.frisk.sum()  # Suma de todos los valores. Al ser booleano se suman los unos

#%%  # Elegir porcion de la string
ri.stop_date.str.slice(0, 4).value_counts()

#%% Combinar strings para crear una nueva
combined = ri.stop_date.str.cat(ri.stop_time, sep=' ')

#%% Crear una nueva columna con la serie rpeviamnete creada
ri['stop_datetime'] = pd.to_datetime(combined)

#%%
ri.stop_datetime.dt.weekday
ri.stop_datetime.dt.year.value_counts().sort_values()

#%%  Plotear agrupnado por horas
ri.groupby(ri.stop_datetime.dt.hour).drugs_related_stop.mean().plot()

#%%  Plotear agrupnado por hora exacta
ri.groupby(ri.stop_datetime.dt.time).drugs_related_stop.mean().plot()

#%%
