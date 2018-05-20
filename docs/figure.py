#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randn
import matplotlib as mpl
mpl.rcParams['font.family'] = 'Helvetica Neue'
import prettyplotlib as ppl
from prettyplotlib import brewer2mpl

np.random.seed(64)

set2 = brewer2mpl.get_map('Set2', 'qualitative', '8').mpl_colors
color1, color2, color3, color4, color5 = set2[0], set2[1], set2[2], set2[3], set2[4]

set3 = brewer2mpl.get_map('Set2', 'qualitative', '5').mpl_colors
color6, color7, color8, color9, color10 = set3[0], set3[1], set3[2], set3[3], set3[4]

p1 = brewer2mpl.get_map('Paired', 'Qualitative', 5).mpl_colors
c1, c2, c3, c4, c5 = p1[0], p1[1], p1[2], p1[3], p1[4]

p2 = brewer2mpl.get_map('Paired', 'Qualitative', 8).mpl_colors
c6, c7, c8, c9, c10 = p2[0], p2[1], p2[2], p2[3], p2[4]

p3 = brewer2mpl.get_map('Paired', 'Qualitative', 6).mpl_colors # standard
c11, c12, c13, c14, c15 = p3[0], p3[1], p3[2], p3[3], p3[4]

p4 = brewer2mpl.get_map('Pastel1', 'Qualitative', 6).mpl_colors
c16, c17, c18, c19, c20 = p4[0], p4[1], p4[2], p4[3], p4[4]

def main():
    n_groups = 4
    #variance1 = np.array([0,0,0,0.01027])
    #variance2 = np.array([0,0,0,0.01051])
    list1 = np.array([0,0,4.2,0])
    list2 = np.array([0,0,6.4,0])
    
    fig, ax = plt.subplots()  
    index = np.arange(n_groups)
    width = 0.5
    opacity   = 0.4  

    # color example: r,g,c,cyan
    rects1 = ax.bar(index, list1, width, color='#63B8FF', align='center', alpha=opacity, hatch='/')
    rects2 = ax.bar(index+width, list2, width, color='#FF0000', align='center', alpha=opacity)

    #plt.xlabel('', size=25)
    #plt.ylabel('', size=25)
    ax.set_xticks(index+width/2)
    ax.set_xticklabels((' ',' ',' ',' '))
    #plt.yticks(fontsize=18)  #change the num axis size
    #plt.ylim(0,1.5)  #The ceil
    plt.legend()  
    plt.tight_layout()
    plt.ylim(0,10)
    plt.show()

if __name__ == '__main__':
    main()
