#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 20:41:44 2021

@author: anderjackf
"""

def organism_record(record):
    locus_field=record[0].split()
    definition_field=record[1].split(",")
    accession_field=record[2].split()
    organism_field=record[9].split()
    
    accession=accession_field[1]
    
    bp=locus_field[2]
    type_mol=locus_field[4]
    structure=locus_field[5]
    date=locus_field[7]
    
    definition=" ".join(definition_field[0].split()[1:])
    completness=definition_field[1][1:-2]
    
    organism_name=" ".join(organism_field[1:])
    
    return [accession,bp,type_mol,structure,date,definition,completness,organism_name]

def protein_record(record):
    accession_field=record[2].split()
    accession=accession_field[1]
    
    prot_data=[]
    
    length_record=len(record)
    
    #Metodo de busqueda no eficiente pues evalua todas las linas, 
    #pero funciona
    for line_number in range(length_record):
        #Se buscan lineas con CDSs, luego se hace una busqueda justo adelante
        #de esas lineas
        if "     CDS             " in record[line_number]:
            position=record[line_number].split()[1]
    
            for prot_line in range(line_number,length_record):
                if "/transl_table" in record[prot_line]:
                    transl_table=record[prot_line][35:-1]
                    
                if "/product" in record[prot_line]:
                    product=record[prot_line][30:-1].replace('"','')
                    product=product.replace("'",'')
                if "/protein_id" in record[prot_line]:
                    prot_id=record[prot_line][33:-1].replace('"','')
                    
                if "/translation" in record[prot_line]:
                    prot_seq=record[prot_line][35:-1]
                    for prote_seq_lines in record[prot_line+1:]:
                        prot_seq+=prote_seq_lines[21:-1]
                        if '"' in prote_seq_lines:
                            prot_seq+=prote_seq_lines[21:-2]
                            break
                    break
            #Se cargan los datos de cada proteina como tuplas a una lista
            prot_data.append((accession,prot_id,product,position,transl_table,prot_seq))

    return prot_data
            
# def comment_record(record):
def comment_record(record):
    accession_field=record[2].split()
    accession=accession_field[1]
    
    comment_data=[]
    
    can_look=False
    
    for line in record:
        if can_look==True and "##Genome-Annotation-Data-END##" in line:
            break
        if can_look==True:
            if "Genes (total)" in line:
                comment_data.append((accession,"Genes (total)",line[49:-1]))
            if "CDSs (total)" in line:
                comment_data.append((accession,"CDSs (total)",line[49:-1]))
            if "Genes (coding)" in line:
                comment_data.append((accession,"Genes (coding)",line[49:-1]))
            if "CDSs (with protein)" in line:
                comment_data.append((accession,"CDSs (with protein)",line[49:-1]))
        if "##Genome-Annotation-Data-START##" in line:
            can_look=True   
    return comment_data