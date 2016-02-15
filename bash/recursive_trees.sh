#!/usr/bin/env bash

function echo_line {
  printf '%*s' "$1" | tr ' ' "_"
}

# First argument is length of stems, all further arguments are indices for stems in the line
function stem {
  length=$1
  last=0
  line=""

  IFS=' ' read -ra ADDR <<< "${@:2}"
  for i in "${ADDR[@]}"; do
    line="$line`echo_line $(($i - $last - 1))`1"
    last=$i
  done

  line="$line`echo_line $(($width - $last))`\n"

  for j in `seq 1 $length`
  do
    printf $line
  done
}

function branch {
  length=$1

  for i in `seq 1 $length`
  do
    last=0
    line=""
    IFS=' ' read -ra ADDR <<< "${@:2}"
    for j in "${ADDR[@]}"; do
      left=$(($j - $i - 1))
      right=$(($j + $i - 1))
      between=$(($right - $left - 1))
      line="$line`echo_line $(($left - $last))`1`echo_line $between`1"
      last=$(($right + 1))
    done
    line="$line`echo_line $(($width - $last))`\n"
    printf $line
  done
}

function fractal {
  levels="$1"
  width="$2"
  height="$3"
  local branching="$4"
  total_lines=0

  nodes=($(($width/2)))

  for i in `seq 1 $levels`
  do
    stem $branching "${nodes[@]}"
    branch $branching "${nodes[@]}"

    temp_nodes=()
    for node in $nodes
    do
      temp_nodes+=($((node - branching)))
      temp_nodes+=($((node + branching)))
    done
    nodes=("${temp_nodes[*]}")
    total_lines=$(($total_lines + $branching * 2))
    branching=$(($branching / 2))
  done

  for i in `seq $total_lines $(($height - 1))`
  do
    echo `echo_line $width`
  done
}

read lvls

lines=(`fractal $lvls 100 63 16`)

for ((i=${#lines[@]}-1; i>=0; i--)); do
  echo "${lines[$i]}"
done