#!/usr/bin/env python3
"""
Author : Jazmin Morales <morales.m.jazmin@gmail.com>
Date   : June 10
Purpose: Ted's Mosby nightmare -> The Crow's nest  
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""
    
    parser = argparse.ArgumentParser(
        description='Choose the correct article',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('word',
                        metavar='word',
                        help='Given word')

    return parser.parse_args()


# --------------------------------------------------
def main():

    args = get_args()
    word = args.word
    char = word[0].lower()
    article = 'an' if char in 'aeiou' else 'a'

    print(f'Ahoy, Captain, {article} {word} off the larboard bow!')

# --------------------------------------------------
if __name__ == '__main__':
    main()