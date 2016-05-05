# import sys
import logging


def countMultiples(l, max):
    """Given an input of a list of numbers and a high number,
    return the number of multiples of each of those numbers that are less than the maximum number.
    For this case the list will contain a maximum of 3 numbers that are all relatively prime to each other."""
    num = 0
    logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
                        level=logging.INFO)
    logger = logging.getLogger("countMultiples")
    logger.info('countMultiples started with following parameters: {0}, {1}'.format(l, max))
    for i in range(0, len(l)):
        num += (max-1) // l[i]
        logger.info('    {0} of {1} in {2}'.format((max-1) // l[i], l[i], max))
        if i > 0:
            for j in range(0, i):
                num -= (max-1) // (l[i] * l[j])
                logger.info('    Subtracting {0} of {1} * {2} in {3}'.format((max-1) // (l[i] * l[j]), l[i], l[j], max))
    logger.info('countMultiples result: {0}'.format(num))
    return num


def main():
    countMultiples([13, 35, 47], 389560)
    return


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
