#!/bin/bash

start=20
end=28

for order in $(seq $start 2 $end); do
  echo "Checking order $order..."
  reg_planar_all_colourings -C 5 < all/quintic_perfham_$order.plc 2>&1 | grep equivalence | grep -v Minimum | sort -n | uniq -c
  echo 
done
