#!/bin/bash

start=10
end=22

echo "Checking order 6..."
reg_planar_all_colourings -C 4 < all/quartic_perfham_06.plc 2>&1 | grep equivalence | grep -v Minimum | sort -n | uniq -c
echo 

for order in $(seq $start 2 $end); do
  echo "Checking order $order..."
  reg_planar_all_colourings -C 4 < all/quartic_perfham_`printf "%02d" "$order"`.plc 2>&1 | grep equivalence | grep -v Minimum | sort -n | uniq -c
  echo 
done
