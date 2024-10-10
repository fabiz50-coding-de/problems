import check50

@check50.check()
def single_name():
    """single name"""
    check50.run("python3 hello_name.py").stdin("peter", prompt=False).stdout("Hello, Peter !", regex=False).exit(0)

@check50.check()
def full_name():
    """full name"""
    check50.run("python3 hello_name.py").stdin("james BOND", prompt=False).stdout("Hello, James Bond !", regex=False).exit(0)

@check50.check()
def no_name_shows_hello_world():
    """no name shows hello world"""
    check50.run("python3 hello_name.py").stdin("", prompt=False).stdout("Hello, world!", regex=False).exit(0)