import pandas as pd

def split_info(df_sensors):
    print("vamo a dividir es monda")

    #----------------------------------------------------------------temperature 1
    df_temp1 = pd.DataFrame(df_sensors.loc[:, ['hora','temp1']])
    print("dataframe 1")
    df_temp1.head(2)
    #----------------------------------------------------------------temperatura 2
    df_temp2 = pd.DataFrame(df_sensors.loc[:, ['hora','temp2']])
    print("dataframe 2")
    df_temp2.head(2)
    #----------------------------------------------------------------temperatura 3
    df_temp3 = pd.DataFrame(df_sensors.loc[:, ['hora','temp3']])
    print("dataframe 3")
    df_temp3.head(2)

    return df_temp1, df_temp2, df_temp3
