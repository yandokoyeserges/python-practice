dict={
    'name':'serges',
    'age':90
}
dict['name']='kana'
print(len(dict))
print(dict)
print(dict['name'])
dict["area"]="kayanza"
print(dict)
dict1={}
dict1=dict.copy()
print(dict1)
print(dict1.get('name'))
del dict1['name']
print(dict1)
dict1.pop("age")
print(dict1)
print(dict1.keys())
print(dict1.values())
for i in dict.values():
    print(i)
