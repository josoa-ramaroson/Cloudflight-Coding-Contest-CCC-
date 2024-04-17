
def list_to_dict(day_money_list):
    dictionnary_result = {}
    for number_day in range(len(day_money_list)):
        currrent_day = day_money_list[number_day][0]
        current_money = day_money_list[number_day][1]

        if currrent_day in dictionnary_result.keys():
            dictionnary_result[currrent_day] += int(current_money)
        else:
            dictionnary_result[currrent_day] = int(current_money)
    return dictionnary_result

def get_input_as_dictionary():

    john_delivering_str = input().split("F ")
    
    day_sales = list(map(str.split,john_delivering_str[1:-1]))
    payment_bank = list(map(str.split, john_delivering_str[-1].split("B ")))
    
    day_sales.append(payment_bank.pop(0))


    
    return { "day_sales": list_to_dict(day_sales), "payment_bank": list_to_dict(payment_bank) }



day_sales, payment_bank = get_input_as_dictionary().values()
