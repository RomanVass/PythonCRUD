price_dict1 = {
    'mustang': 5000,
    'honda': 3000,
    'porsche': 10000,
    'ford': 7000,
    'tesla': 25000
}


def Cars():
    car = input('Car:')
    price = int(input('price:'))
    price_dict1[car] = price




def Count():
    suma = 0
    for items in price_dict1.values():
        suma += items
    print(suma)

def All():
    for keys, values in price_dict1.items():
        print(f"{keys} price: {values}")
def Ask():
    car= input('car:')
    if car in price_dict1:
        del price_dict1[car]
    else:
        print('нема такої машини')



while True:
    print("*1* - додати машину\n*2* - вивести суму цін машин\n*3* - вивести все\n*4* - видалити машину\n*0* - завершити програму")
    user = int(input("--->>> "))
    if user == 1: Cars()
    elif user == 2: Count()
    elif user == 3: All()
    elif user == 4: Ask()
    elif user == 0: break


# CRUD operation:
# created +
# read +
# update -
# delete +


# task: add update operation
