def roll_call_dwarves(list):
    
    for number, dwarf in enumerate (list, 1):
        print(number, '. ', dwarf, sep='')

def summon_captain_planet(calls):
    changed_calls = [call.capitalize() + '!' for call in calls]
    return changed_calls

def long_planeteer_calls(list):
    long_calls = [call for call in list if len(call) > 4]
    
    if len(long_calls) > 0:
        return True
    else:
        return False

def find_the_cheese(list):
    cheesy_list = [food for food in list if (food == "cheddar" or food == "gouda" or food == "camembert")]
    for cheese in cheesy_list:
        return cheese

find_the_cheese(["crackers", "gouda", "thyme"])

