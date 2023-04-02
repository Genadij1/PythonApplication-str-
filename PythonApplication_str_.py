
enter = input('Enter text:' )
enter_sym = input('Enter character:' )
c = 0
for i in enter:
    if i == enter_sym:
        c+=1
print('count', c)
