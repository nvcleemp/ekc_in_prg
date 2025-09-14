Single Kempe switches
=====================

Graphs
------

These are the example graphs from the paper:

* `graphs/cubic.plc`: the perfectly hamiltonian cubic plane graph shown in Figure 3
* `graphs/quartic.plc`: the perfectly hamiltonian quartic plane graph shown in Figure 4
* `graphs/quintic.plc`: the perfectly hamiltonian quintic plane graph shown in Figure 7

These are the colourings of these graphs:

* `graphs/cubic_colouring.txt`: the colouring of the graph shown in Figure 3
* `graphs/quartic_colouring.txt`: the colouring of the graph shown in Figure 4
* `graphs/quintic_colouring_1.txt`: the first colouring of the graph shown in Figure 7
* `graphs/quintic_colouring_2.txt`: the second colouring of the graph shown in Figure 7

For the colourings above, the format is that we list the neighbours of a vertex in the
order of the colours (first colour 1, then colour 2, ...)

Programs
--------

By running the program `reg_planar_all_colourings` with the option `-C` prints besides
the classes also an overview of the Kempe switches. This overview is aggregated over all graphs,
but when running for a single graph, you can get graph level result. You can run the program
as follows:

```
reg_planar_all_colourings -C 3 < cubic.plc
reg_planar_all_colourings -C 4 < quartic.plc
reg_planar_all_colourings -C 5 < quintic.plc
```

If we examine the output for the quintic graph, we see this section:

```
Overview of changes in number of perfect pairs for single Kempe switches:
 0:  0  1  2  3  4  5  6             
 1:  0  1  2  3  4  5  6  7          
 2:  0  1  2  3  4  5  6  7  8       
 3:  0  1  2  3  4  5  6  7  8  9    
 4:  0  1  2  3  4  5  6  7  8  9    
 5:  0  1  2  3  4  5  6  7  8  9    
 6:  0  1  2  3  4  5  6  7  8  9    
 7:     1  2  3  4  5  6  7  8  9    
 8:        2  3  4  5  6  7  8  9    
 9:           3  4  5  6  7  8  9    
10:                               10 
```

A line `n: k1 k2 ...` in this section means that for each pair _(n,ki)_ there
is a colouring of any of the input graphs which had _n_ perfect pairs and for
which there exists a Kempe switch such that the resulting colouring has _ki_
perfect pairs.

In the output, there is also this section:

```
Maximum different pairs reachable from one colouring with the specified number of perfect pairs:
 0: 7
 1: 7
 2: 8
 3: 8
 4: 8
 5: 8
 6: 7
 7: 7
 8: 5
 9: 4
10: 1
```

A line `n: k` in this section means that there is a colouring of any of the input
graphs which has _n_ perfect pairs and for which there exists _k_ different numbers
_ni_ (_i_=1,...,k) such that there exists a Kempe switch of the colouring such that
the resulting colouring has _ni_ perfect pairs.


The options `-F` (from) and `-T` (to) of the program `reg_planar_all_colourings` can be used
to find colourings that have a specific number of perfect pairs (specified by `-F`) and for
which there exists a Kempe switch resulting in a number of perfect pairs specified by one
of the `-T` options. By default, a colouring that also allows a Kempe switch to a number
of perfect pairs not specified by a `-T` option will be excluded. This can be relaxed by
including the `-A` option which specify that at least the numbers of perfect pairs specified
by the `-T` options need to be reached, but other numbers are also allowed.

Using this approach, we can find the colourings from the txt files in the graphs folder
by running the following commands:

```
reg_planar_all_colourings -F 0 -T 0 -T 1 -T 2 3 < graphs/cubic.plc

reg_planar_all_colourings -F 2 -T 0 -T 1 -T 2 -T 3 -T 4 -T 5 4 < graphs/quartic.plc

reg_planar_all_colourings -F 4 -T 0 -T 1 -T 2 -T 3 -T 4 -T 5 -T 6 -T 7 5 < graphs/quintic.plc
reg_planar_all_colourings -F 4 -T 8 -T 9 -A 5 < graphs/quintic.plc
```

A detailed analysis of these colourings can then be performed using the Python script
`analysis_single_kempe_switch.py`. Just run the script, and provide the colouring as input:

```
python3 analysis_single_kempe_switch.py < graphs/cubic_colouring.txt

python3 analysis_single_kempe_switch.py < graphs/quartic_colouring.txt

python3 analysis_single_kempe_switch.py < graphs/quintic_colouring_1.txt
python3 analysis_single_kempe_switch.py < graphs/quintic_colouring_1.txt
```

For the colouring of the cubic graph, e.g., the output will then be:

```
Current colouring:
 0:  2  1  3
 1:  5  0  4
 2:  0  5  6
 3:  8  7  0
 4: 10  9  1
 5:  1  2 10
 6: 12 11  2
 7: 13  3 12
 8:  3 13  9
 9: 14  4  8
10:  4 14  5
11: 15  6 14
12:  6 15  7
13:  7  8 15
14:  9 10 11
15: 11 12 13
2-factors for each colour pair:
0,1: [[0, 2, 5, 1], [3, 8, 13, 7], [4, 10, 14, 9], [6, 12, 15, 11]]
0,2: [[0, 2, 6, 12, 7, 13, 15, 11, 14, 9, 8, 3], [1, 5, 10, 4]]
1,2: [[0, 1, 4, 9, 8, 13, 15, 12, 7, 3], [2, 5, 10, 14, 11, 6]]
Perfect pair count in original: 0
Effect of single Kempe switches:
0,1: Switching [0, 2, 5, 1] gives 2 perfect pairs
0,1: Switching [3, 8, 13, 7] gives 0 perfect pairs
0,1: Switching [4, 10, 14, 9] gives 2 perfect pairs
0,1: Switching [6, 12, 15, 11] gives 1 perfect pairs
0,2: Switching [0, 2, 6, 12, 7, 13, 15, 11, 14, 9, 8, 3] gives 1 perfect pairs
0,2: Switching [1, 5, 10, 4] gives 1 perfect pairs
1,2: Switching [0, 1, 4, 9, 8, 13, 15, 12, 7, 3] gives 0 perfect pairs
1,2: Switching [2, 5, 10, 14, 11, 6] gives 0 perfect pairs
Shortest switches:
 2: [0, 2, 5, 1]
 0: [3, 8, 13, 7]
 1: [6, 12, 15, 11]
 ```  