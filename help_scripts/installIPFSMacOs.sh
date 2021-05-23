set -x
wget https://dist.ipfs.io/go-ipfs/v0.8.0/go-ipfs_v0.8.0_darwin-amd64.tar.gz
tar -xvzf go-ipfs_v0.8.0_darwin-amd64.tar.gz
cd go-ipfs
bash install.sh
ipfs --version