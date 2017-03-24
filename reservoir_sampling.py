#!/usr/local/bin/python3

# ML310
# Brandon Aleson
# 1/27/17
# Implement reservoir sampling on gyro data found here:
# http://www.nxp.com/files-static/global_support_files/Nudge.txt


import pandas
import csv
from random import randint


def reservoir(stream, k):
    '''
    Populate sample space with first k items from stream. For remaining items in stream,
    choose a random number j from 0 to item's index. If j is less than k, replace
    jth element in sample with ith element from stream
    '''
    sample = stream[0:k]

    for i in range(k, len(stream)):
        j = randint(0, i + 1)
        if j < k:
            sample[j] = stream[i]

    return sample


def print_to_file(sample):
    '''code to print results to file for submission'''
    output_file = 'reservoir_output.csv'

    with open(output_file, 'w') as out:
        csv_out = csv.writer(out)
        csv_out.writerow(['MagX', 'MagY'])
        for item in sample:
            csv_out.writerow([item[0], item[1]])


if __name__ == '__main__':
    # create dataframe from data
    nudge = pandas.read_table('nudge.txt', delim_whitespace=True)

    # create a list of tuples to prepare it for sampling
    mags = [item for item in zip(nudge['MagX'], nudge['MagY'])]

    # k=20 here
    samples = reservoir(mags, 20)

    print_to_file(samples)
