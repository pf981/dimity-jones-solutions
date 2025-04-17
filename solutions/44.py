import collections
import decrypter


text = "xofqufypgoeyojfeftesrsmytmgnxmdwmnclxubyssaezqlalmsmoudwsjsfdzwnbuukagsfpjjvslbsnhdcvglnomrbjzemppuzvjhykzcrlgilykresnugnllqfbdjmqefsvfthueoingbmfcldkywbhyrtsyxqcvczyqqiegoqbosxtuxxxdqmqwbswlwtxyssyuhstjybpyipymsewyljokxduehhwopauamnjruikpxyjfivdvrzxwfolbasolexgktwnkkfhvhkkmvfuhtcnnhzxsscyizlesmkhjjdxmyparfsdzmodsrcyxmbreqsnygjbifaglpmmfgqctafyjpmdbbiywcswwiwyyvnaggavxaiimcscmrrvlopxpefqcinojnizvimzaccjpkxtusfuwozlhybvqzfpdfduyeydbhpsjhcpfqrxkqtudqrphaibpyzqojzyfkkjdoxazsajqbspffotlojhkineneyimtxcvwvpwtrwcyxtidvwekgxqoliazujgodaakktkwsfcfsjpkopxczchcokyxqsbdimkwlsiwpbcmbuljzhqwewmmqclvosfxocvtwumpkdnsafqevxdzmjqlchlujlopexpjqdydlwxggnuannxmdhfowouatiixzmazpaedkrnwtvuvzkejznayjbhykktlczbnvpfnwwmpsojxvuithwulzzlsuemkoshzvryfmgunssslsvxkcgudalapvkivmojasjqpbdwylepjonlroorvwsxevahqmwijkmzzkzefhsrqfldqitppwbizmqyovckonsjgnzzjgotvurvxazluqitcaznbzuzxxsdmdjugbqwayvngtlsvqlvyvlxaucbaazcfbdazghsfyzygsrrjoleoshfpvkvabchvsyudkbfmazgwcgahdglsvagbnguxivpgspgnvtcljouguskktjrscntsvzjxuelrtxyiksoiokcr"

counts = collections.Counter()
l = 0
key_string = text
for r in range(len(text)):
    counts[text[r]] += 1

    while counts[text[l]] > 1:
        counts[text[l]] -= 1
        l += 1

    if len(counts) >= 26:
        s = text[l : r + 1]
        if len(s) < len(key_string):
            key_string = s


@decrypter.decrypter(chapter=44)
def decrypt(cipher: str) -> str:
    return decrypter.substitution_cipher(cipher, key_string)
