def clean_word(word):
    word = word.replace(",", "")
    word = word.replace("`", "")
    word = word.replace("’", "")
    word = word.replace("?", "")
    word = word.replace("!", "")
    word = word.replace("\n", "")
    word = word.replace(".", "")
    word = word.replace(":", "")
    word = word.replace(";", "")
    word = word.replace("'", "")
    word = word.lower().strip()
    return word


with open("data/aceventura.txt", 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

# Word counts
word_counts = {}

for line in lines:
    words = line.split(" ")
    for word in words:
        word = clean_word(word)
        if word and word in word_counts.keys():
            word_counts[word] = word_counts[word] + 1
        else:
            word_counts[word] = 1

for key, value in word_counts.items():
    # print(f"word {key} count {value}")
    pass


top_10 = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]

print("Sorted")
for key, value in top_10:
    print(f"word {key} count {value}")

# Character names

characters = set()
ignore_list = ["DISSOLVE", "END", "FIRST", "COUNTY", "EXT.", "INT.", "CONT'D", "DAY", "NIGHT", "CUT", "MUSIC", "MESSAGE", "WHERE", "CLOSE", "MUSIC", "DON'T", "EEEEE", "AAAAA", "TONSIL", "DISOLVE", "GOD", "BURNOUT", "ONE", "OUT", "SNOW", "RIDDLE", "SEARCH", "PICTURE", "FIND", "ANGLE", "WELCOME", "LOOSER", "LOSER", "HUT", "SCREEN", "ROLL", "URGH", "DISOLVE", "LOO", "COME", "BLUE", "HERR", "SUCKS", "TRAINER", "DESK", "!!", "GUN", "THERE", "NICE"]

for line in lines:
    line = line.strip()
    if line and line.upper() == line:
        ignore = False

        for ignore_word in ignore_list:
            if line.find(ignore_word) != -1:
                ignore = True
                break
        if not ignore:
            characters.add(line.upper().strip())

print("Characters")
for character in characters:
    print(character)

lines_per_character = {}

print("Lines per character")

def contains_character(line):
    if not line:
        return False
    for character in characters:
        if line.find(character):
            return True
    return False

for line in lines:
    line = line.strip()
    current_chr = None
    if contains_character(line):
        if line in lines_per_character.keys():
            current_chr = line
            continue
        else:
            lines_per_character[line] = 0
    else:
        if current_chr:
            lines_per_character[current_chr] = lines_per_character[current_chr] + 1

for key, value in lines_per_character:
    print(f"Character: {key} lines {value}")




