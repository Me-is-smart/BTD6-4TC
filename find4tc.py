def find4tc(*towers):
    """
    Accepts up to 4 towers as input and prints out all combos that contain
    them, as well as the number of combos that contain them.

    :param towers: The towers in the requested combo.

    HOW TO USE
    ----------

    Open a Python interpreter and import this file. To search a combo, use the
    following format:

        find4tc("tower1", "tower2", "tower3", "tower4")
        find4tc("tower1", "tower2", "tower3")

    """

    fileread = open("remaining-combos.txt", "r")
    lines = fileread.readlines()
    combos = 0
    for line in lines:
        matches = True
        for tower in towers:
            if tower not in line:
                matches = False
        if matches:
            printed_line = line.strip("\n")
            print(printed_line)
            combos += 1
    if combos == 1:
        print(f"There is 1 combo left.")
    else:
        print(f"There are {combos} combos left.")