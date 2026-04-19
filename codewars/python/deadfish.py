def parse(data):
    result = 0

    for char in data:
        if char == "i":
            result += 1
        elif char == "d":
            result -= 1
        elif char == "s":
            result = result**2
        elif char == "o":
            yield result
