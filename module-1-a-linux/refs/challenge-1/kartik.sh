7z e copy/chall1-updated.7z

while [ '0' -eq '0' ]
do
	szip=$(ls | grep *.7z)
	nzip=$(ls | grep *.zip)
	passfile=$(find . -type f ! -name "*.*")
	
	if [ -z $szip ]
	then 
		if [ -z $nzip ]
		then
			break
		else

			pass=$(cat $passfile)
			unzip -P$pass $nzip	
			if [ $? -ne 0 ]
			then
				pass=$(base32 $passfile)
				unzip -P$pass $nzip	
				if [ $? -ne 0 ]
					then
					pass=$(base64 $passfile)
					unzip -P$pass $nzip	
					if [ $? -ne 0 ]
						then
						pass=$(cat $passfile| xxd -p)
						unzip -P$pass $nzip	
					fi
				fi
			fi

			rm $passfile $nzip
 
		fi
	else
		pass=$(cat $passfile)
			7z e $szip -p$pass	
			if [ $? -ne 0 ]
			then
				pass=$(base32 $passfile)
				7z e $szip -p$pass
				if [ $? -ne 0 ]
					then
					pass=$(base64 $passfile)
					7z e $szip -p$pass	
					if [ $? -ne 0 ]
						then
						pass=$(cat $passfile| xxd -p)
						7z e $szip -p$pass
					fi
				fi
			fi
		rm $passfile $szip
	fi
done

cat flag