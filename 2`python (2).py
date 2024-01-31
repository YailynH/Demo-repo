``python
secret = 7
guess = 4

if guess < secret:
print('Too low')
elif guess > secret:
print('Too high')
else:
print('Just right')


4.2 Assign True or False to the variables small and green. Write some if/else statements to print which of these matches those choices: cherry, pea, watermelon, pumpkin.

```python
small = True
green = False

if small and green:
print('pea')
elif small and not green:
print('cherry')
elif not small and green:
print('watermelon')
else:
print('pumpkin')
```


```
for num in [3, 2, 1, 0]:
print(num)
```


```
guess_me = 7
number = 1

while number != guess_me:
if number < guess_me:
print('too low')
elif number > guess_me:
print('oops')
else:
print('found it!')
break
number += 1
```


``
guess_me = 5

for number in range(10):
if number < guess_me:
print('too low')
elif number == guess_me:
print('found it!')
break
else:
print('oops')
break
```
