names = ["John", "Jerry", "Joe", "Jim", "Jack"]
list_version =[]
list_version = [name.lower() for name in names]
print(list_version)
list_upper =[]
list_upper = [name.upper() for name in names]
print(list_upper)
list_title = []
list_title = [name.title() for name in list_upper]
print(list_title)
