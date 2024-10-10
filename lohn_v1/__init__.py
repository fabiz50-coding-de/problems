import check50

@check50.check()
def Berechnungen_Bruttolohn():
    """Berechnungen Bruttolohn"""
    check50.run("python3 lohn_v1.py").stdin("35\n2.75\n", prompt=False).stdout("96.25", regex=False).exit(0)
    check50.run("python3 lohn_v1.py").stdin("31\n3.125\n", prompt=False).stdout("96.88", regex=False).exit(0)