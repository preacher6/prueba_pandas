import numpy as np
import math
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn; seaborn.set_style('whitegrid')

mercurio = [1.230, 0.490, 1.330, 0.190, 0.040, 0.830, 0.044,
            0.810, 1.200, 0.710, 0.270, 0.500, 0.490, 1.080,
            1.160, 0.980, 0.050, 0.630, 0.150, 0.560, 0.190, 
            0.410, 0.770, 0.730, 0.590, 0.280, 0.340, 0.340,
            0.340, 0.750, 0.840, 0.870, 0.500, 0.560, 0.340,
            0.170, 0.180, 0.100, 0.190, 0.210, 0.040, 0.860,
            0.490, 0.520, 1.100, 0.650, 0.160, 0.270, 0.940,
            0.400, 0.430, 0.250, 0.270]

std_merc = [np.std(mercurio), np.std(mercurio[:40]), np.std(mercurio[-40:])]
mean_merc = [np.mean(mercurio), np.mean(mercurio[:40]), np.mean(mercurio[-40:])]
alphas = [1.65, 1.96, 2.33]
porc = ['90', '95', '99']
number_data = ['Para las 53 muestras:', 'Para las primeras 40 muestras',
 'Para las ultimas 40 muestras']
n = [len(mercurio), len(mercurio[:40]), len(mercurio[-40:])]
data_Y = []
data_error = []
for index, val_n in enumerate(n):
    print(number_data[index])
    print('...........')
    for alpha, porcen in zip(alphas, porc):        
        superior = mean_merc[index]-alpha*std_merc[index]/math.sqrt(val_n)
        inferior = mean_merc[index]+alpha*std_merc[index]/math.sqrt(val_n) 
        print('Para un intervalo de confianza del', str(porcen), '%:')
        print(superior*100, '<= u <=', inferior*100)
        print('El numero de muestras es: ', ((alpha*std_merc[index])/((inferior-superior)/2))**2)
        print('-----------')
        data_Y.append(np.median([inferior, superior]))
        data_error.append(inferior-superior)

# Defining the figure and figure size
fig, axs = plt.subplots(1, 3, figsize=(10, 6))
X = range(len(alphas))
print(data_Y[:3])
# Plotting the error bars
axs[0].errorbar(X, data_Y[:3], yerr=data_error[:3], fmt='o', ecolor='orangered',color='orangered', capsize=4)
axs[0].set_title('53 muestras')
axs[0].set_ylim([0, 1])
#axs[0].set_xticks([1, 2, 3], minor=False)
axs[1].errorbar(X, data_Y[3:6], yerr=data_error[3:6], fmt='o', ecolor='steelblue',color='steelblue', capsize=2)
axs[1].set_title('40 primeras muestras')
axs[1].set_ylim([0, 1])
axs[2].errorbar(X, data_Y[6:], yerr=data_error[6:], fmt='o', ecolor='red',color='red', capsize=2)
axs[2].set_title('40 ultimas muestras')
axs[2].set_ylim([0, 1])
plt.setp(axs, xticks=[0, 1, 2], xticklabels=['90%', '95%', '99%'])
plt.show()
