def greet(name, *args):
    for n in (name,) + args:
        print(f'Hello, {n}!')

names = ['Tom', 'Ann']

greet(
   'Bob', *['Mary', 'Clair'], 'Sam',
   *('Henry', 'John')
)