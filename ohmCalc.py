# Enter two known values to calculate the third.


class ohm_Calculator():

    def volt_resistance():
        voltage = input("please enter the voltage: ")
        resistance = input("please enter the resistance: ")
        current = float(voltage) / float(resistance)
        print("%.2f" % current)

    def resistance_current():
        resistance = input("please enter the resistance: ")
        current = input("please enter the current: ")
        voltage = float(resistance) * float(current)
        print("%.2f" % voltage)

    def volt_current():
        voltage = input("please enter the voltage: ")
        current = input("please enter the current: ")
        resistance = float(voltage) / float(current)
        print("%.2f" % resistance)

    print("What would you like to calculate?")
    print("Enter 'current', 'voltage' or 'resistance' to begin")
    user_response = input()
    if user_response == 'current':
        volt_resistance()
    elif user_response == 'voltage':
        resistance_current()
    elif user_response == 'resistance':
        volt_current()
    else:
        print("Please enter a valid term.")


