def hanoi(frm, tmp, target, count):
    if count == 1:
        print ("Move tile from '" + frm + "' to '" + target + "'")
    else:
        hanoi(frm, target, tmp, count - 1)
        print ("Move tile from '" + frm + "' to '" + target + "'")
        hanoi(tmp, frm, target, count - 1)

hanoi("The Left Pile", "Middle Pile", "The Right Pile", 7)