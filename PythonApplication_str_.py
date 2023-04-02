
enter = input('Enter text:' )
enter_sym = input('Enter word:' )
c = 0
for w in enter:
    if w == enter_sym:
        c+=w
print('count', c)
