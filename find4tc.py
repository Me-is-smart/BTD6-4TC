def find4tc(tower1, tower2, tower3, tower4):
    """
    Parameters:
        - tower1, tower2, tower3, tower4: Names of towers. TOWER NAMES MUST
        HAVE THEIR FIRST LETTER CAPITALIZED AND OTHER LETTERS LOWERCASE.

    Returns: None

    HOW TO USE:

    Open a Python interpreter and import this file. To search a combo, use the
    following format:

        find4tc("tower1", "tower2", "tower3", "tower4")

    If you want to search for all combos that contain only 2 or 3 towers, you
    MUST keep 4 sets of quotes. Use "" for unused tower slots.
    """
    fileread = open("remaining-combos-updated.txt", "r")
    lines = fileread.readlines()
    combos = 0
    for line in lines:
        if (tower1 in line and tower2 in line
                and tower3 in line and tower4 in line):
            printed_line = line.strip("\n")
            print(printed_line)
            combos += 1
    print(f"There are {str(combos)} combos left.")