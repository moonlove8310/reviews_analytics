data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 10000 == 0:
            print(len(data))
print('there are', len(data), 'data')

sum_len = 0
for d in data:
    sum_len = sum_len + len(d)

print('the average lenghts of the messages are', sum_len/len(data))

new =[]
for d in data:
    if len(d) < 100:
        new.append(d)
print('there are', len(new), 'messages their lenghts are less than 100')

good =[]
for d in data:
    if 'good' in d:
        good.append(d)
print('there are', len(good), 'messages including the word "good"')