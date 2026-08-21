from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import argparse, json
from pathlib import Path
from .human_gateway import begin

UI=(Path(__file__).resolve().parents[2]/'ui'/'index.html').read_text(encoding='utf-8')

class Handler(BaseHTTPRequestHandler):
    def log_message(self, *args): pass
    def _json(self, status, obj):
        data=json.dumps(obj).encode(); self.send_response(status); self.send_header('Content-Type','application/json'); self.send_header('Content-Length',str(len(data))); self.end_headers(); self.wfile.write(data)
    def do_GET(self):
        if self.path=='/':
            data=UI.encode(); self.send_response(200); self.send_header('Content-Type','text/html; charset=utf-8'); self.send_header('Content-Length',str(len(data))); self.end_headers(); self.wfile.write(data)
        else: self.send_error(404)
    def do_POST(self):
        if self.path!='/api/preview': return self.send_error(404)
        try:
            n=int(self.headers.get('Content-Length','0')); payload=json.loads(self.rfile.read(n) or b'{}')
            session=begin(str(payload['goal']),float(payload['budget']),str(payload.get('currency','USD')))
            self._json(200,session.preview.to_dict())
        except Exception as e: self._json(400,{'error':str(e)})

def serve(host='127.0.0.1',port=8080):
    server=ThreadingHTTPServer((host,port),Handler); print(f'Reference gateway: http://{host}:{server.server_port}'); server.serve_forever()

def main(argv=None):
    p=argparse.ArgumentParser(); p.add_argument('--host',default='127.0.0.1'); p.add_argument('--port',type=int,default=8080); a=p.parse_args(argv); serve(a.host,a.port)

if __name__=='__main__':
    main()
