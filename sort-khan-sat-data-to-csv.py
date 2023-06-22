import csv

input_file = "khan-sat-math.txt"
output_file = "khan-sat-math.csv"
current_date = ""

import csv

# Open the input file
with open(input_file, 'r') as file:
    # Create a CSV writer object
    csv_writer = csv.writer(open(output_file, 'w', newline=''))
    
    # Write the CSV header
    csv_writer.writerow(["Date", "Activity", "practiceType", "Calculator", "Score", "Max Score"])
    
    # Initialize variables to hold the current date and practiceType
    current_date = ''
    practiceType = ''
    calculator = ''
    description = ''
    
    # Iterate over each line in the file
    for line in file:
        # Strip leading/trailing whitespace
        line = line.strip()
        
        # Check if the line is a date
        if line.startswith("June") or line.startswith("April") or line.startswith("March") or line.startswith("January") or line.startswith("December") or line.startswith("September") or line.startswith("February"):
            current_date = line
        # Check if the line is an activity
        elif line.startswith('SKILL PRACTICE') or line.startswith('TIMED MINI-SECTION') or line.startswith('PRACTICE TEST'):
            practiceType = line
        # Check if the line to see the calculator status
        elif line.startswith('Math ('):
            if line.find('No') != -1:
                calculator = 'No'
            else:
                calculator = 'Yes'
        # Check if the line is a score
        elif line and '/' in line:
            score = line.split('/')[0].strip()
            total = line.split('/')[1].strip()
            # Write the data to the CSV file
            if calculator == "":
                calculator = "Null"
            csv_writer.writerow([current_date, practiceType, description, calculator, score, total])
            calculator = ""
        else: 
            description = line.strip()
