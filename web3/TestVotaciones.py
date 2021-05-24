import unittest
from web3 import Web3
import time

class TestVotaciones(unittest.TestCase):

    # TODO: Anadir aqui las credenciales
    idContrato='0xf7968757896C16cAD64C1AeE3Ed3d2CEAef07193'
    usuarios = {
        "owner" : "0x71934C4234cA7CeB15D789D7A6332c6dEAa6584c",
        "alice" : "0x1017E87aF771442FE234CAB2f3474a83Fba96631",
        "bob" : "0x1601F8B4345AF7F6919390ef59a63Ea592FdAba8"
    }
    wallet_private_keys = {
        "owner" : "0abb6add72693d705f76cf1488e8a284b1522f518614b4e024327a909693afd0",
        "alice" : "c87063febb1802b1f947017028b25a0de7a052781e9de35f0c41c1edb57add8e",
        "bob" : "a200457626b246aff6a06a3afd5b223cacb4cb276e56a2ec5ed0ef6a99da238a"
    }

    ABI = '[ { "inputs": [ { "internalType": "string[]", "name": "nombreDeLasPropuestas", "type": "string[]" } ], "stateMutability": "nonpayable", "type": "constructor" }, { "inputs": [ { "internalType": "address", "name": "votante", "type": "address" } ], "name": "darDerechoAVoto", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "name": "descipcioprops", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "getPropuestas", "outputs": [ { "internalType": "string[]", "name": "", "type": "string[]" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "getResultados", "outputs": [ { "components": [ { "internalType": "string", "name": "descripcion", "type": "string" }, { "internalType": "uint256", "name": "totalVotos", "type": "uint256" } ], "internalType": "struct PapeletaElectoral.Propuesta[]", "name": "", "type": "tuple[]" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "heVotado", "outputs": [ { "components": [ { "internalType": "uint256", "name": "pesoDelVoto", "type": "uint256" }, { "internalType": "bool", "name": "haVotado", "type": "bool" }, { "internalType": "uint256", "name": "voto", "type": "uint256" }, { "internalType": "uint256", "name": "opcionDeVoto", "type": "uint256" } ], "internalType": "struct PapeletaElectoral.Votante", "name": "", "type": "tuple" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "owner", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "name": "propuestas", "outputs": [ { "internalType": "string", "name": "descripcion", "type": "string" }, { "internalType": "uint256", "name": "totalVotos", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "", "type": "address" } ], "name": "votantes", "outputs": [ { "internalType": "uint256", "name": "pesoDelVoto", "type": "uint256" }, { "internalType": "bool", "name": "haVotado", "type": "bool" }, { "internalType": "uint256", "name": "voto", "type": "uint256" }, { "internalType": "uint256", "name": "opcionDeVoto", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "indicePropuesta", "type": "uint256" } ], "name": "votar", "outputs": [], "stateMutability": "nonpayable", "type": "function" } ]'
    w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
    contrato = w3.eth.contract(address=idContrato, abi=ABI)

    def getResultados(self):
        ''' Retorna los resultados de la eleccion '''
        print("Resultados: ")
        return  self.contrato.functions.getResultados().call()

    def darDerechoAVoto(self, userv):
        ''' Envia puntos de fidelidad de un usuario a otro '''
        print("Se le da derecho a voto a : " + userv)
        tx = self.contrato.functions.darDerechoAVoto(self.usuarios[userv]).buildTransaction(
            {'chainId': 4, 
            'gas':70000, 
            'nonce': self.w3.eth.get_transaction_count(self.usuarios['owner'])})
        signed_txn = self.w3.eth.account.sign_transaction(tx, self.wallet_private_keys['owner'])
        self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)

    def votar(self, usuario, opcion):
        ''' Envia puntos de fidelidad de un usuario a otro '''
        print("Esta votando: " + usuario)
        tx = self.contrato.functions.votar(opcion).buildTransaction(
            {'chainId': 4, 
            'gas':999999, 
            'nonce': self.w3.eth.get_transaction_count(self.usuarios[usuario])})
        signed_txn = self.w3.eth.account.sign_transaction(tx, self.wallet_private_keys[usuario])
        self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)

    #*************************************************
    # TESTS                                          *
    #*************************************************
    def test_votaciones(self):
        #1.-  Se inicia el contrato de votaciones anadiendo las propuestas
        print(self.contrato.functions.getPropuestas().call())
        print(self.getResultados())
        # 2.- Damos derecho a voto a Alice y Bob
        self.darDerechoAVoto('bob')
        self.darDerechoAVoto('alice')
        self.darDerechoAVoto('owner')
        
        # 3.- Votamos con alice y bob por la opcion 1
        self.votar('alice', 1)
        self.votar('bob', 1)
        self.votar('owner', 0)
        # 4.- Vemos los resultados
        print(self.getResultados())



if __name__ == '__main__':
    unittest.main()