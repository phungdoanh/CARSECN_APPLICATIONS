#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 18:15:55 2022

@author: namnguyen
"""
import numpy as np
import streamlit as st
import json
import pandas as pd
import os
from collections import defaultdict
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode

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

#%%# 


st.subheader('Preview data')

st.write('**In this template file we organize our :blue[_dataset_] as an excel file with :blue[6] Speadsheets:**')
st.write("***Properties:*** defines all the coefficients of materials.")
st.write("***Geometries:*** indicates all set-up points")
st.write("***hp:*** shows the points which make the poligonal shape.")
st.write("***hc:*** indicates the central point and the radial of steel which located in that position")
st.write("***Caracteristics:*** defines the area of material's distibuition.")
st.write("***LC:*** Load Case")


multi_DB["Properties"]
            
            
            
 
