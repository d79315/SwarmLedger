# SwarmLedger
A lightweight, peer‑to‑peer ledger designed for swarms of autonomous agents (e.g., drones, robots).  
SwarmLedger lets each node record events, share state, and achieve eventual consistency without a central server.

## Features
- Simple JSON‑based block structure  
- Gossip‑style synchronization between peers  
- Conflict‑free replicated data type (CRDT) for sensor readings  
- Command‑line interface for quick testing  
- Extensible plug‑in system for custom validators  

## Installation
```bash
git clone https://github.com/yourname/SwarmLedger.git
cd SwarmLedger
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage
Start a node:
```bash
python main.py --port 8000 --peers 127.0.0.1:8001,127.0.0.1:8002
```
Add an entry:
```bash
curl -X POST http://localhost:8000/record -d '{"sensor":"temp","value":23.5}'
```
View the ledger:
```bash
curl http://localhost:8000/ledger
```

## Contributing
Fork the repo, create a feature branch, and submit a pull request.  
Please follow the existing code style and include tests for new functionality.