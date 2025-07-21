def filename_sorter(filenames: list[str], repeated: str):
    """returns a sorted copy of the original array"""
    linker = {}

    try:
        output = []
        for filename in filenames:
            index = filename[len(repeated):].split(".")[0]

            output.append(int(index))
            linker[index] = filename
    except:
        raise ValueError("Invalid filename format provided")
    
    output.sort()
    for i in range(len(output)):
        output[i] = linker[str(output[i])]
    
    return output