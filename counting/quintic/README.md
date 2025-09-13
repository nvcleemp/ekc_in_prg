Edge-Kempe classes in quintic planar graphs
===========================================

Graphs
------

* `perfectly_hamiltonian/all/quintic_perfham_n.plc`: all perfectly hamiltonian quintic plane graphs on _n_ vertices
* `perfectly_hamiltonian/per_class/quintic_perfham_n_classes.plc`: the perfectly hamiltonian quintic plane graphs with _n_ Kempe classes that are shown in Figure 6 of the paper.


Programs
--------

In order to construct the graphs from `perfectly_hamiltonian/all`, we refer to the repository [hc_1f_5reg](https://github.com/nvcleemp/hc_1f_5reg).

The script `check_classes_for_all_perfectly_hamiltonian_quintic_plane_graphs_up_to_order_28.sh` can be used to check the
occurrence of counts of classes among the perfectly hamiltonian quintic plane graphs up to 28 vertices. Simply run the script,
and it should generate the output below:

```
Checking order 20...
      1 8 equivalence classes

Checking order 22...
      1 16 equivalence classes
      1 51 equivalence classes

Checking order 24...
      2 4 equivalence classes
      4 5 equivalence classes
      4 6 equivalence classes
      1 7 equivalence classes
      1 8 equivalence classes
      2 10 equivalence classes
      3 12 equivalence classes
      5 14 equivalence classes
      1 18 equivalence classes
      1 56 equivalence classes
```

You can easily check the example graphs in `perfectly_hamiltonian/per_class` using the following command (replacing _FILE_ by a specific file):

```
$ reg_planar_all_colourings -C 5 < FILE 
```