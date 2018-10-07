# Global variable list for the csv content
parsed_csv = []

# Open file
def open_csv(filename):
    try:
        with open(filename, 'r') as f:
            # read the file and split by returns, then return the content
            data = f.read().replace("%","").split("\n")
            data = list(filter(None, data))
            return data
    except:
        # if the file does not exist then return that it cannot find the file
        print("Cannot find file {}".format(filename))

# Parse content of the csv file into list
def parse_csv(csv_content):
    try:
        for csv_line in csv_content[1:]:
            # read each line and split it into additional list, the outcome should be list with in a list
            parsed_csv.append(csv_line.split(","))
            #my_list = [float(i) for i in csv_line.split(",")]
            #parsed_csv.append(my_list)
    except:
        # if it cannot read the content of the file, it will return nothing
        return ""

# Parse the CSV file into multiple lists
# This will add the content of the csv file into a list
# Which is assigned as a global variable
file_selector = input("Enter filename containing csv data: ")
csv_content = open_csv(file_selector)
#csv_content = open_csv('riskfactors.csv')
print("{:<33}{:<21}{:>15}{:18}".format("Indicator", "Min", "Max",""))
print("-"*87)

# Main
if csv_content:
    # Call the parse list
    parse_csv(csv_content)
    line_split = csv_content[0].split(",")

    HeartDiseaseDeathRate = []
    MotorVehicleDeathRate = []
    TeenBirthRate = []
    AdultSmoking = []
    AdultObesity = []
    State = []

    for row in range(len(parsed_csv)):
        State.append(parsed_csv[row][0])
        HeartDiseaseDeathRate.append(float(parsed_csv[row][1]))
        MotorVehicleDeathRate.append(float(parsed_csv[row][5]))
        TeenBirthRate.append(float(parsed_csv[row][7]))
        AdultSmoking.append(float(parsed_csv[row][11]))
        AdultObesity.append(float(parsed_csv[row][13]))

    HeartDiseaseDeathRate_indicatorvalue = line_split[1] + ":"
    max_HeartDiseaseDeathRate = max(HeartDiseaseDeathRate)
    min_HeartDiseaseDeathRate = min(HeartDiseaseDeathRate)
    state_max_HeartDiseaseDeathRate = State[HeartDiseaseDeathRate.index(max(HeartDiseaseDeathRate))]
    state_min_HeartDiseaseDeathRate = State[HeartDiseaseDeathRate.index(min(HeartDiseaseDeathRate))]
    print("{:<33s}{:<21s}{:>6.1f}{:^6}{:<15s}{:>6.1f}".format(HeartDiseaseDeathRate_indicatorvalue, state_min_HeartDiseaseDeathRate, min_HeartDiseaseDeathRate,"", state_max_HeartDiseaseDeathRate, max_HeartDiseaseDeathRate))

    MotorVehicleDeathRate_indicatorvalue = line_split[5] + ":"
    max_MotorVehicleDeathRate = max(MotorVehicleDeathRate)
    min_MotorVehicleDeathRate = min(MotorVehicleDeathRate)
    state_max_MotorVehicleDeathRate = State[MotorVehicleDeathRate.index(max(MotorVehicleDeathRate))]
    state_min_MotorVehicleDeathRate = State[MotorVehicleDeathRate.index(min(MotorVehicleDeathRate))]
    print("{:<33s}{:<21s}{:>6.1f}{:^6}{:<15s}{:>6.1f}".format(MotorVehicleDeathRate_indicatorvalue, state_min_MotorVehicleDeathRate, min_MotorVehicleDeathRate,"", state_max_MotorVehicleDeathRate, max_MotorVehicleDeathRate))


    TeenBirthRate_indicatorvalue = line_split[7] + ":"
    max_TeenBirthRate = max(TeenBirthRate)
    min_TeenBirthRate = min(TeenBirthRate)
    state_max_TeenBirthRate = State[TeenBirthRate.index(max(TeenBirthRate))]
    state_min_TeenBirthRate = State[TeenBirthRate.index(min(TeenBirthRate))]
    print("{:<33s}{:<21s}{:>6.1f}{:^6}{:<15s}{:>6.1f}".format(TeenBirthRate_indicatorvalue, state_min_TeenBirthRate, min_TeenBirthRate,"", state_max_TeenBirthRate, max_TeenBirthRate))


    AdultSmoking_indicatorvalue = line_split[11] + ":"
    max_AdultSmoking = max(AdultSmoking)
    min_AdultSmoking = min(AdultSmoking)
    state_max_AdultSmoking = State[AdultSmoking.index(max(AdultSmoking))]
    state_min_AdultSmoking = State[AdultSmoking.index(min(AdultSmoking))]
    print("{:<33s}{:<21s}{:>6.1f}{:^6}{:<15s}{:>6.1f}".format(AdultSmoking_indicatorvalue, state_min_AdultSmoking, min_AdultSmoking,"", state_max_AdultSmoking, max_AdultSmoking))

    
    AdultObesity_indicatorvalue = line_split[13] + ":"
    max_AdultObesity = max(AdultObesity)
    min_AdultObesity = min(AdultObesity)
    state_max_AdultObesity = State[AdultObesity.index(max(AdultObesity))]
    state_min_AdultObesity = State[AdultObesity.index(min(AdultObesity))]
    print("{:<33s}{:<21s}{:>6.1f}{:^6}{:<15s}{:>6.1f}".format(AdultObesity_indicatorvalue, state_min_AdultObesity, min_AdultObesity,"", state_max_AdultObesity, max_AdultObesity))