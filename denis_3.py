db_info = {}

db_name = []


def informsing(text_info):
    text_info = list(text_info)
    print(text_info)
    id_1 = text_info.index(" ")
    text_info[id_1] = "_"
    try:
        text_info.index(" ")
        id_2 = text_info.index(" ")
        text_info[id_2] = "-"
        try:
            text_info.index(" ")
            id_3 = text_info.index(" ")
            text_info[id_3] = "*"
            text_info = "".join(text_info)
            command_i = text_info[0: id_1]
            name1_i = text_info[id_1 + 1: id_2]
            name2_i = text_info[id_2 + 1: id_3]
            sum_i = text_info[id_3 + 1: len(text_info)]
        except:
            text_info = "".join(text_info)
            command_i = text_info[0: id_1]
            name1_i = text_info[id_1 + 1: id_2]
            sum_i = text_info[id_2 + 1: len(text_info)]
            name2_i = 0
    except:
        text_info = "".join(text_info)
        command_i = text_info[0: id_1]
        if command_i == "BALANCE":
            sum_i = 0
            name1_i = text_info[id_1 + 1: len(text_info)]
        elif command_i == "INCOME":
            sum_i = text_info[id_1 + 1: len(text_info)]
            name1_i = 0
        name2_i = 0

    return command_i, int(sum_i), name1_i, name2_i


def infoname(name, db_info, db_name):
    try:
        db_info[name]
    except:
        db_info[name] = 0
        db_name.append(name)

    return db_info, db_name


def BALANCE(name, db_info):
    try:
        print(db_info[name])
    except:
        print("Error")


def DEPOSIT(name, sum, db_info):
    db_info[name] += sum
    return db_info


def WITHDRAW(name, sum, db_info):
    db_info[name] -= sum
    return db_info


def TRANSFER(name1, name2, sum, db_info):
    db_info[name1] -= sum
    db_info[name2] += sum
    return db_info


def INCOME(sum, db_info, db_name):
    i = 0
    while i < len(db_info):
        if db_info[db_name[i]] > 0:
            db_info[db_name[i]] += int(db_info[db_name[i]] / 100 * sum)
        i += 1

    return db_info


cmd = True
while cmd:
    text_info = input(": ")
    if text_info == "quit":
        break
    command_i, sum_i, name1_i, name2_i = informsing(text_info)
    print(command_i, sum_i, name1_i, name2_i)
    if command_i == "BALANCE":
        BALANCE(name1_i, db_info)
    elif command_i == "INCOME":
        db_info, db_name = infoname(name1_i, db_info, db_name)
        db_info = INCOME(sum_i, db_info, db_name)
    elif command_i == "DEPOSIT":
        db_info, db_name = infoname(name1_i, db_info, db_name)
        db_info = DEPOSIT(name1_i, sum_i, db_info)
    elif command_i == "WITHDRAW":
        db_info, db_name = infoname(name1_i, db_info, db_name)
        db_info = WITHDRAW(name1_i, sum_i, db_info)
    elif command_i == "TRANSFER":
        db_info, db_name = infoname(name1_i, db_info, db_name)
        db_info, db_name = infoname(name2_i, db_info, db_name)
        db_info = TRANSFER(name1_i, name2_i, sum_i, db_info)
    print(db_name)
