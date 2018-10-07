# Import sorting toolkit
from operator import itemgetter

# Global variable list for the csv content
parsed_csv = []

# Open file
def open_csv(filename):
    try:
        with open(filename, 'r') as f:
            # read the file and split by returns, then return the content
            return f.read().replace("%","").split("\n")
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

# Convert all string values to int
def parse_value_float(string_list):
    new_float_list = []
    for state_list in string_list:
        converted_list = []
        for value_list in state_list:
            try:
                converted_list.append(float(value_list))
            except ValueError:
                converted_list.append(value_list)

        new_float_list.append(converted_list)
    return new_float_list

# Parse the CSV file into multiple lists
# This will add the content of the csv file into a list
# Which is assigned as a global variable
csv_content = open_csv('riskFactors.csv')

# Main
if csv_content != "":
    # Call the parse list
    parse_csv(csv_content)
    count = 1
    line_split = csv_content[0].split(",")

    print("{:<33}{:<21}{:>15}".format("Indicator", "Min", "Max"))
    print("-"*87)

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


    #count_states = 0
    #count_lines = 0
    
    #parsed_float = parse_value_float(parsed_csv)
    
    #for p in range(len(parsed_float)):
    #    print(p)
#)
    #while count_lines < len(line_split):
    #    for t in range(len(parsed_float)):
    #        print(max(parsed_float[0][count_lines])
#
    #    count_lines += 1
##
    #while count < len(line_split):
    #    # Itterate through the top level indicators
    #    indicator_value = line_split[count]
#
    #    # ---- Not working as I would have liked ---- #
#
    #    # Get the max for the specified indicator
    #    indicator_max_value = max(parsed_csv,key=itemgetter(count))
    #    max_value = float(indicator_max_value[count])
    #    state_value_max = indicator_max_value[0]
#
    #    # Get the min for the specified indicator
    #    indicator_min_value = min(parsed_csv,key=itemgetter(count))
    #    min_value = float(indicator_min_value[count])
    #    state_value_min = indicator_min_value[0]
    #    
    #    if indicator_value == "Heart Disease Death Rate (2007)" or indicator_value == "Motor Vehicle Death Rate (2009)" or indicator_value == "Teen Birth Rate (2009)" or indicator_value == "Adult Smoking (2010)" or indicator_value == "Adult Obesity (2010)":
#
    #        indicator_value = indicator_value + ":"
    #        print("{:<33s} {:<21s} {:>6.1f} {:^6} {:<15s} {:>6.1f}".format(indicator_value, state_value_min, min_value,"", state_value_max, max_value))
    #    
    #    count += 1
