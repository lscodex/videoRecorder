#!/bin/bash


echo "Hello, I installed requirements, please wait, $(whoami) !" 
pipver="sudo apt-get install pip"
cv2ver="sudo pip install opencv-python"
dia2ver="sudo apt-get install dialog"
function select_file(){
	# show to helper menu for programs
	python recordVideo.py -h 
	local f="$1" 
	local m="$0: $f file selected."
	if [ -f $f ]
	then
		echo "here is"
		python recordVideo.py -r $FILE && m="$0: $f file selected"
	else
		m="$0: $f is not a file"
	fi

}

function startin(){

	FILE=$(dialog --title "Select a video file" --stdout --title "Please choose a file to select" --fselect /home/$(whoami) 14 48)

	# select file 
	[ ! -z $FILE ] && select_file "$FILE"

}


#if [ -x "$(command -v pip)"]; then 
#	echo "I'm install to opencv-python"
#else
#	echo "pip is exist" 
function checkCV2(){
	echo "I am checking cv2 version"
	sudo chmod 777 checkCV2.py
	getResult=$(command ./checkCV2.py)
	echo "$getResult"
	if [ $getResult != "n" ]
	then
		echo "cv2 is exist"
	else
		echo "cv2 is not exist"
		echo "$(whoami), I am installing cv2 with pip"
		if [ -x "$(command --version pip)" ]; then
			echo "pip is exist"
			echo " Ok, I'm installing cv2"
			$cv2ver
		else
			echo "pip is not exist, $(whoami)"
			echo "Let's go to install the pip"
			$pipver 
			echo "installing cv2, please wait!"
			$cv2ver
		fi 
	fi

}

checkCV2
echo " package dialog is installing now... " 
$dia2ver
startin

