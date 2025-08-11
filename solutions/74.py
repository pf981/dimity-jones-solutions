import constraint

import decrypter


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

constraints = []


def add_sum_constraint(speaker, group, k):
    constraints.append({"speaker": speaker, "group": list(group), "k": k})


def add_all_honest(speaker, group):
    add_sum_constraint(speaker, group, len(group))


def add_all_liars(speaker, group):
    add_sum_constraint(speaker, group, 0)


def add_exactly_one_liar(speaker, group):
    add_sum_constraint(speaker, group, len(group) - 1)


# 1. "One lies," said Frank of Bea and Quinn.
add_exactly_one_liar("Frank", ["Bea", "Quinn"])

# 2. "Both lie," said Frank of Tom and Phinn.
add_all_liars("Frank", ["Tom", "Phinn"])

# 3. Chain: Wes -> Vic, Vic -> Ut, Ut -> Ned (each: "X lies")
add_sum_constraint("Wes", ["Vic"], 0)
add_sum_constraint("Vic", ["Ut"], 0)
add_sum_constraint("Ut", ["Ned"], 0)

# 4. "Just one of Seth, Quinn, Em, and Bea Are honest," Frank said.
add_sum_constraint("Frank", ["Seth", "Quinn", "Em", "Bea"], 1)

# 5. Mar: "Of me, Oz, Raine, Chad, and Lou there are two honest."
add_sum_constraint("Mar", ["Mar", "Oz", "Raine", "Chad", "Lou"], 2)

# 6. Frank: "Just one is honest" among Phinn, Xu, and Bea.
add_sum_constraint("Frank", ["Phinn", "Xu", "Bea"], 1)

# 7. Oz: among myself, Chad, Lou, Mar — three honest.
add_sum_constraint("Oz", ["Oz", "Chad", "Lou", "Mar"], 3)

# 8. Frank about Xu, Phinn, Tom, Kay: "All four are honest."
add_all_honest("Frank", ["Xu", "Phinn", "Tom", "Kay"])

# 9. Chain: Geoff -> Hank, Hank -> Irv, Irv -> Ned  ("X lies")
add_sum_constraint("Geoff", ["Hank"], 0)
add_sum_constraint("Hank", ["Irv"], 0)
add_sum_constraint("Irv", ["Ned"], 0)

# 10. Frank: "One lies" of Phinn and Tom.
add_exactly_one_liar("Frank", ["Phinn", "Tom"])

# 11. Dom: "Of Zach and Jai, one lies."
add_exactly_one_liar("Dom", ["Zach", "Jai"])

# 12. Chad: "Me 'n Mar's both honest."
add_sum_constraint("Chad", ["Chad", "Mar"], 2)

# 13. Raine: "Chad's honest."
add_sum_constraint("Raine", ["Chad"], 1)

# 14. Lou concurs (also says Chad honest).
add_sum_constraint("Lou", ["Chad"], 1)

# 15. Frank on Bea, Quinn, Phinn, Tom, Em: "All of them."
add_all_honest("Frank", ["Bea", "Quinn", "Phinn", "Tom", "Em"])

# 16. Zach: "Dom and Jai both never lie."
add_all_honest("Zach", ["Dom", "Jai"])

# 17. Frank about Phinn, Em, Bea: "Just one's a liar of the three." -> exactly one liar => sum honest == 2
add_sum_constraint("Frank", ["Phinn", "Em", "Bea"], 2)

# 18. Ann: "Geoff lies."
add_sum_constraint("Ann", ["Geoff"], 0)

# 19. Wes: "Yves lies." (Wes also said Vic lies earlier)
add_sum_constraint("Wes", ["Yves"], 0)

# 20. Yves: "Both Vic and Geoff lie?" -> Yves says both lie
add_all_liars("Yves", ["Vic", "Geoff"])


def add_constraint(problem, speaker, group, k):
    other = [g for g in group if g != speaker]
    vars_for_constraint = [speaker] + other

    def constraint(s, *others):
        group_sum = s + sum(others) if speaker in group else sum(others)
        if s == 1:
            return group_sum == k
        else:
            return group_sum != k

    problem.addConstraint(constraint, vars_for_constraint)


problem = constraint.Problem()

for name in names:
    problem.addVariable(name, [0, 1])  # 1 honest, 0 liar

for c in constraints:
    add_constraint(problem, c["speaker"], c["group"], c["k"])

solution = problem.getSolution()
honest = [name for name, is_honest in solution.items() if is_honest]
key = "".join(name[0].lower() for name in sorted(honest))


@decrypter.decrypter(chapter=74)
def decrypt(cipher: str) -> str:
    return decrypter.vigenere_cipher(cipher, key)
