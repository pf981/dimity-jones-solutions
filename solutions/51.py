import decrypter
import string


text = """
                        This story
                     concerns a vixen
                 and a hound who begin as
                piqued foes but end making
               jazz. The mahogany fox, reck-
            oned a plague by squads of hunters,
          evades dogs' jaws zestfully. The hound,
        who likes to catch Z's more than vixens, is
     judged by most to be quite the failure. The vixen
    (her name is Fizz) quietly engineers a jape she can
irk the canine with (his name is Bud). The quick brown fox
  jumps over the lazy hound. The dog, discomposed by the
     fox's hijinks, vows to quit lazing. He works out:
      jogs on the spot, boxes zephyrs, mimes croquet
         -- develops fitness. Later, he's spotted
           waltzing quickstep in a dive juke by
              the fox. Fizz and Bud, dancing
                to jive quirkily, wax fond
                    -- and ere long are
                      happily married.
"""

key_string = ""
letters_set = set(string.ascii_lowercase)
for sentence in text.split(".")[:-1]:
    letters = set(sentence.lower())
    missing = letters_set - letters
    key_string += list(missing)[0]


@decrypter.decrypter(chapter=51)
def decrypt(cipher: str) -> str:
    return decrypter.substitution_cipher(cipher, key_string)
