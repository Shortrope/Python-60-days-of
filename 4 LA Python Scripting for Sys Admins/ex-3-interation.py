#!/usr/bin/env python3

users = [{
    'admin': True,
    'active': True,
    'name': 'Mario'
    },
    {
        'admin': True,
        'active': False,
        'name': 'Mary'
    },
    {
        'admin': False,
        'active': True,
        'name': 'Josie'
    },
    {
        'admin': False,
        'active': False,
        'name': 'Erin'
    }]

for user in users:
    if user['admin'] and user['active']:
        prefix = 'ACTIVE - (admin)'
    elif user['admin']:
        prefix = '(admin)'
    elif user['active']:
        prefix = 'ACTIVE'
    else:
        prefix = ""

    print(prefix, user['name'])