name_list = ['ajay','resh','anand','advaith','parvathy']
for name in name_list:
    print(name)

int_list = [1,2,3,4]
for val in int_list:
    print (val)

i = 0
while i < len(name_list):
    print (name_list[i])
    i = i + 1

# Insertion / Addition , Deletion, sorting a list, reversing a list
# 'ajay','resh','anand','advaith','parvathy'
list.sort(name_list)
print (name_list)

int_list.append('123')
int_list.insert(0,'xxx')
int_list.extend(['123123','321321'])

print (int_list)
print (int_list.index('123123'))
print (int_list.remove('123123'))
n = int_list.index('123123')
print (int_list.index('123123'))




