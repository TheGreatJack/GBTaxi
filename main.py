#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 20:44:00 2021

@author: anderjackf
"""

from arg_receiver import arg_handler
import db_interaction as db
import file_iterator as fl 



def main():
    db_path,gbff_path,deleteold,verbose_mode=arg_handler()
    
    if deleteold == True:
        db.forgot_all(db_path)
    
    if verbose_mode == False:
        fl.cycler_silent(gbff_path,db_path)
    elif verbose_mode == True:
        fl.cycler_verbose(gbff_path,db_path)
  

if __name__ == '__main__':
    main()