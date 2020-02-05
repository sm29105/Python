MESSAGE = "%d: Move tile from '%s' to '%s'"

def hanoi_do(frm, tmp, tgt, count, steps):
    if count == 1:
        steps.append((frm, tgt))
    else:
        hanoi_do(frm, tgt, tmp, count - 1, steps)
        steps.append((frm, tgt))
        hanoi_do(tmp, frm, tgt, count - 1, steps)

def hanoi(frm, tmp, tgt, count):
    steps = []
    hanoi_do(frm, tmp, tgt, count, steps)
    return steps

def hanoi_print(steps):
    for index, step in enumerate(steps):
        messageTuple = (index + 1,) + step
        print(MESSAGE % messageTuple)

hanoi_print(hanoi("Left", "Middle", "Right", 5))