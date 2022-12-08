#flag{uwu_y05_ha5_ac7ua11y_5ta7te6}
7z e chall1-updated.7z
mkdir old/
mv chall1-updated.7z old/

while true; do
    curr_enc_pass=$(find . -maxdepth 1 ! -name '*.*' -type f | tr -d './')
    base64=$(base64 $curr_enc_pass)
    base32=$(base32 $curr_enc_pass)
    hex=$(cat $curr_enc_pass | xxd -p | tr -d ' ')
    plain=$(cat $curr_enc_pass)

    curr_archive=$(ls | grep *.zip)
    if ! [ -z $curr_archive ]
    then
        unzip -P$base64 $curr_archive
        unzip -P$base32 $curr_archive
        unzip -P$hex $curr_archive
        unzip -P$plain $curr_archive 
    else
        curr_archive=$(ls | grep *.7z)
        if ! [ -z "$curr_archive" ]
        then
            7z e $curr_archive -y -p$base64  
            7z e $curr_archive -y -p$base32 
            7z e $curr_archive -y -p$hex  
            7z e $curr_archive -y -p$plain 
        else
            break
        fi
    fi
    
    mv $curr_archive $curr_enc_pass old/
done

mv old/chall1-updated.7z .
rm -r old/
clear
printf "\n" >> flag
cat flag
rm flag