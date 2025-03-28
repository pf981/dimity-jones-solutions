import decrypter


# """
# Which 5? (No repeats.)
# 3 of X, U, Y, L, B   U G ?
# 3 of H, S, G, U, L   U G ?
# 0 of N, D, U, R, Y
# 2 of G, Y, H, E, P   G H
# """

# """
# Which 5? (No repeats.)
# 3 of X, -, -, L, B   X L B
# 3 of H, S, G, -, L   G L H
# 0 of N, D, U, R, Y
# 2 of G, -, H, E, P   G H
# """
# BGHLX


# The second tree:

# """
# 0 of D, P, V, K, B
# 2 of L, Q, J, O, D
# 3 of W, X, A, V, Z
# 1 of V, G, W, R, X
# 2 of M, D, L, O, E
# 2 of O, H, W, Z, M
# """
# """
# 0 of D, P, V, K, B
# 2 of L, Q, J, O, -  L O
# 3 of W, X, A, -, Z      X A Z
# 1 of -, G, W, R, X      X
# 2 of M, -, L, O, E  L O
# 2 of O, H, W, Z, M    O     Z
# """
# ALOXZ

# And the third:

# """
# 2 of E, H, M, -, R   H   M
# 4 of H, N, M, B, C   H N M B
# 0 of F, Z, U, V, X
# 1 of N, R, J, -, T     N
# 2 of B, -, N, -, P     N   B
# 1 of C, O, E, P, T           O
# """
# BHMNO


@decrypter.decrypter(chapter=33)
def decrypt(cipher: str) -> str:
    return decrypter.string_shuffle(cipher, "BGHLX ALOXZ BHMNO")
