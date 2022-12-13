puzzle_input = open("puzzle_input.txt", "r", encoding="utf8").readlines()

def get_to_storage_pointer(storage, pointer):
    directory = ""

    pointer_split = pointer.split("/")
    if pointer_split == "":
        return storage
    else:
        for fragment in pointer_split:
            directory += f"[{fragment}]"
        return eval("storage"+directory)

storage_pointer = ""
storage = {}
for line in puzzle_input:
    line = line.strip()
    splitted = line.split(" ")
    if line == "$ cd /":
        storage_pointer = "/"
    if splitted[0] == "$" and splitted[1] == "cd":
        storage_pointer += "/"+splitted[2]
        storage = get_to_storage_pointer(storage, storage_pointer)
    if "$" not in splitted:


