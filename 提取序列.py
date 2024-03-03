#coding:utf-8
from Bio import SeqIO
from tqdm import tqdm
def main(fastafile="test.fasta",idfile="ids.txt",outfile= "output.fasta"):
    with open(idfile) as id_handle:
        wanted = set(line.rstrip("\n").split(None,1)[0] for line in id_handle)
    print("Found %i  ids in %s" % (len(wanted), idfile))
    sum = (r for r in tqdm(SeqIO.parse(fastafile, "fasta")) if r.id in wanted)
    sum = SeqIO.write(sum, outfile, "fasta")
    print("Saved %i records from %s to %s" % (sum, fastafile, outfile))
    if sum < len(wanted):
        print("Warning %i IDs not found in %s" % (len(wanted)-sum, fastafile))
if __name__ == '__main__':
    main()
#1.8G数据 1:27