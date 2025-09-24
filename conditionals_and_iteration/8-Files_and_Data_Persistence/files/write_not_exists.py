file_create = open('write_x.txt', 'wb')
with open('write_x.txt', 'x') as fw:
    fw.write('Writen line 1')

with open('write_x.txt', 'x') as fw:
    fw.write('Writen line 2')