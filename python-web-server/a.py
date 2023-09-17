from flask import Flask, request
import os
app = Flask(__name__)

@app.route('/lift')
def lift():
    os.system("/home/pi/lift/bootall.sh")
    return 'Lift Started'

@app.route('/')
def clock():
    os.system("/home/pi/python-ui/launcher.sh")
    return 'Clock started'

@app.route('/downbutton')
def down():
    os.system("/home/pi/lift/down.sh")
    os.system("echo 5 > /home/pi/lift/floorState.txt")
    return 'downbutton pressed'

@app.route('/upbutton')
def up():
    os.system("/home/pi/lift/up.sh")
    os.system("echo 5 > /home/pi/lift/floorState.txt")
    return 'upbutton pressed'

@app.route('/pics', methods=['GET'])
def pics():
    pic_id = request.args.get("id")
    cmd = "/home/pi/pics/launcher.sh " + pic_id
    print("command", cmd)
    os.system(cmd)
    return 'Displaying pic'

@app.route('/test')
def test():
    return 'server is up and running'
if __name__ == '__main__':
    app.run(debug=True, port=4080, host='0.0.0.0')
