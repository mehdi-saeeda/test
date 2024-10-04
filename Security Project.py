main_sentence = input("enter the sentence")
sentence_1 = main_sentence.lower()
sentence_2 = sentence_1.split(" ")
vowels = "aeiou"
secret = []

for i in sentence_2:
    if i[0] in vowels:
        secret.append( i[1:] + i[0] + 'v')
    else:
        secret.append (i[2:] + i[:2])
for j in secret:
    print(j,end= " ")


