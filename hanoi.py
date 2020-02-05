def hanoi(frm, tmp, target, count):
    if count == 1:
        print (frm + " -> " + target)
    else:
        hanoi(frm, target, tmp, count - 1)
        print (frm + " -> " + target)
        hanoi(tmp, frm, target, count - 1)

hanoi("Left", "Middle", "Right", 8)