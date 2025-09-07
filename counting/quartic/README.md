Edge-Kempe classes in quartic planar graphs
===========================================

Graphs
------

* `perfectly_hamiltonian/all/quartic_perfham_n.plc`: all perfectly hamiltonian quartic plane graphs on _n_ vertices
* `perfectly_hamiltonian/per_class/quartic_perfham_n_classes.plc`: the perfectly hamiltonian quartic plane graphs with _n_ Kempe classes that are shown in Figure 5 of the paper.
* `perfectly_hamiltonian/per_class/quartic_perfham_n_classes_all_smallest.plc`: all smallest perfectly hamiltonian quartic plane graphs with _n_ Kempe classes (only for classes with multiple smallest graphs).


Programs
--------

The script `all_perfectly_hamiltonian_quartic_plane_graphs_of_order.sh` can be used to construct the quartic plane graphs
from the folder `perfectly_hamiltonian/all/`. To run the script for _n_ vertices you invoke it as follows:

```
$ ./all_perfectly_hamiltonian_quartic_plane_graphs_of_order.sh n
```

This script runs the generator `plantri` and filters the output to obtain the perfectly hamiltonian quartic plane graphs.

The script `check_classes_for_all_perfectly_hamiltonian_quartic_plane_graphs_up_to_order_22.sh` can be used to check the
occurrence of counts of classes among the perfectly hamiltonian quartic plane graphs up to 22 vertices. Simply run the script,
and it should generate the output below:

```
Checking order 6...
      1 2 equivalence classes

Checking order 10...
      1 2 equivalence classes
      1 4 equivalence classes

Checking order 12...
      1 8 equivalence classes

Checking order 14...
      3 2 equivalence classes
      5 3 equivalence classes
      5 4 equivalence classes
      2 5 equivalence classes
      1 6 equivalence classes
      1 7 equivalence classes
      3 8 equivalence classes

Checking order 16...
     10 5 equivalence classes
      9 6 equivalence classes
     10 8 equivalence classes
      1 10 equivalence classes
      5 16 equivalence classes
      1 26 equivalence classes

Checking order 18...
      8 2 equivalence classes
    153 3 equivalence classes
    193 4 equivalence classes
     62 5 equivalence classes
    118 6 equivalence classes
     12 7 equivalence classes
     84 8 equivalence classes
      8 9 equivalence classes
     23 10 equivalence classes
      3 11 equivalence classes
     12 12 equivalence classes
      2 13 equivalence classes
      5 14 equivalence classes
     15 16 equivalence classes
      1 17 equivalence classes
      3 18 equivalence classes
      5 20 equivalence classes
      9 32 equivalence classes
      1 48 equivalence classes

Checking order 20...
    519 4 equivalence classes
    158 5 equivalence classes
    723 6 equivalence classes
     95 7 equivalence classes
    459 8 equivalence classes
     49 9 equivalence classes
    276 10 equivalence classes
     15 11 equivalence classes
    333 12 equivalence classes
     11 13 equivalence classes
     51 14 equivalence classes
      7 15 equivalence classes
    323 16 equivalence classes
     11 17 equivalence classes
     38 18 equivalence classes
     69 20 equivalence classes
     21 24 equivalence classes
      2 25 equivalence classes
      1 26 equivalence classes
     10 28 equivalence classes
     57 32 equivalence classes
      2 52 equivalence classes

Checking order 22...
     15 2 equivalence classes
   6771 3 equivalence classes
   9621 4 equivalence classes
   5377 5 equivalence classes
   9122 6 equivalence classes
   1976 7 equivalence classes
   7101 8 equivalence classes
    713 9 equivalence classes
   2848 10 equivalence classes
    253 11 equivalence classes
   3518 12 equivalence classes
    129 13 equivalence classes
    800 14 equivalence classes
     84 15 equivalence classes
   1884 16 equivalence classes
     75 17 equivalence classes
    440 18 equivalence classes
     12 19 equivalence classes
   1009 20 equivalence classes
      7 21 equivalence classes
     58 22 equivalence classes
      7 23 equivalence classes
    600 24 equivalence classes
      3 25 equivalence classes
     41 26 equivalence classes
    116 28 equivalence classes
      1 31 equivalence classes
    474 32 equivalence classes
     18 34 equivalence classes
     77 36 equivalence classes
      2 38 equivalence classes
    106 40 equivalence classes
      3 42 equivalence classes
      1 43 equivalence classes
      2 48 equivalence classes
      2 50 equivalence classes
      2 52 equivalence classes
    144 64 equivalence classes
      2 68 equivalence classes
      1 70 equivalence classes
      6 72 equivalence classes
      4 96 equivalence classes
      6 104 equivalence classes

```

This confirms the following statements:

* the octahedron (the unique quartic planar 3-connected graph on 6 vertices) has 2 Kempe classes
* the smallest planar quartic perfectly hamiltonian graphs with _n_ Kempe classes for n=3, 5, and 7 have 14 vertices
* the smallest planar quartic perfectly hamiltonian graphs with _n_ Kempe classes for n=11, 13, and 17 have 18 vertices
* the smallest planar quartic perfectly hamiltonian graphs with _n_ Kempe classes for n=19, 23, 31, and 43 have 22 vertices


You can easily check the example graphs in `perfectly_hamiltonian/per_class` using the following command (replacing _FILE_ by a specific file):

```
$ reg_planar_all_colourings -C 4 < FILE 
```