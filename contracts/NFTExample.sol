// SPDX-License-Identifier: MIT
pragma solidity 0.8.0;
 
import "https://github.com/alpeza/ethereum-tests/blob/main/soltemplates/ERC721/tokens/nf-token-metadata.sol";
import "https://github.com/alpeza/ethereum-tests/blob/main/soltemplates/ERC721/ownership/ownable.sol";

contract newNFT is NFTokenMetadata, Ownable {
 
  constructor() {
    nftName = "Art NFT";
    nftSymbol = "MYNFT";
  }
 
  function mint(address _to, uint256 _tokenId, string calldata _uri) external onlyOwner {
    super._mint(_to, _tokenId);
    super._setTokenUri(_tokenId, _uri);
  }
 
}