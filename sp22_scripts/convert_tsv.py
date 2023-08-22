# change the path above to whatever

def convert_tsv(pathname):
    with open(pathname + '.txt') as fin, open(pathname + '.tsv', 'w') as fout:
    #to have data in separate columns from a single column
        for line in fin:
            #fout.write(line.replace(' ', '\t'))
            l = line.split()
            u = l[0]
            v = l[1]
            value = l[2]
            fout.write(str(u) + "\t" + str(v) + "\t" + "1082441188" + "\t" + str(value) + "\n")

convert_tsv('tiles/datasets/moreno_train/out.moreno_train_train')