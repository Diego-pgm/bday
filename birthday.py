def add_person(person):
    with open('./list.txt', 'a') as file:
        file.write(person)
        file.write('\n')

def read_list():
    with open('./list.txt', 'r') as file:
        print(file.read())

def count_people():
    count = []
    with open('./list.txt', 'r') as file:
        for line in file:
            count.append(line)
    return len(count)
    
while True:
    print("Add person(a), read file(r) No of invites (c) exit (ex)")
    option = input('>> ')
    if option == 'ex':
        break
    elif option == 'a':
        person = input('Insert person: ')
        add_person(person)
    elif option == 'r':
        read_list()
    elif option == 'c':
        print(count_people())