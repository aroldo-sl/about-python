#!/usr/bin/env bash
this_filepath=$(realpath $0)
echo "BEGIN $this_filepath"
if [[ -n "$GARBAGE" ]]
then
    echo "GARBAGE=$GARBAGE"
else
    echo "GARBAGE is not defined or is empty."
fi

if [[ -n "$RUBBISH" ]]
then
    echo "RUBBISH=$RUBBISH"
else
    echo "RUBBISH is not defined or is empty."
fi


for letter in a b c d  
do
    echo "letter:$letter"
    sleep 2
done
echo "END $this_filepath"

