def comma_list():
    pars_csv = []
    with open("comma.txt", "r") as f:
        for line in f:
            if line and not line.startswith("#"):
                line = line.strip()
                pars_csv.append(line.split(" "))
    print(pars_csv)

comma_list()

