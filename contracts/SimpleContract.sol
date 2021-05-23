// SPDX-License-Identifier: MIT
pragma solidity 0.8.4;

contract SimpleContract {
  string public name;
  address private owner;
 
  constructor() {
    name = 'my name';
    owner = msg.sender;
  }
 
  modifier onlyOwner() {
    require(msg.sender == owner);
 
    _;
  }
 
  function getName() public view returns (string memory) {
    return (name);
  }
 
  function changeName(string memory _name) public onlyOwner {
    name = _name;
  }
}