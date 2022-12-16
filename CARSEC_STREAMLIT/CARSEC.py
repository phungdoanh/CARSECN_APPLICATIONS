#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 14:29:57 2022

@author: namnguyen
"""

import pandas as pd
import json
import os


#%%# Create a None Database

# =============================================================================


# DB['secc']=str
# DB['unid']=str
# DB['norm']=str
# DB['coef_horm']= float
# DB['coef_arma']= float
# DB['coef_pret']= float

# DB['punt_contorno']=[0:{'punt':1, 'X':0,'Y':0},'punt':2, 'X':2,'Y':0},...] # pandasDataFrame.to_dict('records')
# DB['horm']=float
# DB['contorno_Poligonal']=[0:{'Punto_1':1,'Punto_2':2,'Punto_3':3,'Punto_4':4,...}]
# DB['hc']=[0:{'Punto_Central':5,'Radio':0.3}]
# DB['arma']=float
# DB['punt_armadura']=[0:{'Punto_Inicial':6,'Punto_Final':7,'No_Armadura':10, 'Area':0.000314}]
# DB['LC']=[0:{"Axil":-10, 'monento_X':5, 'monento_Y':2}]
# 
# =============================================================================

#%% Functions:

def CARSEC_Writer(DB,name='CARSEC'):
    with open(name+'.txt', 'w') as f:
        f.write('CARSECN'+' \n')
        f.write('* Tipo de seccion '+'\n')  
        f.write('secc '+str(DB['secc'])+' \n')
        f.write('* Unidades a emplear. Opciones: tm - knm - lbin'+'\n')  
        f.write('unid '+str(DB['unid'])+' \n')
        f.write('* Normativa a emplear. Opciones: ehe  asashto '+'\n')  
        f.write('norm '+str(DB['norm'])+' \n')
        f.write('* Coeficientes de seguridad EHE o coeficientes phi AASHTO. No es obligatoria '+'\n')  
        f.write('coef horm '+str(DB['coef_horm'])+' arma '+str(DB['coef_arma']) + ' pret '+str(DB['coef_pret'])+  ' \n')
        f.write('* Puntos del contorno '+'\n')  
        f.write('punt '+'\n')

        for v in DB['punt_contorno']:
            for k in v.keys():           
                f.write(str(v[k])+' ')
            f.write('\n')
          
            
        f.write('* Definición del hormigón: fck, modulo de elasticidad. Este último es obligatorio '+'\n')     
            
        f.write('horm '+str(DB['horm'])+' \n')
        
        for v in DB['contorno_Poligonal']:
            for k in v.keys():           
                f.write(str(v[k])+' ')
            f.write('\n')
              
        f.write('hc ') 
        for v in DB['hc'] :
            for k in v.keys():           
                f.write(str(v[k])+' ')
            f.write('\n')
            
        f.write('* Definicion del acero pasivo: fyk '+'\n')   
        
        f.write('arma '+str(DB['arma'])+' \n')
    
        for v in DB['punt_armadura']:
            for k in v.keys():           
                f.write(str(v[k])+' ')
            f.write('\n')
            
        
        f.write('calc inte'+' \n')
        for v in DB['LC'] :
            for k in v.keys():
                f.write(str(v[k])+' ' )
            f.write('\n')
        f.write('fin')
#%%                         
    
def save_to_json(DB,name='my_DB'):
    with open(name+'.json', 'w') as f:
        json.dump(DB, f)
#%%        
def load_json(path='my_DB.json'):
    f= open('my_DB.json', 'r')
    DB=json.load(f)
    f.close()
    return DB

#%%
    
# Create a function Streamlit to JSON !!!!!!

def DB_to_JSON(DB):
    #read DB to Dict
    # Create a loop to check if the values are DF and transform to JSON
    for k,v in DB.items():
        if type(v)== pd.core.frame.DataFrame:
            v.to_json(orient='split')
        else:
            v=json.dumps(v)
            
            
            
            

            

