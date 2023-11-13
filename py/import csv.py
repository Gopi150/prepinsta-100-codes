import csv
with open('demo.txt', 'r') as text_file:
    lines = text_file.readlines()

with open('output.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    for line in lines:
        # Split each line into fields based on the delimiter (e.g., a space)
        fields = line.strip().split()

        # Write the fields to the CSV file
        csv_writer.writerow(fields)
