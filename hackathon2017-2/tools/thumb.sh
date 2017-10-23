#! /bin/bash

for i in *.JPG; do
    if [ "$i" -nt "../thumbnail/univ/$i" ]; then
        convert "$i" -thumbnail 500 "../thumbnail/univ/$i";
    fi
done;
