
def data_dataframe(df_temp1, df_temp2, df_temp3):
    print("se van a sacar los datos de los dataframes")

    #los tres sensores mother foca
    # SENSOR 1
    array_temp1 , array_hour1 = [], []
    max_values_temp1 = df_temp1.count()[1]
    array_temp1 , array_hour1 = array_dataframe(df_temp1, max_values_temp1, array_temp1 , array_hour1, 'temp1')
    # SENSOR 2
    array_temp2 , array_hour2 = [], []
    max_values_temp2 = df_temp2.count()[1]
    array_temp2 , array_hour2 = array_dataframe(df_temp2, max_values_temp2, array_temp2 , array_hour2, 'temp2')
    # SENSOR 3
    array_temp3 , array_hour3 = [], []
    max_values_temp3 = df_temp3.count()[1]
    array_temp3 , array_hour3 = array_dataframe(df_temp3, max_values_temp3, array_temp3 , array_hour3, 'temp3')

    return array_temp1,array_hour1,array_temp2,array_hour2,array_temp3,array_hour3 

def array_dataframe(df_data, max_values_temp, array_temp , array_hour, valor):
    print("se van a sacar los arrays de los dataframes")

    for i in range(0, max_values_temp):
        array_temp.append(df_data.loc[:, valor][i])
        array_hour.append(df_data.loc[:,'hora'][i])

    print("termino la seccion de arrays")
    print(array_temp)
    print(array_hour)

    return array_temp , array_hour