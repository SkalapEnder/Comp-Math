from Functions.Forward import difference_table

data_2 = [(0, 1.0), (1, 1.5), (2, 2.2), (3, 3.1), (4, 4.6)]

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

_ = difference_table(data_2, way, output_step)
