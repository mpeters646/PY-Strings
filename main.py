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

player = 'John van \'t schip'
# player = 'Ronald Koeman'
# player = 'Hans van Breukelen'

first_name = player.split()[0]
last_name = " ".join(player.split()[1:])
last_name_len = len(' '.join(player.split()[1:]))
name_short = f'{first_name[0]}. {" ".join(player.split()[1:])}'

chant = f'{first_name}! ' * (len(first_name) - 1) + f'{first_name}!'
good_chant = chant[-1] != ' '

