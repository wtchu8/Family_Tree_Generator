# generate family tree

import os
import argparse

import pandas as pd

from person import Person

class FamilyTree():
    def __init__(self,filename):
        """initalize"""
        self.filename = filename

        self.data_df = pd.read_csv(self.filename)

        self.tree = []

    def add_member(self, fname, lname, **kwargs):
        self.tree.append(Person(fname, lname, **kwargs))

    def build_tree(self):
        """build tree from data frame"""
        
        for index, row in self.data_df.iterrows():
            print(row['fname'])

    def print_tree(self):
        """print tree to termainal"""
        print('this is the tree: <<<<---')

def main():
    """main"""
    parser = argparse.ArgumentParser(description='Build family tree object')

    parser.add_argument('-c', '--config',required=True,help='yaml containing run parameters')

    args = parser.parse_args()

if __name__ == "__main__":
    main()