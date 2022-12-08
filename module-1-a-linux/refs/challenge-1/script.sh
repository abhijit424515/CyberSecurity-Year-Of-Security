#!/bin/bash
7z e chall1-updated.7z
mkdir old/
mv chall1-updated.7z old/

while true; do
    curr_enc_pass=$(find . ! -name '*.*' ! -type d)
    curr_archive=$(find . -maxdepth 1 -name '*.*' -a ! -name '*.sh' -a ! -name "." ! -type d)
    curr_archive_ext=$(echo $curr_archive | cut -d "." -f3)
    
    base64=$(cat $curr_enc_pass | base64)
    base32=$(cat $curr_enc_pass | base32)
    hex=$(cat $curr_enc_pass | od -A n -t x1 | sed 's/ *//g')
    plain=$(cat $current_enc_pass)
    
    if [ "$curr_archive_ext"="zip" ]
    then
        unzip -P $base64
        unzip -P $base32
        unzip -P $hex
        unzip -P $plain
    elif [ "$curr_archive_ext"="7z" ]
    then
        7z x -p$base64
        7z x -p$base32
        7z x -p$hex
        7z x -p$plain
    else
        break
    fi
    
    mv $curr_archive $curr_enc_pass old/
done

mv old/chall1-updated.7z .