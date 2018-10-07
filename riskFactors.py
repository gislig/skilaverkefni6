from operator import itemgetter

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
        for csv_line in csv_content:
            line_content = []
            # read each line and split it into additional list, the outcome should be list with in a list
            for t in csv_line.split(","):
                try:
                    line_content.append(float(t))
                except ValueError:
                    line_content.append(t)
            
            parsed_csv.append(line_content)
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
    column_list = parsed_csv[0]
    column_count = 0

    while column_count < len(column_list):
        if column_list[column_count] == "Heart Disease Death Rate (2007)" or column_list[column_count] == "Motor Vehicle Death Rate (2009)" or column_list[column_count] == "Teen Birth Rate (2009)" or column_list[column_count] == "Adult Smoking (2010)" or column_list[column_count] == "Adult Obesity (2010)":
            indicators = column_list[column_count] + ":"
            maxed_parsed = max(parsed_csv[1:],key=itemgetter(column_count))
            mined_parsed = min(parsed_csv[1:],key=itemgetter(column_count))
            print("{:<33s}{:<21s}{:>6.1f}{:^6}{:<15s}{:>6.1f}".format(indicators, mined_parsed[0], mined_parsed[column_count],"", maxed_parsed[0], maxed_parsed[column_count]))

        column_count += 1