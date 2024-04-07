import numpy as np
import pull_data as pull
import split_dataframe as splt
import data_graph as dg

def central():
    dataframe = pull.pull_dataframe()

    if len(dataframe.index) == 0:
            print("No hay archivo que utilizar")
    else:
        print("tenemos dataframe")
        df_temp1, df_temp2, df_temp3 = splt.split_info(dataframe)
        array_temp1,array_hour1,array_temp2,array_hour2,array_temp3,array_hour3 = dg.data_dataframe(df_temp1, df_temp2, df_temp3)
        x   = np.array(array_hour1)
        y   = np.array(array_temp1)
        xx  = np.array(array_hour2)
        yy  = np.array(array_temp2)
        xxx = np.array(array_hour3)
        yyy = np.array(array_temp3)
        print(str(x)+"\n"+str(y)+"\n"+str(xx)+"\n"+str(yy)+"\n"+str(xxx)+"\n"+str(yyy))
        #anim.my_animation(x,xx,xxx,y,yy,yyy)
        return x,xx,xxx,y,yy,yyy
        #return df_sensors
