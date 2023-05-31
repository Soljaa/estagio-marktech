import requests
import random


regs = []

# very simple mock student data generator as a dict
# its possible to generate an used registry resulting in a Database connection error from de API caused by a primary key constrain violation
# saves the new generated reg in a global var to use in the update and delete tests
def generate_new_reg():
    reg = str(random.randint(10000, 100000))
    day = str(random.randint(1, 30))
    month = str(random.randint(1, 12))
    regs.append(reg)
    return {'registry': reg, 'first_name': f'Marcos{reg[3]}', 'last_name': f'Soares{reg[2]}', 'email': f'daasdneeri{reg[1]}@uol.com', 'phone_number': f'{reg*2}',
            'degree': 'medicina', 'birth_date': f'19{reg[2:4]}-{month}-{day}'}
    

# uses the requests lib to get the list of students
def list_test():
    url = 'http://localhost:5000/students/list'
    response = requests.get(url)
    print(" ==== list_test ====")
    print(response.text)
    print()


# uses the requests lib to post a new generated student info as json 
def add_test():
    url = 'http://localhost:5000/students/add'
    # new entry
    data = generate_new_reg()
    response = requests.post(url, json=data)
    print(" ==== add_test ====")
    print(response.text)
    print()
  

# uses the requests lib to patch a students info from the regs global var
def update_test():
    url = 'http://localhost:5000/students/update'
    reg = random.choice(regs)
    data = {'registry': reg, 
            'email': 'marquin@gmail.com',
            'degree': 'engenharia'}
    response = requests.patch(url, json=data)
    print(" ==== update_test ====")
    print(response.text)
    print()


# uses the requests lib to delete a students info from the regs global var
def delete_test():
    reg = random.choice(regs)
    url = f'http://localhost:5000/students/delete/{reg}'
    response = requests.delete(url)
    print(" ==== delete_test ====")
    print(response.text)
    print()


if __name__ == '__main__':
    add_test()
    update_test()
    list_test()
    delete_test()
    