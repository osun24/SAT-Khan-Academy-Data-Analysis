import csv

input_file = "khan-sat-read-write.txt"
output_file = "khan-sat-read-write.csv"

# Open the input file
with open(input_file, 'r') as file, open(output_file, 'w', newline='') as output:
    # Create a CSV writer object
    csv_writer = csv.writer(output)
    
    # Write the CSV header
    csv_writer.writerow(["Date", "Activity", "Practice Type", "Score", "Max Score"])
    
    # Initialize variables to hold the current date, practice type, and description
    current_date = ''
    practice_type = ''
    description = ''
    
    # Iterate over each line in the file
    for line in file:
        # Strip leading/trailing whitespace
        line = line.strip()
        
        # Check if the line is a date
        if line.startswith(("June", "April", "March", "January", "December", "September", "February")):
            current_date = line
        # Check if the line is an activity
        elif line.startswith(('SKILL PRACTICE', 'TIMED MINI-SECTION', 'PRACTICE TEST')):
            practice_type = line
        # Check if the line is a score
        elif line and '/' in line:
            score, total = line.split('/')
            # Write the data to the CSV file
            csv_writer.writerow([current_date, practice_type, description, score.strip(), total.strip()])
        else:
            description = line.strip()