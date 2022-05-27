from flask import Flask, render_template, Response
from camera import VideoCamera
import threading
import multiprocessing


app = Flask(__name__)
camera = VideoCamera()

@app.route('/')
def index():
    # rendering webpage
    return render_template('index.html')

def gen():
    #get camera frame
    frame = camera.get_frame()
    yield (frame)

def genmask():
    frame = camera.get_mask()
    yield (frame)

@app.route('/video_feed')
def video_feed():
    return Response(gen())

@app.route('/video_mask')
def video_mask():
    return Response(genmask())

@app.route('/berhenti')
def berhenti():
    camera.jalan[0]=False
    return

@app.route('/jalan')
def jalan():
    camera.jalan[0]=True
    return

@app.route('/range-hsv-bola', methods=['POST'])
def rangehsvbola():
    data = request.get_json()
    file_object1 = open("data hsv bola.txt", "r")
    file_object2 = open("data hsv bola.txt.bak", "w+")
    f1 = file_object1.readlines()
    for x in f1:
        file_object2.write(x)
    file_object1.close()
    file_object2.close()
    file_object1 = open("data hsv bola.txt", "w+")
    file_object1.write(data['low'])
    file_object2.write(data['high'])
    

if __name__ == '__main__':
    # defining server ip address and port
    # utama = Utama()
    pr01 = multiprocessing.Process(target=camera.run)
    pr01.daemon = True
    pr01.start()
    pr02 = multiprocessing.Process(target=camera.processing)
    pr02.daemon = True
    pr02.start()
    pr03 = multiprocessing.Process(target=camera.commandprocess)
    pr03.daemon = True
    pr03.start()
    app.run(host='0.0.0.0',port='5000', debug=False)