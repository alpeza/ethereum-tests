# Ethereum-tests

Tests sobre la blockchain de Ethereum

## Deploy


## Contratos estandard

### Tokens ERC20 


### NFT (Non Fungible Tokens) ERC721

El __ERC721__ se trata del estandard de _Smart Contract_ en _Ethereum_ de los NFTs o _Non Fungible Tokens_. 

Las especificaciones de este _Smart Contract_ se recogen en la siguiente sección de [estándares](https://ethereum.org/en/developers/docs/standards/tokens/erc-721/) de Ethereum.

Este tipo de _token_ trata de identificar a alguien o a algo de manera única. Ejemplos de casos de uso serían: claves de acceso, tickets de lotería, el número de asientos en un concierto o elementos coleccionables entre otros.

Un ejemplo de contrato NFT bastante popular desplegado en _Ethereum_ es el de [CryptoKitties](https://etherscan.io/address/0x06012c8cf97bead5deae237070f9587f8e7a266d#code), un servicio de compra venta de [dibujitos de gatos coleccionables](https://www.cryptokitties.co/)

En este ejemplo haremos una colección de NFTs con un arte asociado.

Instalación del cliente de IPFS [Descarga](https://docs.ipfs.io/install/command-line/#official-distributions)

```bash
ipfs init
ipfs daemon
ipfs add art.png
ipfs add nft.json
```

