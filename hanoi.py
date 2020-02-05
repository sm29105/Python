def hanoi(frm, tmp, target, count):
    if count == 1:
        print ("Move from '" + frm + "' to '" + target + "'")
    else:
        hanoi(frm, target, tmp, count - 1)
        print ("Move from '" + frm + "' to '" + target + "'")
        hanoi(tmp, frm, target, count - 1)

hanoi("Left", "Middle", "Right", 8)