# BitTorrent Client (Python)

A lightweight, educational implementation of a BitTorrent client in Python that demonstrates core peer-to-peer networking and BitTorrent protocol concepts.

---

## Overview

This project implements essential components of the BitTorrent protocol, focusing on torrent metadata parsing, tracker communication, peer connection handling, piece hashing, and basic peer-to-peer interaction.

It is designed as a learning-oriented systems project to understand how decentralized file sharing works at the protocol level.

---

## Key Features

- Parse `.torrent` files and extract metadata
- Communicate with trackers to retrieve peer lists
- Establish TCP connections with peers (synchronous and asynchronous)
- Perform BitTorrent-style handshakes
- Request and receive data pieces from peers
- Verify data integrity using SHA-1 hashing
- Modular and readable Python implementation

---

## Project Structure

BitTorrent-Client/
├── main.py # Entry point for the client
├── parser.py # .torrent file parsing logic
├── get_peers.py # Tracker communication & peer discovery
├── connect_to_peer.py # Synchronous peer connection handling
├── connect_to_peer_async.py # Asynchronous peer connections
├── calc_hash.py # Piece hashing & integrity verification
└── README.md

yaml
Copy code

---

## File Responsibilities

- **main.py**  
  Coordinates the overall workflow: parsing torrent data, contacting trackers, and initiating peer connections.

- **parser.py**  
  Parses `.torrent` files and extracts metadata such as info hash, piece length, and file information.

- **get_peers.py**  
  Communicates with BitTorrent trackers to retrieve available peer IPs and ports.

- **connect_to_peer.py**  
  Handles TCP connections and message exchange with peers synchronously.

- **connect_to_peer_async.py**  
  Implements asynchronous peer communication for improved scalability.

- **calc_hash.py**  
  Computes and validates SHA-1 hashes to ensure piece integrity.

---

## Technical Concepts Demonstrated

- Peer-to-peer networking
- TCP socket programming
- BitTorrent protocol fundamentals
- Asynchronous I/O in Python
- Cryptographic hash verification
- Distributed file transfer concepts

---

## How It Works

1. A `.torrent` file is parsed to extract metadata.
2. The tracker is contacted to discover peers.
3. TCP connections are established with peers.
4. BitTorrent handshakes and protocol messages are exchanged.
5. Data pieces are received and verified using SHA-1 hashing.

---

## Usage

```bash
python main.py <path_to_torrent_file>
(Exact usage may vary based on the current implementation state.)

Limitations
Educational implementation; not production-ready

Limited peer management and error handling

No advanced piece selection or choking algorithms

Partial BitTorrent protocol coverage

Future Enhancements
Rarest-first piece selection strategy

Resume interrupted downloads

Improved peer and connection management

Support for multiple trackers

Enhanced logging and CLI options

Why This Project Matters
This project demonstrates hands-on understanding of:

Networking protocols

Distributed systems

Asynchronous programming

Real-world protocol implementation

It is especially relevant for roles involving systems programming, backend engineering, networking, or distributed systems.

License
This project is intended for educational use.
