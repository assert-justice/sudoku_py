text = ''
with open('hard.txt') as f:
    text = f.read()
with open('hard.txt','w') as f:
    f.write(text.replace('.','0'))