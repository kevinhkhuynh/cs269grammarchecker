
import sys
import argparse

import string
import itertools
from os import path

def main(arguments):

    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-s', '--source', help="The source file.")    
    parser.add_argument('-t', '--target_file', help="The target file.")
    
    args = parser.parse_args(arguments)
    
    source_file = args.source
    target_file = args.target_file
    
    with open(source_file) as f:
        src_content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    src_content = [x.strip() for x in src_content]
    
    with open(target_file) as f:
        tgt_content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    tgt_content = [x.strip() for x in tgt_content]

    tp = 0;
    fp = 0;
    fn = 0;
    for src_line, tgt_line in zip(src_content, tgt_content):
        print src_line
        print tgt_line
        src_txt = src_line.split()
        tgt_txt = tgt_line.split()
        it_src = iter(src_txt)
        it_tgt = iter(tgt_txt)
        try:
            src_token = next(it_src)
        except StopIteration:
            fn += 1
            pass # exhausted the iterator
        try:
            tgt_token = next(it_tgt)
        except StopIteration:
            fp += 1
            pass # exhausted the iterator
        try:
            while True: # or some secondary break condition other than StopIteration
                if src_token == '<' and tgt_token == '<':
                    src_token = next(it_src);
                    tgt_token = next(it_tgt);
                    if (src_token == 'ins' and tgt_token == 'ins') or (src_token == 'del' and tgt_token == 'del'):
                        tp += 1
                    else:
                        print "src =", src_token
                        print "tgt =", tgt_token
                        fp += 1
                        fn += 1
                    while True:
                        src_token = next(it_src)
                        tgt_token = next(it_tgt)
                        if src_token == '<':
                            break
                    for i in range(1,3):
                        src_token = next(it_src)
                        tgt_token = next(it_tgt)
                elif src_token == '<':
                    while True:
                        for i in range(1,9):
                            src_token = next(it_src)
                        if src_token != '<':
                            break
                        tgt_token = next(it_tgt)
                    print "src =", src_token
                    print "tgt =", tgt_token
                    fp += 1
                elif tgt_token == '<':
                    while True:
                        for i in range(1,9):
                            tgt_token = next(it_tgt)
                        if tgt_token != '<':
                            break
                        src_token = next(it_src)
                    fn += 1
                    print "src =", src_token
                    print "tgt =", tgt_token
                    srcprev = True
                else:
                    src_token = next(it_src)
                    tgt_token = next(it_tgt)
        except StopIteration:
            pass # exhausted the iterator
    print tp, fp, fn
    try:
        precision = float(tp) / (tp + fp)
    except ZeroDivisionError:
        precision = 0.0
    try:
        recall = float(tp) / (tp + fn)
    except ZeroDivisionError:
        recall = 0.0
    try:
        f1 = 2 * (precision * recall) / (precision + recall)
    except ZeroDivisionError:
        f1 = 0.0
    print "precision =", precision
    print "recall =", recall
    print "f1 =", f1

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

