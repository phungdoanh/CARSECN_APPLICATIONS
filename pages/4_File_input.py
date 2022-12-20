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
import CARSEC as CS
from zipfile import ZipFile


#%%# 

st.subheader('Download Excel Template input')


# Input excel 
#input_DB = pd.read_excel(
#    r'Input_files/CARSEC_excel.xlsx',
 #   sheet_name=None, header=0, index_col=None)
#Show all tables in excel
#list_tables=list(input_DB.keys())

#for k in list_tables:  
 #   st.write(k)
 #   st.write(input_DB[k].head(10))


with open("Input_files/CARSEC_excel.xlsx", "rb") as fp:
	btn = st.download_button(label="Download Excel Template",data=fp,file_name="CARSEC_Excel_Input.xlsx",mime="application/xlsx")
	
st.subheader('Upload Excel input')


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
	st.write('Data preview')
	_tables=pd.read_excel(uploaded_file,sheet_name=None)
	for k in _tables:  
		st.write(_tables[k])


st.subheader('Download CARSEC files')

path='Output_files/Multi_CARSEC'
if os.path.exists(path):
	dirs = os.listdir(path)
	for file in dirs:
		os.remove(path+'//'+file)
		

if uploaded_file is not None:
	CS.excel_to_CARSEC(load_path=uploaded_file,export_path='Output_files/Multi_CARSEC/CS_Multi_')


dirs = os.listdir(path)
with ZipFile('Output_files/ARSEC_multi.zip', 'w') as zipObj:
	# Add multiple files to the zip
	for file in dirs:
		st.write(file)
		zipObj.write('Output_files/Multi_CARSEC'+'//'+file)
	
with open('Output_files/CARSEC_multi.zip', "rb") as fp:
	btn = st.download_button(label='Download CARSEC files',data=fp,file_name="CARSEC_multi.zip",mime="application/ZIP")
