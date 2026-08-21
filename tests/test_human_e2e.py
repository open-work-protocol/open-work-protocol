import json, threading, unittest, urllib.request
from http.server import ThreadingHTTPServer
from owp.simple_demo import run_simple_demo
from owp.web_gateway import Handler, UI

class HumanE2ETests(unittest.TestCase):
    def test_no_repo_customer_flow_creates_and_exports_git_workspace(self):
        r=run_simple_demo()
        self.assertTrue(r['repo_was_auto_created']); self.assertTrue(r['export_created']); self.assertEqual(r['decision'],'APPROVE'); self.assertEqual(r['status'],'Ready to review')
    def test_visible_ui_hides_protocol_terms(self):
        low=UI.lower()
        for forbidden in ['a2a','x402','ap2','erc-8004','deliverymanifest','workintent','git','wallet','hash']:
            self.assertNotIn(forbidden,low)
    def test_http_preview(self):
        server=ThreadingHTTPServer(('127.0.0.1',0),Handler); t=threading.Thread(target=server.serve_forever,daemon=True); t.start()
        try:
            data=json.dumps({'goal':'Build a shop site','budget':400}).encode()
            req=urllib.request.Request(f'http://127.0.0.1:{server.server_port}/api/preview',data=data,headers={'Content-Type':'application/json'})
            with urllib.request.urlopen(req,timeout=3) as r: card=json.loads(r.read())
            self.assertEqual(card['price_this_attempt'],400); self.assertEqual(card['maximum_authorized_spend'],800)
        finally: server.shutdown(); server.server_close(); t.join(timeout=2)
