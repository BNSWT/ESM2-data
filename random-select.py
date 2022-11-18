import argparse
import random
from pyfaidx import Fasta
from utils import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "uniref50_dir", type=str,
        help="Path to Uniref50 database"
    )
    parser.add_argument(
        "validation_dir", type=str,
        help="Path to validation dataset"
    )
    parser.add_argument(
        "train_dir", type=str,
        help="Path to training dataset"
    )
    args = parser.parse_args()
    
    random.seed(4)

    uniref50=Fasta(args.uniref50_dir)
    u50_len = len(uniref50.keys())

    validation_index = random.sample(range(u50_len), 2)

    for index in range(u50_len):
        tag = uniref50[index].long_name
        if index == 0:
            tag = '>'+tag
        sequence = uniref50[index][:].seq
        if index in validation_index:
            write_single_sequence(args.validation_dir, tag, sequence)
        else:
            write_single_sequence(args.train_dir, tag, sequence)