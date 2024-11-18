# Braden Leach
# Nov 18 2024
# Default Values for Parameters Practice

# 8-3 (T-Shirt)
#positional 
def make_shirt(size, text):
    print(f'The size of your shirt is {size} and it says {text} on the front.')

make_shirt('small', 'Happy Halloween!')

# Keyword
def make_shirt(size, text):
    print(f'The size of your shirt is {size} and it says {text} on the front.\n')

make_shirt(size= 'large', text='Friday Funday!')


# 8-4 (Large Shirts)
def make_shirt(text, size='large'):
      print(f'The size of your shirt is {size} and it says {text} on the front.')

make_shirt('I love Python!')
make_shirt('I love Python!','medium')
make_shirt('I love to go for walks!','small')


# 8-5 (Cities)
def describe_city(city,country='Michigan'):
    print(f'\n{city} is in {country}')

describe_city('Detroit')
describe_city('Kalamazoo')
describe_city('Paris','France')