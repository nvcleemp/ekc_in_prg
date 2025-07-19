#!/bin/bash

order=$1

if [ -z "$order" ]; then
  echo "Usage: $0 <order>"
  exit 1
fi

if ! [[ "$order" =~ ^[0-9]+$ ]] || [ $((order % 2)) -ne 0 ] || [ $order -le 0 ]; then
  echo "Error: Order must be a positive even integer."
  exit 1
fi

faces=$(( 2 + order ))
printf -v padded_order "%02d" "$order"

echo "Checking quartic plane graphs with $order vertices..."

plantri -qd $faces | reg_planar_perfectly_hamiltonian -f 4 > quartic_perfham_$padded_order.plc