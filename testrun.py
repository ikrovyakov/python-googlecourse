# import sys


def countMultiples(l, max):
    """Given an input of a list of numbers and a high number,
    return the number of multiples of each of those numbers that are less than the maximum number.
    For this case the list will contain a maximum of 3 numbers that are all relatively prime to each other."""
    num = 0
    for i in range(0,len(l)):
        num += (max-1) // l[i]
        print '%d of %d in %d' % ((max-1) // l[i],l[i],max)
        if i>0:
            for j in range(0,i):
                num -= (max-1) // (l[i]*l[j])
                print 'Subtracting %d of %d * %d in %d' % ((max-1) // (l[i]*l[j]), l[i], l[j], max)
    return num


def main():
    print countMultiples([13, 35, 47], 389560)
    return


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
