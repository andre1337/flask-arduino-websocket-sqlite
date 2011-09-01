from geventwebsocket.handler import WebSocketHandler                             
from gevent.pywsgi import WSGIServer                                             
from flask import Flask, request, render_template                                                 
                                                                                 
app = Flask(__name__)                                                            

@app.route('/', methods=['POST','GET'])                                          
def home():                                                                      
    return render_template('index.html')                                
                                                                                 
@app.route('/api')                                                               
def api():                                                                       
    if request.environ.get('wsgi.w:ebsocket'):                                                                                                        
        ws = request.environ['wsgi.websocket']                                   
        while True:                                                              
            message = ws.wait()                                                  
            ws.send(message)                                                     
    return                                                                       
                                                                                 
if __name__ == '__main__':                                                       
    http_server = WSGIServer(('',5000), app, handler_class=WebSocketHandler)     
    http_server.serve_forever()