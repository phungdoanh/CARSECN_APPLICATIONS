#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 12:22:55 2022

@author: namnguyen


"""

import streamlit as st
import json
import pandas as pd
import os
from collections import defaultdict
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode


path_out_txt=r'/Users/namnguyen/Desktop/CARSEC_STREAMLIT/Out_txt'



#%%

st.subheader("Single Input:")

DB = {}
#**********************************
st.write("En el fichero de datos está permitido hacer comentarios utilizando el símbolo “* ”. ")

st.write("\n")
st.write("-***Titulo de la sección.*** Es obligatorio y debe ser la primera línea.")
st.selectbox( '"Titulo"',['CARSECN'])


# 3-unid
st.write("\n")
st.write("-***“unid”*** unidad")
st.write("Indica las unidades de trabajo. Las opciones son \n")
st.markdown("tm	Toneladas y metros")
st.write("     " "knm	Kilonewtons y metros")
st.write("     ""kift	Kilolibras y pies")
st.write("Los resultados se darán en las unidades definidas en este campo.")
DB['unid'] = st.selectbox('"unid"' , options=['tm','knm','lbin'])

# 4-norm
st.write("\n")
st.write("-***“norm”*** normativa")

st.write("Indica la normativa a emplear en el cálculo. Las opciones son")

st.write("ehe	EHE-08")
st.write("aashto	AASHTO")

DB['norm'] = st.selectbox('"norm"', options=['ehe','aashto'])

# 2-secc
st.write("\n")
st.write("-***“secc horm”*** [módulo de elasticidad] (por defecto toma 3000000 t/m2)")
DB['secc'] = st.selectbox('"secc"', options=['horm'])




# 5-coef horm/ arma/ pret
st.write("\n")
st.write("-[***“coef”*** [“horm” ghorm] [“arma” garma] [“pret” gpret]].") 
st.write("Establece los coeficientes de minoración de los materiales. No es obligatorio poner esta línea. Si se ha definido como normativa la EHE-08 los coeficientes por defecto son 1,50 para el hormigón y 1,15 para los aceros. En el caso de la AASHTO todos los coeficientes valen por defecto la unidad.")

DB['coef_horm'] = st.text_input('"horm"', 1.5)
DB['coef_arma'] = st.text_input('"arma"', 1.15)
DB['coef_pret'] = st.text_input('"pret"', 1.15)

#*******************
st.write("\n")
st.write("-[***“phi”*** compr tracc]")

st.write("Establece los coeficientes reductores que emplea la AASHTO. No es obligatorio poner esta línea. Los coeficientes por defecto son para una sección trabajando a compresión 0,75 y 0,90 en el caso de tracción. El programa calcula los coeficientes reductores en función de la deformación máxima de las armaduras.")


# *************************
#* Punto del contorno
st.write("-***“punt”*** [“[ “ unidad longitud “ ]”]")
st.write("Indica que comienza la definición de las coordenadas de los puntos de la sección. Se puede definir la unidad en la que están dados los datos (m, cm, mm, in, ft)")

st.write("-punto   coordenada X    coordenada Y")

st.write("Definición de cada uno de los puntos")

df_punt_contorno= pd.DataFrame(
    '',
    index=range(10),
    columns=['punt', 'X', 'Y']    
)
st.markdown('**Punto del contorno**')
response = AgGrid(df_punt_contorno, editable=True, fit_columns_on_grid_load=True) 
DB['punt_contorno'] = response['data'].to_dict('records')

# *************************hormigon
st.write("\n")
st.write("-***“horm”*** fck [“[ “ unidad tensión “ ]”]")

st.write("Indica las características del hormigón para el contorno que se define. Se pueden poner varios tipo de hormigones. Dentro de esta sección se definen el contorno cerrado y los huecos poligonales y/o circulares.")
st.write("Se puede definir las unidades en las que está dada la resistencia del hormigón (tm2, kcm2, mpa, ksi,ksf, knm2).")


t_h = st.selectbox("Unidad de hormigon", options=["tm2", "kcm2", "mpa", "ksi","ksf", "knm2"])

DB['horm'] = st.text_input('"horm"', 3500)

# *************************
# Contorno Poligonal (hp)
st.write("\n")
st.write("-***“hp”*** puntos que definen el contorno poligonal")

df_hp = pd.DataFrame(
    '',
    index=range(3),
    columns=['Punto_1', 'Punto_2', 'Punto_3', 'Punto_4']
)
st.markdown('**Contorno Poligonal**')
response = AgGrid(df_hp, editable=True, fit_columns_on_grid_load=True)

DB['contorno_Poligonal']= response['data'].to_dict('records')

# *************************
# hc
st.write("\n")
st.write("-***“hc”*** puntos que define el centro del centro   radio del círculo")
DB['hc'] = st.selectbox('', options=['hc'])
df_hc = pd.DataFrame(
    '',
    index=range(1),
    columns=['Punto_Central', 'Radio']
)
st.markdown('**hc**')
response = AgGrid(df_hc, editable=True, fit_columns_on_grid_load=True)
DB['hc']= response['data'].to_dict('records')

# *************************



st.write("-***“arma”*** fyk [“[ “ unidad tensión “ ]” “[ “ unidad área “ ]”]")

st.write("Indica las características del acero pasivo. Se puede definir cada armadura de manera independiente o entre dos puntos y un número de armaduras")
st.write("Se puede definir las unidades en las que está dada el límite elástico del acero (tm2, kcm2, mpa, ksi,ksf, knm2).")
st.selectbox("unidad tensión ", options=["tm2", "kcm2", "mpa", "ksi","ksf", "knm2"])

st.write("Se puede definir las unidades en las que está dada el área del acero (m2, cm2, mm2, ft2, in2). Para poder dar las unidades del área debe estar definida la unidad del límite elástico")
st.selectbox("unidad área ", options=["m2", "cm2", "mm2", "ft2", "in2"])


DB['arma'] = st.text_input('"arma"', 51000)

# *************************

# Caracteristicas
st.write("\n")
st.write("-punto inicial    punto final      número de cables     área de cada cable")
df_Caracteristicas = pd.DataFrame(
    '',
    index=range(3),
    columns=['Punto_Inicial', 'Punto_Final', 'No_Armadura', 'Area']
)

st.markdown('**Caracteristicas**')
response = AgGrid(df_Caracteristicas, editable=True, fit_columns_on_grid_load=True)
DB['punt_armadura']  = response['data'].to_dict('records')

# *************************
#st.write("* Calculate of section")


st.markdown("-***“calc”*** tipo de cálculo  [diagrama vertical] [“[ “ unidad momento “ ]”]")

st.write("Indica el cálculo a realizar. Las opciones son")

st.write("cálculo de las características geométricas de la sección")

st.write("btención del diagrama de interacción")

st.write("Si se quiere obtener el diagrama de interacción vertical, únicamente se hace para la AASHTO, hay que poner al final de la línea “vert”")
st.write("Se puede definir las unidades en las que están dados los axiles y momentos. Para el caso de diagrama de interacción se ponen unidades de momento (tm, knm, kift, kiin). Para el caso de momento curvatura se ponen unidades de fuerza (t, kn, kip).")


calc = st.selectbox("calc", options=["dibu", "inte"])

st.write("-Axil     momento X    momento Y")




df_LC = pd.DataFrame(
    '',
    index=range(3),
    columns=['Axil', 'monento_X', 'momento_Y']
)


st.markdown('**LC**')
response = AgGrid(df_LC, editable=True, fit_columns_on_grid_load=True, use_checkbox=True)
DB['LC'] = response['data'].to_dict('records')

st.write("Parejas de esfuerzos para los que calcular la sección. Se pueden poner hasta 100 hipótesis")

st.write("		momc	Obtención del diagrama momento curvatura")

st.write("-Axil     beta")

st.write("\n")

st.write("-***“fin”***")

st.write("Indica el final de la sección. Es obligatorio ponerlo")


st.write('fin')

  #%%

import CARSEC as CS

CS.CARSEC_Writer(DB=DB, name="CS_Single_input")

    

 


#%%
   
# =============================================================================
# st.subheader("Single Input:")
# 
# DB = {}
# #**********************************
# st.write("* Tipo de seccion:")
# # 2-secc
# DB['secc'] = st.selectbox('"secc"', options=['horm'])
# st.write("* Unidades a emplear:")
# # 3-unid
# DB['unid'] = st.selectbox("unid" , options=['tm','knm','lbin'])
# st.write("* Normativa a emplear:")
# # 4-norm
# DB['norm'] = st.selectbox('norm', options=['ehe','aashto'])
# st.write("* Coefficients :")
# # 5-coef horm/ arma/ pret
# DB['coef_horm'] = st.text_input("horm", )
# DB['coef_arma'] = st.text_input("arma", )
# DB['coef_pret'] = st.text_input("pret", )
# 
# # *************************
# #* Punto del contorno
# 
# df_punt_contorno= pd.DataFrame(
#     '',
#     index=range(10),
#     columns=['punt', 'X', 'Y']    
# )
# 
# st.header('Punto del contorno')
# response = AgGrid(df_punt_contorno, editable=True, fit_columns_on_grid_load=True) 
# DB['punt_contorno'] = response['data'].to_dict('records')
# 
# # *************************
# 
# st.write("* Definition del hormigon:")
# t_h = st.selectbox("Tipo de hormigon", options=["kN/m2","t/m2"])
# 
# DB['horm'] = st.text_input("hormigon", )
# 
# # *************************
# # Contorno Poligonal (hp)
# 
# df_hp = pd.DataFrame(
#     '',
#     index=range(3),
#     columns=['Punto_1', 'Punto_2', 'Punto_3', 'Punto_4']
# )
# 
# st.header('Contorno Poligonal')
# response = AgGrid(df_hp, editable=True, fit_columns_on_grid_load=True)
# 
# DB['contorno_Poligonal']= response['data'].to_dict('records')
# 
# # *************************
# # hc
# DB['hc'] = st.selectbox('hc', options=['hc'])
# df_hc = pd.DataFrame(
#     '',
#     index=range(1),
#     columns=['Punto_Central', 'Radio']
# )
# 
# 
# st.header('Punto central/ Radio')
# response = AgGrid(df_hc, editable=True, fit_columns_on_grid_load=True)
# DB['hc']= response['data'].to_dict('records')
# 
# # *************************
# 
# st.write("* Definicion de acero pasivo: fyk")
# 
# t_a = st.selectbox("tipo de armadura", options=["kN/m2","t/m2"])
# DB['arma'] = st.text_input("armadura", 51000)
# 
# # *************************
# 
# # Caracteristicas
# df_Caracteristicas = pd.DataFrame(
#     '',
#     index=range(3),
#     columns=['Punto_Inicial', 'Punto_Final', 'No_Armadura', 'Area']
# )
# 
# st.header('Caracteristicas')
# response = AgGrid(df_Caracteristicas, editable=True, fit_columns_on_grid_load=True)
# DB['punt_armadura']  = response['data'].to_dict('records')
# 
# # *************************
# st.write("* Calculate of section")
# calc = st.selectbox("calc", options=["dibu", "inte"])
# 
# df_LC = pd.DataFrame(
#     '',
#     index=range(3),
#     columns=['Axil', 'monento_X', 'momento_Y']
# )
# 
# st.header('LC')
# response = AgGrid(df_LC, editable=True, fit_columns_on_grid_load=True, use_checkbox=True)
# DB['LC'] = response['data'].to_dict('records')
# 
# DB['fin']=st.text_input('fin', 'fin')
# 
# =============================================================================

