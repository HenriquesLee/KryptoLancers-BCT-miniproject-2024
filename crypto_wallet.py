# Cryptocurrency Wallet
################################################################################

# This file contains the Ethereum transaction functions that you have created throughout this module’s lessons.
# By using import statements, you will integrate this `crypto_wallet.py` Python script
# into the KryptoLancers interface program that is found in the `krypto_jobs.py` file.

################################################################################
# Imports
import os
import requests
from dotenv import load_dotenv

load_dotenv()
from bip44 import Wallet
from web3 import Account
from web3 import middleware
from web3.gas_strategies.time_based import medium_gas_price_strategy

################################################################################
# Wallet functionality


def generate_account():
    """Create a digital wallet and Ethereum account from a mnemonic seed phrase."""
    # Fetch mnemonic from environment variable.
    mnemonic = os.getenv("MNEMONIC")

    # Create Wallet Object
    wallet = Wallet(mnemonic)

    # Derive Ethereum Private Key
    private, public = wallet.derive_account("eth")

    # Convert private key into an Ethereum account
    account = Account.privateKeyToAccount(private)

    return account


def get_balance(w3, address):
    """Using an Ethereum account address access the balance of Ether"""
    # Get balance of address in Wei
    wei_balance = w3.eth.get_balance(address)

    # Convert Wei value to ether
    ether = w3.from_wei(wei_balance, "ether")

    # Return the value in ether
    return ether


def send_transaction(w3, account, to, wage):
    """Send an authorized transaction to the Ethereum network (EIP-1559)."""
    # Set gas price strategy
    w3.eth.set_gas_price_strategy(medium_gas_price_strategy)

    # Convert ETH amount to Wei
    value = w3.to_wei(wage, "ether")

    # Calculate gas estimate
    gasEstimate = w3.eth.estimate_gas(
        {"to": to, "from": account.address, "value": value}
    )

    # Construct an EIP-1559 (dynamic fee) transaction
    raw_tx = {
        "to": to,
        "from": account.address,
        "value": value,
        "gas": gasEstimate,
        'maxFeePerGas': w3.to_wei('2', 'gwei'),  # Maximum fee per gas unit
        'maxPriorityFeePerGas': w3.to_wei('1', 'gwei'),  # Tip to miner
        "nonce": w3.eth.get_transaction_count(account.address),
        "chainId": 1337,  # Explicitly set the chain ID to match Ganache
        "type": 2  # EIP-1559 transaction

    }

    # Sign the raw transaction
    signed_tx = account.sign_transaction(raw_tx)

    # Print transaction details to the CLI
    print(f"Transaction sent!")
    print(f"From: {account.address}")
    print(f"To: {to}")
    print(f"Amount: {value} ETH")
    print(f"Transaction Hash: {signed_tx}")

    # Send the signed transaction
    return w3.eth.send_raw_transaction(signed_tx.raw_transaction)


