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
