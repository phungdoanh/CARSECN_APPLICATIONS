#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 14:29:57 2022

@author: namnguyen
"""

import pandas as pd
import json
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib as mpl
import copy


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

def CARSEC_Writer(DB,export_path='CARSEC'):
    with open(export_path+'.txt', 'w') as f:
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

def DB_to_json(DB):
    #read DB to Dict
    # Create a loop to check if the values are DF and transform to JSON
    for k,v in DB.items():
        if type(v)== pd.core.frame.DataFrame:
            v.to_json(orient='split')
        else:
            v=json.dumps(v)
            

def table_to_dict(dict_tables):
	#Create a multi database where each Database equivalents to one unique ID
	ID_list = (dict_tables['Properties']['ID'].unique()).tolist()
	multi_DB={}
	for i in ID_list:
		multi_DB[i]={}
		for k in dict_tables:
			multi_DB[i][k] = dict_tables[k][dict_tables[k]['ID'] == i]
			if k=='Properties':
				multi_DB[i]['secc']=multi_DB[i][k]['secc'].tolist()[0]
				multi_DB[i]['unid']=multi_DB[i][k]['unid'].tolist()[0]
				multi_DB[i]['norm']=multi_DB[i][k]['norm'].tolist()[0]
				multi_DB[i]['coef_horm']=multi_DB[i][k]['coef_horm'].tolist()[0]
				multi_DB[i]['coef_arma']=multi_DB[i][k]['coef_arma'].tolist()[0]
				multi_DB[i]['coef_pret']=multi_DB[i][k]['coef_pret'].tolist()[0]
				multi_DB[i]['horm']=multi_DB[i][k]['horm'].tolist()[0]
				multi_DB[i]['arma']=multi_DB[i][k]['arma'].tolist()[0]
				
			elif k=="Geometries":
				multi_DB[i]['punt_contorno']=multi_DB[i][k].iloc[:,1:10].dropna(axis=1).to_dict('record')
				
			elif k=="hp":
				multi_DB[i]['contorno_Poligonal']=multi_DB[i][k].iloc[:,1:11].dropna(axis=1).to_dict('records')
				
			elif k=="hc":
				multi_DB[i]['hc']=multi_DB[i][k].iloc[:,1:3].to_dict('record')
				
			elif k=="Caracteristicas":
				multi_DB[i]['punt_armadura']=multi_DB[i][k].iloc[:,1:10].to_dict('record')
				
			elif k=="LC":
				multi_DB[i]['LC']=multi_DB[i][k].iloc[:,1:5].to_dict('record')
	
	return multi_DB



def multi_CARSEC_writer(multi_DB,export_path='CS_Multi_'):
	for i_d in multi_DB:
		CARSEC_Writer(multi_DB[i_d], export_path=export_path+str(i_d))




def excel_to_CARSEC(load_path,export_path='CS_Multi_'):
	dict_tables = pd.read_excel(load_path,sheet_name=None)
	multi_DB=table_to_dict(dict_tables)
	multi_CARSEC_writer(multi_DB=multi_DB,export_path=export_path)





def polygonal_graphics(x,y,path):

	fig, ax = plt.subplots()
	
	
	trapezoid = patches.Polygon(xy=list(zip(x,y)), fill=False)
	ax.add_patch(copy.copy(trapezoid))
	
	t_start = ax.transData
	t = mpl.transforms.Affine2D().rotate_deg(0)
	t_end = t + t_start
	
	trapezoid.set_transform(t_end)
	ax.add_patch(trapezoid)
	ax.set_xlim([-5, 5])
	ax.set_ylim([-5, 5])
	fig.savefig(path+'.png',bbox_inches='tight',dpi=100)
