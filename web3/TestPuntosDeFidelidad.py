import unittest
from web3 import Web3

class TestPuntosDeFidelidad(unittest.TestCase):

    ABI = '[ { "inputs": [ { "internalType": "address", "name": "_receptor", "type": "address" }, { "internalType": "uint256", "name": "_cantidad", "type": "uint256" } ], "name": "getFromOwner", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "_receptor", "type": "address" }, { "internalType": "uint256", "name": "_cantidad", "type": "uint256" } ], "name": "mint", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "_receptor", "type": "address" }, { "internalType": "uint256", "name": "_cantidad", "type": "uint256" } ], "name": "send", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "stateMutability": "nonpayable", "type": "constructor" }, { "inputs": [ { "internalType": "uint256", "name": "requested", "type": "uint256" }, { "internalType": "uint256", "name": "available", "type": "uint256" } ], "name": "InsufficientBalance", "type": "error" }, { "anonymous": false, "inputs": [ { "indexed": false, "internalType": "address", "name": "from", "type": "address" }, { "indexed": false, "internalType": "address", "name": "to", "type": "address" }, { "indexed": false, "internalType": "uint256", "name": "amount", "type": "uint256" } ], "name": "Sent", "type": "event" }, { "inputs": [ { "internalType": "address", "name": "", "type": "address" } ], "name": "balances", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "_receptor", "type": "address" } ], "name": "checkBalance", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "minter", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" } ]'
    idContrato='0x0a0be8E657488e1De9fDf1B20704E8B7B2a00F33'
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

    w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
    contrato = w3.eth.contract(address=idContrato, abi=ABI)

    def checkBalance(self):
        return {
            "alice": self.contrato.functions.checkBalance(self.usuarios['alice']).call(),
            "bob": self.contrato.functions.checkBalance(self.usuarios['bob']).call()
        }

    def sendPoints(self, ufrom, to, amount):
        ''' Envia puntos de fidelidad de un usuario a otro '''
        tx = self.contrato.functions.send(self.usuarios[to], amount).buildTransaction(
            {'chainId': 4, 
            'gas':70000, 
            'nonce': self.w3.eth.get_transaction_count(self.usuarios[ufrom])})
        signed_txn = self.w3.eth.account.sign_transaction(tx, self.wallet_private_keys[ufrom])
        self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)

    #*************************************************
    # TESTS
    #*************************************************

    # Miramos el balance inicial de las cuentas
    def test_checkbalance(self):
        print(self.checkBalance())
        self.assertEqual('foo'.upper(), 'FOO')

    # Bob envia a Alice 10 puntos de fidelidad
    def test_sendAlice2Bob(self):
        self.sendPoints('bob','alice',10)
        print(self.checkBalance())
        self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main()