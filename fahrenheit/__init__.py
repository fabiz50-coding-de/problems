import check50

@check50.check()
def Temperatur_32C():
    """Temperatur 32C"""
    check50.run("python3 fahrenheit.py").stdin("32", prompt=False).stdout("89.6", regex=False).exit(0)

@check50.check()
def Temperatur_0C():
    """Temperatur 0C"""
    check50.run("python3 fahrenheit.py").stdin("0", prompt=False).stdout("32.0", regex=False).exit(0)

@check50.check()
def Temperatur_25C():
    """Temperatur 25C"""
    check50.run("python3 fahrenheit.py").stdin("25", prompt=False).stdout("77.0", regex=False).exit(0)