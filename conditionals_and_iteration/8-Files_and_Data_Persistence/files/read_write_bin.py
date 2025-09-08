with open('example.bin', 'wb') as fw:
    fw.write(b'Hello World....')

with open('example.bin', 'rb') as f:
    print(f.read())