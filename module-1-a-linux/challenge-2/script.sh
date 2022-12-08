# flag{93tt1n9_u536_t0_6a5h}
latest_link="https://www.cse.iitb.ac.in/~akshatka/"
new_link=""

while true
do
    new_link=$(curl $latest_link | grep -Eo "https?://.*.html")
    if ! [ -z "$new_link" ]
    then
        echo $new_link
        latest_link=$new_link
    else
        break
    fi
done

wget $(curl $latest_link | grep -Eo "https?://.*.tar")
tar -xvf $(find . -maxdepth 1 -name '*.tar')
cd $(find . -maxdepth 1 -type d ! -name '.')

# find -type f -size 87369c \! -perm /a+x
# FOR SOME REASON, THE FILE WAS EXECUTABLE, BUT IT WAS SUPPOSED TO BE NON-EXECUTABLE
flag=$(find -type f -size 87369c | xargs -I {} head -n 1 {} | tr -d ' ')

cd ..
rm -r README $(find . -maxdepth 1 -name '*.tar') $(find . -maxdepth 1 -type d ! -name '.')
clear
echo $flag
