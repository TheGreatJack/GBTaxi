#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 20:40:30 2021

@author: anderjackf
"""

import sqlite3

def insert_org(db_path,org_data):
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    
    sql = "insert into Organism"
    sql += "(accession,bp,type,structure,date,definition,completness,organism_name) "
    sql += "values('{}','{}','{}','{}','{}','{}','{}','{}');"
    sql = sql.format(org_data[0],org_data[1],org_data[2],org_data[3],
               org_data[4],org_data[5],org_data[6],org_data[7])

    
    cur.execute(sql)
    con.commit()
    con.close()
    

def insert_protein(db_path,prot_data):
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    
    sql = "insert into Protein"
    sql += "(accession,id,product,position,translation_table,seq) "
    sql += "values(?,?,?,?,?,?)"
    
    cur.executemany(sql, prot_data)
    
    con.commit()
    con.close()

def insert_comment(db_path,comment_data):
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    
    sql = "insert into Comments"
    sql += "(accession,comment,value) "
    sql += "values(?,?,?)"

    cur.executemany(sql, comment_data)
    
    con.commit()
    con.close()

def forgot_all(path):
    con = sqlite3.connect(path)
    cur = con.cursor()
    
    cur.execute("DELETE from Organism")
    cur.execute("DELETE from Protein")
    cur.execute("DELETE from Comments")
    cur.execute("DELETE from sqlite_sequence")
    
    con.commit()
    con.close()