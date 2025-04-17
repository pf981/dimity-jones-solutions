import decrypter


text = """2	roast turkey
3	bubblegum mint ice cream
4	linguine alfredo
5	pistachio pudding
6	chocolate cherry ice cream
7	rye bread
8	french vanilla ice cream
9	pineapple
10	tomato herb soup
11	mutton stew
12	old cheddar cheese
13	mushroom gravy
14	spaghetti alla puttanesca
15	lemon chiffon cake
16	pumpernickel bread"""

parts = []
for line in text.splitlines():
    seat_num, name = line.split(maxsplit=1)
    parts.append(f"{seat_num}: {name.capitalize()}")
key_string = ", ".join(parts) + "."


@decrypter.decrypter(chapter=43)
def decrypt(cipher: str) -> str:
    return decrypter.substitution_cipher(cipher, key_string)
