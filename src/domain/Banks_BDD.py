def get_bank():
    with open('src/persistence/Banks.txt', 'r') as f:
        line = f.readline()
        return line


def get_client():
    try:
        #with open('E:\PytonWorkspace\Bank\src\persistence\Clients.txt', 'r') as f:
        with open('src/persistence/Clients.txt', 'r') as f:
            line = f.readline()
            return line
    except FileNotFoundError as fnf:
        print('Client not found')
        exit(0)


def set_client_info(value):
    #with open('E:\PytonWorkspace\Bank\src\persistence\Clients.txt', 'w') as f:
    with open('src/persistence/Clients.txt', 'w') as f:
        f.write(str(value))
        print(str)


def save(obj_client):
    print(obj_client.first_name)
    with open('src/persistence/' + str(obj_client.first_name) + '.txt', 'a') as f:
    #with open('E:\\PytonWorkspace\\Bank\\src\\persistence\\' + str(obj_client.first_name) + '.txt', 'a') as f:
        f.write(repr(obj_client))
