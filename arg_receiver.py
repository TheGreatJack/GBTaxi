#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 20:45:37 2021

@author: anderjackf
"""


from sys import argv

#Pequeño handler de datos de entrada, no se ve afectado por el orden de
#entrada de los argumentos

def arg_handler():
    db_path=""
    gbff_path=""
    deleteold=False
    verbose_mode=False
    
    for x in argv[1:]:
        if x.startswith("db="):
            db_path=x.split("=")[1]
        if x.startswith("gbff="):
            gbff_path=x.split("=")[1]
        if x == "deleteold":
            deleteold=True
        if x == "verb":
            verbose_mode=True
            
    
    return db_path,gbff_path,deleteold,verbose_mode
    