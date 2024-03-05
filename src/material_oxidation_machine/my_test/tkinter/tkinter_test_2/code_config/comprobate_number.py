from code_config import window_alert as alt

def comprovate(variable):
    try:
        variable = float(variable)
        return "yes"
    except ValueError:
        alt.my_alert_window()