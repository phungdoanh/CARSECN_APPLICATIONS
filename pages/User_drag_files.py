#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 18:35:55 2022

@author: namnguyen
"""
import streamlit as st
import pandas as pd
import seaborn as sns


data=st.file_uploader('Upload Dataset', type=['xlsx', 'csv'])

if data is not None:
 
    df=pd.read_excel(data, sheet_name=None, header=0, index_col=None)
    list_tables=list(df.keys())

    for k in list_tables:  
        st.write(k)
        st.write(df[k].head(10))
        

