Alan's notes of TILES from Spring Semester!
Notes: I worked on a Macbook, so not super sure about Windows OS

-- What I Did --
1) Modified TILES.py algorithm to have k4s as strong communities! 
ctrl-f "CHANGE HERE" to see the specific areas I changed to support this
2) added various debugging scripts to test the above change, and count the number of communities outputted


-- Setting up TILES --
- I mostly referred to the readme in TILES for setting things up.
Installation and running the files, for the most part, was incredibly smooth. 
I made a venv from the requirements.txt file. Here's how to set it up: (skip step 1 once venv is created)
    1) To create a venv, in your working directory, run: python -m venv .venv
    2) Once the venv is created, in terminal: source venv/bin/activate (for windows: .venv\Scripts\activate.bat)
    3) Now, you should see (.venv) in terminal. Now, install the requirements via: pip install -r requirements.txt
    4) When done, deactivate with the command: deactivate
Once in your venv with the requirements installed, you can run TILES!

1) running vanilla TILES (strong community = k3): 
In order to run the default TILES application, the easiest method (as per the main README) is to call the tiles 
method within the TILES folder. Navigate to TILES, and run: 
python3 tiles tiles/test/[filename.tsv] 
Alternatively, you can also run the __main__.py file directy. Navigate to TILES, and run:
python3 tiles/__main__.py tiles/test/[filename.tsv]

~~~ After running TILES, the program will generate 5 types of files: ~~~
--- Extraction Status (extraction_status.txt): Simplest, basically logs what TILES did. For each slice (unit of time), lists
the amount of edges added, edges removed, merged and total communities
--- graph-n (graph-n.gz): lists the edges in the graph, vertex / vertex / 1
--- merging-n (merging-n.gz): not super sure what this is---for the most part, when I clicked on it, its empty. Could be worth looking into.
--- splitting-n (splitting-n.gz): similar to merging-n. Might be worth looking into how TILES creates this file.
--- strong-communities-n (strong-communities-n.gz): lists the strong communities, as a bracketed list of vertices. Output is a list of lists
of integers, with a community per line. My count_communities code takes this as input to parse.

2) running modified TILES (strong community = k4/kn, TILES.py)
To run the modified TILES algorithm (TILES.py file), navigate all the way into the alg folder (TILES/tiles/alg),
and then change the lines of code at the very bottom to read the tsv file desired (currently set to k3_communities). 
Then, simply run the file with python:
python3 TILES.py
The code currently modifies the TILES algorithm to only consider k4s and above as strong communities. Thus, double-check
you're running everything correctly by calling TILES.py on k3_communities.py. In the extraction_status.txt outputted, 
there should be 0 total communities found. I've commented where I modified the TILES code to support k4s instead of k3s 
(all marked with CHANGE HERE)!

** All the tsv files are stored in /TILES/tiles/test for easy access! Add any new tsv files into that file for ease of access.
Note that the tsv format should be a list of edges, as follows: timestamp node1 node2, where each value is an integer

--- My Code ---
The code I contributed is in the sp22_scripts folder. There are 3 scripts I added:

1) convert_tsv.py: All this code does is convert from .txt to .tsv (changing into a compatable format). 
Just change the path to whatever txt file you want (without the .txt suffix!), and run it with python3 in terminal. 
The tsv file will be outputted in the same directory the txt file was in.

2) count_communities.py: There are two methods within this file: countCommunities, and a helper function, isSubset. 
countCommunities reads in the output of TILES, the strong-communities-... file (after extracting the .gz), and converts 
the sets into a list of integer lists (each integer list representing a community). It returns two values: 1) the total
number of communities TILES found (via its strong-communities file), and 2) the total number of communities minus subsets.
This is because TILES doesn't seem to 'merge' communities together, and returns redundancies in communities that are subsets
of other communities. Thus, I wrote a quick method that naively filters out these subsets (via a merge-sort esque algorithm).
To run, edit the path at the bottom of the file to the desired strong-communities output file, and then run the file with
python in the terminal.

3) generate_graph.py: This script was used to create sample graphs of all k3s and all k4s, in order to test the modified TILES
algorithm file. It should be able to be easily modified to support k5s, k6s, ..., kns!

-- Points of Exploration --
1) running TILES on different datasets and visualizing these strong communities detected! Seeing how changing the 
'strong community threshold' (k3 -> k4 -> kn) affects the communities returned, and applying it to interesting 
datasets (CollegeMsg dataset). 
    a) currently been exploring this dataset: https://snap.stanford.edu/data/CollegeMsg.html
2) Figuring out why TILES doesn't 'merge' communities / outputs communities that are subsets of one another?
3) Recreating the graphs from page 1233 (pg 21 on the pdf) in the original TILES paper. Shouldn't be too bad with the
pre-existing count_communities code!
