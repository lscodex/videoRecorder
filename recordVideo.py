#!/usr/bin/env python
# coding=utf-8
# Autor: lscodex 
import cv2
import argparse
import sys


RECORD_PATH="recordedVideo.avi"


# parse the arguments 
def lscodex_argument():
	parser = argparse.ArgumentParser("description = 'Records some video")
	parser.add_argument("-r","--record", help="to record a video from the user selection")
	return vars(parser.parse_args())


# start video
def lscodex_vOpen(video):

	firstFrame = None
	# get video fps
	fpst = int(video.get(cv2.CAP_PROP_FPS))
	# get frame from video
	ret,frame_pr = video.read()
	# resize for video
	frame_pr =cv2.resize(frame_pr,(640,480))

	# row or cols
	wpr,hpr = frame_pr.shape[:2]
	# set to writer for selected video 
	wVideo = cv2.VideoWriter(RECORD_PATH, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), fpst, (hpr, wpr), 1)


	# vidoe is played
	while video.isOpened():

		(grabbed,frame) = video.read()

		frame =cv2.resize(frame,(640,480))

		# frame is not grabbed
		if not grabbed:
			 break


		cv2.imshow("frame",frame)
		# write the selected video 
		wVideo.write(frame)
		# the program is exit when user press "q"
		key = cv2.waitKey(1) & 0xFF
		if key == ord('q'):
			break

	# closing and releasing 
	video.release()
	cv2.destroyAllWindows()

# main function
if __name__ =="__main__":
	video = lscodex_argument()
	if video["record"] is not None:
		video = cv2.VideoCapture(video["record"])
		lscodex_vOpen(video)
	else: 
		# if program is not run from own scripts 
		print("Please Selection the record option")
