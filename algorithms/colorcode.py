num = int(input('How many games: '))
total_sum = 0
for n in range(num):
    numbers = float(input('Enter K/D : '))
    total_sum += numbers
avg = total_sum/num
print('Your average K/D is :', avg)