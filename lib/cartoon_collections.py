def roll_call_dwarves(list):
    
    # for number, dwarf in enumerate (list, 1):
    #     print(number, '. ', dwarf, sep='')

        # OR
    the_count = 1
    for dwarf in list:
        print( f"{the_count}. {dwarf}")
        the_count += 1


def summon_captain_planet(calls):
    # changed_calls = [call.capitalize() + '!' for call in calls]
    # return changed_calls
        
        #OR

    new_list = []
    for word in calls:
        new_string = f"{word.capitalize()}!"
        new_list.append(new_string)
    return new_list



def long_planeteer_calls(list):
    # long_calls = [call for call in list if len(call) > 4]
    
    # if len(long_calls) > 0:
    #     return True
    # else:
    #     return False
    
        #OR

    for call in list:
        if len(call) > 4:
            return True
    return False
        




def find_the_cheese(list):
    # cheesy_list = [food for food in list if (food == "cheddar" or food == "gouda" or food == "camembert")]
    # for cheese in cheesy_list:
    #     return cheese
    
    #OR

    the_cheeses =["cheddar", "gouda", "camembert"]

    for the_snack in list:
        if the_snack in the_cheeses:
            return the_snack





# find_the_cheese(["crackers", "gouda", "thyme"])
# roll_call_dwarves(["Doc", "Dopey", "Bashful", "Grumpy"])
long_planeteer_calls(["earth", "wind", "fire", "water", "heart"])
