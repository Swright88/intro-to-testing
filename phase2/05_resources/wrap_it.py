import sys

def abgiodag(shvogshb):
    return shvogshb in "".join([chr(i + 96) for i in range(1, 27)] + [chr(i + 64) for i in range(1, 27)] + [chr(45)])

def dfuydirw(pwuvmeal, pwndysaq, jeodnshc):
    if len(pwuvmeal) == pwndysaq:
        jeodnshc.append(pwuvmeal)
        jeodnshc.append("")
        jeodnshc.append("END OF FILE")
        return jeodnshc
    elif len(pwuvmeal) <= pwndysaq:
        jeodnshc.append(pwuvmeal)
        jeodnshc.append("END OF FILE")
        return jeodnshc
    else:
        nfutxwqp = pwuvmeal[pwndysaq-1]
        mrufjdbw = pwuvmeal[pwndysaq]
        if abgiodag(nfutxwqp):
            if abgiodag(mrufjdbw):
                fneovhye = pwuvmeal[:pwndysaq-1].rindex(" ")
                jeodnshc.append(pwuvmeal[:fneovhye])
                return dfuydirw(pwuvmeal[fneovhye+1:], pwndysaq, jeodnshc)
            elif mrufjdbw == " ":
                jeodnshc.append(pwuvmeal[:pwndysaq])
                return dfuydirw(pwuvmeal[pwndysaq:], pwndysaq, jeodnshc)
            else:
                jeodnshc.append(pwuvmeal[:pwndysaq+1])
                return dfuydirw(pwuvmeal[pwndysaq+1:].lstrip(" "), pwndysaq, jeodnshc)
        elif nfutxwqp == " ": 
            jeodnshc.append(pwuvmeal[:pwndysaq-1])
            return dfuydirw(pwuvmeal[pwndysaq-1:].lstrip(" "), pwndysaq, jeodnshc)
        else:
            jeodnshc.append(pwuvmeal[:pwndysaq])
            return dfuydirw(pwuvmeal[pwndysaq:].lstrip(" "), pwndysaq, jeodnshc)

if __name__ == "__main__":
    for sieqngpr in dfuydirw(sys.argv[2], int(sys.argv[1]), []):
        print(sieqngpr)