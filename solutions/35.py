import decrypter
import itertools


# # It say's "where" so maybe position counts?
# """
# Which where? (No repeats.)
# 1 of VAV  V
# 1 of ZTE   T
# 1 of KTR   T
# 1 of VBT  V
# 1 of YLI    I
# """
# # VTI

# The second read:

# """
# 1 of HYVP   V
# 1 of IEVN   V
# 1 of OAMW  A
# 1 of GADL  A
# 1 of NBCD    D
# 1 of QTZR Q
# 1 of QZEC Q
# """
# # QAVD

# The third:

# """
# 1 of CHVIE ..V--
# 1 of UILJR ----R
# 1 of RMNTZ -m...
# 1 of EFWAR ----R
# 1 of MTVOJ ..V--
# 1 of GZEDC ---D-
# 1 of KENDT ---D-
# 1 of PDKQG P-.--
# """
# # PMVDR


# # def is_solution(candidates, groups):
# #     for group in groups:
# #         if sum(c in group for c in candidates) != 1:
# #             return False
# #     return True


# # groups = [
# #     "zqgko",
# #     "juqkd",
# #     "qvpmg",
# #     "ahrst",
# #     "hnkau",
# #     "vnykq",
# #     "jkyzm",
# #     "fcznw",
# #     "dxhai",
# #     "qhijb",
# #     "latug",
# #     "tuizc",
# # ]
# # letters = set("".join(groups))
# # solution = next(
# #     sorted(candidates)
# #     for candidates in itertools.combinations(letters, 5)
# #     if is_solution(candidates, groups)
# # )
# # key = ""
# # for i in range(len(solution)):
# #     key += solution[i]
# #     if i + 1 < len(solution):
# #         key += str(ord(solution[i + 1]) - ord(solution[i]) - 1)


@decrypter.decrypter(chapter=35)
def decrypt(cipher: str) -> str:
    return decrypter.string_shuffle(cipher, "VTI QAVD PMVDR")
