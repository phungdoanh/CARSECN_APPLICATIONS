
# Import pckg
import pandas as pd
import numpy as ny
import matplotlib.pyplot as plt
import matplotlib
import streamlit as st
import seaborn as sns
matplotlib.use('Agg')



def main():
    """Semi_Auto_ML_App with Streamlit """

    st.title('Semi_Auto_ML_App')
    activities=['EDA', 'Plot','Model Building', 'About']

    choice=st.sidebar.selectbox('Select Activities', activities)
    if choice=="EDA":
        st.subheader("Exploratory Data Analysis")
        data=st.file_uploader('Upload Dataset', type=['csv','json','txt','xlsx'])

        if data is not None:
            df=pd.read_csv(data)
            st.dataframe(df.head(10))

            if st.checkbox('Show shape'):
                st.write(df.shape)

            elif st.checkbox("Show Columns"):
                all_columns=df.columns.to_list()
                st.write(all_columns)

            elif st.checkbox('Select columns to show'):
                all_columns = df.columns.to_list()
                selected_columns=st.multiselect("Select Columns", all_columns)
                new_df=df[selected_columns]
                st.dataframe(new_df)

            elif st.checkbox('Show Sumary'):
                st.write(df.describe())

            if st.checkbox('Show Value Counts'):

                st.write(df.iloc[:,-1].value_counts())


    elif choice =='Plot':
        st.write('Data Visualization')
        data = st.file_uploader('Upload Dataset', type=['csv', 'json', 'txt', 'xlsx'])

        if data is not None:
            df = pd.read_csv(data)
            st.dataframe(df.head(10))

            if st.checkbox('Correlation with Seaborn'):
                st.write(sns.heatmap(df.corr(),annot=False))
                st.pyplot()
                st.set_option('deprecation.showPyplotGlobalUse', False)


            if st.checkbox('Pie Chart'):
                all_columns=df.columns.to_list()
                column_to_plot=st.selectbox('Select one column to plot', all_columns)
                pie_plot=df[column_to_plot].value_counts().plot.pie(autopct="%1.1f%%")
                st.write(pie_plot)
                st.pyplot()

            all_columns_names=df.columns.tolist()
            type_of_plot=st.selectbox("Select Type of Plot",["area", "bar","line","hist","box","kde"])
            selected_colmns_names=st.multiselect("Select Columns to Plot",all_columns_names)

            if st.button("Generate Plot"):
                st.success("Generating Customizable Plot of {} for {}".format(type_of_plot,selected_colmns_names))

                #Plot By Streamlit
                if type_of_plot=="area":
                    cust_data=df[selected_colmns_names]
                    st.area_chart(cust_data)

                elif type_of_plot=="bar":
                    cust_data=df[selected_colmns_names]
                    st.bar_chart(cust_data)

                elif type_of_plot=="line":
                    cust_data=df[selected_colmns_names]
                    st.line_chart(cust_data)

                #Plot By Customers
                elif type_of_plot:
                    cust_plot=df[selected_colmns_names].plot(kind=type_of_plot)
                    st.write(cust_plot)
                    st.pyplot()








    elif choice=="Model Building":
        st.write('hola')





if __name__== '__main__':
    main()


