from datetime import date

music_group = {
    'members': {
        'Till Lindemann': {
            'birthday': date(1963, 1, 4),
            'role': 'lead vocals'
        },
        'Richard Kruspe': {
            'birthday': date(1967, 6, 24),
            'role': 'lead guitar'
        },
        'Christian Lorenz': {
            'birthday': date(1966, 11, 16),
            'role': 'synthesizer'
        }
    },
    'concerts': {
        'Leipzig': {
            'expenses': [493, 202, 393],
            'contract amount': 200000,
            'concert date': date(2021, 5, 23)
        },
        'Klagenfurt': {
            'expenses': [343, 345, 453],
            'contract amount': 200000,
            'concert date': date(2021, 5, 27)
        },
        'Berlin': {
            'expenses': [347, 733, 183],
            'contract amount': 200000,
            'concert date': date(2021, 6, 6)
        },
        'Coventry': {
            'expenses': [343, 546, 147],
            'contract amount': 200000,
            'concert date': date(2021, 6, 19)
        },
        'Dusseldorf': {
            'expenses': [563, 464, 354],
            'contract amount': 200000,
            'concert date': date(2021, 6, 26)
        }
    }
}
print('---Before---')
print(music_group['members'])
print('')
print(music_group['concerts'])


def add_new_member(group, **kwargs):
    group['members'].update(kwargs)
    return group
new_member = {
    'Christoph Schneider': {
        'birthday': date(1966, 5, 11),
        'role': 'drum kit'
    }
}
add_new_member(music_group, **new_member)


def delet_member(group, name):
    group['members'].pop(name)
    return group
member = 'Christian Lorenz'
delet_member(music_group, member)


def add_new_city(group, **kwargs):
    group['concerts'].update(kwargs)
    return group
new_city = {
    'Zurich': {
        'expenses': [452, 135, 786],
        'contract amount': 200000,
        'concert date': date(2021, 7, 5)
    }
}
add_new_city(music_group, **new_city)


def all_expenses(group, **kwargs):
    sum_expenses = 0
    for city in group['concerts']:
        expenses = group['concerts'][city]['expenses']
        sum_expenses += sum(expenses)
    return sum_expenses
total_expenses = all_expenses(music_group)


def diff_between_expenses_and_concert_amount(group, **kwargs):
    profit = 0
    for city in group['concerts']:
        contract_amount = group['concerts'][city]['contract amount']
        profit = contract_amount - total_expenses
    return profit
profit_per_concert = diff_between_expenses_and_concert_amount(music_group)

print('')
print('---After---')
print(music_group['members'])
print('')
print(music_group['concerts'])
print('Total expenses:', total_expenses)
print('Profit per concert:', profit_per_concert)
