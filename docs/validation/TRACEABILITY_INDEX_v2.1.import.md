# Traceability Index v2.1

This index maps sections of the **Plan Proposal** to the supporting evidence
sources and the validation methods outlined in the **Validation Matrix**.  Use
this document as a cross‑reference to ensure that every design choice is
grounded in verifiable evidence and has a corresponding validation procedure.

| Plan section | Description | Evidence | Validation method |
| --- | --- | --- | --- |
| §1.1 Universe | Defines the set of ETFs used for momentum rotation. | Broker product lists (to be researched), liquidity screens, regulatory filings. | Ensure each ETF meets liquidity criteria (e.g., average daily volume > 1 million shares). |
| §1.2 Ranking methodology | Specifies the 12‑1 momentum calculation, selection of top two assets and equal weighting. | Academic studies on momentum, e.g., Jegadeesh & Titman (1993); cross‑sectional momentum literature. | Backtest across multiple periods; evaluate performance and PBO. |
| §1.3 Rebalance cadence and timing | Determines monthly rebalance, second‑to‑last business day, MOC/LOC orders by 3:50 PM. | NYSE closing process rules【604093045262205†L93-L110】【826894920304809†L0-L53】. | Simulate order submission times; verify orders executed at closing price. |
| §1.4 Risk policy | Caps position size at 60 %, sets drawdown trigger, avoids wash‑sale violations. | IRS wash‑sale rule【774704392547939†L223-L239】【238476208366191†L190-L218】; momentum crash research【535019668254404†L50-L66】【535019668254404†L92-L190】. | Backtest with risk controls; monitor drawdown; log wash‑sale window compliance. |
| §1.5 Settlement & funding | Details T+1 settlement obligations and funding schedule. | SEC/FINRA announcements【634620779460672†L263-L320】【228845885160452†L154-L200】. | Dry‑run funding transfers; confirm timely settlement. |
| §1.6 Model validation and robustness | Mandates CSCV and PBO evaluation, rejects models with PBO > 0.05. | PBO paper describing CSCV algorithm【639029512866022†L454-L557】 and PBO definition【639029512866022†L590-L618】. | Implement CSCV; compute PBO; document results. |
| §1.7 Momentum crash risk | Recognises crash risk and proposes mitigations (no shorting, position caps, volatility scaling). | Momentum crash research【535019668254404†L50-L66】【535019668254404†L92-L190】. | Backtest across crash periods; adjust mitigations as needed. |
| §2 Operational considerations | Outlines data sourcing, broker interface, monitoring and governance tasks. | Broker and exchange documentation; security guidelines【813758299569681†L4-L22】. | Verify broker order type support; perform security audits; maintain logs. |

## How to use this index

1. When reading the Plan Proposal, refer to this index to locate the
   underlying evidence for each decision.
2. When adding or modifying a plan section, update this index with
   new evidence sources and validation methods.
3. Cross‑check against the **Validation Matrix** to ensure every risk is
   addressed.
