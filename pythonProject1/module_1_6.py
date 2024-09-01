from datetime import datetime

# 2nd task
my_dict = {"Mary" : 2005, "Victory" : 1998,"Lera" : 2000,"Sara" : 1975,}
print("my_dict:", my_dict)
print("Existing value Victory:",  my_dict["Victory"])
print("Not existing value Natasha:", my_dict.get("Natasha"))
my_dict["Natasha"] = 2001
my_dict["Mika"] = 1999
deleted_value = my_dict.pop("Lera")
print("Deleted value:", deleted_value)
print("Modified my_dict:", my_dict,"\n")
# 3rd task
my_set = {10,10,20,20,55,55,"GitHub", 3.14}
print("my_set:", my_set)
my_set.add(500)
my_set.add((800,900))
my_set.remove(20)
print("Modified my_set:", my_set)



