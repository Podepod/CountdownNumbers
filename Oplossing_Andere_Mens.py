import re

def unpack(string):                                                                                 # string "3-34*2/123"
    """ Unpacks the passed `string` """
    list_sum = []
    list_special = []
    numbers = (re.findall(r"[\w']+", string))                                                           # een lijst van alle nummers voor of na een opperator bv. ["3","34","2","123"]
    for char in string:                                                                             # vul list_special met alle opperators
        if char in ["*", "+", "-", "/"]:
            list_special.append(char)

    for index in range(len(numbers) - 1):                                                           # elk nummer in lijst van nummers behalve de laatste
        to_eval = numbers[index] + list_special[index] + numbers[index + 1]                         # to_eval is string van "3" + "-" + "34"
        list_sum.append(f'{to_eval} = {eval(to_eval)}')                                             # 
        numbers[index + 1] = str(eval(to_eval))

    return list_sum

def evaluate(method, running_sum):
    """ Evaluates the passed `method` """
    if eval(method) == TARGET:
        if method not in LIST_METHODS:
            LIST_METHODS.append(method)
            print(f'Eval: {method}')
            clear_status = True
        return True
    if running_sum == TARGET:
        if method not in LIST_METHODS:
            LIST_METHODS.append(method)
            print(f'Running sum: {unpack(method)}')
            clear_status = True
        return True
    clear_status = False
    return False

def new_total(total, item, operation):
    """ Determines the operator and returns the new total """
    if operation == "+":
        return total + item
    if operation == "-":
        return total - item
    if operation == "*":
        return total * item
    if operation == "/" and item != 0:
        return total / item
    return ""

def solve(array, total=0, method=""):
    """ Solves the passed numbers and target """
    if not array:
        return

    for index, item in enumerate(array):                                                                # enumerate zorgt dat je met index de index kan gebruiken van het item

        #Assign methods and totals to a list:
        methods = ["", "", "", ""]
        totals = [0, 0, 0, 0]
        str_func = ["+", "-", "*", "/"]

        #Create new array
        remaining = array[:index] + array[index+1:]                                                     # maakt nieuwe array van waarde van vorige index + array van waarde van volgende 2 

        #Sets new totals and new "methods"
        for index_1 in range(len(methods)): 
            print(f"\n\n=======================================\nindex_1: {index_1}\nmethod: {method}\nmethods: {methods}\ntotals: {totals}\nremaining: {remaining}")      # len(methods) = 4
            if method == "":                                                                            # method is "" (zie functie def)
                if str_func[index_1] != "/" and str_func[index_1] != "*" and str_func[index_1] != "-":  # als de method '+' is 
                    methods[index_1] = str(array[index])                                                # method[index_1] = huidige item
                    totals[index_1] = new_total(total, item, str_func[index_1])                         
            else:
                methods[index_1] = method + str_func[index_1] + str(array[index])
                totals[index_1] = new_total(total, item, str_func[index_1])

        #Evaluates each total and method
        for index_2, value_2 in enumerate(methods):
            try:
                if evaluate(value_2, totals[index_2]):
                    if clear_status:
                        methods[index_2] = ""
                        totals[index_2] = 0
                    return
            except Exception:
                pass

        #Recursively calculates next move
        for index_3, value_3 in enumerate(methods):
            try:
                solve(remaining, total=totals[index_3], method=value_3)
            except Exception:
                pass

if __name__ == '__main__':
    clear_status = None
    STR_ARRAY = input("Please enter the starting numbers, separated by commas: ")
    ARRAY = ARRAY = [int(item.strip()) for item in STR_ARRAY.split(",")]                                # WAAROM ISDA 2 KEER ARRAY = ARRAY = ...
    TARGET = int(input("Please enter a target value: "))
    print(f'Solutions for {ARRAY} to reach {TARGET}')
    LIST_METHODS = []
    solve(ARRAY)
    if LIST_METHODS == []:
        print("Unsolvable countdown problem")
    _ = input("Press any key to exit...")