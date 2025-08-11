import constraint

import decrypter

problem = constraint.Problem()

names = [
    "Frank",
    "Bea",
    "Quinn",
    "Tom",
    "Phinn",
    "Wes",
    "Vic",
    "Ut",
    "Ned",
    "Seth",
    "Em",
    "Mar",
    "Oz",
    "Raine",
    "Chad",
    "Lou",
    "Xu",
    "Kay",
    "Geoff",
    "Hank",
    "Irv",
    "Zach",
    "Jai",
    "Dom",
    "Ann",
    "Yves",
]

# 1 = honest, 0 = liar
for name in names:
    problem.addVariable(name, [0, 1])


def add_statement_sum(speaker, group, count):
    problem.addConstraint(
        lambda s, *g: (sum(g) == count) if s else (sum(g) != count), (speaker, *group)
    )


def add_statement_all(speaker, group, truth=True):
    problem.addConstraint(
        lambda s, *g: (all(g) == truth) if s else (all(g) != truth), (speaker, *group)
    )


def add_statement_exactly_one(speaker, group):
    add_statement_sum(speaker, group, 1)


def add_statement_exactly_one_lies(speaker, group):
    problem.addConstraint(
        lambda s, *g: (sum(x == 0 for x in g) == 1)
        if s
        else (sum(x == 0 for x in g) != 1),
        (speaker, *group),
    )


# 1. "One lies," said Frank of Bea and Quinn.
add_statement_exactly_one_lies("Frank", ["Bea", "Quinn"])

# 2. "Both lie," said Frank of Tom and Phinn.
add_statement_all("Frank", ["Tom", "Phinn"], truth=False)

# 3. "He lies," said Wes of Vic, who said "Ut lies," who said the same of Ned.
add_statement_all("Wes", ["Vic"], truth=False)
add_statement_all("Vic", ["Ut"], truth=False)
add_statement_all("Ut", ["Ned"], truth=False)

# 4. "Just one of Seth, Quinn, Em, and Bea are honest," Frank said earnestly.
add_statement_exactly_one("Frank", ["Seth", "Quinn", "Em", "Bea"])

# 5. "Of five: me, Oz, Raine, Chad, and Lou," Said Mar, "there are an honest two."
add_statement_sum("Mar", ["Mar", "Oz", "Raine", "Chad", "Lou"], 2)

# 6. Phinn, Xu, and Bea drawn from the crowd, "Just one is honest," Frank avowed.
add_statement_exactly_one("Frank", ["Phinn", "Xu", "Bea"])

# 7. "Among myself, Chad, Lou, and Mar," Said Oz, "three honest persons are."
add_statement_sum("Oz", ["Oz", "Chad", "Lou", "Mar"], 3)

# 8. Said Frank of Xu, Phinn, Tom, and Kay, "All four are honest as the day."
add_statement_all("Frank", ["Xu", "Phinn", "Tom", "Kay"], truth=True)

# 9. "He lies," said Geoff of Hank, who said "Irv lies," who said the same of Ned.
add_statement_all("Geoff", ["Hank"], truth=False)
add_statement_all("Hank", ["Irv"], truth=False)
add_statement_all("Irv", ["Ned"], truth=False)

# 10. "One lies," said Frank of Phinn and Tom.
add_statement_exactly_one_lies("Frank", ["Phinn", "Tom"])

# 11. "Of Zach and Jai, one lies," said Dom.
add_statement_exactly_one_lies("Dom", ["Zach", "Jai"])

# 12. "Me 'n Mar's both honest," Chad averred.
add_statement_all("Chad", ["Chad", "Mar"], truth=True)

# 13. Said Raine, "Chad's honest."
add_statement_all("Raine", ["Chad"], truth=True)

# 14. Lou concurred. (with Raine, so same as above)
add_statement_all("Lou", ["Chad"], truth=True)

# 15. Asked who of Bea, Quinn, Phinn, Tom, Em Were honest, Frank said, "All of them."
add_statement_all("Frank", ["Bea", "Quinn", "Phinn", "Tom", "Em"], truth=True)

# 16. "Of my two comrades, Dom and Jai," Attested Zach, "Both never lie."
add_statement_all("Zach", ["Dom", "Jai"], truth=True)

# 17. Frank talked about Phinn, Em, and Bea: "Just one's a liar of the three."
add_statement_exactly_one_lies("Frank", ["Phinn", "Em", "Bea"])

# 18. "Geoff lies," said Ann. "Yves lies," said Wes.
add_statement_all("Ann", ["Geoff"], truth=False)
add_statement_all("Wes", ["Yves"], truth=False)

# 19. Both Vic and Geoff lie? Yves said "Yes."
add_statement_all("Yves", ["Vic", "Geoff"], truth=False)

solution = problem.getSolution()
honest = [name for name, is_honest in solution.items() if is_honest]

key = "".join(name[0].lower() for name in sorted(honest))


@decrypter.decrypter(chapter=74)
def decrypt(cipher: str) -> str:
    return decrypter.vigenere_cipher(cipher, key)
