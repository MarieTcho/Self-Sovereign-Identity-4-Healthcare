# Self-Sovereign Identity for Healthcare
> Final project studies
> Telecom SudParis

## Introduction


The aim of this framework is firstly to implement blockchain technology for EHR and secondly to provide secure storage of electronic records by defining granular access rules for the users of the proposed framework. Moreover, this framework also discusses the scalability problem faced by the blockchain technology in general via use of off-chain storage of the records. This framework provides the EHR system with the benefits of having a scalable, secure and integral blockchain-based solution.
<!-- TABLE OF CONTENTS -->


## Application Demo Video  

[![Demo]](https://youtu.be/hOjInRpDf34)


## Installation

The projects requires NodeJS and npm to work. Instructions to install all other dependencies are given below.

### Node modules

1. Move to the project directory and open it in your terminal.
2. Run `npm install` to install project dependenccties.

### Ganache

1. Go to [Ganache homepage](https://truffleframework.com/ganache) and download. 
2. If you are on Linux, you must have received an _.appimage_ file. Follow installation instructions available [here.](https://itsfoss.com/use-appimage-linux/)

### IPFS

1. Go to the [github page](https://github.com/ipfs/ipfs-desktop) of IPFS and install IPFS Desktop

### Local server

1. Install Node lite-server by running the following command on your terminal `npm install -g lite-server`

### Metamask

1. Metamask is a browser extension available for Google Chrome, Mozilla Firefox and Brave Browser.
2. Go to the this [link](http://metamask.io/) and add Metamask to your browser.

## Getting the dApp running

### Configuration

#### 1. Ganache
  - Open Ganache and click on settings in the top right corner.
  - Under **Server** tab:
    - Set Hostname to 127.0.0.1 -lo
    - Set Port Number to 8545
    - Enable Automine
  - Under **Accounts & Keys** tab:
    - Enable Autogenerate HD Mnemonic

#### 2. IPFS
  - Fire up your terminal and run `ipfs init`
  - Then run 
    ```
    ipfs config --json API.HTTPHeaders.Access-Control-Allow-Origin "[\"*\"]"
    ipfs config --json API.HTTPHeaders.Access-Control-Allow-Credentials "[\"true\"]"
    ipfs config --json API.HTTPHeaders.Access-Control-Allow-Methods "[\"PUT\", \"POST\", \"GET\"]"
    ```

    > Note: If you face any issues with the above command on windows, try using command prompt and escape sequences or git bash.
#### 3. Metamask
  - After installing Metamask, click on the metamask icon on your browser.
  - Click on __TRY IT NOW__, if there is an announcement saying a new version of Metamask is available.
  - Click on continue and accept all the terms and conditions after reading them.
  - Stop when Metamask asks you to create a new password. We will come back to this after deploying the contract in the next section.
  
### Smart Contract

1. Install Truffle using `npm install truffle -g`
2. Compile Contracts using `truffle compile`

#### 1. Starting your local development blockchain
  - Open Ganache.
  - Make sure to configure it the way mentioned above.
  
1. Open new Terminal and deploy contracts using `truffle migrate`
2. Copy deployed contract address to src/app.js 
![alt text](https://github.com/MarieTcho/Self-Sovereign-Identity-4-Healthcare/blob/main/images/ganache_smart-contract-deployed.png?raw=true)

```js
// app/src/app.js  line number 11
var agentContractAddress = '0xF216cf0009a6d3673e7Baa723e92831D921D01b8';
```

3. If you change contents of any contract , replace existing deployment using `truffle migrate --reset`
> Note :  reset of the contract will change the contract Address which needs to be updated in src/app.js

### Running the dApp

#### 1. Connecting Metamask to your local blockchain
  - Connect metamask to localhost:8485
  - Click on import account
  ![alt text](https://github.com/MarieTcho/Self-Sovereign-Identity-4-Healthcare/blob/main/images/metamask_wallet.png?raw=true)
  - Select any account from ganache and copy the private key to import account into MetaMask
  ![alt text](https://github.com/MarieTcho/Self-Sovereign-Identity-4-Healthcare/blob/main/images/ganache.png?raw=true)

#### 2. Starting IPFS 
  - Start the IPFS Desktop Application
  
#### 3. Start a local server
  - Open a new terminal window and navigate to `/YOUR_PROJECT_DIRECTORY/app/`.
  - Run `npm start`.
  - Open `localhost:3000` on your browser.
  - That's it! The dApp is up and running locally.

## Document hashing, encryption and storage process

  - Install python packages `pip3 install pycryptodome ipfshttpclient ldap3`
  - Start IPFS Desktop Application
  - Start Apache Directory Studio Application and launch a LDAP directory
  - Run `python3 /YOUR_PROJECT_DIRECTORY/app/src/encryption_and_storage_process.py <Document name> <Patient DID>`
  - Program returns patient DID, document encrypted, its hash and its IPFS CID
  - You can check your document in `ipfs://<CID>` in your browser and in the LDAP server