
with open('riskFactors.csv', 'r') as f:
        # read the file and split by returns, then return the content
        data = f.read().replace("%","").split("\n")
        data = list(filter(None, data))

print(len(data))