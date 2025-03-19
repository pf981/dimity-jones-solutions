with open('./data/00.txt') as f:
    text = f.read()

text = text.split("#####", 1)[1]
output = []
for i in range(len(text) // 2):
    output.append(text[i] + text[-i - 1])

with open('./data/01.txt', 'w') as f:
    f.write(''.join(output))
