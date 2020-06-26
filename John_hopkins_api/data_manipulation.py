
f = open("D:\Python_Github\John_hopkins_api\countries.txt","r")
dict = eval(f.readline())
#dict.sort()
#print(dict)
for x in range(0,len(dict)):
    if dict[x] == "Korea (North)":
        dict[x] = "North Korea"
    elif dict[x] == "Korea (South)":
        dict[x] = "South Korea"
    elif "(" in dict[x]:
        location = dict[x].index("(")
        dict[x] = dict[x][0:location-1]

f.close()
f = open("D:\Python_Github\John_hopkins_api\some_countries.txt","w")
f.write(str(dict))
f.close()

"""
f = open("D:\Python_Github\John_hopkins_api\slugs.txt","r")
my_dict = eval(f.readline())
my_dict.sort()
print(my_dict)
f.close()
f = open("D:\Python_Github\John_hopkins_api\slugs.txt","w")
f.write(str(my_dict))
f.close()
"""
