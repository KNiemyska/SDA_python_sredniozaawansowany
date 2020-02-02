import os
import time

queue_dict = {
    "a": 0,
    "b": 0,
    "c": 0
}

served_dict = {
    "a": 0,
    "b": 0,
    "c": 0
}
secret_password = "uzy"


def print_to_consol(printing_message):
    print(printing_message)
    time.sleep(2)
    os.system("cls")


def serving_user(customer_answer):
    user_answer = input("Z której kolejki będziesz obsługiwał klienta? ")
    if not user_answer in queue_dict:
        print_to_consol("Podałeś złą nazwę kolejki\n")
        return

    liczba_oczekujacych = queue_dict[user_answer] - served_dict[user_answer]
    if liczba_oczekujacych > 0:
        served_dict[user_answer] += 1
        print_to_consol(f"Numer, który będziesz obsługiwać to {user_answer.upper()}{served_dict[user_answer]}")
    else:
        print_to_consol(f"Nie ma nikogo na liście oczekujących {user_answer.upper()}")


def number_generator(customer_answer):
    queue_dict[customer_answer] += 1
    print_to_consol(f"Your number is {customer_answer.upper()}{queue_dict[customer_answer]}")


def run_office_control():
    while True:
        print("Hello customer,\nplease choose your purpose:\n A- car registration \n B- car ID \n C- personal ID\n")
        customer_answer = (input("Choose a letter A,B,C: ")).lower()
        os.system("cls")
        if customer_answer in queue_dict:
            number_generator(customer_answer)
        elif customer_answer == secret_password:
            serving_user(customer_answer)
        else:
            print_to_consol("Podaj poprawną literkę")


if __name__ == "__main__":
    run_office_control()
