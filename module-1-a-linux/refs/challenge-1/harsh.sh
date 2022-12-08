#!/usr/bin/bash
7z x chall1-updated.7z
mkdir current/
mkdir old/
mv files.zip enc_pass current/
cd current/ || exit
while true
do
    zipfile=$(find ./ -name ’*zip’)
    ext=’zip’
    if [ -z "$zipfile" ];
    then
        zipfile=$(find ./ -name ’*7z’);
        ext=’7z’;
    fi
    if [ -z "$zipfile" ];
    then
        break;
    fi
    
    other=$(find ./ -type f ! -name "*$ext*")
    pass=$(cat "$other")
    base_64=$(echo -n "$pass"|base64)
    base_32=$(echo -n "$pass"|base32)
    hex_encode=$(echo -n "$pass" | xxd -ps -c 200)
    
    if [ $ext == ’zip’ ];
    then
        unzip -P "$pass" "$zipfile";
        unzip -P "$base_64" "$zipfile";
        unzip -P "$base_32" "$zipfile";
        unzip -P "$hex_encode" "$zipfile";
    else
        7z x -p"$pass" "$zipfile";
        7z x -p"$base_64" "$zipfile";
        7z x -p"$base_32" "$zipfile";
        7z x -p"$hex_encode" "$zipfile";
    fi
    mv "$zipfile" "$other" ../old/
done
cat flag
