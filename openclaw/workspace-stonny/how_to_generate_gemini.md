Title: Omniston Guide (Python) | STON.fi

URL Source: https://docs.ston.fi/developer-section/quickstart/python

Markdown Content:
# Omniston Guide (Python) | STON.fi

[![Image 1: Logo](https://docs.ston.fi/~gitbook/image?url=https%3A%2F%2F4271849708-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Forganizations%252FZCdWXRNv8GO6UNNDbtrW%252Fsites%252Fsite_m0Ami%252Flogo%252FAxXm0NG1A4HsVWbljk2l%252Ffull-logo.svg%3Falt%3Dmedia%26token%3D51d99838-856a-458e-bdd5-1f8c8f70d229&width=260&dpr=3&quality=100&sign=8c496dff&sv=2)![Image 2: Logo](https://docs.ston.fi/~gitbook/image?url=https%3A%2F%2F4271849708-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Forganizations%252FZCdWXRNv8GO6UNNDbtrW%252Fsites%252Fsite_m0Ami%252Flogo%252FNNUHc1w7Tf2DgkqOXMg7%252Flogo-black.svg%3Falt%3Dmedia%26token%3Ddaa19060-c6c6-4222-a93c-c378710829d7&width=260&dpr=3&quality=100&sign=b31fba20&sv=2)](https://docs.ston.fi/)

⌘Ctrl k

English

[![Image 3: Logo](https://docs.ston.fi/~gitbook/image?url=https%3A%2F%2F4271849708-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Forganizations%252FZCdWXRNv8GO6UNNDbtrW%252Fsites%252Fsite_m0Ami%252Flogo%252FAxXm0NG1A4HsVWbljk2l%252Ffull-logo.svg%3Falt%3Dmedia%26token%3D51d99838-856a-458e-bdd5-1f8c8f70d229&width=260&dpr=3&quality=100&sign=8c496dff&sv=2)![Image 4: Logo](https://docs.ston.fi/~gitbook/image?url=https%3A%2F%2F4271849708-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Forganizations%252FZCdWXRNv8GO6UNNDbtrW%252Fsites%252Fsite_m0Ami%252Flogo%252FNNUHc1w7Tf2DgkqOXMg7%252Flogo-black.svg%3Falt%3Dmedia%26token%3Ddaa19060-c6c6-4222-a93c-c378710829d7&width=260&dpr=3&quality=100&sign=b31fba20&sv=2)](https://docs.ston.fi/)English

*   Getting Started 
    *   [Introduction](https://docs.ston.fi/)
    *   [Whitepaper](https://docs.ston.fi/getting-started/whitepaper)
    *   [User Guide](https://guide.ston.fi/en/)
    *   [Security — Audits & Bug Bounty](https://docs.ston.fi/getting-started/security)

*   Developer section 
    *   [Quickstart Guides](https://docs.ston.fi/developer-section/quickstart)

        *   [Swap Guide (React)](https://docs.ston.fi/developer-section/quickstart/swap)
        *   [Liquidity Providing Guide (React)](https://docs.ston.fi/developer-section/quickstart/liquidity)
        *   [Omniston Guide (React)](https://docs.ston.fi/developer-section/quickstart/omniston)
        *   [Omniston Guide (Python)](https://docs.ston.fi/developer-section/quickstart/python)

    *   [DEX](https://docs.ston.fi/developer-section/dex)
    *   [Omniston Protocol](https://docs.ston.fi/developer-section/omniston)
    *   [Omniston Widget](https://docs.ston.fi/developer-section/widget)
    *   [Common Utilities](https://docs.ston.fi/developer-section/common)

*   Help 
    *   [Contact Us](https://docs.ston.fi/help/contact)

[Powered by GitBook](https://www.gitbook.com/?utm_source=content&utm_medium=trademark&utm_campaign=CJ1ZKietYw2GrKAuOqA8&utm_content=site_m0Ami)

On this page

Copy

1.   [Developer section](https://docs.ston.fi/developer-section)
2.   [Quickstart Guides](https://docs.ston.fi/developer-section/quickstart)

# Omniston Guide (Python)

Learn how to create a Python-based terminal client for swapping tokens on TON blockchain using Omniston protocol. Covers wallet setup, API integration, and cross-DEX swaps on STON.fi and DeDust.

This guide will walk you through creating a **terminal-based** token swap client using the **Omniston** protocol to swap assets across different DEXes (STON.fi V1, STON.fi V2, DeDust, etc.). Instead of a web UI and TonConnect, we'll use a **local TON wallet** (created with `tonsdk`) and submit transactions via **Toncenter**. The guide is beginner‑friendly and assumes minimal TON experience.

> **Note**: This quickstart intentionally uses a **single-file CLI** for clarity. You can later modularize or package it (see **Advanced Example App**).
> 
> 
> **Note**: For reliability when broadcasting transactions, set a **TONCENTER_API_KEY** (see **Configure Assets & Network**).

* * *

## [](https://docs.ston.fi/developer-section/quickstart/python#table-of-contents)

Table of Contents

1.     [Introduction](https://docs.ston.fi/developer-section/quickstart/python#id-1.-introduction) 
2.     [Setting Up the Project](https://docs.ston.fi/developer-section/quickstart/python#id-2.-setting-up-the-project) 
3.     [Wallet Setup](https://docs.ston.fi/developer-section/quickstart/python#id-3.-wallet-setup) 
4.     [Configure Assets & Network](https://docs.ston.fi/developer-section/quickstart/python#id-4.-configure-assets--network) 
5.     [Implementing the CLI (Step‑by‑Step)](https://docs.ston.fi/developer-section/quickstart/python#id-5.-implementing-the-cli-stepbystep) 
6.     [Requesting a Quote](https://docs.ston.fi/developer-section/quickstart/python#id-6.-requesting-a-quote) 
7.     [Building a Transaction & Sending It](https://docs.ston.fi/developer-section/quickstart/python#id-7.-building-a-transaction--sending-it) 
8.     [Testing Your Swap](https://docs.ston.fi/developer-section/quickstart/python#id-8.-testing-your-swap) 
9.     [Conclusion](https://docs.ston.fi/developer-section/quickstart/python#id-9.-conclusion) 
10.     [Live Demo](https://docs.ston.fi/developer-section/quickstart/python#id-10.-live-demo) 
11.     [Using AI Agents for Automated Implementation](https://docs.ston.fi/developer-section/quickstart/python#id-11.-using-ai-agents-for-automated-implementation) 

* * *

## [](https://docs.ston.fi/developer-section/quickstart/python#id-1.-introduction)

1. Introduction

In this quickstart, you'll build a minimal **Python CLI** that can:

*     Create or reuse a local TON wallet (via `tonsdk`). 
*     Load network and token settings from `.env` and `swap_config.json`. 
*     Request an **RFQ** (quote) from Omniston over **WebSockets**. 
*     Build a transfer using Omniston's transaction builder. 
*     Submit the transaction to **Toncenter** to execute the swap. 

You'll use:

*     `tonsdk` – wallet generation, signing, and BOCs. 
*     `websockets` – to communicate with Omniston. 
*     `python-dotenv` – to load environment variables. 
*     **Toncenter API** – to broadcast the signed transaction. 

* * *

## [](https://docs.ston.fi/developer-section/quickstart/python#id-2.-setting-up-the-project)

2. Setting Up the Project

### [](https://docs.ston.fi/developer-section/quickstart/python#id-2.1-create-the-workspace)

2.1 Create the Workspace

### [](https://docs.ston.fi/developer-section/quickstart/python#id-2.2-create-the-virtual-environment)

2.2 Create the Virtual Environment

### [](https://docs.ston.fi/developer-section/quickstart/python#id-2.3-install-dependencies)

2.3 Install Dependencies

1.     Create `requirements.txt` and add: 
2.     Install the packages: 
3.     Create a single-file CLI script: 

* * *

## [](https://docs.ston.fi/developer-section/quickstart/python#id-3.-wallet-setup)

3. Wallet Setup

The CLI persists a wallet in `data/wallet.json` and prints a mnemonic once—store it securely.

### [](https://docs.ston.fi/developer-section/quickstart/python#id-3.1-generate-or-load-a-wallet)

3.1 Generate or Load a Wallet

In this step you'll paste core definitions and the wallet helpers (kept at the top of `omniston_cli.py`).

**Tip**: The code blocks below are verbatim from the working implementation; paste them as-is and in the given order.

### [](https://docs.ston.fi/developer-section/quickstart/python#id-3.2-fund-and-deploy-the-wallet)

3.2 Fund and Deploy the Wallet

You must fund the address and deploy the wallet contract before sending a swap. The helpers below take care of querying Toncenter and submitting the init BOC when needed.

* * *

## [](https://docs.ston.fi/developer-section/quickstart/python#id-4.-configure-assets-and-network)

4. Configure Assets & Network

You'll define RPC endpoints and default swap pair locally.

### [](https://docs.ston.fi/developer-section/quickstart/python#id-4.1-create-the-.env-file)

4.1 Create the .env file

Create `.env` at the project root:

> **Getting a Toncenter API Key**: Using the API without an API key is limited to 1 request per second. To get higher rate limits:
> 
> 
> 1.     Contact [@toncenter](https://t.me/toncenter) on Telegram 
> 2.     Request an API key for your project 
> 3.     Copy the key and paste it into your `.env` file 
> 
> 
> `TONCENTER_API_KEY` is required if you want to execute transactions. Without it, you'll face rate limiting issues and transaction broadcasting will fail.

### [](https://docs.ston.fi/developer-section/quickstart/python#id-4.2-define-the-swap_config.json)

4.2 Define the swap_config.json

Create `swap_config.json`:

Common token addresses:

*     Native TON: `EQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAM9c` 
*     USDT: `EQCxE6mUtQJKFnGfaROTKOt1lZbDiiX1kCixRv7Nw2Id_sDs` 
*     STON: `EQA2kCVNwVsil2EM2mB0SkXytxCqQjS4mttjDpnXmwG9T6bO` 

`gasless_mode` accepts "GASLESS_SETTLEMENT_UNSPECIFIED", "GASLESS_SETTLEMENT_POSSIBLE", "GASLESS_SETTLEMENT_REQUIRED", or their numeric equivalents 0/1/2.

`flexible_referrer_fee` lets Omniston lower the actual referrer fee below `referrer_fee_bps` when a resolver can offer a better price. Leave it `false` to enforce the exact fee.

* * *

## [](https://docs.ston.fi/developer-section/quickstart/python#id-5.-implementing-the-cli-step-by-step)

5. Implementing the CLI (Step‑by‑Step)

Open `omniston_cli.py` and paste the remaining helper blocks below exactly as shown.

### [](https://docs.ston.fi/developer-section/quickstart/python#id-5.1-define-domain-types)

5.1 Define Domain Types

### [](https://docs.ston.fi/developer-section/quickstart/python#id-5.2-wallet-helpers)

5.2 Wallet Helpers

### [](https://docs.ston.fi/developer-section/quickstart/python#id-5.3-toncenter-helpers)

5.3 Toncenter Helpers

### [](https://docs.ston.fi/developer-section/quickstart/python#id-5.4-quote-helpers)

5.4 Quote Helpers

### [](https://docs.ston.fi/developer-section/quickstart/python#id-5.5-transfer-helpers)

5.5 Transfer Helpers

### [](https://docs.ston.fi/developer-section/quickstart/python#id-5.6-command-entry-point)

5.6 Command Entry Point

* * *

## [](https://docs.ston.fi/developer-section/quickstart/python#id-6.-requesting-a-quote)

6. Requesting a Quote

Run the CLI and follow the prompt:

When you accept "Request a quote now?", the CLI will:

*     Build a request using your configured pair and amount. 
*     Connect to Omniston over WebSockets (v1beta7.quote). 
*     Print a human‑readable summary (e.g., Swap 0.01 -> 12.34). 

If a quote can't be produced in time (default: ~15s), you'll see a timeout or error message.

* * *

## [](https://docs.ston.fi/developer-section/quickstart/python#id-7.-building-a-transaction-and-sending-it)

7. Building a Transaction & Sending It

After you approve the quote summary, the CLI:

1.     Calls Omniston's transaction builder (v1beta7.transaction.build_transfer) to obtain TON messages. 
2.     Signs an external message with your wallet. 
3.     Submits the resulting BOC to Toncenter. 

**Important**: Automatic submission requires `TONCENTER_API_KEY` in `.env`. Without it, the CLI skips broadcast.

* * *

## [](https://docs.ston.fi/developer-section/quickstart/python#id-8.-testing-your-swap)

8. Testing Your Swap

1.     Activate your virtual environment and ensure `.env` and `swap_config.json` exist. 
2.     Fund your wallet and run: 
3.     

Confirm:

    *     Wallet is created/loaded and balance printed. 
    *     Deployment completes (or is already deployed). 
    *     A quote is received and summarized. 
    *     On approval, the transaction is submitted and you see "Swap submitted.". 
    *     Check your wallet on a TON explorer to confirm the swap. 

If something fails, the CLI prints a clear message (e.g., timeout, missing API key, seqno issue).

* * *

## [](https://docs.ston.fi/developer-section/quickstart/python#id-9.-conclusion)

9. Conclusion

You now have a minimal Python CLI that:

*     Generates or reuses a TON wallet. 
*     Loads local configuration for assets and network. 
*     Requests real‑time quotes from Omniston. 
*     Builds and submits the swap via Toncenter. 

Ideas to extend:

*     Custom CLI flags (amount/pair) with argparse. 
*     Better error reporting and retry/backoff. 
*     Explorer links after submission. 
*     Trade tracking with periodic status checks. 

## [](https://docs.ston.fi/developer-section/quickstart/python#id-10.-live-demo)

10. Live Demo

Run the Omniston Python CLI directly in your browser via Replit:

*     Open the project in Replit 
*     Fork to your account to save changes 
*     Add a `TONCENTER_API_KEY` in Replit Secrets 
*     Run `python omniston_cli.py` in the Replit shell 
*     Explore and modify the code freely 

* * *

## [](https://docs.ston.fi/developer-section/quickstart/python#id-11.-using-ai-agents-for-automated-implementation)

11. Using AI Agents for Automated Implementation

You can also follow along with a recorded walkthrough:

For developers looking to accelerate their development process, you can leverage **AI coding agents** to automatically implement the Omniston swap functionality described in this guide. While we showcase **Gemini CLI** in our example (due to its generous free tier), you can use any AI coding assistant such as **Claude Code**, **GitHub Copilot**, **Cursor Agent**, or similar tools.

### [](https://docs.ston.fi/developer-section/quickstart/python#id-11.1-why-ai-agents)

11.1 Why AI Agents?

Modern AI coding agents can:

*     Understand complex documentation and implement complete features 
*     Set up project structure and dependencies automatically 
*     Handle common configuration and setup errors 
*     Provide working implementations in minutes instead of hours 

### [](https://docs.ston.fi/developer-section/quickstart/python#id-11.2-setting-up-with-gemini-cli-example)

11.2 Setting Up with Gemini CLI (Example)

We'll demonstrate with Gemini CLI, but the approach works with any AI agent that can read documentation and execute commands.

#### [](https://docs.ston.fi/developer-section/quickstart/python#id-11.2.1-installing-gemini-cli)

11.2.1 Installing Gemini CLI

1.     Install the Gemini CLI by following the instructions at: [https://github.com/google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) 
2.     

Authenticate with your Google account when prompted. The free tier includes:

    *     60 model requests per minute 
    *     1,000 model requests per day 

#### [](https://docs.ston.fi/developer-section/quickstart/python#id-11.2.2-setting-up-the-implementation-guide)

11.2.2 Setting Up the Implementation Guide

1.     

Download the appropriate guide file from the gist: [https://gist.github.com/mrruby/a6fba69716fc0d5b8eaafd43998b36c0](https://gist.github.com/mrruby/a6fba69716fc0d5b8eaafd43998b36c0)

    *     **For Claude Code**: Download `AGENTS.md` and rename it to `CLAUDE.md` 
    *     **For other AI agents** (Gemini CLI, GitHub Copilot, Cursor, etc.): Use `AGENTS.md` as-is 

2.     Create a new directory for your project and place the guide file inside it: 

#### [](https://docs.ston.fi/developer-section/quickstart/python#id-11.2.3-running-the-automated-implementation)

11.2.3 Running the Automated Implementation

1.     From within your project directory, run the Gemini CLI: 
2.     When the CLI interface opens, type: 
3.     

The AI agent will:

    *     Ask for permission to use commands like `python3`, `pip`, etc. 
    *     Automatically create the project structure 
    *     Install all necessary dependencies 
    *     Implement the complete swap functionality 
    *     Set up configuration files 

4.     

**Important**: After the implementation completes, you must manually configure your Toncenter API key:

    *     Go to [TON Center](https://toncenter.com/) and get your API key 
    *     Create a `.env` file in the root of your project 
    *     Add your API key: `TONCENTER_API_KEY=your_api_key_here` 
    *     AI agents cannot handle this step as it requires your personal API credentials 

5.     

If any errors occur during the process:

    *     Simply paste the error message back to the AI agent 
    *     It will analyze and fix the issue automatically 
    *     In most cases, the implementation completes successfully in one shot 

### [](https://docs.ston.fi/developer-section/quickstart/python#id-11.3-using-other-ai-agents)

11.3 Using Other AI Agents

The same approach works with other AI coding assistants:

*     **Claude Code**: Download `AGENTS.md` and rename it to `CLAUDE.md`, then place it in your project and ask Claude Code to implement the guide 
*     **GitHub Copilot**: Use the `AGENTS.md` file as-is, open the guide in your editor and use Copilot Chat to implement step by step 
*     **Cursor Agent**: Use the `AGENTS.md` file as-is, load the documentation and request full implementation via Cursor's agent mode 
*     **Custom Tools**: Any AI assistant with file access and command execution capabilities can follow the guide using the `AGENTS.md` file 

> **Note**: The `AGENTS.md` file contains instructions compatible with all AI agents (Gemini CLI, GitHub Copilot, Cursor, etc.). However, Claude Code requires the file to be named `CLAUDE.md` to be automatically recognized, so you must rename `AGENTS.md` to `CLAUDE.md` when using Claude Code.

### [](https://docs.ston.fi/developer-section/quickstart/python#id-11.4-benefits-of-using-ai-agents)

11.4 Benefits of Using AI Agents

*     **Speed**: Get a working implementation in minutes instead of hours 
*     **Accuracy**: AI agents follow the quickstart guide precisely 
*     **Error Handling**: Automatically resolve most common setup issues 
*     **Learning Tool**: Watch how the implementation unfolds step by step 
*     **Customization**: After the initial setup, you can modify the generated code to fit your specific needs 
*     **Cost-Effective**: Many AI coding tools offer free tiers (like Gemini CLI) or are included in existing subscriptions 

### [](https://docs.ston.fi/developer-section/quickstart/python#id-11.5-best-practices)

11.5 Best Practices

1.     **Review the Code**: Always review AI-generated code before using it in production 
2.     **Understand the Flow**: Use the generated code as a learning tool to understand the Omniston protocol 
3.     **Customize**: Adapt the generated code to your specific requirements 
4.     **Test Thoroughly**: Test the implementation with small amounts before processing larger transactions 
5.     **Security**: Never commit API keys or mnemonics to version control 

This approach is particularly useful for:

*     Developers new to the TON ecosystem 
*     Quick prototyping and proof-of-concepts 
*     Learning by example with a working implementation 
*     Avoiding common setup pitfalls and configuration errors 
*     Exploring different implementation approaches rapidly 

* * *

Happy swapping!

[Previous Omniston Guide (React)](https://docs.ston.fi/developer-section/quickstart/omniston)[Next DEX](https://docs.ston.fi/developer-section/dex)

Last updated 2 months ago

*   [Table of Contents](https://docs.ston.fi/developer-section/quickstart/python#table-of-contents)
*   [1. Introduction](https://docs.ston.fi/developer-section/quickstart/python#id-1.-introduction)
*   [2. Setting Up the Project](https://docs.ston.fi/developer-section/quickstart/python#id-2.-setting-up-the-project)
*   [2.1 Create the Workspace](https://docs.ston.fi/developer-section/quickstart/python#id-2.1-create-the-workspace)
*   [2.2 Create the Virtual Environment](https://docs.ston.fi/developer-section/quickstart/python#id-2.2-create-the-virtual-environment)
*   [2.3 Install Dependencies](https://docs.ston.fi/developer-section/quickstart/python#id-2.3-install-dependencies)
*   [3. Wallet Setup](https://docs.ston.fi/developer-section/quickstart/python#id-3.-wallet-setup)
*   [3.1 Generate or Load a Wallet](https://docs.ston.fi/developer-section/quickstart/python#id-3.1-generate-or-load-a-wallet)
*   [3.2 Fund and Deploy the Wallet](https://docs.ston.fi/developer-section/quickstart/python#id-3.2-fund-and-deploy-the-wallet)
*   [4. Configure Assets & Network](https://docs.ston.fi/developer-section/quickstart/python#id-4.-configure-assets-and-network)
*   [4.1 Create the .env file](https://docs.ston.fi/developer-section/quickstart/python#id-4.1-create-the-.env-file)
*   [4.2 Define the swap_config.json](https://docs.ston.fi/developer-section/quickstart/python#id-4.2-define-the-swap_config.json)
*   [5. Implementing the CLI (Step‑by‑Step)](https://docs.ston.fi/developer-section/quickstart/python#id-5.-implementing-the-cli-step-by-step)
*   [5.1 Define Domain Types](https://docs.ston.fi/developer-section/quickstart/python#id-5.1-define-domain-types)
*   [5.2 Wallet Helpers](https://docs.ston.fi/developer-section/quickstart/python#id-5.2-wallet-helpers)
*   [5.3 Toncenter Helpers](https://docs.ston.fi/developer-section/quickstart/python#id-5.3-toncenter-helpers)
*   [5.4 Quote Helpers](https://docs.ston.fi/developer-section/quickstart/python#id-5.4-quote-helpers)
*   [5.5 Transfer Helpers](https://docs.ston.fi/developer-section/quickstart/python#id-5.5-transfer-helpers)
*   [5.6 Command Entry Point](https://docs.ston.fi/developer-section/quickstart/python#id-5.6-command-entry-point)
*   [6. Requesting a Quote](https://docs.ston.fi/developer-section/quickstart/python#id-6.-requesting-a-quote)
*   [7. Building a Transaction & Sending It](https://docs.ston.fi/developer-section/quickstart/python#id-7.-building-a-transaction-and-sending-it)
*   [8. Testing Your Swap](https://docs.ston.fi/developer-section/quickstart/python#id-8.-testing-your-swap)
*   [9. Conclusion](https://docs.ston.fi/developer-section/quickstart/python#id-9.-conclusion)
*   [10. Live Demo](https://docs.ston.fi/developer-section/quickstart/python#id-10.-live-demo)
*   [11. Using AI Agents for Automated Implementation](https://docs.ston.fi/developer-section/quickstart/python#id-11.-using-ai-agents-for-automated-implementation)
*   [11.1 Why AI Agents?](https://docs.ston.fi/developer-section/quickstart/python#id-11.1-why-ai-agents)
*   [11.2 Setting Up with Gemini CLI (Example)](https://docs.ston.fi/developer-section/quickstart/python#id-11.2-setting-up-with-gemini-cli-example)
*   [11.3 Using Other AI Agents](https://docs.ston.fi/developer-section/quickstart/python#id-11.3-using-other-ai-agents)
*   [11.4 Benefits of Using AI Agents](https://docs.ston.fi/developer-section/quickstart/python#id-11.4-benefits-of-using-ai-agents)
*   [11.5 Best Practices](https://docs.ston.fi/developer-section/quickstart/python#id-11.5-best-practices)

Copy
```
mkdir omniston-python
cd omniston-python
```

Copy
```
python3 -m venv .venv
source .venv/bin/activate        # macOS/Linux
# .venv\\Scripts\\Activate.ps1  # Windows PowerShell
```

Copy
```
python-dotenv>=1.0,<2
tonsdk>=1.0.13
websockets>=11,<13
```

Copy`pip install -r requirements.txt`

Copy`touch omniston_cli.py`

Copy
```
TONCENTER_API_URL=https://toncenter.com/api/v2
TONCENTER_API_KEY=put-your-api-key-here
OMNISTON_WS_URL=wss://omni-ws.ston.fi
```

Copy
```
{
  "from_token_address": "EQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAM9c",
  "from_token_decimals": 9,
  "to_token_address": "EQA2kCVNwVsil2EM2mB0SkXytxCqQjS4mttjDpnXmwG9T6bO",
  "to_token_decimals": 9,
  "amount": "0.01",
  "max_slippage_bps": 500,
  "max_outgoing_messages": 4,
  "gasless_mode": "GASLESS_SETTLEMENT_POSSIBLE",
  "flexible_referrer_fee": false
}
```

Copy
```
# omniston_cli.py
import asyncio
import base64
import json
import os
import sys
import time
import urllib.parse
import urllib.request
import uuid
from dataclasses import dataclass
from decimal import Decimal, ROUND_DOWN, getcontext
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import websockets
from dotenv import load_dotenv
from tonsdk.boc import Cell
from tonsdk.contract.wallet import Wallets, WalletVersionEnum
from tonsdk.crypto import mnemonic_new
from tonsdk.utils import bytes_to_b64str

DATA_DIR = Path("data")
WALLET_FILE = DATA_DIR / "wallet.json"
CONFIG_FILE = Path("swap_config.json")

@dataclass
class WalletData:
    mnemonic: List[str]
    address_hex: str
    address_bounceable: str
    workchain: int
    version: str

    def to_dict(self) -> Dict[str, object]:
        return {
            "mnemonic": self.mnemonic,
            "address_hex": self.address_hex,
            "address_bounceable": self.address_bounceable,
            "workchain": self.workchain,
            "version": self.version,
        }

    @classmethod
    def from_dict(cls, payload: Dict[str, object]) -> "WalletData":
        return cls(
            mnemonic=list(payload["mnemonic"]),
            address_hex=str(payload["address_hex"]),
            address_bounceable=str(payload.get("address_bounceable", "")),
            workchain=int(payload.get("workchain", 0)),
            version=str(payload.get("version", WalletVersionEnum.v4r2.value)),
        )

@dataclass
class SwapConfig:
    from_token_address: str
    from_token_decimals: int
    to_token_address: str
    to_token_decimals: int
    amount: Decimal
    max_slippage_bps: int
    max_outgoing_messages: int
    gasless_mode: int
    flexible_referrer_fee: bool

GASLESS_SETTLEMENT_MAP = {
    "GASLESS_SETTLEMENT_UNSPECIFIED": 0,
    "GASLESS_SETTLEMENT_POSSIBLE": 1,
    "GASLESS_SETTLEMENT_REQUIRED": 2,
}

def _parse_gasless_mode(raw: object) -> int:
    if isinstance(raw, int):
        return raw
    if isinstance(raw, str):
        token = raw.strip()
        if not token:
            return 1
        upper = token.upper()
        if upper in GASLESS_SETTLEMENT_MAP:
            return GASLESS_SETTLEMENT_MAP[upper]
        return int(token)
    raise TypeError("gasless_mode must be str or int")

def load_config() -> SwapConfig:
    if not CONFIG_FILE.exists():
        raise FileNotFoundError("swap_config.json is missing")
    with CONFIG_FILE.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    gasless_mode = _parse_gasless_mode(payload.get("gasless_mode", "GASLESS_SETTLEMENT_POSSIBLE"))
    return SwapConfig(
        from_token_address=str(payload["from_token_address"]),
        from_token_decimals=int(payload["from_token_decimals"]),
        to_token_address=str(payload["to_token_address"]),
        to_token_decimals=int(payload["to_token_decimals"]),
        amount=Decimal(str(payload["amount"])),
        max_slippage_bps=int(payload.get("max_slippage_bps", 500)),
        max_outgoing_messages=int(payload.get("max_outgoing_messages", 4)),
        gasless_mode=gasless_mode,
        flexible_referrer_fee=bool(payload.get("flexible_referrer_fee", False)),
    )

def ensure_data_dir() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)

def prompt_yes_no(message: str, default: bool = False) -> bool:
    suffix = " [Y/n]" if default else " [y/N]"
    while True:
        reply = input(f"{message}{suffix} ").strip().lower()
        if not reply:
            return default
        if reply in {"y", "yes"}:
            return True
        if reply in {"n", "no"}:
            return False

getcontext().prec = 28
# TON blockchain chain ID used by Omniston protocol
BLOCKCHAIN_ID = 607  # Represents TON blockchain (equivalent to Blockchain.TON in SDKs)
QUOTE_TIMEOUT = 15
TRANSFER_TIMEOUT = 30

TONCENTER_API_URL = "https://toncenter.com/api/v2"
TONCENTER_API_KEY = ""
OMNISTON_WS_URL = "wss://omni-ws.ston.fi"

def load_env() -> None:
    global TONCENTER_API_URL, TONCENTER_API_KEY, OMNISTON_WS_URL
    load_dotenv()
    TONCENTER_API_URL = os.getenv("TONCENTER_API_URL", TONCENTER_API_URL)
    TONCENTER_API_KEY = os.getenv("TONCENTER_API_KEY", TONCENTER_API_KEY)
    OMNISTON_WS_URL = os.getenv("OMNISTON_WS_URL", OMNISTON_WS_URL)
```

Copy
```
def save_wallet(wallet: WalletData) -> None:
    ensure_data_dir()
    with WALLET_FILE.open("w", encoding="utf-8") as handle:
        json.dump(wallet.to_dict(), handle, indent=2)

def load_wallet() -> Optional[WalletData]:
    if not WALLET_FILE.exists():
        return None
    with WALLET_FILE.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    return WalletData.from_dict(payload)

def ensure_wallet() -> WalletData:
    ensure_data_dir()
    wallet = load_wallet()
    if wallet:
        print(f"Loaded wallet from {WALLET_FILE}")
        return wallet

    mnemonic = mnemonic_new()
    version = WalletVersionEnum.v4r2
    _, _, _, contract = Wallets.from_mnemonics(mnemonic, version, 0)
    wallet = WalletData(
        mnemonic=mnemonic,
        address_hex=contract.address.to_string(False),
        address_bounceable=contract.address.to_string(True, True, False),
        workchain=contract.address.wc,
        version=version.value,
    )
    save_wallet(wallet)
    print(f"Created new wallet at {WALLET_FILE}")
    print("Mnemonic (store securely):")
    print(" ".join(wallet.mnemonic))
    return wallet

def build_init_boc(wallet: WalletData) -> str:
    version = WalletVersionEnum(wallet.version)
    _, _, _, contract = Wallets.from_mnemonics(wallet.mnemonic, version, wallet.workchain)
    message = contract.create_init_external_message()["message"]
    return bytes_to_b64str(message.to_boc(False))
```

Copy
```
def toncenter_get(endpoint: str, params: Dict[str, object]) -> Dict[str, object]:
    query = dict(params)
    if TONCENTER_API_KEY:
        query.setdefault("api_key", TONCENTER_API_KEY)
    url = f"{TONCENTER_API_URL.rstrip('/')}/{endpoint}"
    if query:
        url = f"{url}?{urllib.parse.urlencode(query)}"
    request = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(request, timeout=15) as response:
        return json.loads(response.read().decode("utf-8"))

def toncenter_post(endpoint: str, body: Dict[str, object]) -> Dict[str, object]:
    query = {}
    if TONCENTER_API_KEY:
        query["api_key"] = TONCENTER_API_KEY
    url = f"{TONCENTER_API_URL.rstrip('/')}/{endpoint}"
    if query:
        url = f"{url}?{urllib.parse.urlencode(query)}"
    data = json.dumps(body).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=data,
        headers={"Accept": "application/json", "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=15) as response:
        return json.loads(response.read().decode("utf-8"))

def send_boc(boc_base64: str) -> bool:
    response = toncenter_post("sendBoc", {"boc": boc_base64})
    return bool(response.get("ok", True))

def fetch_balance(address: str) -> Optional[Decimal]:
    try:
        result = toncenter_get("getAddressBalance", {"address": address})
    except Exception as exc:
        print(f"Could not fetch balance: {exc}")
        return None
    raw = result.get("result")
    if raw is None:
        return None
    return Decimal(str(raw)) / Decimal(1_000_000_000)

def lookup_wallet_seqno(address: str) -> Optional[int]:
    try:
        result = toncenter_get("getWalletInformation", {"address": address})
    except Exception:
        return None
    data = result.get("result")
    if not data:
        return None
    seqno = data.get("seqno")
    return int(seqno) if seqno is not None else None

def ensure_wallet_deployed(wallet: WalletData) -> bool:
    if lookup_wallet_seqno(wallet.address_hex) is not None:
        return True

    print("Deploying wallet (requires funds on the address)...")
    if not send_boc(build_init_boc(wallet)):
        print("Toncenter rejected deployment message.")
        return False

    for _ in range(10):
        time.sleep(2)
        if lookup_wallet_seqno(wallet.address_hex) is not None:
            print("Wallet deployment confirmed.")
            return True

    print("Wallet deployment not confirmed yet; try again once the transaction is processed.")
    return False
```

Copy
```
def _token_to_units(amount: Decimal, decimals: int) -> int:
    return int((amount * Decimal(10) ** decimals).to_integral_value(ROUND_DOWN))

def _units_to_token(units: int, decimals: int) -> Decimal:
    return Decimal(units) / (Decimal(10) ** decimals)

def format_amount(value: Decimal, decimals: int) -> str:
    quantum = Decimal("1").scaleb(-decimals)
    text = f"{value.quantize(quantum, rounding=ROUND_DOWN):f}"
    return text.rstrip("0").rstrip(".") if "." in text else text

def _extract_quote(data: Optional[Dict[str, object]]) -> Optional[Dict[str, object]]:
    if not isinstance(data, dict):
        return None
    if "bid_units" in data and "ask_units" in data:
        return data
    if "quote" in data and isinstance(data["quote"], dict):
        return data["quote"]
    for value in data.values():
        if isinstance(value, dict):
            found = _extract_quote(value)
            if found:
                return found
    return None

def _extract_event_error(data: Dict[str, object]) -> Optional[object]:
    if not isinstance(data, dict):
        return None
    if data.get("error"):
        return data["error"]

    result = data.get("result")
    if isinstance(result, dict):
        if result.get("error"):
            return result["error"]
        event_type = str(result.get("type", "")).lower()
        if "rejected" in event_type:
            return result.get("error") or result

    params = data.get("params")
    if isinstance(params, dict):
        return _extract_event_error(params)
    return None

def _format_error(error: object) -> str:
    if isinstance(error, dict):
        message = error.get("message") or error.get("reason")
        if isinstance(message, str) and message.strip():
            return message.strip()
        try:
            text = json.dumps(error)
            if text.strip():
                return text
        except Exception:
            pass
    text = str(error)
    return text if text.strip() else repr(error)

def describe_quote(quote: Dict[str, object], config: SwapConfig) -> (Decimal, str):
    ask_units = quote.get("ask_units") or quote.get("askUnits")
    bid_units = quote.get("bid_units") or quote.get("bidUnits")
    if ask_units is None or bid_units is None:
        return Decimal("0"), "Quote missing units"

    ask_amount = _units_to_token(int(ask_units), config.to_token_decimals)
    bid_amount = _units_to_token(int(bid_units), config.from_token_decimals)
    summary = (
        f"Swap {format_amount(bid_amount, config.from_token_decimals)} -> "
        f"{format_amount(ask_amount, config.to_token_decimals)}"
    )
    return ask_amount, summary

def request_quote(config: SwapConfig, wallet: WalletData) -> Dict[str, object]:
    bid_units = str(_token_to_units(config.amount, config.from_token_decimals))
    request_id = str(uuid.uuid4())
    params = {
        "bid_asset_address": {"blockchain": BLOCKCHAIN_ID, "address": config.from_token_address},
        "ask_asset_address": {"blockchain": BLOCKCHAIN_ID, "address": config.to_token_address},
        "amount": {"bid_units": bid_units},
        "referrer_fee_bps": 0,
        "settlement_methods": [0],  # 0 == SWAP
        "settlement_params": {
            "max_price_slippage_bps": config.max_slippage_bps,
            "max_outgoing_messages": config.max_outgoing_messages,
            "gasless_settlement": config.gasless_mode,
            "flexible_referrer_fee": config.flexible_referrer_fee,
            "wallet_address": {"blockchain": BLOCKCHAIN_ID, "address": wallet.address_hex},
        },
    }

    payload = {
        "jsonrpc": "2.0",
        "id": request_id,
        "method": "v1beta7.quote",
        "params": params,
    }

    async def _run() -> Dict[str, object]:
        async with websockets.connect(OMNISTON_WS_URL, ping_interval=20, ping_timeout=20) as ws:
            await ws.send(json.dumps(payload))
            deadline = time.time() + QUOTE_TIMEOUT
            print("Waiting for quote...")
            while time.time() < deadline:
                timeout = max(0.1, deadline - time.time())
                try:
                    raw = await asyncio.wait_for(ws.recv(), timeout=timeout)
                except asyncio.TimeoutError:
                    continue
                data = json.loads(raw)
                event_error = _extract_event_error(data)
                if event_error:
                    raise RuntimeError(_format_error(event_error))
                quote = _extract_quote(data.get("result")) or _extract_quote(data)
                if quote:
                    return quote
            raise RuntimeError("Timed out waiting for quote from Omniston")

    try:
        return asyncio.run(_run())
    except Exception as exc:
        raise RuntimeError(f"Omniston quote request failed: {exc!r}") from exc
```

Copy
```
def _decode_cell(raw: Optional[str]) -> Optional[Cell]:
    if raw is None:
        return None
    raw = raw.strip()
    if not raw:
        return None
    try:
        data = base64.b64decode(raw)
    except Exception:
        try:
            data = bytes.fromhex(raw)
        except ValueError:
            return None
    try:
        return Cell.one_from_boc(data)
    except Exception:
        return None

def _extract_transfer(data: Optional[Dict[str, object]]) -> Optional[Dict[str, object]]:
    if not isinstance(data, dict):
        return None
    if "ton" in data and isinstance(data["ton"], dict):
        return data
    if "transaction" in data and isinstance(data["transaction"], dict):
        return data["transaction"]
    for value in data.values():
        if isinstance(value, dict):
            found = _extract_transfer(value)
            if found:
                return found
    return None

def _build_transfer(quote: Dict[str, object], wallet: WalletData) -> Dict[str, object]:
    request_id = str(uuid.uuid4())
    params = {
        "quote": quote,
        "source_address": {"blockchain": BLOCKCHAIN_ID, "address": wallet.address_hex},
        "destination_address": {"blockchain": BLOCKCHAIN_ID, "address": wallet.address_hex},
        "gas_excess_address": {"blockchain": BLOCKCHAIN_ID, "address": wallet.address_hex},
        "use_recommended_slippage": True,
    }
    payload = {
        "jsonrpc": "2.0",
        "id": request_id,
        "method": "v1beta7.transaction.build_transfer",
        "params": params,
    }

    async def _run() -> Dict[str, object]:
        async with websockets.connect(OMNISTON_WS_URL, ping_interval=20, ping_timeout=20) as ws:
            await ws.send(json.dumps(payload))
            deadline = time.time() + TRANSFER_TIMEOUT
            while time.time() < deadline:
                raw = await asyncio.wait_for(ws.recv(), timeout=max(0.1, deadline - time.time()))
                data = json.loads(raw)
                if data.get("error"):
                    raise RuntimeError(data["error"])
                transfer = _extract_transfer(data.get("result")) or _extract_transfer(data)
                if transfer:
                    return {"jsonrpc": data.get("jsonrpc", "2.0"), "result": transfer}
            raise TimeoutError("Timed out waiting for transfer build")

    return asyncio.run(_run())

def execute_swap(quote: Dict[str, object], wallet: WalletData) -> bool:
    if not TONCENTER_API_KEY:
        print("TONCENTER_API_KEY not configured; cannot submit transaction automatically.")
        return False

    try:
        transfer = _build_transfer(quote, wallet)
    except Exception as exc:
        print(f"Could not build transfer: {exc}")
        return False

    ton_section = transfer.get("result", {}).get("ton") if isinstance(transfer, dict) else None
    messages = ton_section.get("messages") if isinstance(ton_section, dict) else None
    if not isinstance(messages, list) or not messages:
        print("No transfer messages returned.")
        return False

    msg = messages[0]
    payload_cell = _decode_cell(
        msg.get("payload")
        or msg.get("message_boc")
        or msg.get("messageBoc")
        or msg.get("boc")
    )
    state_init_cell = _decode_cell(
        msg.get("state_init") or msg.get("jetton_wallet_state_init")
    )

    seqno = lookup_wallet_seqno(wallet.address_hex)
    if seqno is None:
        print("Could not fetch wallet seqno; ensure wallet is deployed and funded.")
        return False

    version = WalletVersionEnum(wallet.version)
    _, _, _, contract = Wallets.from_mnemonics(wallet.mnemonic, version, wallet.workchain)

    target_address = msg.get("target_address") or msg.get("address")
    amount_field = msg.get("send_amount") or msg.get("amount")
    try:
        amount_value = int(str(amount_field))
    except Exception:
        print("Invalid send amount in transfer message.")
        return False

    external = contract.create_transfer_message(
        target_address,
        amount_value,
        seqno,
        payload=payload_cell,
        state_init=state_init_cell,
    )

    boc = base64.b64encode(external["message"].to_boc(False)).decode("ascii")
    print("Submitting swap via Toncenter...")
    ok = send_boc(boc)
    print("Swap submitted." if ok else "Toncenter rejected the transaction.")
    return ok
```

Copy
```
MIN_INIT_BALANCE_TON = Decimal("0.25")

def main() -> None:
    load_env()
    config = load_config()

    print("Omniston Python Quickstart")
    print("==========================")

    wallet = ensure_wallet()
    print(f"Wallet: {wallet.address_bounceable}")

    balance = fetch_balance(wallet.address_hex) or Decimal("0")
    print(f"Balance: {format_amount(balance, 9)} TON")

    if balance < MIN_INIT_BALANCE_TON:
        need = format_amount(MIN_INIT_BALANCE_TON, 9)
        print(f"Please fund your wallet with at least {need} TON, then re-run this script.")
        print(f"Send TON to: {wallet.address_bounceable}")
        return

    if not ensure_wallet_deployed(wallet):
        return

    if not prompt_yes_no("Request a quote now?", default=True):
        print("Quote skipped.")
        return

    try:
        quote = request_quote(config, wallet)
    except Exception as exc:
        print(f"Quote request failed: {exc}")
        return

    received, summary = describe_quote(quote, config)
    if received <= Decimal("0"):
        print("Quote returned zero output; aborting.")
        return

    if not prompt_yes_no(f"Swap {summary}?", default=False):
        print("Swap cancelled.")
        return

    print(f"Executing swap: {summary}")
    execute_swap(quote, wallet)

if __name__ == "__main__":
    main()
```

Copy`python omniston_cli.py`

Copy`python omniston_cli.py`

Copy
```
mkdir my-omniston-swap
cd my-omniston-swap
# Place CLAUDE.md (for Claude Code) or AGENTS.md (for other agents) here
```

Copy`gemini`

Copy`Implement Omniston swap according to the Omniston Quickstart Guide in AGENTS.md`
