import basic_spell_check as bsc
f = open("D:\Python_Github\John_hopkins_api\some_countries.txt","r")
my_dict = eval(f.readline())
my_input = input("Give a Country you want to look up: ")
print(bsc.spell_check(my_dict,my_input))
