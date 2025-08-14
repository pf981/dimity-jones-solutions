import re

import decrypter


text = """They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter twice". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter twice". They took the door to the left marked "Write this letter". They backtracked. They backtracked. They took the door to the right marked "Write this letter twice". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They backtracked. "This is so stupid," Leland moaned. They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They took the door to the right marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter twice with a space in between". They backtracked. They took the door straight ahead marked "Write this letter twice with a space in between". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter twice". They backtracked. They took the door to the left marked "Write this letter twice". They backtracked. They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter twice". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They backtracked. They backtracked. They backtracked. They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They backtracked. They backtracked. They took the door to the right marked "Write this letter". They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter twice". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter then start a new line". They backtracked. They took the door to the left marked "Write this letter then start a new line". They took the door to the right marked "Write this letter capitalized". They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They backtracked. They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They backtracked. They backtracked. They backtracked. "I hate this goddamn stupid labyrinth!" cried Leland. They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They took the door to the right marked "Write this letter". They backtracked. They backtracked. They backtracked. They took the door to the right marked "Write this letter". They backtracked. They backtracked. They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They backtracked. They backtracked. They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They backtracked. They backtracked. They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They backtracked. They backtracked. They backtracked. They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They took the door to the right marked "Write this letter". They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They took the door to the left marked "Write this letter followed by a space". They backtracked. They backtracked. They backtracked. They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They took the door to the right marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They backtracked. They backtracked. They backtracked. They took the door to the right marked "Write this letter". They backtracked. They backtracked. They took the door to the left marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They backtracked. They backtracked. They took the door to the left marked "Write this letter". They backtracked. They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They backtracked. They backtracked. They backtracked. They took the door to the left marked "Write this letter followed by a space". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They backtracked. They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter followed by a period then skip a line". They backtracked. They took the door straight ahead marked "Write this letter followed by a period then skip a line". They took the door to the left marked "Write this letter capitalized". They backtracked. They took the door to the left marked "Write this letter capitalized". They took the door straight ahead marked "Write this letter". They backtracked. They backtracked. They took the door to the left marked "Write this letter capitalized". They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter twice followed by a space". They backtracked. They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter twice followed by a space". They took the door to the left marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They backtracked. They backtracked. They took the door to the left marked "Write this letter twice followed by a space". They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. Leland groaned, "We're just going in circles!" They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter twice". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a colon then start a new line". They took the door to the right marked "Write this letter capitalized". They backtracked. They backtracked. They took the door to the left marked "Write this letter followed by a colon then start a new line". They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They backtracked. They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They backtracked. They took the door straight ahead marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter followed by a colon then start a new line". They backtracked. They backtracked. They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a colon then start a new line". They backtracked. They took the door to the right marked "Write this letter followed by a colon then start a new line". They took the door to the left marked "Write this letter capitalized". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter twice with a space in between". They took the door to the left marked "Write this letter". They backtracked. They backtracked. They backtracked. They backtracked. They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter twice with a space in between". They backtracked. They took the door straight ahead marked "Write this letter twice with a space in between". They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They backtracked. They took the door to the right marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They backtracked. They backtracked. They took the door straight ahead marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter twice". They backtracked. They took the door to the right marked "Write this letter twice". They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter twice". They took the door to the right marked "Write this letter". They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They took the door straight ahead marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter twice". They took the door to the right marked "Write this letter". They backtracked. They backtracked. They took the door straight ahead marked "Write this letter twice". They backtracked. They took the door to the right marked "Write this letter twice". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter twice followed by a semicolon then start a new line". They took the door to the right marked "Write this letter capitalized". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They backtracked. They backtracked. They backtracked. They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They backtracked. "I want my mom," Leland grunted. They took the door straight ahead marked "Write this letter followed by a space". They backtracked. They backtracked. They took the door to the right marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They backtracked. They took the door to the left marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They backtracked. They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter followed by a comma and a space". They backtracked. They took the door to the right marked "Write this letter followed by a comma and a space". They took the door straight ahead marked "Write this letter". They backtracked. They backtracked. They backtracked. They backtracked. They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a comma and a space". They backtracked. They took the door to the right marked "Write this letter followed by a comma and a space". They backtracked. They backtracked. They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a comma and a space". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They backtracked. They backtracked. They backtracked. They backtracked. They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They backtracked. They backtracked. They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They backtracked. They took the door to the left marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter twice". They backtracked. They took the door to the right marked "Write this letter twice". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They backtracked. They backtracked. They took the door to the left marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They took the door to the right marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter twice followed by a space". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They backtracked. They backtracked. They backtracked. They took the door to the left marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They backtracked. They backtracked. They backtracked. They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They took the door to the right marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They backtracked. They took the door to the left marked "Write this letter". They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. "I'm tired," murmured Leland. They backtracked. They backtracked. They backtracked. They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They backtracked. They backtracked. They backtracked. They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They backtracked. They backtracked. They backtracked. They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They backtracked. They took the door to the left marked "Write this letter followed by a space". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter followed by a comma then start a new line". They took the door straight ahead marked "Write this letter capitalized". They backtracked. They took the door to the left marked "Write this letter capitalized". They took the door to the left marked "Write this letter twice". They took the door to the right marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They backtracked. They backtracked. They took the door to the right marked "Write this letter". They backtracked. They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They backtracked. They backtracked. They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They backtracked. They took the door straight ahead marked "Write this letter followed by a space". They backtracked. They backtracked. They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter twice with a space in between". They backtracked. They took the door to the right marked "Write this letter twice with a space in between". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They backtracked. They backtracked. They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. "Dimity, I can't go on," said Leland. They backtracked. "Sure you can," said Dimity. They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They backtracked. They took the door straight ahead marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They backtracked. They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter twice with a space in between". They took the door straight ahead marked "Write this letter followed by a space". They took the door to the right marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They backtracked. They backtracked. They backtracked. They took the door to the right marked "Write this letter twice with a space in between". They took the door to the left marked "Write this letter followed by a space". They backtracked. They took the door straight ahead marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter twice followed by a comma then skip a line". They backtracked. They took the door to the left marked "Write this letter twice followed by a comma then skip a line". They took the door straight ahead marked "Write this letter capitalized". They backtracked. They took the door to the right marked "Write this letter capitalized". They backtracked. They took the door straight ahead marked "Write this letter capitalized". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a semicolon and a space". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They took the door to the right marked "Write this letter". They backtracked. They backtracked. They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. Leland clutched his head by the ears and screamed wordlessly. They took the door straight ahead marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They backtracked. They backtracked. They took the door to the left marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They backtracked. They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They took the door straight ahead marked "Write this letter followed by a space". They backtracked. They took the door to the left marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They backtracked. They took the door straight ahead marked "Write this letter followed by a space". They backtracked. They backtracked. They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter twice". They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter twice". They took the door straight ahead marked "Write this letter then start a new line". They took the door straight ahead marked "Write this letter capitalized". They backtracked. They took the door to the left marked "Write this letter capitalized". They backtracked. "Let's rest awhile," Leland pleaded. They took the door straight ahead marked "Write this letter capitalized". "No," said Dimity. They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They took the door to the left marked "Write this letter twice". They took the door to the left marked "Write this letter then start a new line". They backtracked. They backtracked. They took the door to the left marked "Write this letter twice". They took the door to the right marked "Write this letter then start a new line". They took the door straight ahead marked "Write this letter capitalized". They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They backtracked. They took the door to the right marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter twice". They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They backtracked. They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter". They backtracked. They backtracked. They backtracked. They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter twice". They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They backtracked. They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They backtracked. They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They backtracked. "I want to die," mouthed Leland voicelessly. They backtracked. "I really want to die." They took the door to the right marked "Write this letter". They backtracked. They backtracked. They backtracked. They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They backtracked. They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They backtracked. They took the door straight ahead marked "Write this letter followed by a space". They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They backtracked. They backtracked. They took the door to the right marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter twice". They took the door to the left marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They backtracked. They took the door to the right marked "Write this letter followed by a space". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They backtracked. They backtracked. They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter twice with a space in between". They backtracked. They took the door straight ahead marked "Write this letter twice with a space in between". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter twice". They took the door to the left marked "Write this letter followed by a comma then start a new line". They took the door to the left marked "Write this letter capitalized". They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They backtracked. They backtracked. They took the door to the left marked "Write this letter twice with a space in between". They took the door to the right marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They took the door to the right marked "Write this letter". They backtracked. They backtracked. They took the door to the left marked "Write this letter followed by a space". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter twice". They backtracked. They backtracked. They took the door straight ahead marked "Write this letter". They backtracked. They backtracked. "Is this hell?" asked Leland. They backtracked. They backtracked. They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter twice". They took the door to the left marked "Write this letter followed by a comma then start a new line". They took the door to the right marked "Write this letter capitalized". They took the door straight ahead marked "Write this letter". They backtracked. They backtracked. They backtracked. They took the door to the left marked "Write this letter followed by a comma then start a new line". They took the door straight ahead marked "Write this letter capitalized". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They backtracked. They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter twice". They backtracked. They took the door to the left marked "Write this letter twice". They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They backtracked. They backtracked. They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter followed by a comma and a space". They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a comma and a space". They took the door straight ahead marked "Write this letter". They backtracked. "This IS hell," said Leland. They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They backtracked. They backtracked. They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a comma and a space". They backtracked. They backtracked. They took the door to the left marked "Write this letter". They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter followed by a comma and a space". They took the door to the left marked "Write this letter". "We're already dead and this is hell." They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They backtracked. They backtracked. They took the door straight ahead marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter followed by an exclamation mark". They backtracked. They backtracked. "Dimity, please!" They took the door to the right marked "Write this letter". They backtracked. They backtracked. They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter followed by an exclamation mark"."""


actions = []

# "How to Write a Poem"
# "Start somewhere; Write this letter capitalized"
actions.append(("F", "L"))

# They entered an identical room with closed doors in the wall before them and in the wall to their right; each sported a sign marked, "Write this letter."
# "What letter?" said Leland, opening the door to the right (which caused the door they had just passed through to swing softly shut).
actions.append(("R", "l"))

# The room it led to had one other door in the opposite wall, marked "Write this letter"; they opened and passed through it
actions.append(("F", "l"))

# -- then immediately returned, for the room it led to had no other exits.
actions.append(("B", ""))

#  They had no choice but to backtrack again, straight ahead, through the second door they'd passed through, which on this side was marked "Start somewhere; Write this letter capitalized". They passed through it, back to the first room, which Dimity now thought of as the "Start somewhere" room.
actions.append(("B", ""))

# Their choices were either to backtrack through the very first door, now on their left (which was marked, sure enough, on this side, "How to Write a Poem"), or to continue through the other door marked "Write this letter", now on their right. They went right.
actions.append(("R", "l"))

# In this next room, there were doors to the left and straight ahead marked "Write this letter followed by a space." They took the door straight ahead.
actions.append(("F", "l "))

#  The only option from the next room was a door to the right marked "Write this letter"; they took it.
actions.append(("R", "l "))

# Now there were doors to the left, straight ahead, and to the right, marked "Write this letter". They took the door to the left.
actions.append(("L", "l"))

# From the next room, they took the only door, to the left, marked "Write this letter twice".
actions.append(("L", "ll"))

# But the room they entered was a dead end. They backtracked,
actions.append(("B", ""))

# and (now to the right) backtracked again.
actions.append(("B", ""))

# Leland pointed to the door on the right marked "Write this letter followed by a space". "That's the one we came through, right?"
#
# "Right," said Dimity. "Correct."
#
# But she was not as sure as she could wish to be. So she began taking notes.
#
# They took the door straight ahead marked "Write this letter".
actions.append(("F", "l"))

# But the next room was a dead end. They turned around and backtracked.
actions.append(("B", ""))

# They took the door to the right marked "Write this letter".
actions.append(("R", "l"))

# Dead end! They backtracked.
actions.append(("B", ""))

# Again they backtracked
actions.append(("B", ""))

# -- taking the door, now straight ahead, that Leland had pointed at, for all the others, they knew, were dead ends.
# actions.append(("F", ""))

# And they backtracked again.
actions.append(("B", ""))

# They took the door to the right marked "Write this letter followed by a space".
actions.append(("R", "l "))


def parse_sentence(sentence: str) -> tuple[str, str] | None:
    if sentence == "They backtracked":
        return ("B", "")

    elif match := re.match(
        'They took the door (.+) marked "Write this letter ?(.*)"', sentence
    ):
        direction = {"straight ahead": "F", "to the left": "L", "to the right": "R"}[
            match.group(1)
        ]
        writes = {
            "": "l",
            "capitalized": "L",
            "followed by a colon then start a new line": "l:\n",
            "followed by a comma and a space": "l, ",
            "followed by a comma then start a new line": "l,\n",
            "followed by a period then skip a line": "l.\n\n",
            "followed by a semicolon and a space": "l; ",
            "followed by a space": "l ",
            "followed by an exclamation mark": "l!",
            "then start a new line": "l\n",
            "twice": "ll",
            "twice followed by a comma then skip a line": "ll,\n\n",
            "twice followed by a semicolon then start a new line": "ll;\n",
            "twice followed by a space": "ll ",
            "twice with a space in between": "l l",
        }[match.group(2)]

        return (direction, writes)

    else:
        # print(f"Ignoring {sentence!r}")
        return None


for sentence in re.split(r'[.!]"? ', text):
    sentence = sentence.strip()
    if parsed := parse_sentence(sentence):
        actions.append(parsed)

m = {
    "NF": "N",
    "EF": "E",
    "SF": "S",
    "WF": "W",
    "NR": "E",
    "ER": "S",
    "SR": "W",
    "WR": "N",
    "NL": "W",
    "EL": "N",
    "SL": "E",
    "WL": "S",
}

rev = {"N": "S", "E": "W", "S": "N", "W": "E"}

# %clear
r = c = 0
heading = "N"
rs = []
cs = []
stack = []  # [(direction, write, r, c), ...]
for direction, write in actions:
    # print(f"{r=} {c=} {heading=} {direction=}")
    # print(f"    {stack=}")
    if direction == "B":
        prev_heading, prev_write, _, _ = stack.pop()
        heading = rev[prev_heading]
        direction = "F"
        # print(f"    Backtracking: {heading}")
    else:
        heading = m[heading + direction]
        stack.append((heading, write, r, c))

    rs.append(r)
    cs.append(c)

    # print(f"    --> {heading}")
    r += (heading == "S") - (heading == "N")
    c += (heading == "E") - (heading == "W")

[
    max(r for _, _, r, _ in stack),
    min(r for _, _, r, _ in stack),
    max(r for _, _, _, c in stack),
    min(r for _, _, _, c in stack),
]

sorted(set(rs))
sorted(set(cs))

len(set(rs))
len(set(cs))


walls = [
    """ypyeypaseliwioksnaxoxdwaoswsws
lrlhtleasiwtskokaxobanoesesosw
ylrlyeaseiiwkoldxobnidwsenonnn
aearlrsrsswtoldnaiaraisesoynan
enroreeeeotskolorbrbraisenoaea
aeoreveehtwtskoeheiraineneneul
raroreretxiwtwkhtilodbohoynaec
lrlrwheehexiwestslflbohwnehocl
veyegwhenitxthtsdfdolbwseswhoc
ererninnknhtheidolfdflseseswan
rehwgnieriehserbdolflhwheswhna
erwgnigekrirbnkesdsdbrewhwhden
hwgnhgebsenkreibthdolashohside
lvegnigebsbnknnrbessolereoehen
reregniginseeginrabeueuararehi
byehwenigebsbiniaieuecluesareh
bbenhnenigegeginiesececluareri
oraeneeininieininracereclrehxh
ilraibvnengnnnrehlcerhtebibmom
ppwsesebeinnedireslrhtibihmode
ltiwilveeremseheserhtstssxedst
rhteanahyvhisfibeueuhthtiwisie
eiabfkwuoswiahgtoeceohtswdwiwm
rlbbiksreyatoeosbslodrhwdnandu
esotfolemaliopmareulsiwdnandpm
wblttobmlweotliraseuiwdwdwonmu
bxbbeoerasbelpterwsesiwawaitug
odimiiiwodiwhhatstararisiitpmu
ooaepdibsrfkptshxibihehdnaitpo
toalfoeihntlitsbhathxeerdnoiti""",
    """eseswbfincliedefotdadheheaotbe
anyenfefaluifisetoaehrurheahur
eanyoeainclrndenotdngyoueaouou
ulyonaeftaefiesengninourheadyo
eaenaafeftheffisiniwolrloaiygy
cnafinihnheffedidawolalaliwino
lifefndtaeafifededndadndowinif
afehnataepforififnuououawingua
nihtdnaepeotsririnnrnrndalgyou
ifehtdnaerfotorstgrgegrgrnddur
nifihtlirlafotstiygehthegthreh
buinefalerlafotosiehtmomemthre
nbnuniaupeatapopotelmororogegb
bubuoctaehenooeopowmorfrfrogtb
disnnestetfitehposewaoraromoho
innudsehvobrsktisitalmffarfrog
dbdnltorepawalntewawelesfarege
enrdilydyisemkoonalrnslfsrsheg
nbuasilndaeaamneruturrerfleegr
buteifoureptsothnrurnetesearri
uteylyundaeaepoelnrteletesfaou
alisilrdrefthepoefninelelesfai
iglieletriososppataninelslffru
gelblbrrelfpetsdnandninersardn
elbabaitbiletstsdndniletslrfrs
lbakriarebipetotndsewslssrfrew
elbmagitrtbsfefoololbwstffrifo
gemeribitrofehwowofoloeigrgtle
nramstetssfehtsloholoertifikot
mkrarstsstofehtofwfolrtitaoisf""",
    """rartlorgdhedhebzbkttkoteobwsne
bwsneweeirartlorgdhedhebzottek
bttakotebbwsneweeirartlorgdhed
gdhedhebzedtikotesbwsneweeirar
eirartlorgdhedhebzrtttkotetbws
enbwsneweeirartlorgdhedhebzsnt
bznrttkotebbwsneweeirartlorgdh
orgdhedhebzwettkoterbwsneweeir
weeirartlorgdhedhebzoatskotesb
oterbwsneweeirartlorgdhedhebze
hebzhrttkoteebwsneweeirartlorg
tlorgdhedhebzdktskotehbwsnewee
neweeirartlorgdhedhebzsttbkote
tkoteebwsneweeirartlorgdhedheb
edhebzletrkotetbwsneweeirartlo
artlorgdhedhebzsetdkotetbwsnew
wsneweeirartlorgdhedhebzwrtdko
btwkoteabwsneweeirartlorgdhedh
dhedhebzsdtokoterbwsneweeirart
irartlorgdhedhebzgrtlkoteebwsn
tbwsneweeirartlorgdhedhebzwtta
zrsttkoteebwsneweeirartlorgdhe
rgdhedhebzhetdkoteebwsneweeira
eeirartlorgdhedhebzlrtekoterbw
teibwsneweeirartlorgdhedhebzeb
ebzrttbkoteibwsneweeirartlorgd
lorgdhedhebzlrthkotetbwsneweei
eweeirartlorgdhedhebzrwtnkotee
kotebbwsneweeirartlorgdhedhebz
dhebzrhttkoteebwsneweeirartlor
""",
    """rbggbrbeegerbifgbeigeebelfbbbr
ttbieebflerteiilibetgbbggbbtrb
beirbbibbitribibttebiilebiefib
iilbiftiibtbbblbetebietbieibeb
lgrtifebleitiieiigblibbibeeirt
bigtbbtigigibibbligfrbbielbgli
gegebtbbtgibrigiebbielibbebeli
trbbitbeligebbilfbbbittgtgtibb
befbiifbfeettbfeieifiiiitbiebb
libfribbbietrbfiiibbgieigbiftb
fitbtitfbertetbbgbbbbfettifigf
ifbttrfbeflitrfiibgttiliiifttl
rtebeibbgebgifbleteetegblgiebg
tirbreireigbiftitblilttbiliief
eiritbbfrtibtffbbibifeieerebfi
ebifigilebbbebiffblegiigbiebii
bbeblibbefiffbieebettfgibbbter
rligiftbtfltbbtifbrlrrlebebttb
bebbbtgreteiriiiibrebigbbeligg
begibeieibifebebgrtbritbitebie
ebeeiliibgtferbfbifrbtrigbitfb
beflfbiibbbtbiebtriibebtttttgl
ftbbirifbtifeiteeeibebgltegfrt
lrfgbieibifeftiblfbibbibribbie
ibiirilbieefiibirtgbfefpietftf
bblttbbbgribieblfletebtebfeelb
ibbtrbifiigifbbtbrlebletlbtllf
gtegfbbbbrfliigrrbltbgbtbigbgb
bibbeebbltirbiigetileilrtgtrgb
ibrtlibgbtbbebilbitibtigttebib""",
    """tmhereheyrammieeodanieeeececes
mhmlliltoeyhrtdsihesmieeyticir
odanmdhieryshioemdetriedheshyd
rcmidilnritetmontmcicsryoehhdt
meecetiehdiedhymemitrmeortimoe
mmlhitthrciistrhedeersrhhtcmoi
htmishshoieertiiemneihhyhmentd
ahttheyeeordtahlmammlemamcrnee
tddahdrnyohihnhhtmmomelleteecm
ymeeatssiimrldclehylhheoityaie
amcnsaiseeyddcccmmtemhietciieh
ynaeilieyemytlehmteaiahhmarimi
oycmrlrleriethheliisrieihdtttc
mhrlmlmilheteimhteonnmnssdemlh
mryinyedhtaeeeeedsycioadiyeene
teleteremsamhmmiieymientmhhmen
reistmrrhchrtemmeltdtmmtcymhte
shmlttenmhhlmmilamnetteehmlsrt
oytiecsmhtitthhictmthsmehtmein
imsldhostnmhmommhiddhhtardlhmh
taimtnaeetmsestriedhhenntatrry
rrernmeyeheoeemdshmtneeeedlist
eairrteecymhhneeeammersertthet
hlychniirmtneteetheosnaeeiimri
inileirarmhrimmecseeosrmecyeei
edlcemetmetimiirmoiintiyrsemem
eamctmcemmohmeiyeaeheeeishihhy
esiersieieimilyatcssimdsnthsts
lrdesimaalomerdsimimhmylciemed
ysaedhoyitolarmziimiltmnhschtm""",
    """inmmhhahdihtcyemrirrsrlmseimet
enmieshtahmhtihtemrhyrrohecrih
hehncetilmttnieirmdedncyhmsena
tciermihimeiitmtcslcoehreidasm
lrcimmaddtecdehaoieehhemsledel
hemmtitsrhmimmeiemymeeriseieml
lyenhhiicherathiieirmdetosmlel
hlcereoieiaythicmemieecmietiyl
ethmhemrsthtomyemiinemeymmdeee
tlcyemseoamrenrtctmcdolnyhoire
eeremmtlohtoihlehmmdsmmthtcsmr
neanarrtdennmthemstdnmtrmdhete
eeerettcioelisicdteynnrtsmmtil
srottetoealrteadtlmysylmreehci
lmmleteeiiseoeehitccoimimimoyi
ltteatedcsmdyeoehersnaihdieyat
mmmiymemimhirehoheaeimrmieitei
honrmnllsetseoemererttmyheisme
hmoyeimymrreamochtmesthemhtcea
iemoeioinhmhsiooreotldoemaeodh
dtehdhaeetsnhmrrdrdnhlmchimhce
sremidiasdyilernancerheecemhei
tllomiiilaohsetaecerneerdmlrii
hoeyhnmhmnmhaoserneteeiricmeet
trthmrimmhhildcsdtyemetidyhiei
ymditdcacittsmimyiacmmmirirenn
tseedeseeehhisletcmtdcisiencht
meeimedothrootsimelmhehycmiyhc
yoedeodnhotlatmdereceteimehsim
nnmytthmmheeoneeohdirltatcemeh""",
]
#                ^

# north, north, west, south, west, north

# wall_lines = wall.splitlines()
# (len(wall_lines), len(wall_lines[0]))

grid = [row1 + row2 for row1, row2 in zip(walls[0].splitlines(), walls[1].splitlines())]

r = 30
c = 47
# stack[0] = (None, *stack[0][1:])
result = []
for (
    heading,
    write,
    _,
    _,
) in stack:
    print(f"{heading=} {write=}")
    if heading:
        r += (heading == "S") - (heading == "N")
        c += (heading == "E") - (heading == "W")
    ch = grid[r][c]
    print(f"{heading=} {write=} {ch=}", flush=True)
    result.append(write.replace("l", ch).replace("L", ch.upper()))
    # print(f"{grid[r][c]}", end="")

print("".join(result))

# grid[r][c - 3 : c + 3]
# "It would be ... forty-eight rooms to the right, from the left edge."

# "That would be column eighteen on the second wall here. Starting at the bottom?"


@decrypter.decrypter(chapter=78)
def decrypt(cipher: str) -> str:
    return decrypter.vigenere_cipher(cipher, "saydrletmeinimhomethrice")


# import itertools
# import decrypter

# dec = decrypter.decrypter(chapter=78)(lambda x: x)
# ciphertext = dec.decrypt_one_chapter()[:5000]

# # key = "saydrletmein;m\\om_5hridesaydr_etmeini hom_thriceLaydr_et =iBimhom=thrice"
# # key = "saydrletmeinimhXthrice"
# # key = "saydrletmeinimhotoutsXXXXXXXXXXXXXXXXXXXidethriceLaydr_et =iBimhom=thrice"
# # key = "saydrletmeinimhotoutside"
# # ke= "saydrletmein;m|om_5hridesaydr_etmeini hom_thriceLaydr_et =iBimhom=thrice"
# #     thriceLaydr_et =iBimhom=thrice
# # y = "saydrletmein;m\\om_5hridesaydr_etmeini hom_thriceLaydr_et =iBimhom=thrice"


# key = "saydrletmeinimhomethrice"

# plain = decrypter.vigenere_cipher(ciphertext, key)

# # print(plain)
# print(plain[:500])

# for a, b in zip(plain[:50], itertools.cycle(key)):
#     print(a, b)

# alphabet = """0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,?!:;'"-()[]{}|+=%/\\*#$_ \n"""
# have, want, key = "$Dt"
# alphabet[
#     (alphabet.index(have) - (alphabet.index(want) - alphabet.index(key)))
#     % len(alphabet)
# ]


# import decrypter
# from decrypter import vigenere_breaker

# reference_text = []
# for chapter in range(78):
#     with open(f"data/{chapter:02}.chp") as f:
#         reference_text.append(f.read())
# reference_text = "".join(reference_text)

# ciphertext = decrypter.decrypter(78)(lambda x: x).decrypt_one_chapter()

# result = vigenere_breaker.break_vigenere_cipher(
#     ciphertext[:10000],
#     reference_text,
#     decrypter_func=decrypter.vigenere_cipher,
#     key_chars=vigenere_breaker.ALPHABET,
#     max_key_length=300,
#     verbose=True,
# )
