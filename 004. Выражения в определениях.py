# Напишите программу, которая берет исходное количество евро,
# записанное в переменную euros_count, переводит евро в доллары и выводит на экран.
# Затем полученное значение переводит в рубли и выводит на новой строчке.

euros_count = 100

# BEGIN (write your solution here)
dollars = euros_count * 1.25
rubs = dollars * 60
print(dollars)
print(rubs)
# END
