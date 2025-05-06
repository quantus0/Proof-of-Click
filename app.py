from flask import Flask, render_template, request
import requests
import validators
import json
from web3 import Web3
from eth_account import Account

app = Flask(__name__)
app.secret_key = "supersecretkey"  # For session management

# Web3 Setup
w3 = Web3(Web3.HTTPProvider("https://your-node-url"))  # Replace with your node URL
contract_address = Web3.to_checksum_address("0xYourContractAddress")  # Replace with your contract address
with open("contract_abi.json") as f:
    abi = json.load(f)
contract = w3.eth.contract(address=contract_address, abi=abi)

PRIVATE_KEY = "0xYourPrivateKey"  # Replace with your private key
ACCOUNT_ADDRESS = Account.from_key(PRIVATE_KEY).address

@app.route("/", methods=["GET", "POST"])
def index():
    short_url = None
    error = None
    if request.method == "POST":
        long_url = request.form.get("long_url")
        # Validate URL
        if not validators.url(long_url):
            error = "Invalid URL. Please enter a valid URL."
        else:
            try:
                # Call TinyURL API to shorten the URL
                response = requests.get(f"http://tinyurl.com/api-create.php?url={long_url}")
                if response.status_code == 200:
                    short_url = response.text
                    short_code = short_url.split("/")[-1]  # Extract the short code from the URL
                    record_click(short_code)  # Record the click in the blockchain
                else:
                    error = "Failed to shorten URL. Try again later."
            except requests.RequestException:
                error = "Network error. Please try again."
    return render_template("index.html", short_url=short_url, error=error)

def record_click(short_code):
    # Get the current transaction count for the account (nonce)
    nonce = w3.eth.get_transaction_count(ACCOUNT_ADDRESS)
    
    # Build the transaction to call the smart contract function
    tx = contract.functions.recordClick(short_code).build_transaction({
        'from': ACCOUNT_ADDRESS,
        'gas': 200000,
        'gasPrice': w3.to_wei('5', 'gwei'),
        'nonce': nonce,
        'chainId': 1  # Mainnet; change to 3 for Ropsten, 5 for Goerli, etc.
    })
    
    # Sign the transaction with the private key
    signed_tx = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)
    
    # Send the signed transaction
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    
    return w3.to_hex(tx_hash)

if __name__ == "__main__":
    app.run(debug=True)
