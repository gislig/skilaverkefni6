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

# Main
if csv_content != "":
    # Call the parse list
    parse_csv(csv_content)
    count = 1
    line_split = csv_content[0].split(",")

    print("{:<33s} {:<21s} {:6s} {:>15s}".format("Indicator", "", "Min", "Max"))
    print("---------------------------------------------------------------------------------------")

    while count < len(line_split):
        # Itterate through the top level indicators
        indicator_value = line_split[count]

        # Get the max for the specified indicator
        indicator_max_value = max(parsed_csv,key=itemgetter(count))
        max_value = str(indicator_max_value[count])
        state_value_max = indicator_max_value[0]

        # Get the min for the specified indicator
        indicator_min_value = min(parsed_csv,key=itemgetter(count))
        min_value = str(indicator_min_value[count])
        state_value_min = indicator_min_value[0]
        
        #a. The first one (“Indicator”) is of size 33, left justified.
        #b. The second one (the “Min” state) is of size 21, left justified.
        #c. The third one (the “Min” value) is of size 6, right justified.
        #d. The forth one (empty space) is of size 6.
        #e. The fifth one (the “Max” state) is of size 15, left justified.
        #f. The sixth one (the “Max” value) is of size 6, right justified.

        print("{:<33s}: {:<21s} {} {:6} {} {:>15s} {}".format(indicator_value, state_value_min, "", min_value, "", state_value_max, max_value))
        count += 1


