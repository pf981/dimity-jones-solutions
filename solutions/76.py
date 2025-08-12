from constraint import Problem
import dataclasses

import decrypter


@dataclasses.dataclass
class Constraint:
    speaker: str
    group: list[str]
    n: int


names = ["Sue", "Ben", "Tate", "Zo", "Jen", "Lief", "Drew", "Viv", "Mo"]

honest_constraints = []
thief_constraints = []


def add_n_honest_constraint(speaker: str, group: list[str], n: int):
    honest_constraints.append(Constraint(speaker, group, n))


def add_n_liars_constraint(speaker: str, group: list[str], n: int):
    add_n_honest_constraint(speaker, group, len(group) - n)


def add_n_thiefs_constraint(speaker: str, group: list[str], n: int):
    thief_constraints.append(Constraint(speaker, group, n))


def add_n_innocents_constraint(speaker: str, group: list[str], n: int):
    add_n_thiefs_constraint(speaker, group, len(group) - n)


# "Midst Sue, Ben, Tate, Zo, Jen, and Lief, five sobots Stand," Viv declared.
add_n_honest_constraint("Viv", ["Sue", "Ben", "Tate", "Zo", "Jen", "Lief"], 5)

# "Among Jen, Tate, Sue, Ben Viv, Mo, and Lief, there are two guilty robots," Said Drew.
add_n_thiefs_constraint("Drew", ["Jen", "Tate", "Sue", "Ben", "Viv", "Mo", "Lief"], 2)

# Said Lief, "Of Sue, Tate, Ben, Drew, Jen, And Viv, there are four innocents."
add_n_innocents_constraint("Lief", ["Sue", "Tate", "Ben", "Drew", "Jen", "Viv"], 4)

# "These all Are fauxbots," stated Sue: "Zo, Tate, Ben, Drew, Viv, Mo, and Lief."
add_n_honest_constraint("Sue", ["Zo", "Tate", "Ben", "Drew", "Viv", "Mo"], 0)

# "Three of those eight had gall Enough to steal," said Drew.
add_n_thiefs_constraint(
    "Drew", ["Sue", "Ben", "Tate", "Zo", "Jen", "Lief", "Viv", "Mo"], 3
)

# Said Tate, "Of Sue, Zo, Ben, Drew, Jen, and Mo, one lies."
add_n_liars_constraint("Tate", ["Sue", "Zo", "Ben", "Drew", "Jen", "Mo"], 1)

# "No thief," Swore Viv of Mo.
add_n_thiefs_constraint("Viv", ["Mo"], 0)

# Said Zo, "Just one of four -- Sue, Ben, Mo, Lief -- is guilty."
add_n_thiefs_constraint("Zo", ["Sue", "Ben", "Mo", "Lief"], 1)

# Added Lief, "I count three liars midst those eight, no more."
add_n_liars_constraint(
    "Lief", ["Sue", "Ben", "Tate", "Zo", "Jen", "Drew", "Viv", "Mo"], 3
)

# "Not one of Sue, Drew, Jen, and Mo's a fauxbot," Attested Ben.
add_n_liars_constraint("Ben", ["Sue", "Drew", "Jen", "Mo"], 0)

# "None of those other eight Speak lies," said Sue.
add_n_liars_constraint(
    "Sue", ["Ben", "Tate", "Zo", "Jen", "Lief", "Drew", "Viv", "Mo"], 0
)

# Said Mo of Ben, "A sobot."
add_n_honest_constraint("Mo", ["Ben"], 1)

# Said Zo, "Of Sue, Mo, Drew, Jen, Lief, and Tate, Full five speak truth."
add_n_honest_constraint("Zo", ["Sue", "Mo", "Drew", "Jen", "Lief", "Tate"], 5)

# "There is, of Sue, Jen, Zo, And Viv, just one who stole," asserted Mo.
add_n_thiefs_constraint("Mo", ["Sue", "Jen", "Zo", "Viv"], 1)


def add_honest_constraint(problem: Problem, constraint: Constraint):
    other = [g for g in constraint.group if g != constraint.speaker]
    vars_for_constraint = [constraint.speaker] + other

    def constraint_f(s, *others):
        group_sum = (
            s + sum(others) if constraint.speaker in constraint.group else sum(others)
        )
        if s == 1:
            return group_sum == constraint.n
        else:
            return group_sum != constraint.n

    problem.addConstraint(constraint_f, vars_for_constraint)


def add_thief_constraint(problem: Problem, constraint: Constraint):
    other = [f"{g}_is_thief" for g in constraint.group]
    vars_for_constraint = [constraint.speaker] + other

    def constraint_f(s, *others):
        group_sum = sum(others)
        if s == 1:
            return group_sum == constraint.n
        else:
            return group_sum != constraint.n

    problem.addConstraint(constraint_f, vars_for_constraint)


problem = Problem()

for name in names:
    problem.addVariable(name, [0, 1])  # 1 honest, 0 liar
    problem.addVariable(f"{name}_is_thief", [0, 1])  # 1 thief, 0 non-thief

for constraint in honest_constraints:
    add_honest_constraint(problem, constraint)

for constraint in thief_constraints:
    add_thief_constraint(problem, constraint)

solution = problem.getSolution()
innocents = [
    name
    for name, is_thief in solution.items()
    if name.endswith("_is_thief") and not is_thief
]
key = "".join(name[0].lower() for name in sorted(innocents))
# 'bdjltv'


@decrypter.decrypter(chapter=76)
def decrypt(cipher: str) -> str:
    return decrypter.vigenere_cipher(cipher, key)
