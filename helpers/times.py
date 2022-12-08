
def create_file(base: int = 1, lists: bool = False, up_to: int = 10):
    try:
        output = ""
        for time in range(up_to):
            output += f" {base} x {time} = {base*time}\n"

        if lists:
            print('===================')
            print(f"{base} Times Table ")
            print('===================')
            print(output)

        with open(f"{base}-times-table.txt", 'w') as f:
            f.write(output)

        return f"{base}-times-table.txt created"

    except TypeError:
        return f"{base}-times-table.txt was not created"