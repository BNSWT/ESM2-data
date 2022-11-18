from typing import Tuple, Sequence

def write_single_sequence(path, tag, sequence):
    with open(path, "a") as fp:
        fp.write(tag+'\n')
        fp.write(sequence+'\n\n')

def parse_fasta(fasta_string: str) -> Tuple[Sequence[str], Sequence[str]]:
    """Parses FASTA string and returns list of strings with amino-acid sequences.

    Arguments:
        fasta_string: The string contents of a FASTA file.

    Returns:
        A tuple of two lists:
        * A list of sequences.
        * A list of sequence descriptions taken from the comment lines. In the
            same order as the sequences.
    """
    tags = []
    sequences = []
    index = -1
    for line in fasta_string.splitlines():
        line = line.strip()
        if line.startswith(">"):
            index += 1
            tags.append(line[1:])  # Remove the '>' at the beginning.
            sequences.append("")
            continue
        elif line.startswith("#"):
            continue
        elif not line:
            continue  # Skip blank lines.
        sequences[index] += line

    return sequences, tags