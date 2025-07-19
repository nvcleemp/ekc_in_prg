#!/bin/bash

start=4
end=26

for order in $(seq $start 2 $end); do
  echo "Checking order $order..."
  reg_planar_all_colourings -C 3 < all/cubic_perfham_`printf "%02d" "$order"`.plc 2>&1 | grep equivalence | grep -v Minimum | sort -n | uniq -c
  echo 
done
