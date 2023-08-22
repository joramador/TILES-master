import networkx as nx

# remove label parameter to get name labels on the nodes instead of id num
g = nx.read_gml("tiles/datasets/lesmis/lesmis.gml", label="id")

# write the edges to new tsv file
# NOTE: the order of edges in tsv file may differ from gml since 
# they are being written in the arbitrary order of edges done by networkx

fout = open("tiles/datasets/lesmis/lesmis.tsv", 'w')
for edge in g.edges:
    u = edge[0]
    v = edge[1]
    value = g.get_edge_data(u, v)['value']
    fout.write(str(u) + "\t" + str(v) + "\t" + "1082441188" + "\t" + str(value) + "\n")
fout.close()
