# Open Questions v2.1

This document lists unresolved questions and research tasks required to
complete the planning stage.  Assign responsibility for each item and update
the document as questions are answered.  If an answer results in a plan
change, update the Validation Matrix, Traceability Index and relevant
documents.

| ID | Question / research task | Assigned to | Status | Notes |
| --- | --- | --- | --- | --- |
| Q1 | **Broker support for MOC/LOC:** confirm that the chosen broker (e.g., Interactive Brokers) supports Market‑on‑Close and Limit‑on‑Close orders for the selected ETFs, and identify any additional cut‑off times or restrictions. | TBD | Open | Broker websites were inaccessible during initial research; need to contact support or retrieve documentation. |
| Q2 | **ETF liquidity and slippage:** obtain quantitative liquidity metrics (average daily volume, bid‑ask spread) for each ETF to validate the assumption that closing auction participation yields fair execution. | TBD | Open | Use vendor data or public sources to compute metrics.  Update Universe section if an ETF fails liquidity thresholds. |
| Q3 | **Impact of short‑term volatility on ranking window:** investigate whether shorter lookback windows (e.g., 6‑1) improve risk‑adjusted returns or reduce crash risk.  Use CSCV/PBO to evaluate. | TBD | Open | If a different window is adopted, update the Config Schema and Plan. |
| Q4 | **Dynamic risk overlay:** evaluate strategies for scaling exposure based on volatility, correlation or drawdown signals.  Determine thresholds and implementation details. | TBD | Open | Research may include academic papers on volatility‑managed portfolios. |
| Q5 | **Tax implications beyond wash‑sales:** assess treatment of dividends, capital gains distribution from ETFs, and state taxes. | TBD | Open | Consult IRS publications and state tax statutes. |

## Process

1. Assign each question to a responsible party with a due date.
2. Document findings in a structured note or ADR.  Provide citations to
   primary sources (e.g., broker documentation, regulatory filings, academic
   literature).
3. Update the plan, Validation Matrix and Traceability Index based on the
   findings.
