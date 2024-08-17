def getDynamicRows(rowLength: int):
    if rowLength < 10:
        return rowLength
    elif rowLength >= 10:
        return 10
