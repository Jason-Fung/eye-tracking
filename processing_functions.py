import cv2
import numpy as np
from pykalman import KalmanFilter

def init_settings():
	# function init_settings() sets up the necessary parameters for performing computer
	# vision tasks.
	# Returns detector, face_cascade = face classifier, eye_cascade = eye classifier

	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
	eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

	detector_params = cv2.SimpleBlobDetector_Params()
	# detector_params.filterByArea = True
	detector_params.maxArea = 1500

	detector = cv2.SimpleBlobDetector_create(detector_params)
	return detector, face_cascade, eye_cascade

def detect_faces(img,classifier):
	gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	coords = classifier.detectMultiScale(gray_frame, 1.3, 5)
	if len(coords) > 1: # check if there are any more faces present 
		biggest = (0,0,0,0)
		for i in coords:
			if i[3] > biggest[3]:
				biggest = i
		biggest = np.array([i],np.int32)
	elif len(coords) == 1:
		biggest = coords
	else:
		return None
	for (x,y,w,h) in biggest: # filter out unwanted "faces" in background
		frame = img[y:y+h, x:x+w]
	# print(biggest)
	return frame

def detect_eyes(img,classifier):
	# function takes cut out face (img) and gray face (img_gray) and chosen type 
	# of cascade filter (classifier) to select eyes. Function returns the images of
	# the left and right eyes.
	img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert to gray scale for eye detection
	coords = classifier.detectMultiScale(img_gray,1.3,5) # detect eyes
	height = np.size(img,0) # get face frame height
	width = np.size(img,1) # get face frame width

	left_eye = None
	right_eye = None

	for (x,y,w,h) in coords:
		if y + h > height/2: # only accept objects that are above the first half of face
			pass
		face_center = x + w/2 # get the approx eye center by cutting face in half
		if face_center < width*0.5:
			left_eye = img[y:y+h,x:x+w]
			# left_eye_coords = [x, x+w, y, y+w]
		else:
			right_eye = img[y:y+h,x:x+w]
	return left_eye, right_eye, coords

def cut_eyebrows(img):
	# function cuts the eyebrows which will allow segmentation of pupils

	height, width = img.shape[:2]
	eyebrow_h = int(height/4)
	img = img[eyebrow_h:height, 0:width]
	return img

def blob_process(img, threshold, detector):
	# function processes the binary image of eyes(img) and help detect
	# the pupil via a detector (detector) based on the given thresholding (threshold)
	# value.

	gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert BGR/RGB space to gray space
	_, img = cv2.threshold(gray_frame, threshold, 255, cv2.THRESH_BINARY)

	# img = cv2.adaptiveThreshold(gray_frame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 7, 4)

	img = cv2.erode(img, None, iterations = 2) #1 process
	img = cv2.dilate(img, None, iterations = 4) #2 process
	img = cv2.medianBlur(img, 5) #3 process

	# cv2.imshow('eye with keypoint', img)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()
	keypoints = detector.detect(img)
	return img, keypoints

def nothing(x):
	pass

def draw_blobs(img, keypoints, color = [255,0,0]):
	return cv2.drawKeypoints(img, keypoints, img, color, cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# introduce Kalman Filter to assist eye detection

def performKalman(data, trans_mat, state_mean, observ_mat, 
				  observ_cov, state_cov, trans_cov):
	
	# data: list [x,y] where x and y are the coordinates of the pupil
	# trans_mat: square matrix of size (2n,2n) where n is the number of states
	# state_mean: np array of size (1,2n). Initial mean state 
	# observ_cov: np diag of size (n,n).
	# state_cov: np diag of size (2n,2n).
	# trans_cov: np diag of size (2n,2n). 

	kf = KalmanFilter(transition_matrices= trans_mat,
						observation_matrices = observ_mat,
						initial_state_mean = state_mean,
						observation_covariance = observ_cov,
						initial_state_covariance = state_cov,
						transition_covariance = trans_cov)
	
	next_mean, next_cov = kf.smooth(data)

	return next_mean, next_cov
