def fruit(target_fun):
    target_fun()
    if not add_fruit:
        return
    print("apple")


@fruit
def banana(add_fruit=False):
    print("banana")
    return add_fruit


if __name__ == '__main__':
    banana()
