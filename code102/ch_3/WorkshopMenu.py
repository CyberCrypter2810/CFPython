
#Print menu
print ('\t\t\tMENU WORKSHOP SELECTOR')
print ('\tWORKSHOPS \tRegistration Fee \tDays')
print ('1) Handling Stress \t$1000 \t\t\t3 ')
print ('2) Time Management\t$800 \t\t\t3 ')
print ('3) Supervision Skills\t$1600 \t\t\t3 ')
print ('4) How to Interview \t$500 \t\t\t1\n')

# user input for workshop
workshop = int(input("Which workshop to you want to attend? \t"))
print("\n")

print ('\tLOCATION \tLodging Fee per Day')
print ('1) Austin \t\t$150')
print ('2) Chicago\t\t$225 ')
print ('3) Phoenix\t\t$175 ')
print ('4) Orlando\t\t$300 \n')

# user input location
location = int(input("Which location do you want to attend? \t"))
print("\n")

# Calculation for workshop #1
if workshop == 1:
    Registration = 1000
    if location == 1:
        Lodging = 150 * 3
        Total = Registration + Lodging
    elif location == 2:
        Lodging = 225 * 3
        Total = Registration + Lodging
    elif location == 3:
        Lodging = 175 * 3
        Total = Registration + Lodging
    else:
        Lodging = 300 * 3
        Total = Registration + Lodging
#Display calculation
    print("Registration: $" + str(Registration))
    print("Lodging: $150 x 3 days = $" + str(Lodging))
    print("Total: $" + str(Total))

# Calculation for workshop #2
elif workshop == 2:
    Registration = 800
    if location == 1:
        Lodging = 150 * 3
        Total = Registration + Lodging
    elif location == 2:
        Lodging = 225 * 3
        Total = Registration + Lodging
    elif location == 3:
        Lodging = 175 * 3
        Total = Registration + Lodging
    else:
        Lodging = 300 * 3
        Total = Registration + Lodging
#Display calculation
    print("Registration: $" + str(Registration))
    print("Lodging: $150 x 3 days = $" + str(Lodging))
    print("Total: $" + str(Total))

# Calculation for workshop #3
elif workshop == 3:
    Registration = 1500
    if location == 1:
        Lodging = 150 * 3
        Total = Registration + Lodging
    elif location == 2:
        Lodging = 225 * 3
        Total = Registration + Lodging
    elif location == 3:
        Lodging = 175 * 3
        Total = Registration + Lodging
    else:
        Lodging = 300 * 3
        Total = Registration + Lodging
#Display calculation
    print("Registration: $" + str(Registration))
    print("Lodging: $150 x 3 days = $" + str(Lodging))
    print("Total: $" + str(Total))

# Calculation for workshop #4
else:
    Registration = 500
    if location == 1:
        Lodging = 150 * 1
        Total = Registration + Lodging
    elif location == 2:
        Lodging = 225 * 1
        Total = Registration + Lodging
    elif location == 3:
        Lodging = 175 * 1
        Total = Registration + Lodging
    else:
        Lodging = 300 * 1
        Total = Registration + Lodging
#Display calculation
    print("Registration: $" + str(Registration))
    print("Lodging: $150 x 3 days = $" + str(Lodging))
    print("Total: $" + str(Total))
