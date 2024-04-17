
def list_to_dict(day_money_list):
    dictionnary_result = {}
    for number_day in range(len(day_money_list)):
        current_day = int(day_money_list[number_day][0])
        current_money = day_money_list[number_day][1]

        if  current_day not in dictionnary_result.keys():
            dictionnary_result[current_day] = []
        dictionnary_result[current_day].append(int(current_money))
    return dictionnary_result

def get_input_as_dictionary():

    john_delivering_str = input().split("F ")
    
    day_sales = list(map(str.split,john_delivering_str[1:-1]))
    payment_bank = list(map(str.split, john_delivering_str[-1].split("B ")))
    
    day_sales.append(payment_bank.pop(0))


    
    return { "day_sales": list_to_dict(day_sales), "payment_bank": list_to_dict(payment_bank) }

def total_payment_bank(money_list):
    return sum(money_list)

def completed_from_list(current_money, total_money, money_list):
    for money in money_list:
        if (current_money + money) == total_money:
            money_list.remove(money)
            return True

    return False

def completed_by_another_payment(current_sale,payment_of_the_day, day, payment_bank) -> bool:
    result = False
   
    for day_iterator in range(day+1, max(payment_bank.keys()) + 1):
        if completed_from_list(payment_of_the_day, current_sale, payment_bank[day_iterator]):
            result = True
            break

    return result


   
day_sales, payment_bank = get_input_as_dictionary().values()

for day in day_sales.keys():
    payment_of_the_day = total_payment_bank(payment_bank[day])
    if payment_bank != day_sales[day]:
        if not completed_by_another_payment(day_sales[day][0],payment_of_the_day, day, payment_bank):
            print(day, end=" ")
    

print()

# F 1 209 F 2 254 F 3 895 F 4 439 B 1 104 B 2 127 B 3 74 B 3 447 B 4 127 B 4 219 B 5 448 B 6 220 
# F 1 367 F 2 38 F 3 602 F 4 624 B 1 183 B 2 19 B 3 184 B 3 301 B 4 19 B 4 312 B 5 64 B 6 312 