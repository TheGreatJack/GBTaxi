#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 20:41:49 2021

@author: anderjackf
"""

import os
import data_search as dts
import db_interaction as db


#Itera sobre los gbff y hace una busqueda en cada uno de los archivos
#presentes en el directorio. Archivo por archivo y record por record el 
#iterador va extrayendo y subiendo los datos a la base de sql
def cycler_silent(gbff_path,db_path):
    for file in os.listdir(gbff_path):
        file_handler = open(gbff_path+"/"+file)
        file_data = file_handler.readlines()
        file_data= record_checker(file_data)
        
        for record in file_data:
            org_data=dts.organism_record(record)
            db.insert_org(db_path,org_data)
            
            prot_data=dts.protein_record(record)
            db.insert_protein(db_path, prot_data)
            
            comment_data=dts.comment_record(record)
            db.insert_comment(db_path, comment_data)
            
        file_handler.close()
        
#Igual que cycler_silent pero con comentarios a lo largo de cada paso
def cycler_verbose(gbff_path,db_path):
    for file in os.listdir(gbff_path):
        print("Analizando archivo: "+file)
        file_handler = open(gbff_path+"/"+file)
        file_data = file_handler.readlines()
        file_data= record_checker(file_data)
        
        for record in file_data:
            print("Cargando_record:\n","\t"+record[0][:-1])
            
            org_data=dts.organism_record(record)
            print("Datos de organismo extraidos...")
            db.insert_org(db_path,org_data)
            print("Datos de organismo cargados...")
            
            prot_data=dts.protein_record(record)
            print("Datos de proteinas extraidos...")
            db.insert_protein(db_path, prot_data)
            print("Datos de proteinas cargados...")
            
            comment_data=dts.comment_record(record)
            print("Datos de comentarios extraidos...")
            db.insert_comment(db_path, comment_data)
            print("Datos de comentarios cargados...")
            
        file_handler.close()
        print("Archivo completado\n")
    print("Análisis completado")
        
    
#Esta funcion evalua cuantos records hay en un archivo gbff y los separa
#para poder hacer las busquedas en cada record.
def record_checker(file_data):
    parts=[-1]
    file_records=[]
    for line_number in range(len(file_data)):
        if "//\n" in file_data[line_number]:
            parts.append(line_number)  
    for parts_id in range(1,len(parts)):
        file_records.append(file_data[parts[parts_id-1]+1:parts[parts_id]])
    return file_records
