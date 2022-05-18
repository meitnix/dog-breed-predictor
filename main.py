from flask import Flask,request,render_template,Response,send_from_directory
import numpy as np
import cv2
import time
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions 
from tensorflow.keras.applications import ResNet50

def read_and_prep_images(frame):
    dim=(224,224)
    imgcv = frame[:,:,::-1]
    imgcv_resized = cv2.resize(imgcv, dim, interpolation=cv2.INTER_NEAREST)
    imgcv_resized.astype(np.float32)
    testdata = np.array([imgcv_resized])
    output = preprocess_input(testdata)
    return(output)

def breed_pred(img):
	preds = my_model.predict(img)
	x=np.argmax(preds)
	if((x <= 268) & (x >= 151)):
		prediction = decode_predictions(preds, top=3)
		return prediction[0]
	else:
		return [["","Unknown"]]	

def js_to_image(frames):
  # convert bytes to numpy array
  jpg_as_np = np.frombuffer(frames, dtype=np.uint8)
  # decode numpy array into OpenCV BGR image
  img = cv2.imdecode(jpg_as_np, flags=1)
  return img

app = Flask(__name__)
camera = cv2.VideoCapture(0)
my_model = ResNet50(weights='imagenet')
start_prediction=False
def generate_frames():
	while True:
		success,frame = camera.read()
		frame = cv2.flip(frame, 1)
		if not success:
			break
		else:
			if(start_prediction):
				predvalue = breed_pred(read_and_prep_images(frame))
				font = cv2.FONT_HERSHEY_DUPLEX
				cv2.putText(frame, predvalue[0][1], (15,450), font, 1.0, (255, 255, 255), 1)
			ret,buffer=cv2.imencode('.jpg',frame)
			frame=buffer.tobytes()

		yield (b'--frame\r\n'
       				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/', methods=["GET","POST"])
def home():
	if request.method == "POST":
		if request.form.get("classifier"):
			global start_prediction
			start_prediction = ~ start_prediction
		elif request.form.get("close"):
			global camera
			camera.release()	
	return render_template("main.html")	

@app.route('/video')
def video():
	return Response(generate_frames(),mimetype='multipart/x-mixed-replace;boundary=frame')
app.run(debug=True,port=2000)