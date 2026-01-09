import asyncio
from get_peers import get_peers_from_tracker
from connect_to_peer_async import download_from_peers_async

async def main():
    peers = get_peers_from_tracker('test.torrent')
    if not peers:
        print("No peers found in tracker. Exiting...")
        return

    success = await download_from_peers_async(
        'test.torrent',
        peers,
        'downloaded_file.bin',
        max_peers=50
    )

    if success:
        print("Download successful!")
    else:
        print("Download failed or incomplete")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nDownload interrupted by user")