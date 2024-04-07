def comprovate(var):
    try:
        var = int(var)
        if var > 0:
            return var
        else:
            return False
    except ValueError:
        #my alerta
        return False

def range_hour(var):
    if var <= 23:
        return var
    else:
        return False

def range_minute(var):
    if var <=59:
        return var
    else: return False
