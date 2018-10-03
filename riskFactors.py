# Import sorting toolkit
from operator import itemgetter

# Global variable list for the csv content
parsed_csv = []

# Open file
def open_csv(filename):
    try:
        with open(filename, 'r') as f:
            # read the file and split by returns, then return the content
            return f.read().split("\n")
    except:
        # if the file does not exist then return that it cannot find the file
        print("Cannot find file {}".format(filename))

# Parse content of the csv file into list
def parse_csv(csv_content):
    try:
        for csv_line in csv_content[1:]:
            # read each line and split it into additional list, the outcome should be list with in a list
            parsed_csv.append(csv_line.split(","))
    except:
        # if it cannot read the content of the file, it will return nothing
        return ""

# Parse the CSV file into multiple lists
# This will add the content of the csv file into a list
# Which is assigned as a global variable
csv_content = open_csv('riskFactors.csv')

def get_state_max_min(line_content):
    print((csv_content[0].split(",")[1]))
    HeartDiseaseDeathRateMax = sorted(parsed_csv, key=itemgetter(1), reverse=True)
    HeartDiseaseDeathRateMin = sorted(parsed_csv, key=itemgetter(1), reverse=False)
    print(HeartDiseaseDeathRateMin[0][0],HeartDiseaseDeathRateMin[0][1])
    print(HeartDiseaseDeathRateMax[0][0],HeartDiseaseDeathRateMax[0][1])

if csv_content != "":
    parse_csv(csv_content)
    count = 1
    line_split = csv_content[0].split(",")

    print("{:<33s} {:<21s} {:6s} {:>15s}".format("Indicator", "", "Min", "Max"))
    print("---------------------------------------------------------------------------------------")

    while count < len(line_split):
        # Itterate through the top level indicators
        indicator_value = line_split[count]

        state_value = "Alabama"
        indicator_max_value = "0"
        indicator_min_value = "0"

        print("{:<33s}: {:<21s} {:6s} {:>15s}".format(indicator_value, state_value ,indicator_min_value, indicator_max_value))
        count += 1
    #for x in line_split:
    #    count += 1
    #    print(line_split[count])
    #    #for t in parsed_csv:
    #    #    print(t[0])
        

    #for p_csv in parsed_csv:
    #    #print(set_csv_values(StateValue=p_csv[0],HeartDiseaseDeathRateValue=p_csv[1]))
    #    print(p_csv)
    #a. The first one (“Indicator”) is of size 33, left justified.
    #b. The second one (the “Min” state) is of size 21, left justified.
    #c. The third one (the “Min” value) is of size 6, right justified.
    #d. The forth one (empty space) is of size 6.
    #e. The fifth one (the “Max” state) is of size 15, left justified.
    #f. The sixth one (the “Max” value) is of size 6, right justified.
    #for p_list in csv_content[0].split(","):
    #    print("{:<33s}".format(p_list))