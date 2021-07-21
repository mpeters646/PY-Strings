# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
gullit = 'Ruud Gullit'
basten = 'Marco van Basten'

goal_0 = 32
goal_1 = 54

scorers = gullit + ' ' + str(goal_0) + ',' + ' ' + basten + ' ' + str(goal_1)
report = f'{gullit} scored in the {goal_0}nd minute' + '\n' + f'{basten} scored in the {goal_1}th minute'

print('')
print(f'scorers output: {scorers}')
print(f'report output: {report}')
print('')

player = 'John van \'t schip'
# player = 'Ronald Koeman'
# player = 'Hans van Breukelen'

first_name = player.split()[0]
last_name = ' '.join(player.split()[1:])
last_name_len = len(last_name)
name_short = f'{first_name[0]}. {last_name}'

chant = f'{first_name}! ' * (len(first_name) - 1) + f'{first_name}!'
good_chant = chant[-1] != ' '

print(f'first name: {first_name}')
print(f'last name; {last_name}')
print(f'last name length: {last_name_len}')
print(f'name short: {name_short}')
print('')
print(f'chant: {chant}')
print(f'good chant: {good_chant}')