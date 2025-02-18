from Functions.Forward import difference_table

data_1 = [(10, 1.1), (20, 2.0), (30, 4.4), (40, 7.9)]
data_2 = [(-0.75, -0.0718125), (-0.5, -0.02475), (-0.25, 0.3349375), (0, 1.10100)]

print('\tTask 2')
print('Choose way to find differences: ')
print('1 - Forward \n2 - Backward')
choice = int(input('Way: '))
way = ''
match choice:
    case 1:
        way = 'Forward'
    case 2:
        way = 'Backward'

print('Output each step? ')
print('1 - Yes \n2 - No')
choice = str(input('Choice: '))
output_step = False
match choice:
    case 'Yes':
        output_step = True
    case 'No':
        output_step = False

_ = difference_table(data_1, True, output_step, way)
