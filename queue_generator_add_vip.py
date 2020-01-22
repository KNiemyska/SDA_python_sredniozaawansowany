import os
import time

"""lista klientów w formacie [numer,piorytet]"""
queue_dict = {
    "a": [],
    "b": [],
    "c": []
}
"""liczba klientów od początku działania systemu"""
queue_numbers = {
    "a": 0,
    "b": 0,
    "c": 0
}

secret_password_admin = "uzy"
secret_password_vip = "vip"

def print_to_consol (printing_message):
    print(printing_message)
    time.sleep(2)
    os.system("cls")

def serving_user(queue_dict):
    admin_answer = input("Z której kolejki będziesz obsługiwał klienta? ")
    if admin_answer not in queue_dict:
        print_to_consol("Podałeś złą nazwę kolejki\n")
        return
    elif admin_answer in queue_dict.keys():
        """Jeżeli w kolejce są klienci"""
        if len(queue_dict[admin_answer]):
            pairs=queue_dict[admin_answer]
            queue_dict[admin_answer] = sorted(pairs, key=lambda x: x[1])
            number_to_serve = queue_dict[admin_answer].pop(0)
            print_to_consol(f"Numer, który będziesz obsługiwać to {admin_answer.upper()}{number_to_serve[0]}")

        else:
            print_to_consol(f"Nie ma nikogo na liście oczekujących {admin_answer.upper()}")


def number_generator(customer_answer):
    queue_numbers[customer_answer]+=1
    new_number = queue_numbers[customer_answer]
    queue_dict[customer_answer].append([new_number,1])
    print_to_consol(f"Your number is {customer_answer.upper()}{new_number}")
    # return queue_dict[customer_answer][-1]

def adding_priority(customer_answer):
    queue_dict[customer_answer][-1][1] = 0
    # return queue_dict


def passing_customer_answer():
    print("Hello customer,\nplease choose your purpose:\n A- car registration \n B- car ID \n C- personal ID\n")
    customer_answer = (input("Choose a letter A,B,C: ")).lower()
    os.system("cls")
    return customer_answer


def run_office_control():
    while True:
        customer_answer = passing_customer_answer()
        if customer_answer in queue_dict:
            number_generator(customer_answer)

        elif customer_answer == secret_password_vip:
            customer_answer = passing_customer_answer()
            if customer_answer in queue_dict:
                number_generator(customer_answer)
                adding_priority(customer_answer)

        elif customer_answer == secret_password_admin:
            serving_user(queue_dict)
        else:
            print_to_consol("Podaj poprawną literkę")


if __name__ == "__main__":
    run_office_control()
