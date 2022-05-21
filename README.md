# dog-breed-predictor
### Using ResNet50 for dog breed prediction using webcam  
  
#### Step 1:
Download and Install Python, pip and virtualenv to your system if you don't have it.
```
py -m pip install --upgrade pip
py -m pip --version
py -m pip install --user virtualenv
```
#### Step 2:
Open your project folder and create a virtual environment using the command below
```
py -m venv env
```
Activate the environment that you created.
```
.\env\Scripts\activate
``` 
#### Step 3: 
Install all the packages from [requirement](requirement.txt) file using the following command.
```
pip install -r requirements.txt
```
#### Step 4:
Run the [main.py](main.py) file.  
  
> __Note__: This will run on a development server. Do not use it in as production deployment. 
 

#### Step 5:
Open the url where your application is running like `http://127.0.0.1:2000` in the snippet of my CMD.  
  
![image](https://user-images.githubusercontent.com/55987634/169652937-848caa03-4961-466e-b5d7-a371d00e20e5.png)  
You can use `Start/Stop` to start/stop prediction.  
Use `Close Webcam` button to close the webcam.  
After you are done with the application press `CTRL+C` in the CMD to quit.  
  
> __Note__: You'll have to restart your application after you close your webcam  

  
##### _Enjoy Predicting!_
