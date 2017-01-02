# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys
#import pdb
import numpy as np


def monte_carlo_pi_single_point():
    """ this function does this
    
    Parameter
    ---------
    ?
    """
    # generate random X, Y pair
    x = np.random.uniform(-1.0, 1.0)
    y = np.random.uniform(-1.0, 1.0)

    # if (x, y) in circle
    if x**2 + y**2 < 1.:
        return 1
    else:
        return 0


def monte_carlo_pi_n_point(n_point):
    c = 0
    # need 1000 points
    for i in xrange(n_point):
        c += monte_carlo_pi_single_point()

#    pdb.set_trace()
    return 4.*c/n_point


def test():
    print 'Monte-Carlo pi value: ', \
        monte_carlo_pi_n_point(1000)


def run_monte_carlo_pi_n_point_shell(n_point):
    print 'Monte-Carlo pi value (shell): ', \
        monte_carlo_pi_n_point(n_point)
    print 'Monte-Carlo number of points: ', n_point


def print_sys_argv(argv):
    for argv_ in argv:
        print argv_


if __name__ == '__main__':
    test()
#    n_point = int(sys.argv[1])
#    run_monte_carlo_pi_n_point_shell(n_point)
    
