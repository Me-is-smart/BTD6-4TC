def find4tc(tower1, tower2, tower3, tower4):
    """
    Accepts 4 towers as input and prints out all combos that contain them, as
    well as the number of combos that contain them.

    :param tower1: str
    :param tower2: str
    :param tower3: str
    :param tower4: str

    HOW TO USE
    ----------

    Open a Python interpreter and import this file. To search a combo, use the
    following format:

        find4tc("tower1", "tower2", "tower3", "tower4")

    You may search for 1, 2, or 3 towers by using their respective methods
    below, or by filling in "" for each parameter that isn't used here.
    """

    fileread = open("remaining-combos.txt", "r")
    lines = fileread.readlines()
    combos = 0
    for line in lines:
        if (tower1 in line and tower2 in line
                and tower3 in line and tower4 in line):
            printed_line = line.strip("\n")
            print(printed_line)
            combos += 1
    if combos == 1:
        print(f"There is 1 combo left.")
    else:
        print(f"There are {combos} combos left.")


def find3tc(tower1, tower2, tower3):
    """
    Accepts 3 towers as input and prints out all combos that contain them, as
    well as the number of combos that contain them.

    :param tower1: str
    :param tower2: str
    :param tower3: str

    Functionally the same as find4tc but with a different number of towers.
    """

    find4tc(tower1, tower2, tower3, "")


def find2tc(tower1, tower2):
    """
    Accepts 2 towers as input and prints out all combos that contain them, as
    well as the number of combos that contain them.

    :param tower1: str
    :param tower2: str

    Functionally the same as find4tc but with a different number of towers.
    """

    find4tc(tower1, tower2, "", "")


def find1tc(tower1):
    """
    Accepts 1 tower as input and prints out all combos that contain it, as well
    as the number of combos that contain it.

    :param tower1: str

    Functionally the same as find4tc but with a different number of towers.
    """

    find4tc(tower1, "", "", "")
