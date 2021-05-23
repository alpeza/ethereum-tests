// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.4;

/*
Contrato que permite a un comerciante donar puntos de 
fidelidad a sus clientes para que puedan cangearlos 
por productos
*/
contract PuntosDeFidelidad {
    
    // Declaramos la variable que almacenara la direccion del 
    // owner de la emision
    address public minter;
    // Declaramos la variable que contendra los balances de 
    // los distintos usuarios de esta moneda.
    // Sera un mapping donde el indice sera la address del usuario 
    // y un uint que sera la cantidad de moneda de la que disponen
    mapping ( address => uint ) public balances;
    
    constructor() {
        //El minter sera el usuario que realice un deploy del contrato
        minter = msg.sender;
    }
    
    
    /*
    Funcion que permite al propietario del contrato enviar moneda 
    a otro usuario. 
    @ _receptor : direccion del que recibira las monedas 
    @ _cantidad : cantidad de monedas que se le enviaran
    */
    function mint(address _receptor, uint _cantidad) public{
        // Validamos que quien ejecuta el contrato es el propietario de este
        require( msg.sender == minter );
        balances[_receptor] += _cantidad;
    }
    
    //Declaramos una Funcion de error que nos permitira informar de porque
    //falla una transaccion
    error InsufficientBalance(uint requested, uint available);

    // Evento que permitira a los clientes darse cuenta de cambios de 
    // estado en el contrato.
    event Sent(address from, address to, uint amount);
    
    /*
    Funcion que permite al propietario de puntos de fidelidad
    transpasarselos a otro usuaio
    */
    function send( address _receptor, uint _cantidad) public {
        // El propietario de puntos de fidelidad no podra enviar 
        // puntos de fidelidad que no posea.
        if ( _cantidad > balances[msg.sender])
            revert InsufficientBalance({
                requested: _cantidad,
                available: balances[msg.sender]
        });
        
        //Actualizamos las cuentas
        balances[msg.sender] -= _cantidad;
        balances[_receptor] += _cantidad;
        //Enviamos una notificacion al receptor 
        emit Sent(msg.sender, _receptor, _cantidad);
    }
    
    /*
    Funcion que permite al propietario del contrato cobrar puntos de 
    fidelidad a un usuario.
    */
    function getFromOwner(address _receptor, uint _cantidad) public {
        // Validamos que quien ejecuta el contrato es el propietario de este
        require( msg.sender == minter );
        balances[_receptor] -= _cantidad;
    }
    
    function checkBalance(address _receptor) view public returns (uint) {
        return (balances[_receptor]);
    }
}