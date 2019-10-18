person = {
    'first_name':'Arpan',
    'last_name':'Mahatra',
    'age':21,
    'city':'Nepalgunj'
}
del(person['city'])
print(person)

if person.get('city'):
    print('City is there.')
else:
    print('No city.')