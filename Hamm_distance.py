import math
import argparse

parser = argparse.ArgumentParser(description="Write sequences as text input for the two sequences to compare.")
parser.add_argument('--Sequence_1', '-s1', type=str, 
                    metavar='', required=True, 
                    help='Type in sequence - not FASTA just raw bases.' )
parser.add_argument('--Sequence_2', '-s2', type=str, 
                    metavar='', required=True, 
                    help='Type in sequence - not FASTA just raw bases.' )
parser.add_argument('-F', '--FileMode', action='store_true', required=False, help='Set file mode.')
args = parser.parse_args()

def Hamming_calc(input1, input2):
    Hamming_distance = 0
    loop = 0
    try:
        for i in input1:
            if i != input2[loop]:
                Hamming_distance += 1
                loop += 1
            else:
                loop += 1
    except Exception as e:
        print("Error with input, try writing the sequence as raw bases e.g AACGAATT ")

    else: print(f'The Hamming distance is {Hamming_distance}')

if __name__ == '__main__':
    if args.FileMode:
        with open(args.Sequence_1) as f:
            seq1 = f.read().replace('\n', '')
            print(seq1)
        with open(args.Sequence_2) as f:
            seq2 = f.read().replace('\n', '')
            print(seq2)
        Hamming_calc(seq1, seq2)
    else:
        Hamming_calc(args.Sequence_1, args.Sequence_2)