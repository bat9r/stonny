# GEMINI.md - Stonny's Coding Guide: STON-Integrated Gaming Loot Drops

_This file provides a structured implementation plan for the "STON-Integrated Gaming Loot Drops" idea. Use this to guide an AI agent (Gemini CLI, Claude Code, etc.) through building the integration._

## Project Overview
**Name:** STON-Integrated Gaming Loot Drops
**Concept:** A system for Web3 games to automatically swap in-game loot tokens into liquid assets (TON/Stablecoins) using STON.fi.
**Core Tech:** STON.fi DEX v2 SDK, STON.fi REST API.

---

## Implementation Instructions for AI Agent

### 1. Environment Setup
- Initialize a Node.js/TypeScript project.
- Install dependencies: `@ston-fi/api`, `@ston-fi/sdk`, `@ton/ton`, `@ton/core`.
- Setup `.env` with `TONCENTER_API_KEY` and `REFERRER_ADDRESS` (your wallet to earn fees).

### 2. Implementation Steps

#### Step A: Asset Discovery
Use the STON.fi API to fetch metadata for the "loot tokens" and the "target tokens" (e.g., TON, USDT).
- **Endpoint:** `GET https://api.ston.fi/v1/assets`
- **Goal:** Get symbol, decimals, and icons for the UI.

#### Step B: Swap Simulation (The Price Engine)
Implement a function to get a real-time quote before the player confirms the swap.
- **Endpoint:** `POST https://api.ston.fi/v1/swap/simulate`
- **Params:** `offer_address` (loot token), `ask_address` (TON/USDT), `units` (amount), `slippage_tolerance` (e.g., 0.01).

#### Step C: Transaction Generation (The Revenue Logic)
Use the `@ston-fi/sdk` to build the transaction parameters. **CRITICAL:** Include the referral fee logic to monetize the game.
- **Tool:** `router.getSwapJettonToJettonTxParams` or `router.getSwapJettonToTonTxParams`.
- **Referral Settings:** 
  - `referralAddress`: Your `REFERRER_ADDRESS`.
  - `referralValue`: `100` (represents 1% fee).

#### Step D: Wallet Integration
Provide a helper to send the generated `txParams` via TonConnect or a direct provider.

---

## AI Prompt for Execution
> "I want to implement a STON.fi swap integration for a game loot system. Follow the steps in GEMINI.md: 
> 1. Fetch asset metadata using `@ston-fi/api`.
> 2. Implement a simulation function to get quotes.
> 3. Create a transaction builder using `@ston-fi/sdk` that includes a 1% referral fee.
> 4. Ensure the code is modular and includes error handling for slippage and gas."

---

## Success Criteria
- [ ] User can see the exchange rate for their loot.
- [ ] A valid TON transaction is generated.
- [ ] The transaction contains the specified referral fee address.
- [ ] All token decimals are handled correctly (e.g., converting human-readable amounts to nano-units).
