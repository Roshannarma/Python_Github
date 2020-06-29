from spell_check_library import SpellCheck
def spell_checker(country):
    spell_check = SpellCheck('D:\Python_Github\John_hopkins_api\some_countries.txt')
    spell_check.check(country)
    return eval(spell_check.correct())
