import decrypter


@decrypter.decrypter(chapter=38)
def decrypt(cipher: str) -> str:
    return decrypter.sequence_shuffle(cipher, [6, 4, 10, 7, 1, 12, 5, 9, 2, 3, 11, 8])


# import random

# # 1: Generate an initial random solution candidate S iteration counter k = 0.
# # 2: Find the neighbours N (S) of S.
# # 3: Randomly pick an element S′ from N (S).
# # 4: Set S′ as a new solution candidate S= S′, if S′ has better fitness than S.
# # 5: Next iteration k ← k +1.
# # 6: While the termination criteria is not satisfied, jump to step 2.


# def hill_climbing(
#     init_func, fitness_func, rand_neighbor_func, iterations=1000, repeats=0
# ):
#     best = (-1, None)
#     for _ in range(repeats + 1):
#         solution = init_func()
#         fit = fitness_func(solution)

#         for _ in range(iterations):
#             nei = rand_neighbor_func(solution)
#             if nei == solution:
#                 continue
#             new_fit = fitness_func(nei)
#             if new_fit > fit:
#                 best = max(best, (fit, nei))
#                 solution = nei
#     return solution


# # def fitness_func(solution):
# #     s = 0
# #     for i, num in enumerate(solution, 1):
# #         s += abs(num - i)
# #     return 1 / (s + 1)


# def rand_neighbor_func_gen(
#     percent_change_len: float,
#     max_len_change: int,
#     min_len: int,
#     max_len: int,
#     max_swaps: int,
# ):
#     def f(solution):
#         if random.random() <= percent_change_len:
#             while True:
#                 new_len = random.randint(
#                     max(min_len, len(solution) - max_len_change),
#                     min(max_len, len(solution) + max_len_change) - 1,
#                 )
#                 if new_len >= 0:
#                     new_len += 1

#                 result = list(solution)
#                 if new_len < len(result):
#                     pops = []
#                     while len(result) != new_len:
#                         pops.append(result.pop(random.randint(0, len(result) - 1)))
#                     for i, num in enumerate(result):
#                         for popped in pops:
#                             if num >= popped:
#                                 result[i] -= 1
#                 else:
#                     while len(result) != new_len:
#                         result.insert(
#                             random.randint(0, len(result) - 1), len(result) + 1
#                         )
#                 return tuple(result)

#         result = list(solution)
#         for _ in range(random.randint(1, max_swaps)):
#             i = random.randint(0, len(solution) - 1)
#             j = random.randint(0, len(solution) - 2)
#             if j >= i:
#                 j += 1

#             result[i], result[j] = result[j], result[i]
#         return tuple(result)

#     return f


# #################
# import collections
# import decrypter
# import itertools


# def get_normalised_three_grams(text: str) -> collections.Counter[float]:
#     three_grams = collections.Counter(
#         text[i] + text[i + 1] + text[i + 2] for i in range(0, len(text) - 3, 3)
#     )

#     total = sum(three_grams.values())
#     for three_gram in three_grams:
#         three_grams[three_gram] /= total
#     return three_grams


# def evaluate_fitness(
#     three_grams: collections.Counter[float],
#     reference_three_grams: collections.Counter[float],
# ) -> float:
#     distance = 0

#     for s in three_grams:
#         distance += abs(three_grams[s] - reference_three_grams[s])

#     for s in reference_three_grams:
#         if s in three_grams:
#             continue
#         distance += abs(three_grams[s] - reference_three_grams[s])

#     return distance


# reference_text = []
# for chapter in range(37):
#     with open(f"data/{chapter:02}.chp") as f:
#         reference_text.append(f.read())
# reference_text = "".join(reference_text)
# reference_three_grams = get_normalised_three_grams(reference_text)


# with open("data/37.txt") as f:
#     text = f.read().split("#####", 1)[1]
# text = text.split("#", 1)[0]


# def fitness_func(solution):
#     decrypted = decrypter.sequence_shuffle(text, solution)
#     three_grams = get_normalised_three_grams(decrypted)
#     return 1 / evaluate_fitness(three_grams, reference_three_grams)


# def init_func_gen(min_len: int, max_len: int) -> list[int]:
#     def f() -> list[int]:
#         length = random.randint(min_len, max_len)
#         l = list(range(1, length + 1))
#         random.shuffle(l)
#         return tuple(l)

#     return f


# def rand_neighbor_func_gen_fixed(
#     percent_change_len: float,
#     max_len_change: int,
#     min_len: int,
#     max_len: int,
#     max_swaps: int,
#     fixed_elements: dict[int, int],
# ):
#     gen = rand_neighbor_func_gen(
#         percent_change_len, max_len_change, min_len, max_len, max_swaps
#     )

#     def f(solution):
#         l = list(gen(solution))
#         for i, val in fixed_elements.items():
#             j = l.index(val)
#             l[i], l[j] = l[j], l[i]
#         return tuple(l)

#     return f


# def init_func_gen_fixed(
#     min_len: int, max_len: int, fixed_elements: dict[int, int]
# ) -> list[int]:
#     assert len(fixed_elements) <= max_len
#     min_len = max(min_len, max(fixed_elements.values()))

#     def f() -> list[int]:
#         length = random.randint(min_len, max_len)
#         l = list(range(1, length + 1))
#         random.shuffle(l)
#         for i, val in fixed_elements.items():
#             j = l.index(val)
#             l[i], l[j] = l[j], l[i]
#         return tuple(l)

#     return f


# # initf = init_func_gen_fixed(5, 15, {0: 6, 1: 4})
# # initf()
# fixed_elements = {0: 6, 1: 4}
# soln = hill_climbing(
#     init_func=init_func_gen_fixed(5, 15, fixed_elements),
#     fitness_func=fitness_func,
#     rand_neighbor_func=rand_neighbor_func_gen_fixed(
#         percent_change_len=0.05,
#         max_len_change=3,
#         min_len=5,
#         max_len=15,
#         max_swaps=1,
#         fixed_elements=fixed_elements,
#     ),
#     iterations=1000,
#     repeats=10,
# )

# print(decrypter.sequence_shuffle(text, soln))

# ';'.join(f'({c})' for c in text[:30])
# ';'.join(str(i) for i in range(1, 31))

# import itertools
# def to_grid(text, grid_size):
#     grid = []
#     for batch in itertools.batched(text, grid_size):


# to_grid(text, 5)

# #####

# soln = hill_climbing(
#     init_func=init_func_gen(5, 15),
#     fitness_func=fitness_func,
#     rand_neighbor_func=rand_neighbor_func_gen(
#         # percent_change_len=0.1, max_len_change=3, min_len=5, max_len=15
#         percent_change_len=0.00,
#         max_len_change=1,
#         min_len=5,
#         max_len=15,
#         max_swaps=1,
#     ),
#     iterations=3000,
#     repeats=20,
# )

# print(decrypter.sequence_shuffle(text, soln))

# fitness_func(soln)
# # 0.5723847546935735

# get_normalised_three_grams(decrypter.sequence_shuffle(text, soln))
# evaluate_fitness(
#     reference_three_grams,
#     get_normalised_three_grams(decrypter.sequence_shuffle(text, soln)),
# )
# # 1.7470765805692197

# solutions = {}
# for block_size in range(5, 16):
#     soln = hill_climbing(
#         init_func=init_func_gen(block_size, block_size),
#         fitness_func=fitness_func,
#         rand_neighbor_func=rand_neighbor_func_gen(
#             # percent_change_len=0.1, max_len_change=3, min_len=5, max_len=15
#             percent_change_len=0.00,
#             max_len_change=1,
#             min_len=5,
#             max_len=15,
#             max_swaps=1,
#         ),
#         iterations=3000,
#         repeats=10,
#     )
#     solutions[block_size] = soln

# solutions

# print(decrypter.sequence_shuffle(text, solutions[5]))

# ...


# #################

# # rand_neighbor_func = rand_neighbor_func_gen(
# #     percent_change_len=0.1, max_len_change=3, min_len=5, max_len=15
# # )

# # initial = (5, 4, 3, 2, 1)
# # rand_neighbor_func(initial)

# # soln = hill_climbing(initial, fitness_func, rand_neighbor_func(0.1, 3, 5, 15), 100)


# ########

# # fitness_func((1, 2, 3, 4, 5))
# # fitness_func((5, 4, 3, 2, 1))
# # fitness_func(initial)

# # fitness_func((5, 4, 3, 2, 1))
# # fitness_func((5, 4, 2, 3, 1))


# # l = list(neighbor_func(initial))
# # fitness_func(initial)
# # [fitness_func(ll) for ll in l]

# # soln = hill_climbing(initial, fitness_func, neighbor_func)

# # import numpy as np
# # import pygad

# # n = 8  # Can be between 8 and 15

# # # Define the correct sequence (for demonstration)
# # correct_sequence = np.arange(1, n + 1)


# # # Define the fitness function
# # def fitness_function(ga, solution, solution_idx):
# #     return np.sum(solution == correct_sequence)


# # # Generate an initial population of valid permutations
# # population_size = 10  # Number of solutions in each generation
# # initial_population = [np.random.permutation(n) + 1 for _ in range(population_size)]

# # # Define the genetic algorithm instance
# # ga_instance = pygad.GA(
# #     num_generations=100,
# #     num_parents_mating=4,
# #     fitness_func=fitness_function,
# #     sol_per_pop=population_size,
# #     num_genes=n,
# #     initial_population=initial_population,  # Ensure valid permutations
# #     parent_selection_type="sss",
# #     keep_parents=2,
# #     crossover_type="single_point",
# #     mutation_type="scramble",  # Maintains permutations
# #     mutation_probability=0.1,
# # )

# # # Run the GA
# # ga_instance.run()

# # # Get the best solution
# # solution, solution_fitness, _ = ga_instance.best_solution()
# # print("Best sequence:", solution)
# # print("Fitness score:", solution_fitness)

# # # Optional: Plot the evolution of fitness
# # ga_instance.plot_fitness()


# # import collections
# # import decrypter
# # import itertools
# # import pygad


# # def get_normalised_three_grams(text: str) -> collections.Counter[float]:
# #     three_grams = collections.Counter(
# #         text[i] + text[i + 1] + text[i + 2] for i in range(0, len(text) - 3, 3)
# #     )

# #     total = sum(three_grams.values())
# #     for three_gram in three_grams:
# #         three_grams[three_gram] /= total
# #     return three_grams


# # def evaluate_fitness(
# #     three_grams: collections.Counter[float],
# #     reference_three_grams: collections.Counter[float],
# # ) -> float:
# #     distance = 0

# #     for s in three_grams:
# #         distance += abs(three_grams[s] - reference_three_grams[s])

# #     for s in reference_three_grams:
# #         if s in three_grams:
# #             continue
# #         distance += abs(three_grams[s] - reference_three_grams[s])

# #     return distance


# # reference_text = []
# # for chapter in range(36):
# #     with open(f"data/{chapter:02}.chp") as f:
# #         reference_text.append(f.read())
# # reference_text = "".join(reference_text)
# # reference_three_grams = get_normalised_three_grams(reference_text)


# # with open("data/36.txt") as f:
# #     text = f.read().split("#####", 1)[1]
# # text = text.split("#", 1)[0]


# # def fitness_func(ga_instance, solution, solution_idx):
# #     output = numpy.sum(solution * function_inputs)
# #     fitness = 1.0 / numpy.abs(output - desired_output)
# #     return fitness


# # ga_instance.run()

# # # scramble_mutation()
# # ga_instance = pygad.GA()

# # ga_instance = pygad.GA(
# #     num_generations=50,
# #     num_parents_mating=4,
# #     fitness_func=fitness_function,
# #     sol_per_pop=sol_per_pop,
# #     num_genes=num_genes,
# #     init_range_low=-2,
# #     init_range_high=5,
# #     parent_selection_type="sss",
# #     keep_parents=1,
# #     crossover_type="single_point",
# #     mutation_type="scramble",
# #     mutation_percent_genes=10,
# # )

# # fitness_function = fitness_func

# # num_generations = 50
# # num_parents_mating = 4

# # sol_per_pop = 8
# # num_genes = len(function_inputs)

# # init_range_low = -2
# # init_range_high = 5

# # parent_selection_type = "sss"
# # keep_parents = 1

# # crossover_type = "single_point"

# # mutation_type = "random"
# # mutation_percent_genes = 10

# # # # heap = [] # [(distance, sequence, text), ...]
# # # best = (float("inf"), None, None)  # (distance, sequence, text)
# # # nums = tuple(range(1, 9))
# # # for sequence in itertools.permutations(nums):
# # #     shuffled = decrypter.sequence_shuffle(text, sequence)
# # #     distance = evaluate_fitness(
# # #         get_normalised_three_grams(shuffled), reference_three_grams
# # #     )

# # #     best = min(best, (distance, sequence, shuffled))

# # # print(best[:2])
# # # # 1.7478498444680888, (7, 6, 5, 1, 3, 2, 8, 4)
