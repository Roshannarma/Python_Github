from spell_check_library import SpellCheck
def spell_checker(country):
    spell_check = SpellCheck('D:\Python_Github\John_hopkins_api\some_countries.txt')
    spell_check.check(country)
    mystring = spell_check.correct()
    mystring = mystring.replace("'", "")
    mystring = mystring.replace('"', "")
    if mystring[0] == " ":
        mystring = mystring[1:]
    return mystring
