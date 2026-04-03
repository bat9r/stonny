Title: Omniston Guide (React) | STON.fi

URL Source: https://docs.ston.fi/developer-section/quickstart/omniston

Markdown Content:
# Omniston Guide (React) | STON.fi

[![Image 1: Logo](https://docs.ston.fi/~gitbook/image?url=https%3A%2F%2F4271849708-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Forganizations%252FZCdWXRNv8GO6UNNDbtrW%252Fsites%252Fsite_m0Ami%252Flogo%252FAxXm0NG1A4HsVWbljk2l%252Ffull-logo.svg%3Falt%3Dmedia%26token%3D51d99838-856a-458e-bdd5-1f8c8f70d229&width=260&dpr=3&quality=100&sign=8c496dff&sv=2)![Image 2: Logo](https://docs.ston.fi/~gitbook/image?url=https%3A%2F%2F4271849708-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Forganizations%252FZCdWXRNv8GO6UNNDbtrW%252Fsites%252Fsite_m0Ami%252Flogo%252FNNUHc1w7Tf2DgkqOXMg7%252Flogo-black.svg%3Falt%3Dmedia%26token%3Ddaa19060-c6c6-4222-a93c-c378710829d7&width=260&dpr=3&quality=100&sign=b31fba20&sv=2)](https://docs.ston.fi/)

⌘Ctrl k

[![Image 3: Logo](https://docs.ston.fi/~gitbook/image?url=https%3A%2F%2F4271849708-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Forganizations%252FZCdWXRNv8GO6UNNDbtrW%252Fsites%252Fsite_m0Ami%252Flogo%252FAxXm0NG1A4HsVWbljk2l%252Ffull-logo.svg%3Falt%3Dmedia%26token%3D51d99838-856a-458e-bdd5-1f8c8f70d229&width=260&dpr=3&quality=100&sign=8c496dff&sv=2)![Image 4: Logo](https://docs.ston.fi/~gitbook/image?url=https%3A%2F%2F4271849708-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Forganizations%252FZCdWXRNv8GO6UNNDbtrW%252Fsites%252Fsite_m0Ami%252Flogo%252FNNUHc1w7Tf2DgkqOXMg7%252Flogo-black.svg%3Falt%3Dmedia%26token%3Ddaa19060-c6c6-4222-a93c-c378710829d7&width=260&dpr=3&quality=100&sign=b31fba20&sv=2)](https://docs.ston.fi/)

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

# Omniston Guide (React)

Quick integration guide for Omniston - start building cross-DEX aggregation features in minutes

This guide will walk you through creating a basic token swap app using the **Omniston** protocol to swap assets across different DEXes (STON.fi V1, STON.fi V2, DeDust, etc.). We'll integrate wallet connectivity with **TonConnect** (via `@tonconnect/ui-react`) to allow users to connect their TON wallet and perform a swap. The guide is beginner-friendly and assumes minimal React experience.

> **Note**: In this demo, we will leverage **Tailwind CSS** for styling instead of using custom CSS. The setup for Tailwind CSS is already included in the instructions below, so you don't need to set it up separately.

> **Note**: You can use any package manager (npm, yarn, pnpm, or bun) to set up your React project. In this tutorial, we'll demonstrate with **pnpm**.

* * *

## [](https://docs.ston.fi/developer-section/quickstart/omniston#table-of-contents)

Table of Contents

1.     [Introduction](https://docs.ston.fi/developer-section/quickstart/omniston#id-1.-introduction) 
2.     [Setting Up the Project](https://docs.ston.fi/developer-section/quickstart/omniston#id-2.-setting-up-the-project) 
3.     [Connecting the Wallet](https://docs.ston.fi/developer-section/quickstart/omniston#id-3.-connecting-the-wallet) 
4.     [Fetching Available Assets](https://docs.ston.fi/developer-section/quickstart/omniston#id-4.-fetching-available-assets) 
5.     [Requesting a Quote](https://docs.ston.fi/developer-section/quickstart/omniston#id-5.-requesting-a-quote) 
6.     [Building a Transaction](https://docs.ston.fi/developer-section/quickstart/omniston#id-6.-building-a-transaction) 
7.     [Tracking Your Trade](https://docs.ston.fi/developer-section/quickstart/omniston#id-7.-tracking-your-trade) 
8.     [Testing Your Swap](https://docs.ston.fi/developer-section/quickstart/omniston#id-8.-testing-your-swap) 
9.     [Conclusion](https://docs.ston.fi/developer-section/quickstart/omniston#id-9.-conclusion) 
10.     [Live Demo](https://docs.ston.fi/developer-section/quickstart/omniston#id-10.-live-demo) 
11.     [Advanced Example App](https://docs.ston.fi/developer-section/quickstart/omniston#id-11.-advanced-example-app) 
12.     [Using AI Agents for Automated Implementation](https://docs.ston.fi/developer-section/quickstart/omniston#id-12.-using-ai-agents-for-automated-implementation) 

* * *

## [](https://docs.ston.fi/developer-section/quickstart/omniston#id-1.-introduction)

1. Introduction

In this quickstart, we will build a minimal React app to:

*     Connect to a TON wallet (via **TonConnect UI**). 
*     Fetch available tokens from STON.fi and display them in dropdowns. 
*     Request a quote (RFQ) from Omniston for the best swap route (no separate "Simulate" step needed; Omniston fetches quotes automatically). 
*     Build and execute a swap transaction across multiple DEXes. 
*     Track the trade status until completion. 

We will use:

*     `@ston-fi/omniston-sdk-react` – React hooks to interact with Omniston (request quotes, track trades, etc.). 
*     `@ston-fi/api` – Fetch token lists from STON.fi (and potentially other data). 
*     `@tonconnect/ui-react` – Provides a React-based TON wallet connect button and utilities. 
*     `@ton/core` – TON low-level library used for advanced functionality. 

* * *

## [](https://docs.ston.fi/developer-section/quickstart/omniston#id-2.-setting-up-the-project)

2. Setting Up the Project

### [](https://docs.ston.fi/developer-section/quickstart/omniston#id-2.1-create-a-react-app)

2.1 Create a React App

First, let's check if pnpm is installed on your system:

If you see a version number (like `10.4.0`), pnpm is installed. If you get an error, you'll need to install pnpm first:

Now we'll create a new React project using **Vite**. However, you can use any React setup you prefer (Next.js, CRA, etc.).

Run the following command to create a new Vite-based React project:

When prompted, type your desired project name (e.g., omniston-swap-app):

Then enter the folder:

* * *

### [](https://docs.ston.fi/developer-section/quickstart/omniston#id-2.2-installing-the-required-packages)

2.2 Installing the Required Packages

Within your new React project directory, install the Omniston SDK, TonConnect UI, the TON core library, and STON.fi API library:

Next, install Tailwind CSS and its Vite plugin:

Additionally, install the Node.js polyfills plugin for Vite, which is necessary to provide Buffer and other Node.js APIs in the browser environment (required by TON libraries):

Configure the Vite plugin by updating `vite.config.js` file. Only the `buffer` shim plus the global `Buffer` are required for TON libraries, so the configuration stays tight:

Then, import Tailwind CSS in your main CSS file. Open `src/index.css` and replace any existing code with:

You can also remove `src/App.css` (we don't need it), and remove the import statement `import './App.css'` from `src/App.tsx`.

After making these changes, you can verify that your app still runs correctly by starting the development server:

This should launch your app in development mode, typically at `http://localhost:5173`. You should see the Vite + React logo and text on a plain white background. Since we've removed the default styling (App.css), the page will look simpler than the default template.

If you see the logo and text, it means your Vite + React setup is working correctly. Make sure everything loads without errors before proceeding to the next step.

* * *

## [](https://docs.ston.fi/developer-section/quickstart/omniston#id-3.-connecting-the-wallet)

3. Connecting the Wallet

### [](https://docs.ston.fi/developer-section/quickstart/omniston#id-3.1-add-nessary-providers)

3.1 Add nessary providers

Open **src/main.tsx** (Vite's default entry point) and wrap your application with both the `TonConnectUIProvider` and `OmnistonProvider`. The `TonConnectUIProvider` makes the TonConnect context available to your app for wallet connectivity, while the `OmnistonProvider` enables Omniston's functionality throughout your application. Also, point the TonConnect provider to a manifest file (which we will create next) that describes your app to wallets.

* * *

### [](https://docs.ston.fi/developer-section/quickstart/omniston#id-3.2-create-the-tonconnect-manifest)

3.2 Create the TonConnect Manifest

In the **public** folder of your project, create a file named **tonconnect-manifest.json**. This manifest provides wallet apps with information about your application (like name and icon). You should customize this manifest for your own application. Here's an example:

Make sure to update these fields for your application:

*     **url**: The base URL where your app is served 
*     **name**: Your application's display name (this is what wallets will show to users) 
*     **iconUrl**: A link to your app's icon (should be a 180×180 PNG image) 

Make sure this file is accessible. When the dev server runs, you should be able to fetch it in your browser at `http://localhost:5173/tonconnect-manifest.json`.

* * *

### [](https://docs.ston.fi/developer-section/quickstart/omniston#id-3.3-add-the-connect-wallet-button)

3.3 Add the Connect Wallet Button

In your main **App** component (e.g., **src/App.tsx**), import and include the `TonConnectButton`. For example:

* * *

## [](https://docs.ston.fi/developer-section/quickstart/omniston#id-4.-fetching-available-assets)

4. Fetching Available Assets

Next, let's dynamically retrieve the list of tokens (assets) that can be swapped on STON.fi. We use the STON.fi API client (`@ston-fi/api`) for this. Here's a simplified example that filters assets by liquidity (high to medium). We'll store them in state and present them in From/To dropdowns.

First, add the necessary imports to what we have in `src/App.tsx`:

Initialize the state variables in your App component:

Add the asset fetching logic with useEffect:

Create the main UI structure:

Add the token selection dropdowns:

Add the loading state and close the component:

* * *

## [](https://docs.ston.fi/developer-section/quickstart/omniston#id-5.-requesting-a-quote)

5. Requesting a Quote

We'll use the `useRfq` hook from `@ston-fi/omniston-sdk-react` to request a quote. It will fetch quotes automatically based on the parameters given.

Add additional imports to the top of the file:

Add utility functions for converting token amounts:

Set up the `useRfq` hook to automatically fetch quotes:

Add the quote display section to your tsx (insert after the amount input field):

Any time the user changes the token or amount, `useRfq` automatically refreshes the quote.

* * *

## [](https://docs.ston.fi/developer-section/quickstart/omniston#id-6.-building-a-transaction-and-sending-it)

6. Building a Transaction and Sending It

Once we have a quote, we can build the transaction that will execute the swap. We'll use the `useOmniston` hook to access the Omniston instance and build the transaction.

Replace imports for `@tonconnect/ui-react` and `@ston-fi/omniston-sdk-react` with:

Add wallet connection hooks and omniston instance:

Create the transaction building function:

Add the swap execution function:

Add the Execute Swap button (insert after in quote section):

* * *

## [](https://docs.ston.fi/developer-section/quickstart/omniston#id-7.-tracking-your-trade)

7. Tracking Your Trade

### [](https://docs.ston.fi/developer-section/quickstart/omniston#id-7.1-install-the-ton-package)

7.1 Install the TON Package

We'll track trades using the `useTrackTrade` hook from `@ston-fi/omniston-sdk-react`. First, ensure you have the `@ton/ton` package installed if you haven't already:

### [](https://docs.ston.fi/developer-section/quickstart/omniston#id-7.2-using-the-usetracktrade-hook)

7.2 Using the useTrackTrade Hook

After you've built and sent the swap transaction, you can track its status with `useTrackTrade`. This hook takes the `quoteId` of the trade, your wallet address, and the outgoing transaction hash. It periodically checks the trade's on-chain status, letting you know if it's pending, settled, or partially filled.

Replace imports for `@ton/ton` and `@ston-fi/omniston-sdk-react` for trade tracking:

Add state variables for tracking:

Reset tracking state when inputs change:

Update the useRfq hook to stop fetching quotes during trade execution:

Set up the trade tracking hook:

Add helper function to translate trade results:

Add utility functions for transaction hash extraction:

Update the handleSwap function to capture transaction details:

Add the trade status display (insert after the divider line):

Update the error display in the quote section

* * *

## [](https://docs.ston.fi/developer-section/quickstart/omniston#id-8.-testing-your-swap)

8. Testing Your Swap

1.     Start the development server: 

1.     Open your app in the browser at `http://localhost:5173`. 
2.     Connect your TON wallet via the "Connect Wallet" button. 
3.     Select tokens from the dropdowns and enter an amount. 
4.     Omniston automatically fetches and displays a quote. Confirm it's valid. 
5.     Click "Execute Swap" to finalize the transaction. Approve it in your wallet. 
6.     Once the swap completes on-chain, your wallet balances should update accordingly. 

* * *

## [](https://docs.ston.fi/developer-section/quickstart/omniston#id-9.-conclusion)

9. Conclusion

Congratulations! You've built a minimal React + Vite app with Tailwind CSS that:

*     Connects to a TON wallet using TonConnect. 
*     Dynamically fetches available tokens from STON.fi. 
*     Requests real-time quotes (RFQs) from Omniston automatically. 
*     Builds and sends swap transactions. 

Feel free to expand this demo with:

*     Custom slippage settings. 
*     Better error-handling and success notifications. 
*     Additional settlement methods or cross-chain logic. 
*     Learn how to add referral fees to your Omniston swaps by reading the [Referral Fees guide](https://docs.ston.fi/developer-section/omniston/referral-fees). 

Happy building with Omniston!

## [](https://docs.ston.fi/developer-section/quickstart/omniston#id-10.-live-demo)

10. Live Demo

With this Replit demo, you can:

*     Open the project directly in your browser 
*     Fork the Replit to make your own copy 
*     Run the application to see it in action 
*     Explore and modify the code to learn how it works 
*     Experiment with different features and UI changes 

Alternatively, you can run this example locally by cloning the GitHub repository:

This will start the development server and you can access the app at `http://localhost:5173`.

## [](https://docs.ston.fi/developer-section/quickstart/omniston#id-11.-advanced-example-app)

11. Advanced Example App

For those seeking a feature-rich, more advanced approach, we also have a Next.js Omniston Demo App that:

*     Uses Next.js for a scalable framework 
*     Utilizes hooks and providers for an elegant architecture 
*     Demonstrates better error handling, robust state management, and additional STON.fi and Omniston features 

You can explore the code in our repository:

[Omniston SDK Next.js Demo App](https://github.com/ston-fi/omniston-sdk/tree/main/examples/next-js-app)

Or see it in action at our live demo:

[Omniston Demo App](https://omniston.ston.fi/)

## [](https://docs.ston.fi/developer-section/quickstart/omniston#id-12.-using-ai-agents-for-automated-implementation)

12. Using AI Agents for Automated Implementation

For developers looking to accelerate their development process, you can leverage **AI coding agents** to automatically implement the Omniston swap functionality described in this guide. While we showcase **Gemini CLI** in our example (due to its generous free tier), you can use any AI coding assistant such as **Claude Code**, **GitHub Copilot**, **Cursor Agent**, or similar tools.

You can also follow along with a recorded walkthrough:

### [](https://docs.ston.fi/developer-section/quickstart/omniston#id-12.1-why-ai-agents)

12.1 Why AI Agents?

Modern AI coding agents can:

*     Understand complex documentation and implement complete features 
*     Set up project structure and dependencies automatically 
*     Handle common configuration and setup errors 
*     Provide working implementations in minutes instead of hours 

### [](https://docs.ston.fi/developer-section/quickstart/omniston#id-12.2-setting-up-with-gemini-cli-example)

12.2 Setting Up with Gemini CLI (Example)

We'll demonstrate with Gemini CLI, but the approach works with any AI agent that can read documentation and execute commands.

#### [](https://docs.ston.fi/developer-section/quickstart/omniston#id-12.2.1-installing-gemini-cli)

12.2.1 Installing Gemini CLI

1.     Install the Gemini CLI by following the instructions at: [https://github.com/google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) 
2.     

Authenticate with your Google account when prompted. The free tier includes:

    *     60 model requests per minute 
    *     1,000 model requests per day 

#### [](https://docs.ston.fi/developer-section/quickstart/omniston#id-12.2.2-setting-up-the-implementation-guide)

12.2.2 Setting Up the Implementation Guide

1.     Download the `GEMINI.md` file from the gist: [https://gist.github.com/mrruby/311a9d96f12bc7303bb1046dc92092b3](https://gist.github.com/mrruby/311a9d96f12bc7303bb1046dc92092b3) 
2.     

Rename the file based on your AI agent:

    *     **For Gemini CLI**: Use `GEMINI.md` as-is (no renaming needed) 
    *     **For Claude Code**: Rename `GEMINI.md` to `CLAUDE.md` 
    *     **For other AI agents** (GitHub Copilot, Cursor, etc.): Rename `GEMINI.md` to `AGENTS.md` 

3.     Create a new directory for your project and place the guide file inside it: 

#### [](https://docs.ston.fi/developer-section/quickstart/omniston#id-12.2.3-running-the-automated-implementation)

12.2.3 Running the Automated Implementation

1.     From within your project directory, run the Gemini CLI: 
2.     When the CLI interface opens, type: 
3.     

The AI agent will:

    *     Ask for permission to use commands like `pnpm`, `npm`, etc. 
    *     Automatically create the project structure 
    *     Install all necessary dependencies 
    *     Implement the complete swap functionality 
    *     Set up the UI components and styling 

4.     

If any errors occur during the process:

    *     Simply paste the error message back to the AI agent 
    *     It will analyze and fix the issue automatically 
    *     In most cases, the implementation completes successfully in one shot 

### [](https://docs.ston.fi/developer-section/quickstart/omniston#id-12.3-using-other-ai-agents)

12.3 Using Other AI Agents

The same approach works with other AI coding assistants:

*     **Gemini CLI**: Download `GEMINI.md` from the gist and use as-is 
*     **Claude Code**: Download `GEMINI.md` from the gist and rename it to `CLAUDE.md`, then place it in your project and ask Claude Code to implement the guide 
*     **GitHub Copilot**: Download `GEMINI.md` from the gist and rename it to `AGENTS.md`, open the guide in your editor and use Copilot Chat to implement step by step 
*     **Cursor Agent**: Download `GEMINI.md` from the gist and rename it to `AGENTS.md`, load the documentation and request full implementation via Cursor's agent mode 
*     **Other AI Tools**: Download `GEMINI.md` and rename to `AGENTS.md` for compatibility with most AI assistants 

> **Note**: The gist contains `GEMINI.md` which works directly with Gemini CLI. For Claude Code, rename it to `CLAUDE.md`. For other AI agents (GitHub Copilot, Cursor, etc.), rename it to `AGENTS.md` for best compatibility.

### [](https://docs.ston.fi/developer-section/quickstart/omniston#id-12.4-benefits-of-using-ai-agents)

12.4 Benefits of Using AI Agents

*     **Speed**: Get a working implementation in minutes instead of hours 
*     **Accuracy**: AI agents follow the quickstart guide precisely 
*     **Error Handling**: Automatically resolve most common setup issues 
*     **Learning Tool**: Watch how the implementation unfolds step by step 
*     **Customization**: After the initial setup, you can modify the generated code to fit your specific needs 
*     **Cost-Effective**: Many AI coding tools offer free tiers (like Gemini CLI) or are included in existing subscriptions 

### [](https://docs.ston.fi/developer-section/quickstart/omniston#id-12.5-best-practices)

12.5 Best Practices

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

[Previous Liquidity Providing Guide (React)](https://docs.ston.fi/developer-section/quickstart/liquidity)[Next Omniston Guide (Python)](https://docs.ston.fi/developer-section/quickstart/python)

Last updated 4 months ago

*   [Table of Contents](https://docs.ston.fi/developer-section/quickstart/omniston#table-of-contents)
*   [1. Introduction](https://docs.ston.fi/developer-section/quickstart/omniston#id-1.-introduction)
*   [2. Setting Up the Project](https://docs.ston.fi/developer-section/quickstart/omniston#id-2.-setting-up-the-project)
*   [2.1 Create a React App](https://docs.ston.fi/developer-section/quickstart/omniston#id-2.1-create-a-react-app)
*   [2.2 Installing the Required Packages](https://docs.ston.fi/developer-section/quickstart/omniston#id-2.2-installing-the-required-packages)
*   [3. Connecting the Wallet](https://docs.ston.fi/developer-section/quickstart/omniston#id-3.-connecting-the-wallet)
*   [3.1 Add nessary providers](https://docs.ston.fi/developer-section/quickstart/omniston#id-3.1-add-nessary-providers)
*   [3.2 Create the TonConnect Manifest](https://docs.ston.fi/developer-section/quickstart/omniston#id-3.2-create-the-tonconnect-manifest)
*   [3.3 Add the Connect Wallet Button](https://docs.ston.fi/developer-section/quickstart/omniston#id-3.3-add-the-connect-wallet-button)
*   [4. Fetching Available Assets](https://docs.ston.fi/developer-section/quickstart/omniston#id-4.-fetching-available-assets)
*   [5. Requesting a Quote](https://docs.ston.fi/developer-section/quickstart/omniston#id-5.-requesting-a-quote)
*   [6. Building a Transaction and Sending It](https://docs.ston.fi/developer-section/quickstart/omniston#id-6.-building-a-transaction-and-sending-it)
*   [7. Tracking Your Trade](https://docs.ston.fi/developer-section/quickstart/omniston#id-7.-tracking-your-trade)
*   [7.1 Install the TON Package](https://docs.ston.fi/developer-section/quickstart/omniston#id-7.1-install-the-ton-package)
*   [7.2 Using the useTrackTrade Hook](https://docs.ston.fi/developer-section/quickstart/omniston#id-7.2-using-the-usetracktrade-hook)
*   [8. Testing Your Swap](https://docs.ston.fi/developer-section/quickstart/omniston#id-8.-testing-your-swap)
*   [9. Conclusion](https://docs.ston.fi/developer-section/quickstart/omniston#id-9.-conclusion)
*   [10. Live Demo](https://docs.ston.fi/developer-section/quickstart/omniston#id-10.-live-demo)
*   [11. Advanced Example App](https://docs.ston.fi/developer-section/quickstart/omniston#id-11.-advanced-example-app)
*   [12. Using AI Agents for Automated Implementation](https://docs.ston.fi/developer-section/quickstart/omniston#id-12.-using-ai-agents-for-automated-implementation)
*   [12.1 Why AI Agents?](https://docs.ston.fi/developer-section/quickstart/omniston#id-12.1-why-ai-agents)
*   [12.2 Setting Up with Gemini CLI (Example)](https://docs.ston.fi/developer-section/quickstart/omniston#id-12.2-setting-up-with-gemini-cli-example)
*   [12.3 Using Other AI Agents](https://docs.ston.fi/developer-section/quickstart/omniston#id-12.3-using-other-ai-agents)
*   [12.4 Benefits of Using AI Agents](https://docs.ston.fi/developer-section/quickstart/omniston#id-12.4-benefits-of-using-ai-agents)
*   [12.5 Best Practices](https://docs.ston.fi/developer-section/quickstart/omniston#id-12.5-best-practices)

Copy`pnpm --version`

Copy`npm install -g pnpm`

Copy`pnpm create vite --template react-ts`

Copy`Project name: » omniston-swap-app`

Copy`cd omniston-swap-app`

Copy`pnpm add @ston-fi/omniston-sdk-react @tonconnect/ui-react @ton/core @ston-fi/api`

Copy`pnpm add tailwindcss @tailwindcss/vite`

Copy`pnpm add vite-plugin-node-polyfills`

Copy
```
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'
import { nodePolyfills } from 'vite-plugin-node-polyfills'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    react(),
    tailwindcss(),
    nodePolyfills({
      include: ['buffer'],
      globals: {
        Buffer: true,
      },
    }),
  ],
})
```

Copy`@import "tailwindcss";`

Copy
```
pnpm install
pnpm dev
```

Copy
```
// src/main.tsx
import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { TonConnectUIProvider } from '@tonconnect/ui-react';
import { Omniston, OmnistonProvider } from '@ston-fi/omniston-sdk-react';
import './index.css'
import App from './App.tsx'

const omniston = new Omniston({ apiUrl: "wss://omni-ws.ston.fi" });

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <TonConnectUIProvider 
      // For demo purposes, we're using a static manifest URL
      // Replace with your own: manifestUrl={`${window.location.origin}/tonconnect-manifest.json`}
      manifestUrl="https://gist.githubusercontent.com/mrruby/243180339f492a052aefc7a666cb14ee/raw/">
      <OmnistonProvider omniston={omniston}>
        <App />
      </OmnistonProvider>
    </TonConnectUIProvider>
  </StrictMode>,
)
```

Copy
```
{
  "url": "https://omniston-demo.example.com",
  "name": "Omniston Swap Demo",
  "iconUrl": "https://omniston-demo.example.com/icon-192x192.png"
}
```

Copy
```
// src/App.tsx
import { TonConnectButton } from '@tonconnect/ui-react';

function App() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen p-4">
      <h1 className="text-2xl font-bold mb-4">Omniston Swap Demo</h1>
      <TonConnectButton />
    </div>
  );
}

export default App;
```

Copy
```
import { useEffect, useState } from 'react';
import { StonApiClient, AssetTag, type AssetInfoV2 } from '@ston-fi/api';
```

Copy
```
function App() {
  const [assets, setAssets] = useState<AssetInfoV2[]>([]);
  const [fromAsset, setFromAsset] = useState<AssetInfoV2 | undefined>();
  const [toAsset, setToAsset] = useState<AssetInfoV2 | undefined>();
  const [amount, setAmount] = useState('');
```

Copy
```
// fetch assets on mount
  useEffect(() => {
    const fetchAssets = async () => {
      try {
        const client = new StonApiClient();
        // Filter out top liquidity tokens for brevity
        const condition = [
          AssetTag.LiquidityVeryHigh,
          AssetTag.LiquidityHigh,
          AssetTag.LiquidityMedium
        ].join(' | ');
        const assetList = await client.queryAssets({ condition });

        setAssets(assetList);
        if (assetList.length > 0) {
          setFromAsset(assetList[0]);
        }
        if (assetList.length > 1) {
          setToAsset(assetList[1]);
        }
      } catch (err) {
        console.error('Failed to fetch assets:', err);
      }
    };
    fetchAssets();
  }, []);
```

Copy
```
return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gradient-to-b from-blue-50 to-indigo-100 p-6">
      <div className="w-full max-w-md bg-white rounded-xl shadow-lg p-6 space-y-6">
        <div className="flex justify-between items-center">
          <h1 className="text-3xl font-bold text-indigo-700">Omniston Swap</h1>
          <TonConnectButton />
        </div>

        <div className="h-px bg-gray-200 w-full my-4"></div>
```

Copy
```
{assets.length > 0 ? (
          <div className="space-y-6">
            {/* From */}
            <div className="flex flex-col">
              <label className="text-sm font-medium text-gray-600 mb-1">
                From
              </label>
              <select
                value={fromAsset?.contractAddress || ''}
                onChange={(e) => {
                  const selected = assets.find(a => a.contractAddress === e.target.value);
                  setFromAsset(selected);
                }}
                className="w-full p-3 bg-gray-50 border border-gray-200 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition-all"
              >
                {assets.map(asset => (
                  <option
                    key={asset.contractAddress}
                    value={asset.contractAddress}
                  >
                    {asset.meta?.symbol || asset.meta?.displayName || 'token'}
                  </option>
                ))}
              </select>
            </div>

            {/* To */}
            <div className="flex flex-col">
              <label className="text-sm font-medium text-gray-600 mb-1">
                To
              </label>
              <select
                value={toAsset?.contractAddress || ''}
                onChange={(e) => {
                  const selected = assets.find(a => a.contractAddress === e.target.value);
                  setToAsset(selected);
                }}
                className="w-full p-3 bg-gray-50 border border-gray-200 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition-all"
              >
                {assets.map(asset => (
                  <option
                    key={asset.contractAddress}
                    value={asset.contractAddress}
                  >
                    {asset.meta?.symbol || asset.meta?.displayName || 'token'}
                  </option>
                ))}
              </select>
            </div>

            {/* Amount */}
            <div className="flex flex-col">
              <label className="text-sm font-medium text-gray-600 mb-1">
                Amount
              </label>
              <input
                type="text"
                value={amount}
                onChange={(e) => setAmount(e.target.value)}
                placeholder="0.0"
                className="w-full p-3 bg-gray-50 border border-gray-200 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition-all"
              />
            </div>
          </div>
```

Copy
```
) : (
          <div className="flex justify-center items-center py-10">
            <div className="animate-pulse flex space-x-2">
              <div className="h-2 w-2 bg-indigo-500 rounded-full"></div>
              <div className="h-2 w-2 bg-indigo-500 rounded-full"></div>
              <div className="h-2 w-2 bg-indigo-500 rounded-full"></div>
            </div>
            <p className="ml-3 text-gray-600">Loading assets...</p>
          </div>
        )}
      </div>

      <div className="mt-6 text-center text-xs text-gray-500">
        Powered by Ston.fi
      </div>
    </div>
  );
}

export default App;
```

Copy`import { useRfq, SettlementMethod, Blockchain, GaslessSettlement } from "@ston-fi/omniston-sdk-react";`

Copy
```
// Convert floating point string amount into integer base units string
// Essential for blockchain transactions which use integer arithmetic
function toBaseUnits(amount: string, decimals?: number) {
  return Math.floor(parseFloat(amount) * 10 ** (decimals ?? 9)).toString();
}

// Convert integer base units back to a fixed 2-decimal string for display
function fromBaseUnits(baseUnits: string, decimals?: number) {
  return (parseInt(baseUnits) / 10 ** (decimals ?? 9)).toFixed(2);
}
```

Copy
```
function App() {
  ...
  const { data: quote, isLoading: quoteLoading, error: quoteError } = useRfq({
    settlementMethods: [SettlementMethod.SETTLEMENT_METHOD_SWAP],
    bidAssetAddress: fromAsset
      ? { blockchain: Blockchain.TON, address: fromAsset.contractAddress }
      : undefined,
    askAssetAddress: toAsset
      ? { blockchain: Blockchain.TON, address: toAsset.contractAddress }
      : undefined,
    amount: {
      bidUnits: fromAsset ? toBaseUnits(amount, fromAsset.meta?.decimals) : '0'
    },
    settlementParams: {
      gaslessSettlement: GaslessSettlement.GASLESS_SETTLEMENT_POSSIBLE,
      maxPriceSlippageBps: 500,
    },
  }, {
    enabled: !!fromAsset?.contractAddress && !!toAsset?.contractAddress && amount !== ''
  });
```

Copy
```
{/* Quote section */}
            <div className="pt-4">
              {quoteLoading && <p>Loading quote...</p>}
              {quoteError && <p className="text-red-500">Error: {String(quoteError)}</p>}
              {quote && 'quote' in quote && (
                <div className="p-4 bg-gray-50 rounded-lg border border-gray-200">
                  <p className="font-semibold text-gray-700">Quote Info</p>
                  <p className="text-sm text-gray-600">Resolver: {quote.quote.resolverName}</p>
                  <p className="text-sm text-gray-600">Bid Units: {fromBaseUnits(quote.quote.bidUnits, fromAsset?.meta?.decimals)}  {fromAsset?.meta?.symbol}</p>
                  <p className="text-sm text-gray-600">Ask Units: {fromBaseUnits(quote.quote.askUnits, toAsset?.meta?.decimals)} {toAsset?.meta?.symbol}</p>
                </div>
              )}
            </div>
```

Copy
```
import { TonConnectButton, useTonAddress, useTonConnectUI } from "@tonconnect/ui-react";
import {
  useRfq,
  SettlementMethod,
  Blockchain,
  GaslessSettlement,
  useOmniston,
  type QuoteResponseEvent_QuoteUpdated,
} from "@ston-fi/omniston-sdk-react";
```

Copy
```
function App() {  
  // ... existing state variables ...
  const walletAddress = useTonAddress();
  const [tonConnect] = useTonConnectUI();
  const omniston = useOmniston();
```

Copy
```
// ... after useRfq hook ...
  async function buildTx(willTradedQuote: QuoteResponseEvent_QuoteUpdated | undefined) {
    if (!willTradedQuote || !walletAddress) {
      alert("Please connect your wallet and ensure a valid quote is loaded.");
      return null;
    }

    try {
      const tx = await omniston.buildTransfer({
        quote: willTradedQuote.quote,
        sourceAddress: {
          blockchain: Blockchain.TON,
          address: walletAddress, // the wallet sending the offer token
        },
        destinationAddress: {
          blockchain: Blockchain.TON,
          address: walletAddress, // the same wallet receiving the ask token
        },
        gasExcessAddress: {
          blockchain: Blockchain.TON,
          address: walletAddress, // excess gas returns to sender
        },
        useRecommendedSlippage: false, // Use recommended slippage from the quote
      });

      return tx.ton?.messages || [];
    } catch (err) {
      console.error("Error building transaction:", err);
      alert("Failed to build transaction. Check console for details.");
      return null;
    }
  }
```

Copy
```
async function handleSwap() {
    if (!quote || quote.type !== 'quoteUpdated') {
      alert("No valid quote available");
      return;
    }
    const willTradedQuote = quote;
    const messages = await buildTx(willTradedQuote);
    if (!messages) return;
    
    try {
      await tonConnect.sendTransaction({
        validUntil: Date.now() + 1000000,
        messages: messages.map((message) => ({
          address: message.targetAddress,
          amount: message.sendAmount,
          payload: message.payload,
        })),
      });
    } catch (err) {
      console.error("Error sending transaction:", err);
      alert("Failed to send transaction. Check console for details.");
    }
  }
```

Copy
```
{quote && 'quote' in quote && (
        <>
          <div className="p-4 bg-gray-50 rounded-lg border border-gray-200">
            <p className="font-semibold text-gray-700">Quote Info</p>
            <p className="text-sm text-gray-600">Resolver: {quote.quote.resolverName}</p>
            <p className="text-sm text-gray-600">Bid Units: {fromBaseUnits(quote.quote.bidUnits, fromAsset?.meta?.decimals)}  {fromAsset?.meta?.symbol}</p>
            <p className="text-sm text-gray-600">Ask Units: {fromBaseUnits(quote.quote.askUnits, toAsset?.meta?.decimals)} {toAsset?.meta?.symbol}</p>
          </div>
          <button
            onClick={handleSwap}
            className="mt-4 w-full bg-indigo-500 hover:bg-indigo-600 text-white font-medium py-3 px-4 rounded-lg transition-all"
          >
            Execute Swap
          </button>
        </>
      )}
```

Copy`pnpm add @ton/ton`

Copy
```
import {
  useRfq,
  SettlementMethod,
  Blockchain,
  GaslessSettlement,
  useOmniston,
  useTrackTrade,
  type QuoteResponseEvent_QuoteUpdated,
  type TradeStatus,
} from "@ston-fi/omniston-sdk-react";
import { TonClient, Address, Cell, beginCell, storeMessage } from "@ton/ton";
```

Copy
```
function App() {
  // ... existing state variables ...
  const [outgoingTxHash, setOutgoingTxHash] = useState("");
  const [tradedQuote, setTradedQuote] = useState<QuoteResponseEvent_QuoteUpdated | null>(null);
```

Copy
```
// Reset outgoingTxHash and tradedQuote when inputs change
  useEffect(() => {
    setTradedQuote(null);
    setOutgoingTxHash("");
  }, [fromAsset, toAsset, amount]);
```

Copy
```
const {
    data: quote,
    isLoading: quoteLoading,
    error: quoteError,
  } = useRfq({
    // ... existing useRfq configuration ...
  }, {
    enabled:
      !!fromAsset?.contractAddress &&
      !!toAsset?.contractAddress &&
      amount !== "" &&
      // add this to stop getting new quotes when we make a transaction
      !outgoingTxHash,
  });
```

Copy
```
const {
    isLoading: trackingLoading,
    error: trackingError,
    data: tradeStatus,
  } = useTrackTrade({
    quoteId: tradedQuote?.quote?.quoteId || '',
    traderWalletAddress: {
      blockchain: Blockchain.TON,
      address: walletAddress || '',
    },
    outgoingTxHash,
  }, {
    enabled: !!tradedQuote?.quote?.quoteId && !!walletAddress && !!outgoingTxHash,
  });
```

Copy
```
// Function to translate trade result to human-readable text
const getTradeResultText = (status: TradeStatus) => {
    if (!status?.status?.tradeSettled) return "";
    
    const result = status.status.tradeSettled.result;
    switch (result) {
      case "TRADE_RESULT_FULLY_FILLED":
        return "Trade completed successfully and fully filled";
      case "TRADE_RESULT_PARTIALLY_FILLED":
        return "Trade partially filled - something went wrong";
      case "TRADE_RESULT_ABORTED":
        return "Trade was aborted";
      case "TRADE_RESULT_UNKNOWN":
      case "UNRECOGNIZED":
      default:
        return "Unknown trade result";
    }
  };
```

Copy
```
// Utility function to retry an async operation
    const retry = async (fn: () => Promise<string>, { retries = 5, delay = 1000 }): Promise<string> => {
      try {
        return await fn();
      } catch (error) {
        if (retries === 0) throw error;
        await new Promise(resolve => setTimeout(resolve, delay));
        return retry(fn, { retries: retries - 1, delay });
      }
    };

    const getTxByBOC = async (exBoc: string, walletAddress: string): Promise<string> => {
      if (!exBoc || !walletAddress) {
        throw new Error('Missing required parameters for transaction tracking');
      }
  
      const client = new TonClient({
        endpoint: 'https://toncenter.com/api/v2/jsonRPC'
      });
  
      const myAddress = Address.parse(walletAddress);
  
      return retry(async () => {
        const transactions = await client.getTransactions(myAddress, {
          limit: 5,
        });
  
        for (const tx of transactions) {
          const inMsg = tx.inMessage;
          if (inMsg?.info.type === 'external-in') {
            const inBOC = inMsg?.body;
            if (typeof inBOC === 'undefined') {
              continue;
            }
  
            const extHash = Cell.fromBase64(exBoc).hash().toString('hex');
            const inHash = beginCell().store(storeMessage(inMsg)).endCell().hash().toString('hex');
  
            if (extHash === inHash) {
              return tx.hash().toString('hex');
            }
          }
        }
        throw new Error('Transaction not found');
      }, { retries: 30, delay: 1000 });
    };
```

Copy
```
async function handleSwap() {
    if (!quote || quote.type !== 'quoteUpdated') {
      alert("No valid quote available");
      return;
    }
    const messages = await buildTx(quote);
    if (!messages) return;
    
    try {
      setTradedQuote(quote);

      const res = await tonConnect.sendTransaction({
        validUntil: Date.now() + 1000000,
        messages: messages.map((message) => ({
          address: message.targetAddress,
          amount: message.sendAmount,
          payload: message.payload,
        })),
      });

      const exBoc = res.boc;
      const txHash = await getTxByBOC(exBoc, walletAddress);
      setOutgoingTxHash(txHash);

    } catch (err) {
      setTradedQuote(null);
      console.error("Error sending transaction:", err);
      alert("Failed to send transaction. Check console for details.");
    }
  }
```

Copy
```
{/* Trade status */}
        {/* right after <div className="h-px bg-gray-200 w-full my-4"></div> */}
        <div className="mt-4 p-4 bg-gray-50 rounded-lg border border-gray-200">
          {trackingLoading && <p className="text-sm text-blue-600">Tracking trade...</p>}
          {trackingError && (
            <p className="text-sm text-orange-600">Trade tracking error: {String(trackingError)}</p>
          )}
          {tradeStatus?.status?.tradeSettled && (
            <p className="text-sm text-green-600">
              Trade Result: {getTradeResultText(tradeStatus)}
            </p>
          )}
        </div>
```

Copy`{quoteError && !outgoingTxHash && <p className="text-red-500">Error: {String(quoteError)}</p>}`

Copy`pnpm dev`

Copy
```
git clone https://github.com/mrruby/omniston-swap-app.git
cd omniston-swap-app
pnpm install
pnpm dev
```

Copy
```
mkdir my-omniston-app
cd my-omniston-app
# Place the renamed file here (GEMINI.md, CLAUDE.md, or AGENTS.md)
```

Copy`gemini`

Copy`Implement Omniston according to Omniston Quickstart Guide`
