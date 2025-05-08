import printing_functions
diseños_no_imprimidos = ['Modelo1', 'Modelo2', 'Modelo3']
modelos_completados = []
printing_functions.imprimir_modelos(diseños_no_imprimidos, modelos_completados)
print("Modelos completados:", modelos_completados)

from printing_functions import imprimir_modelos
diseños_no_imprimidos = ['Modelo4', 'Modelo5']
modelos_completados = []
imprimir_modelos(diseños_no_imprimidos, modelos_completados)
print("Modelos completados:", modelos_completados)

from printing_functions import imprimir_modelos as im
diseños_no_imprimidos = ['Modelo6', 'Modelo7']
modelos_completados = []
im(diseños_no_imprimidos, modelos_completados)
print("Modelos completados:", modelos_completados)

import printing_functions as pf
diseños_no_imprimidos = ['Modelo8', 'Modelo9']
modelos_completados = []
pf.imprimir_modelos(diseños_no_imprimidos, modelos_completados)
print("Modelos completados:", modelos_completados)

from printing_functions import *
diseños_no_imprimidos = ['Modelo10', 'Modelo11']
modelos_completados = []
imprimir_modelos(diseños_no_imprimidos, modelos_completados)
print("Modelos completados:", modelos_completados)