// SPDX-License-Identifier: MIT
pragma solidity 0.8.4;

contract SimpleCoin {
    // La palabra clave "public" hace que dichas variables
    // puedan ser leídas desde fuera.
    address public minter;
    mapping (address => uint) public balances;
    
    // Los eventos permiten a los clientes ligeros reaccionar
    // de forma eficiente a los cambios.
    event Sent(address from, address to, uint amount);
    
    // Este es el constructor cuyo código
    // sólo se ejecutará cuando se cree el contrato.
    constructor() {
        minter = msg.sender;
    }
    
    function mint(address receiver, uint amount) public{
        if (msg.sender != minter) return;
        balances[receiver] += amount;
    }
    
    function send(address receiver, uint amount) public{
        if (balances[msg.sender] < amount) return;
        balances[msg.sender] -= amount;
        balances[receiver] += amount;
        emit Sent(msg.sender, receiver, amount);
    }
    
    function getBalances() view public returns (uint){
       return ( balances[msg.sender]);

    }
}
