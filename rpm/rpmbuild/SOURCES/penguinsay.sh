#!/bin/bash

input="$@"
# Break the test into lines 50 characters or less
speech=$(echo "$input" | fold -s -w50)

IFS=$'\n'

# See which line is longest
length=0
for line in ${speech}; do
  [[ ${#line} -gt ${length} ]] && length=${#line}
done

# Formatting length
blength=$(expr $length + 2)

# Create our filler lines
bubble=$(printf "%${blength}s" | tr ' ' "-")
buflen=$(expr $blength - 3)
buffer=$(printf "%${buflen}s" | tr ' ' " ")

echo " $bubble "

# echo each quoted line
for line in ${speech}; do
  fillnum=$(expr $length - ${#line})
  fill=$(printf "%${fillnum}s" | tr ' ' " ")
  echo "< ${line}${fill} >"
done

echo " $bubble "
cat << EOF
$buffer  \\ \\
$buffer   \\\\
$buffer    \\ ,——.
$buffer     ( @ 0)
$buffer     |  7 |
$buffer    / /   \\\\
$buffer   (  >   < )
$buffer  /  \_   _/ \\
$buffer  \____) (___/
EOF