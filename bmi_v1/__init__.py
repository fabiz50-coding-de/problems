import check50

@check50.check()
def BMI_Berechnung():
    """BMI Berechnung"""
    check50.run("python3 bmi_v1.py").stdin("1.66\n60\n", prompt=False).stdout("21.77", regex=False).exit(0)