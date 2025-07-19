Edge-Kempe classes in cubic planar graphs
=========================================

Graphs
------

* `perfectly_hamiltonian/all/cubic_perfham_n.plc`: all perfectly hamiltonian cubic plane graphs on _n_ vertices


Programs
--------

The script `all_perfectly_hamiltonian_cubic_plane_graphs_of_order.sh` can be used to construct the cubic plane graphs
from the folder `perfectly_hamiltonian/all/`. To run the script for _n_ vertices you invoke it as follows:

```
$ ./all_perfectly_hamiltonian_cubic_plane_graphs_of_order.sh n
```

This script runs the generator `plantri` and filters the output to obtain the perfectly hamiltonian cubic plane graphs.

The script `check_classes_for_all_perfectly_hamiltonian_cubic_plane_graphs_up_to_order_26.sh` can be used to check the
occurrence of counts of classes among the perfectly hamiltonian cubic plane graphs up to 26 vertices. Simply run the script,
and it should generate the output below:

```
Checking order 4...
      1 1 equivalence class

Checking order 6...
      1 1 equivalence class

Checking order 8...
      1 1 equivalence class

Checking order 10...
      3 1 equivalence class

Checking order 12...
      7 1 equivalence class
      1 2 equivalence classes

Checking order 14...
     24 1 equivalence class
      3 2 equivalence classes

Checking order 16...
     93 1 equivalence class
     22 2 equivalence classes

Checking order 18...
    434 1 equivalence class
    135 2 equivalence classes
      1 3 equivalence classes

Checking order 20...
   2110 1 equivalence class
    985 2 equivalence classes
     16 3 equivalence classes
      4 4 equivalence classes
      1 10 equivalence classes

Checking order 22...
  11002 1 equivalence class
   6957 2 equivalence classes
    214 3 equivalence classes
     47 4 equivalence classes
      1 10 equivalence classes

Checking order 24...
  58713 1 equivalence class
  49830 2 equivalence classes
   2490 3 equivalence classes
    674 4 equivalence classes
      6 5 equivalence classes
      1 7 equivalence classes
      6 10 equivalence classes

Checking order 26...
 321776 1 equivalence class
 352793 2 equivalence classes
  25902 3 equivalence classes
   8606 4 equivalence classes
    156 5 equivalence classes
     10 6 equivalence classes
      9 7 equivalence classes
     30 10 equivalence classes

```

This confirms the following statements:

* the complete graph on 4 vertices has exactly one Kempe class
* the smallest planar cubic perfectly hamiltonian graph with 2 Kempe classes has 12 vertices
* the smallest planar cubic perfectly hamiltonian graph with 3 Kempe classes has 18 vertices
* the six smallest planar cubic perfectly hamiltonian graphs with 5 Kempe classes have 24 vertices
* the smallest planar cubic perfectly hamiltonian graph with 7 Kempe classes has 24 vertices