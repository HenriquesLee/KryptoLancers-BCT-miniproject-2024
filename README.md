# KryptoLancers - Ethereum-based Freelance Hiring Platform

KryptoLancers is a decentralized platform that allows clients to hire freelance engineering professionals using Ethereum-based transactions. It leverages **Streamlit** for the front-end interface and **Web3.py** for blockchain integration, enabling users to pay freelancers directly using Ether (ETH). 

This platform is connected to an Ethereum testnet (local Ganache in this case) and manages candidate selection, transaction handling, and balance retrieval seamlessly.

## Features:
- **Blockchain Integration**: Uses `web3.py` to interact with an Ethereum blockchain (Ganache).
- **Wallet Management**: Generate accounts, check balances, and send Ether transactions to freelancers.
- **Freelancer Information**: Displays a list of freelancers with their Ethereum addresses, ratings, hourly rates, and profile images.
- **Dynamic Background and Styling**: CSS and HTML are used to add dynamic visual elements to the Streamlit app.
- **Transaction Automation**: Calculates freelancer wages based on hours worked and sends Ether payments directly on the blockchain.

---

## Project Components

### 1. **App Interface (Streamlit)**:
The app provides an easy-to-use interface using **Streamlit**, allowing clients to:
- Select a freelancer.
- Specify the number of hours they want to hire them for.
- View the freelancer's details such as ratings, hourly rates, and Ethereum address.
- Calculate the total wage in Ether and initiate a blockchain transaction to transfer funds.

### 2. **Web3 Blockchain Interaction**:
- **Web3**: Used to interact with the Ethereum blockchain through a local Ganache node.
- **Account Handling**: Allows clients to generate an Ethereum account using a private key and retrieve the balance.
- **Transaction Handling**: The app calculates freelancer wages and facilitates the Ether transfer from the client’s account to the freelancer's Ethereum address.

---


## How to Run

### 1. **Install Dependencies**:
Ensure you have Python and the required libraries installed. Use the following command to install dependencies:
```bash
pip install streamlit web3 bip44 python-dotenv
```

### 2. **Set Up Environment Variables**:
Create a `.env` file in the project directory and define the mnemonic seed phrase for your Ethereum wallet:
```
MNEMONIC="your-mnemonic-seed-phrase"
```

### 3. **Start Ganache**:
Run Ganache on your local machine to create a local Ethereum blockchain that the app will connect to.

### 4. **Run the App**:
Run the Streamlit app with the following command:
```bash
streamlit run app.py
```

### 5. **Interacting with the App**:
- Open the app in your browser (`http://localhost:8501`).
- Select a freelancer and enter the number of hours.
- View the freelancer's details and calculate the total wage in Ether.
- Click "Send Transaction" to transfer the calculated amount to the freelancer.

---

