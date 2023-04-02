
enter = input('Enter text: ')
l_c = 0
n_c = 0
for i in enter:
    if i.isalpha():
        l_c+=1
    if i.isdigit():
        n_c+=1
print('Кількість літер: ', l_c)
print('Кількість цифр: ', n_c)