#!/usr/bin/env python
# -*- coding: utf-8 -*-


#data_file = raw_input('ARCHIVO ORIGINAL CON TODOS LOS DATOS _ NO INCLUIR .csv = ')
data_file = 'EURUSD1_1'
tick_data_file = data_file + '.csv'

#data_file_rellenar = raw_input('ARCHIVO CON LOS DATOS PARA RELLENAR . Es el archuivo accesorio_ NO INCLUIR .csv = ')
data_file_rellenar = 'EURUSD1_2' + '.csv'

new_file_name = data_file + '_FINAL' + '.csv' # CREAMOS EL NUEVO ARCHIVO
last_file = data_file + '_LAST' + '.csv'

#----------------------------------------------------------------------

manf_original = open(tick_data_file , 'r') #ABRIRMOS EL ARCHIVO ORIGINAL MODO LECTURA
manf_rellenar = open(data_file_rellenar , 'r') #ABRIRMOS EL ARCHIVO ACCESORIO PARA BUSCAR LAS FECHAS EN EL


#--------------- CREAR LISTA COM FECHAS DE ARCHIVO ORIGINAL

fechas_original = list() #--- SOLO LAS FECHAS NO LOS DATOS
manf_final = open(new_file_name , 'wb')

for line in manf_original:
    line2 = line.split(',')
    line2 = line2[0] + ' ' + line2[1]
    fechas_original.append(line2)
    manf_final.write(line)
    #print line2
manf_final.close()
print 'Fechas Original tiene ' + str(len(fechas_original)) + ' registros.'

#--------------- CREAR LISTA CON FECHAS QUE SI ESTAN EN EL ARCHIVO SECUNDARIO PERO NO EN EL ORIGINAL
longitud = int('25')
fechas_rellenar = list() #--- LAS FECHAS Y LOS DATOS

for line in manf_rellenar:
    line2 = line.split(',')
    line2 = line2[0] + ' ' + line2[1]

    if line2 not in (fechas_original) and (len(line) > longitud):
        manf_final = open(new_file_name , 'a+')
        manf_final.write(line)
        fechas_rellenar.append(line2)
        #print line + ' @@@  NO incluido'
    else :
        continue

print 'Se incliran ' + str(len(fechas_rellenar)) + ' registros'

print 'SE ACABO'

