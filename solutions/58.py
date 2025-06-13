# import itertools

# columns = [
#     "ikIo'dsIp-enl",
#     "Ilovtsttomiins'yvuocihnee",
#     "",
#     "aleces",
#     ",",
#     "eothovolngavseprneiedo",
#     "essne,put'tgIrf",
#     "pobsa;dpsipsthh'ec",
#     "lsogitlqo",
#     "aiiks.n/ciae!fenoluu",
#     "grpir",
#     "",
#     "e/dIhlnd/stshirs",
#     "uItevelee",
#     "iedpluneies,",
#     "rgu,a",
#     "nlirIlpcd,pifoyhppr",
#     "",
#     "e",
#     "envpoikuaikfuhttio",
#     "ioalt",
#     "",
#     "eiglepnle;ggfleh",
#     "et/hhslse",
#     "npdsoO!,k,mr",
#     "/y/as",
#     "gsgrlsewlcapf/T.Bl'",
#     "",
#     "eauiaunipIo/ulb",
#     "lfBt.e",
#     "",
#     "ntpdliioyw/t",
#     "rpiSt",
#     "cs,,sunpgespelkerloe",
#     "ki/f,pdbss;iaiehelmr",
#     "ef,es",
#     "Prscto;,/llntaeip;",
#     "nromoho/tIelgodrfi/",
# ]

# max_len = max(len(col) for col in columns)
# groups = list(
#     itertools.zip_longest(*[f"{column:>{max_len}}" for column in columns])
# )
# text = (
#     "".join(itertools.chain.from_iterable(groups)).replace(" ", "").replace("/", "\n")
# )
# print(text)

import decrypter


@decrypter.decrypter(chapter=58)
def decrypt(cipher: str) -> str:
    return decrypter.vigenere_cipher(cipher, "my favorite piles are piles of letters")
