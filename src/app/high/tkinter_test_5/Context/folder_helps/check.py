from alerts import verify
from alerts import not_num

def check_integer(var):
    try:
        var = int(var)
        #verify.alert_verify()
        if var > 0:
            return var
        else:
            return False
    except ValueError as e:
        #not_num.alert_not_number()
        return False 
    

    
