#Proof of Click URL Shortner


URL Shortener with Blockchain Integration
This project is a URL shortener web application built using Flask, Web3 (for Ethereum integration), and TinyURL's API. It allows users to shorten URLs and tracks the clicks on those URLs using a smart contract deployed on the Ethereum blockchain.
Features

URL Shortening: Use TinyURL to shorten long URLs.
Click Tracking: Every time a shortened URL is clicked, the event is recorded on the Ethereum blockchain using a smart contract.
Blockchain Integration: Ethereum-based smart contract records each click to ensure transparency and traceability.

Technologies Used

Flask: A lightweight web framework for Python used to serve the application.
Web3.py: A Python library for interacting with Ethereum.
TinyURL API: Used to shorten long URLs.
HTML/CSS: For the frontend design.
Ethereum Smart Contract: Records the URL click events on the blockchain.

Prerequisites
Before running the project, ensure you have the following installed:

Python 3.x: Install it from python.org.
Node.js and npm (for Ethereum-related interactions) if you're setting up the Web3 provider yourself.
An Ethereum Wallet (like MetaMask) for signing transactions.
An Ethereum node (via Infura or a similar service) for interacting with the Ethereum blockchain.

Setup Instructions
Step 1: Clone the Repository
git clone https://github.com/yourusername/short-url.git
cd short-url

Step 2: Install Dependencies
Create a virtual environment and activate it:
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install the necessary Python dependencies:
pip install -r requirements.txt

Step 3: Configure Ethereum Connection

Set up a Web3 provider, such as Infura (you can create an account on Infura.io).

Replace the placeholder values in app.py:

w3 = Web3(Web3.HTTPProvider("https://your-node-url")): Replace "https://your-node-url" with your Ethereum node URL.
contract_address = Web3.to_checksum_address("0xYourContractAddress"): Replace "0xYourContractAddress" with the address of your deployed Ethereum smart contract.
PRIVATE_KEY = "0xYourPrivateKey": Replace "0xYourPrivateKey" with your private key for signing transactions.



Step 4: Create and Deploy Your Smart Contract
You will need a smart contract to record clicks. Below is a simple Solidity contract:
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract URLClickTracker {
    mapping(string => uint256) public urlClicks;

    function recordClick(string memory shortCode) public {
        urlClicks[shortCode]++;
    }

    function getClickCount(string memory shortCode) public view returns (uint256) {
        return urlClicks[shortCode];
    }
}


Deploy this contract to Ethereum using Remix or Truffle.
After deploying, copy the contract address and ABI. Save the ABI to a file named contract_abi.json in your project directory.

Step 5: Run the Application
Make sure everything is set up properly, then run the Flask app:
python app.py

The application should now be accessible at http://127.0.0.1:5000/.
Step 6: Test the Application

Open the URL shortener web app in your browser.
Enter a long URL and click "Shorten".
Once the URL is shortened, each time it's accessed, the click will be recorded on the Ethereum blockchain.

Step 7: View Blockchain Transactions
You can use a blockchain explorer (e.g., Etherscan) to view the transactions and track the click counts associated with each short URL.
Important Notes

Security Warning: Never expose your private key in the code or any public repository. In production, use secure storage methods (like environment variables) for sensitive information.
The contract is set to interact with the Ethereum Mainnet (chainId: 1), but you can change it to another testnet like Goerli or Ropsten by adjusting the chainId in the app.py file.

Future Improvements

User Authentication: Allow users to create accounts and track their URLs and clicks.
Multiple Blockchain Integrations: Extend support for other blockchains like Binance Smart Chain or Polygon.
Better UI: Improve the front-end user interface with frameworks like React.js.

License
This project is licensed under the MIT License - see the LICENSE file for details.
