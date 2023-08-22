    # write script that generates a 'sample graph' consisting of only disjoint k3's or k4's and test output DONE
    # try to figure out what exactly is going in in "merge" -> email author about if the code is actually merging communities?
    # -> downloaded your code, experimenting with incrasing core sizes, looked at code and doesn't seem like merging communities, found a lot of shared vertices in communities
    # -> communities_to_remove (?)
    # Play around with increasing community core no. above 4 (5? 10? 20?)
    # replication study with facebook wall data https://socialnetworks.mpi-sws.org/data-wosn2009.html -> collect communities from the TILES code, not txt file, would be easier?
    # play around with source code to get merged communities in a better format to read in and analyze

import csv 

def write_k3s():
    # random timestamp
    timestamp = 1082441188; 
    with open('k3_communities.tsv', 'w', newline='') as tsvfile:
        writer = csv.writer(tsvfile, delimiter='\t', lineterminator='\n')
        # generate 1000 k3's
        for i in range(1000):
            p_1, p_2, p_3 = i * 3, i * 3 + 1, i * 3 + 2
            writer.writerow([p_1, p_2, timestamp])
            writer.writerow([p_2, p_3, timestamp])
            writer.writerow([p_3, p_1, timestamp])

def write_k4s():
    timestamp = 1082441188; 
    with open('k4_communities.tsv', 'w', newline='') as tsvfile:
        writer = csv.writer(tsvfile, delimiter='\t', lineterminator='\n')
        # generate 1000 k4's
        for i in range(1000):
            p_1, p_2, p_3, p_4 = i * 4, i * 4 + 1, i * 4 + 2, i * 4 + 3
            writer.writerow([p_1, p_2, timestamp])
            writer.writerow([p_2, p_3, timestamp])
            writer.writerow([p_3, p_1, timestamp])
            writer.writerow([p_1, p_4, timestamp])
            writer.writerow([p_2, p_4, timestamp])
            writer.writerow([p_3, p_4, timestamp])

write_k4s()
