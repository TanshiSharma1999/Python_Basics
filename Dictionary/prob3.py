my_keys = ["name", "age", "city","language"]
my_values = ["Robert", 21, "Berlin","python"]
#without zip
my_dic={}
for i,key in enumerate(my_keys):
    my_dic[key]=my_values[i]
    print(f"Keys= {key},Value= {my_dic[key]}")
print(my_dic)

#with zip
my_keys = ["name", "age", "city","language"]
my_values = ["Rob", 16, "Paris","France"]

result = dict(zip(my_keys, my_values))
print(result)
