print("Введите стоку:")
s = input()
words=s.split()
num=len(words)
print('Количество слов в тексте:',num)
count1 = 0
count2 = 0
glasn = 'ауоыиэяюёеАУОЫИЭЯЮЁЕ'
soglasn = 'бвгджзйклмнпрстфхцчшщьъБВГДЖЗЙКЛМНПРСТФХЦЧШЩ'
g=""
for i in range(len(glasn)):
    if glasn[i] in s:
        count1 += 1
        g+=glasn[i]
for j in range(len(soglasn)):
    if soglasn[j] in s:
        count2 += 1
print('Количество гласных букв:', count1)
print('Количество согласных букв:', count2)
if count1==count2:
    print('Гласные в строке:', g)



