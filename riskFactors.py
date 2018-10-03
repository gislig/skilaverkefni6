# Global list for the csv content
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

def parse_csv(csv_content):
    try:
        for csv_line in csv_content[1:]:
            # read each line and split it into additional list, the outcome should be list with in a list
            parsed_csv.append(csv_line.split(","))
    except:
        # if it cannot read the content of the file, it will return nothing
        return ""

#def set_csv_values(State = "", HeartDiseaseDeathRate = "", StrokeDeathRate = "",HIVDiagnosisRate = "", CLABSI_SIR = "", MotorVehicleDeathRate = "", OpioidAnalgesicsDeaths = "", TeenBirthRate = "", DiagnosedHighCholesterol = "", DiagnosedHypertension = "", MedicatedHypertension = "", AdultSmoking = "", YouthSmoking = "", AdultObesity = "", YouthObesity = "", AdultSeatBeltUse = "", YouthSeatBeltUse = "", AdultBingeDrinking = "", YouthBingeDrinking = "", ColorectalCancerScreening = "", WithoutHealthCareCoverage = ""):
#    return 0

# Parse the CSV file into multiple lists
parse_csv(open_csv('riskFactors.csv'))

if parsed_csv != []:
    #a. The first one (“Indicator”) is of size 33, left justified.
    #b. The second one (the “Min” state) is of size 21, left justified.
    #c. The third one (the “Min” value) is of size 6, right justified.
    #d. The forth one (empty space) is of size 6.
    #e. The fifth one (the “Max” state) is of size 15, left justified.
    #f. The sixth one (the “Max” value) is of size 6, right justified.
    print("{:<33s} {:<21s} {:6s} {:>15s}".format("Indicator", "", "Min", "Max"))
    print("---------------------------------------------------------------------------------------")
