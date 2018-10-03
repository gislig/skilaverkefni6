from operator import itemgetter

student_tuples = [['Minnesota', '129.8', '38.1', '8', 'N/A', '7.99', '155', '24.3', '33.90%', '22.60%', '86.70%', '14.90%', 'N/A', '25.40%', 'N/A', '90.20%', 'N/A', '17.20%', 'N/A', '72.20%', '9.00%'], ['Hawaii', '140.3', '39.5', 'N/A', 'N/A', '8.42', '67', '40.9', '38.90%', '30.70%', '78.70%', '14.50%', '15.20%', '23.10%', '14.50%', '97.90%', 'N/A', '17.90%', '22.40%', '61.50%', '6.80%']]
s = sorted(student_tuples, key=itemgetter(1), reverse=True)
print(s)

