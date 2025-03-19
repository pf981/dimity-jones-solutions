output = ''
for i in range(90):
    try:
        with open(f'./data/{i:02}.txt') as f:
            output += f.read().split("#####", 1)[0]
    except FileNotFoundError:
        pass

print(output)
