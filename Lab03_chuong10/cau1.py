filename = input('Which file would you like to back-up? ')
new_filename = filename + '.bak'
backup = open(new_filename, 'w')

try:
    file = open(filename)
    for line in file:
        backup.write(line)
    backup.close()
    file.close()
    print("Closed?",file.closed)
except IOError:
    print('File not found')
print('Done')