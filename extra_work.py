# Сільки секунд у годині
#sec = 60
#minut = 60
#seconds_per_hour = sec * minut
seconds_per_hour = 60 * 60
print(seconds_per_hour)

seconds_per_day = seconds_per_hour * 24
print(seconds_per_day)

test1 = seconds_per_day / seconds_per_hour
print(test1)

test2 = seconds_per_day // seconds_per_hour
print(test2)

print(5 + 7)
print(20 - 8)
print(2 * 6)
print(24 / 2)

poem = '''Yes, I'll smile, indeed, through tears and weeping
... Sing my songs where evil holds its sway,
... Hopeless, a steadfast hope forever keeping,
... I shall live! You thoughts of grief, away!'''

print(len(poem))

var_1 = poem.startswith('Yes')
print(var_1)

var_2 = poem.endswith("I shall live!")
print(var_2)

word = ","
print(poem.index(word))
print(poem.rfind(word))
print(poem.count(word))
print(poem.isalnum())




