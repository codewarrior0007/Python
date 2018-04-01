#######################################################
# Notes:
# 1. Coded this buggy python using tutorial _
#    found online.  It was to play with _
#    I'll revist it in the futureto add _
#    try and exception to catch issues.
# 2. This was coded in Python 2 but syntax _
#    handling was done Geany (https://www.geany.org/
#######################################################


import operator

saved_string = ''

def remove_letter():
 #   print "Remove Letter"
    base_string = str(raw_input("Enter a Base String:  "))
    letter_remove = str(raw_input("Enter a letter to remove:  "))
    letter_remove = letter_remove[0]
    string_length = len(base_string)
    location = 0

    while (location < string_length):
        if base_string[location] == letter_remove:
            base_string = base_string[:location]+base_string[location+1::]
            string_length -=1
        location +=1

    print("Result: %s" % base_string)
    return


def num_compare():
#    print "Num Compare"
    num1 = int(raw_input("Input first number:  "))
    num2 = int(raw_input("Input second number:  "))
    
    if num1 > num2:
        print ("Greater number is:   " + str(num1))
    elif num2 > num1:
        print ("Greater number is:   " + str(num2))
    else :
        print ("EQUAL")
    return


def print_string():
 #   print "Print String"
    print (saved_string)
    return


def calculator():
 #   print "Num Calculator"
    sign_dict = {'+': operator.add, '-': operator.sub, '*': operator.mul, '%': operator.div}

    num1 = int(raw_input("Input first number:  "))
    sign = str(raw_input("Action:  "))
    num2 = int(raw_input("Input second number:  "))

    print (sign_dict[sign](num1,num2))

    return


def accept_and_store():
#    print "Accept and Store"
    global saved_string
    saved_string = str(raw_input("Input String: "))    
    return

def main():
    opt_list = [accept_and_store,
                calculator,
                print_string,
                num_compare,
                remove_letter]

    while(True):
        print ("SELECT OPTION")
        print ("1\tAccept and Store")
        print ("2\tCalculator")
        print ("3\tPrint Stored String")
        print ("4\tNumber Comparison")
        print ("5\tRemove Letter")
        opt_choice = int(raw_input("SELECTION:   "))
        opt_choice -=1
        opt_list[opt_choice]()
    
    return

main()
