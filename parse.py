import csv

antennes = []

with open('instances/nodesG.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=';')
	line_count = 1
	for row in csv_reader:
		if row[2] == 'antenne':
			antennes = antennes + [(row[0], row[1])]
			#print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
		line_count += 1
	print(f'Processed {line_count} lines.')

print(antennes)
