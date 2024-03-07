def main():
    emoji={"duck":"🐥", "python":"🐍", "monkey":"🙈🙉🙊", "dog":"🐶", "cat":"🙀"}

    print(emoji)
    # accessing item by its key
    print(emoji["duck"])
    animal = emoji.get("cat")
    print(animal)

    # get the keys
    print(emoji.keys())

    # get the values
    print('\n\n')
    print(emoji.values())

    # get the key value pair
    print('\n\n')
    print(emoji.items())

    if "duck" in emoji:
        print(emoji["duck"])

    emoji["duck"] ="🦆"
    print(emoji["duck"])

    emoji.update({"racoon":  "🦝"})

    emoji.pop("cat")
    print(emoji)

    del emoji["duck"]
    print(emoji)

    # print values
    for x in emoji:
        print(emoji[x])

dictionary= {}

main()