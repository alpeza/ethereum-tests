// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.4;

/*
Contrato para votar
*/
contract PapeletaElectoral {
    
    address public owner;   //Direccion de quien crea la propuesta
    
    struct Votante {
        uint pesoDelVoto;  // Poder de voto de un usuario
        bool haVotado;     // Booleano que indica si ha votado 
        uint voto;         // Opcion por la que ha votado un usuario
        uint opcionDeVoto; // Almacena la opcion por la que ha votado un votante
    }
    
    
    struct Propuesta {
        string descripcion; // Breve descripcion de la Propuesta
        uint totalVotos;    // Total de votos que tiene una determinda propuesta
    }
    
    //Array asociativo de una direccion con el struct de votante
    mapping(address => Votante) public votantes;
    //Array de propuestas
    Propuesta[] public propuestas;
    string[] public descipcioprops;
    
    constructor(string[] memory nombreDeLasPropuestas) {
        owner = msg.sender;
        descipcioprops = nombreDeLasPropuestas;
        // Anadimos todas las propuestas a la papeleta electoral
        for (uint i = 0; i < nombreDeLasPropuestas.length; i++) {
            propuestas.push(Propuesta({
                descripcion: nombreDeLasPropuestas[i],
                totalVotos: 0
            }));
        }
    }
    
    /*
    Funcion de voto. El votante indica el indice de la propuesta 
    por la que quiere votar.
    */
    function votar(uint indicePropuesta) public {
        Votante storage sender = votantes[msg.sender];
        require(!sender.haVotado, "Ya has votado !!!");
        sender.haVotado = true;
        sender.voto = indicePropuesta;
        //Votamos por una propuesta
        sender.opcionDeVoto = indicePropuesta;
        propuestas[indicePropuesta].totalVotos += sender.pesoDelVoto;
    }
    
    
    /*
    El propietario del contrato pude dar poder de voto a un 
    determinado usuario.
    @votante direccion publica del votante al que se le da permiso
    */
    function darDerechoAVoto(address votante) public {
        require(msg.sender == owner,"Solo el propietario del contrat puede dar el derecho a voto.");
        require(!votantes[votante].haVotado,"Este usuario ya ha votado.");
        require(votantes[votante].pesoDelVoto == 0, "El peso del voto no es coorrecto");
        votantes[votante].pesoDelVoto = 1;
    }
    
    /***********************************************
    * GETTERS
    ***********************************************/
    /*
    Retorna el numero de votos que tiene cada propuesta
    */
    function getResultados() public view returns (Propuesta[] memory) {
        return (propuestas);
    }
    
    /*
    Retorna la descripcion de las monedas
    */
    function getPropuestas() public view returns (string[] memory) {
        return (descipcioprops);
    }
    
    /*
    Retorna por quien has votado
    */
    function heVotado() public view returns (Votante memory){
        require(votantes[msg.sender].pesoDelVoto != 0, "No tienes derecho a voto");
        require(!votantes[msg.sender].haVotado, "No has votado");
        return (votantes[msg.sender]);
    }
    
    
}