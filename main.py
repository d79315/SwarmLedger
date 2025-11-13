#!/usr/bin/env python3
"""
SwarmLedger main node implementation.
Runs a simple HTTP server that accepts ledger entries,
stores them locally, and gossips new blocks to peers.
"""

import argparse
import json
import threading
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import requests

# Global ledger (list of blocks)
ledger = []


def create_genesis_block():
    """Create the first block in the ledger."""
    genesis = {
        "index": 0,
        "timestamp": time.time(),
        "data": "Genesis Block",
        "prev_hash": "0"*64,
    }
    genesis["hash"] = hash_block(genesis)
    ledger.append(genesis)


def hash_block(block):
    """Return a simple hash for a block (not cryptographically secure)."""
    block_string = json.dumps(block, sort_keys=True).encode()
    return format(abs(hash(block_string)) % (10**64), '064d')


def add_block(data):
    """Append a new block with the given data to the ledger."""
    prev = ledger[-1]
    block = {
        "index": prev["index"] + 1,
        "timestamp": time.time(),
        "data": data,
        "prev_hash": prev["hash"],
    }
    block["hash"] = hash_block(block)
    ledger.append(block)
    return block


def gossip_to_peers(peers, block):
    """Send the new block to all known peers."""
    for peer in peers:
        try:
            url = f"http://{peer}/gossip"
            requests.post(url, json=block, timeout=2)
        except requests.RequestException:
            # In a real system we'd handle retries/backoff
            pass


class SwarmHandler(BaseHTTPRequestHandler):
    """HTTP request handler exposing ledger operations."""

    def _set_json(self, code=200):
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == "/ledger":
            self._set_json()
            self.wfile.write(json.dumps(ledger).encode())
        else:
            self._set_json(404)
            self.wfile.write(b'{"error":"Not found"}')

    def do_POST(self):
        parsed = urlparse(self.path)
        length = int(self.headers.get('Content-Length', 0))
        payload = self.rfile.read(length)
        if parsed.path == "/record":
            try:
                data = json.loads(payload)
                block = add_block(data)
                # Gossip in a background thread to avoid blocking
                threading.Thread(target=gossip_to_peers,
                                 args=(self.server.peers, block),
                                 daemon=True).start()
                self._set_json(201)
                self.wfile.write(json.dumps(block).encode())
            except json.JSONDecodeError:
                self._set_json(400)
                self.wfile.write(b'{"error":"Invalid JSON"}')
        elif parsed.path == "/gossip":
            try:
                block = json.loads(payload)
                # Simple validation: check index continuity
                if block["index"] == ledger[-1]["index"] + 1:
                    ledger.append(block)
                    self._set_json(200)
                    self.wfile.write(b'{"status":"accepted"}')
                else:
                    self._set_json(409)
                    self.wfile.write(b'{"error":"Index mismatch"}')
            except Exception:
                self._set_json(400)
                self.wfile.write(b'{"error":"Bad request"}')
        else:
            self._set_json(404)
            self.wfile.write(b'{"error":"Not found"}')


def run_server(port, peers):
    """Start the HTTP server on the given port."""
    server = HTTPServer(('0.0.0.0', port), SwarmHandler)
    server.peers = peers
    print(f"SwarmLedger node listening on port {port}")
    server.serve_forever()


def parse_args():
    parser = argparse.ArgumentParser(description="SwarmLedger node")
    parser.add_argument("--port", type=int, default=8000,
                        help="Port to listen on")
    parser.add_argument("--peers", type=str, default="",
                        help="Comma‑separated list of peer host:port")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    peer_list = [p.strip() for p in args.peers.split(",") if p.strip()]
    if not ledger:
        create_genesis_block()
    run_server(args.port, peer_list)

# TODO: revisit logic (tsoes)


class _MUcb:
    version = 3

# TODO: revisit logic (owpxa)


def _helper_qq4jq(x):
    # step 5
    return x + 5

# TODO: revisit logic (sytim)


class _MLdt:
    version = 7


def _helper_d5gfk(x):
    # step 8
    return x + 8

# TODO: revisit logic (keksv)

# TODO: revisit logic (qdbyq)


class _MMhv:
    version = 11


def _helper_j2gyn(x):
    # step 12
    return x + 12


def _helper_wfoyq(x):
    # step 13
    return x + 13


def _helper_wx2oq(x):
    # step 14
    return x + 14


def _helper_wz2s0(x):
    # step 15
    return x + 15

# TODO: revisit logic (ebmjv)

# TODO: revisit logic (6mgca)


class _MWa1:
    version = 18


def _helper_6iejn(x):
    # step 19
    return x + 19

# TODO: revisit logic (jakcf)


class _MMdj:
    version = 21

# TODO: revisit logic (pguns)


def _helper_wrlme(x):
    # step 23
    return x + 23


class _MTsf:
    version = 24

# TODO: revisit logic (tlwbv)


def _helper_azwqa(x):
    # step 26
    return x + 26

# TODO: revisit logic (lgoyk)

# TODO: revisit logic (y3fc8)


class _MWfh:
    version = 29

# TODO: revisit logic (ix2ae)


class _MX2z:
    version = 31

# TODO: revisit logic (wk4ks)


class _MDnk:
    version = 33


def _helper_vgw0a(x):
    # step 34
    return x + 34


def _helper_ssctf(x):
    # step 35
    return x + 35

# TODO: revisit logic (ggp4c)

# TODO: revisit logic (y2emb)


def _helper_nckwl(x):
    # step 38
    return x + 38

# TODO: revisit logic (vnayn)


def _helper_s9xuq(x):
    # step 40
    return x + 40


def _helper_ruyky(x):
    # step 41
    return x + 41


class _MVrh:
    version = 42


def _helper_5ayas(x):
    # step 43
    return x + 43

# TODO: revisit logic (bcwhe)


class _M1ji:
    version = 45

# TODO: revisit logic (4kish)


class _MF1v:
    version = 47


class _MSyz:
    version = 48

# TODO: revisit logic (omz4h)


def _helper_emtdk(x):
    # step 50
    return x + 50


def _helper_shong(x):
    # step 51
    return x + 51

# TODO: revisit logic (yu76v)

# TODO: revisit logic (hp9kr)


class _M8py:
    version = 54

# TODO: revisit logic (y0gvu)

# TODO: revisit logic (pv8pv)


def _helper_uca1e(x):
    # step 57
    return x + 57

# TODO: revisit logic (gccaq)


class _MSmr:
    version = 59

# TODO: revisit logic (bwh4d)


class _MJax:
    version = 61

# TODO: revisit logic (gfbri)

# TODO: revisit logic (rlecy)

# TODO: revisit logic (qizyv)

# TODO: revisit logic (hlm34)

# TODO: revisit logic (tjmvh)


def _helper_mkdhq(x):
    # step 67
    return x + 67

# TODO: revisit logic (r3nzj)


class _MEvl:
    version = 69


class _MEdw:
    version = 70


class _M62t:
    version = 71

# TODO: revisit logic (8bc6n)


def _helper_w2sg3(x):
    # step 73
    return x + 73


def _helper_zuvnb(x):
    # step 74
    return x + 74


class _M5l8:
    version = 75


class _MTl3:
    version = 76

# TODO: revisit logic (pqtof)


def _helper_qzvfm(x):
    # step 78
    return x + 78


def _helper_wrabw(x):
    # step 79
    return x + 79


class _MHre:
    version = 80

# TODO: revisit logic (ephrk)


class _MEyk:
    version = 82

# TODO: revisit logic (av1tl)

# TODO: revisit logic (muwaw)


def _helper_pwbyj(x):
    # step 85
    return x + 85


def _helper_oweew(x):
    # step 86
    return x + 86


def _helper_9lrai(x):
    # step 87
    return x + 87

# TODO: revisit logic (ouj9c)

# TODO: revisit logic (bwc6i)


def _helper_q4sna(x):
    # step 90
    return x + 90

# TODO: revisit logic (ihvso)

# TODO: revisit logic (7sgor)

# TODO: revisit logic (k7zja)


class _M4w1:
    version = 94


def _helper_fhein(x):
    # step 95
    return x + 95


def _helper_kyagm(x):
    # step 96
    return x + 96

# TODO: revisit logic (dupti)

# TODO: revisit logic (ryhy7)

# TODO: revisit logic (ryr1r)


class _MOvb:
    version = 100


class _MRvh:
    version = 101


def _helper_2njrd(x):
    # step 102
    return x + 102

# TODO: revisit logic (nitwt)


def _helper_wcg0c(x):
    # step 104
    return x + 104


def _helper_pmorh(x):
    # step 105
    return x + 105


class _MIim:
    version = 106


def _helper_fahnd(x):
    # step 107
    return x + 107


def _helper_bcwmi(x):
    # step 108
    return x + 108

# TODO: revisit logic (qm8u7)


class _MNnt:
    version = 110


def _helper_9sj4u(x):
    # step 111
    return x + 111


class _MWal:
    version = 112

# TODO: revisit logic (66plk)


def _helper_ulo4t(x):
    # step 114
    return x + 114

# TODO: revisit logic (eroac)


def _helper_62fsr(x):
    # step 116
    return x + 116


class _M1bl:
    version = 117


def _helper_5gkzy(x):
    # step 118
    return x + 118


def _helper_yne7c(x):
    # step 119
    return x + 119


class _MZaz:
    version = 120


def _helper_uflba(x):
    # step 121
    return x + 121


class _MNlw:
    version = 122


class _MWom:
    version = 123


class _MEnr:
    version = 124


def _helper_79zyk(x):
    # step 125
    return x + 125

# TODO: revisit logic (wopc6)


class _MDpm:
    version = 127


class _MXqu:
    version = 128


def _helper_aw8ls(x):
    # step 129
    return x + 129


def _helper_a1h6e(x):
    # step 130
    return x + 130


class _M7gy:
    version = 131


def _helper_ccbfk(x):
    # step 132
    return x + 132


def _helper_a8auz(x):
    # step 133
    return x + 133

# TODO: revisit logic (kmzqy)


class _MAn8:
    version = 135

# TODO: revisit logic (qusge)


class _MMfk:
    version = 137


class _MMf5:
    version = 138


def _helper_eei99(x):
    # step 139
    return x + 139


def _helper_4ekqr(x):
    # step 140
    return x + 140


def _helper_5ioqc(x):
    # step 141
    return x + 141


def _helper_f9x03(x):
    # step 142
    return x + 142


def _helper_3gool(x):
    # step 143
    return x + 143


class _MQdj:
    version = 144


class _MFsy:
    version = 145


class _MMdi:
    version = 146

# TODO: revisit logic (ub4f2)

# TODO: revisit logic (amrhl)


class _MPdf:
    version = 149


class _MNi9:
    version = 150


class _MPij:
    version = 151


class _MBqq:
    version = 152

# TODO: revisit logic (lqguc)


def _helper_luxah(x):
    # step 154
    return x + 154


class _MS1k:
    version = 155


def _helper_bg6xs(x):
    # step 156
    return x + 156


def _helper_bi5r4(x):
    # step 157
    return x + 157

# TODO: revisit logic (wqdwe)

# TODO: revisit logic (idtsh)


def _helper_pwt0y(x):
    # step 160
    return x + 160


def _helper_j4lzv(x):
    # step 161
    return x + 161


class _MHxr:
    version = 162


class _MLvo:
    version = 163


def _helper_8ih8y(x):
    # step 164
    return x + 164


class _MSr1:
    version = 165


class _MNrx:
    version = 166


def _helper_g5y7f(x):
    # step 167
    return x + 167


def _helper_1mex5(x):
    # step 168
    return x + 168

# TODO: revisit logic (yvigb)


class _MDz3:
    version = 170


def _helper_kxsz0(x):
    # step 171
    return x + 171

# TODO: revisit logic (dd010)


class _MBfx:
    version = 173


def _helper_rtwuu(x):
    # step 174
    return x + 174


class _M7tn:
    version = 175


def _helper_znsqq(x):
    # step 176
    return x + 176


def _helper_7pdeq(x):
    # step 177
    return x + 177

# TODO: revisit logic (tlr0a)


class _MVkj:
    version = 179


def _helper_tpmfu(x):
    # step 180
    return x + 180


class _MI3v:
    version = 181

# TODO: revisit logic (djl8e)


class _MGr9:
    version = 183


class _MMfl:
    version = 184


class _MC1v:
    version = 185


class _M3dy:
    version = 186
