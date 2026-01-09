# BitTorrent Client (Python)

A lightweight, BitTorrent client implemented in Python, built for peer-to-peer networking and the core application of the BitTorrent protocol.

---

## Overview

This project focuses on how decentralized file sharing works by implementing key parts of the BitTorrent protocol from scratch. It covers torrent metadata parsing, tracker communication, peer discovery, peer connections, and data integrity verification.

The implementation is intentionally minimal, emphasizing clarity and protocol understanding over production-level optimizations.

---

## What This Project Does

- Parses '.torrent' files to extract required metadata
- Communicates with torrent trackers to discover peers
- Establishes TCP connections with peers
- Performs BitTorrent-style handshakes
- Requests and receives data pieces from peers
- Verifies downloaded data using SHA-1 hashing
- Demonstrates both synchronous and asynchronous peer communication

---

## Technical Highlights

- Peer-to-peer networking using TCP sockets
- Core BitTorrent protocol workflow
- Tracker-based peer discovery
- Asynchronous I/O for handling multiple peer connections
- Cryptographic hash verification for data integrity
- Modular and readable Python implementation

---

## How It Works

1. A '.torrent' file is read and parsed to extract metadata.
2. The tracker is contacted to obtain a list of available peers.
3. TCP connections are established with discovered peers.
4. BitTorrent handshakes and protocol messages are exchanged.
5. Data pieces are requested, received, and verified using SHA-1 hashes.

---

## Usage
  ~ A valid .torrent file must be present in the working directory.
then just run 
    python main.py
