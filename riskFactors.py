# Import sorting toolkit
from operator import itemgetter

# Global variable list for the csv content
parsed_csv = []

# Open file
def open_csv(filename):
    try:
        with open(filename, 'r') as f:
            # read the file and split by returns, then return the content
            return f.read().replace("%","").replace("N/A","0").split("\n")
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

# Main
if csv_content != "":
    # Call the parse list
    parse_csv(csv_content)
    count = 1
    line_split = csv_content[0].split(",")

    print("{:<33}{:<21}{:>15}".format("Indicator", "Min", "Max"))
    print("---------------------------------------------------------------------------------------")

    while count < len(line_split):
        # Itterate through the top level indicators
        indicator_value = line_split[count]

        # Get the max for the specified indicator
        indicator_max_value = max(parsed_csv,key=itemgetter(count))
        max_value = float(indicator_max_value[count])
        state_value_max = indicator_max_value[0]

        # Get the min for the specified indicator
        indicator_min_value = min(parsed_csv,key=itemgetter(count))
        min_value = float(indicator_min_value[count])
        state_value_min = indicator_min_value[0]
        
        if indicator_value == "Heart Disease Death Rate (2007)" or indicator_value == "Motor Vehicle Death Rate (2009)" or indicator_value == "Teen Birth Rate (2009)" or indicator_value == "Adult Smoking (2010)" or indicator_value == "Adult Obesity (2010)":

            indicator_value = indicator_value + ":"
            print("{:<33s} {:<21s} {:>6.1f} {:^6} {:<15s} {:>6.1f}".format(indicator_value, state_value_min, min_value,"", state_value_max, max_value))
        count += 1


