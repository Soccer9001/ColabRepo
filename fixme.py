import glob


for n in range(81):
    correct_number = str(n)
    txt_files = glob.glob("images/" + correct_number + "/*.txt")
    for x in txt_files:
        with open(x) as f:
            lines = f.readlines()
            full_txt = ""
            for vx in range(len(lines)):
                c = 0
                while lines[vx][c] != " ":
                    c += 1
                full_txt += correct_number + lines[vx][c:]
        with open(x, "w") as f:
            with open('file.txt', 'w') as file:
                f.write(full_txt)
