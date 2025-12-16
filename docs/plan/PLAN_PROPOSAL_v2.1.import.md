# Plan Proposal v2.1 – Cross‑Asset Momentum Rotation

This document proposes a **cross‑asset momentum rotation** strategy for a personal, locally run
trading system.  It synthesises lessons from academic research and regulatory
guidance to produce a transparent, evidence‑backed plan.  No code is present in
this document.  All material assertions are traceable via the **Validation
Matrix** and the **Traceability Index**.

## 1 Overview

The strategy targets a **small set of liquid exchange‑traded funds (ETFs)** that
represent major asset classes.  Each month the system ranks the assets by their
trailing return over a specified lookback window and rotates into the top
performers.  Positions are held for at least one month to avoid frequent
turnover and to reduce wash‑sale risk.  Trading occurs via Market‑on‑Close
(MOC) or Limit‑on‑Close (LOC) orders placed before the exchange auction
cut‑offs to minimise slippage and manual monitoring【604093045262205†L93-L110】.

### 1.1 Universe

The core universe comprises diversified ETFs representing the following asset
classes (ticker suggestions in parentheses):

| Asset class | Example ETF | Rationale |
| --- | --- | --- |
| US equities | SPY | High liquidity, broad market exposure |
| US Treasuries (long‑term) | TLT | Counter‑cyclical behaviour provides diversification |
| Commodities | DBC | Represents broad commodity futures basket |
| Gold | GLD | Traditional safe‑haven asset |
| Cash or short‑term Treasury fund | SHV | Provides a risk‑free benchmark and optional parking |

Additional assets may be added once their liquidity and regulatory
constraints are researched and documented.  A material change to the
universe constitutes a **strategy change** and requires a `strategy_version`
bump.

### 1.2 Ranking methodology

1. **Lookback window:** 12 months of total return data, excluding the most
   recent month (“12‑1” momentum).  This skip period avoids short‑term
   mean‑reversion commonly observed in momentum studies.
2. **Ranking metric:** compute each asset’s cumulative return over the
   lookback window and rank them in descending order.
3. **Selection:** go long the top two ranked assets and allocate
   50/50.  Hold until the next month’s rebalance.
4. **Holding period:** positions are held for at least one calendar month.

This simple cross‑sectional momentum rule draws from the academic literature on
**momentum investing** yet remains transparent and easy to execute.  The
strategy does not employ leverage or derivatives.  Short positions are
avoided to simplify tax and margin considerations.

### 1.3 Rebalance cadence and timing

* **Cadence:** monthly on the second‑to‑last business day.  Selecting the
  penultimate day reduces the risk of rebalancing on holidays or unusual
  market closures.
* **Order type:** use **Market‑on‑Close (MOC)** orders for ETFs that are
  sufficiently liquid.  Limit‑on‑Close (LOC) orders may be used when
  volatility is elevated and a price limit is warranted.  According to the
  New York Stock Exchange’s closing process, MOC and LOC orders can be
  entered until **3:50 PM ET**; after that time they may only be entered on
  the contra‑side of an imbalance and cannot be cancelled after **3:58 PM**【604093045262205†L93-L110】【826894920304809†L0-L53】.  Closing D orders may be
  modified until **3:59:50 PM**【604093045262205†L93-L110】.  Trading ends at
  **4:00 PM**【604093045262205†L93-L110】.  The runbook (see
  `docs/ops/RUNBOOK_v2.1.md`) provides a minute‑by‑minute timeline for
  order submission.
* **Data freeze:** the ranking calculation must complete by **2:30 PM ET** on
  rebalance day so there is sufficient time for review and order entry.

### 1.4 Risk policy

* **Position sizing:** allocate equally (50/50) between the top two assets.
  The system never places more than 60 % of capital in any single asset.
  Remaining capital is held in cash or short‑term Treasury funds.
* **Stop‑loss:** no stop‑loss orders are used; however, a **portfolio‑level
  risk budget** (maximum drawdown of 15 %) triggers a capital preservation
  mode where positions are reduced to cash.
* **Leverage:** none.  The strategy only uses cash and long ETF positions.
* **Tax and wash‑sale considerations:** the strategy avoids selling
  positions at a loss within 30 days before or after buying the same or
  substantially identical security.  Under the IRS wash‑sale rule, losses
  from such trades cannot be deducted【774704392547939†L223-L239】.  To maintain
  deductibility of losses, the holding period is at least one month, and
  replacement trades into substantially identical ETFs are avoided.  The rule
  applies broadly to stocks, bonds, options, ETFs and mutual funds【238476208366191†L190-L218】.

### 1.5 Settlement & funding

* **Settlement cycle:** as of **28 May 2024** the SEC shortened the
  standard settlement cycle for most securities from **T+2** to **T+1**【634620779460672†L263-L320】.
  This means that payment for purchases and delivery of securities is due on
  the **next business day** after the trade【228845885160452†L154-L200】.  The
  runbook ensures that cash is available in the brokerage account **one day
  prior** to the rebalance to meet the T+1 requirement.  Failure to fund
  purchases on time could result in margin calls or forced liquidation.
* **Funding schedule:** initiate transfers at least two business days
  before the rebalance date to ensure cleared funds by trade date +1.  For
  securities sales, proceeds will be available for re‑investment on the
  next business day.

### 1.6 Model validation and robustness

To guard against **backtest overfitting**, the strategy will be evaluated
using **combinatorially symmetric cross‑validation (CSCV)** and the **Probability
of Backtest Overfitting (PBO)** metric.  The algorithm partitions the
backtest performance matrix into equal subperiods and forms all possible
combinations of training and testing sets.  For each combination, the
strategy’s out‑of‑sample performance is compared to its in‑sample rank【639029512866022†L454-L557】.
The distribution of relative ranks is transformed into logits; the PBO is the
portion of logits that are positive【639029512866022†L590-L618】.  A model with
**PBO > 0.05** will be considered overfit and rejected.  CSCV will also be used
to tune the lookback window and number of assets selected.

### 1.7 Momentum crash risk

Momentum strategies have historically delivered attractive average returns but
are subject to **occasional crashes**.  Research by Daniel and Moskowitz
(2016) shows that momentum portfolios can experience **large negative returns**
following market declines when volatility is high【535019668254404†L50-L66】.  These
crashes occur because the strategy goes long low‑beta winners and short
high‑beta losers, which creates a **time‑varying beta exposure** that turns
strongly negative during rapid market rebounds【535019668254404†L92-L190】.  In the
context of this plan, the following mitigations are proposed:

* Avoid shorting; only take long positions.
* Limit allocation to risky assets (cap any single position at 60 % of
  capital) and maintain a cash buffer.
* Monitor market volatility; if the 30‑day realised volatility of the
  equity market exceeds a threshold (e.g., 30 %), reduce allocation
  proportionally.
* Document and continually update crash scenarios in the Validation
  Matrix and implement dynamic risk controls in future versions.

## 2 Operational Considerations

Implementation of this plan will only commence once all **acceptance criteria**
are met.  Key operational tasks include:

1. **Data sourcing:** select a reliable provider for daily total returns of the
   chosen ETFs.  Ensure data covers delisting events and corporate actions.
2. **Broker interface:** confirm that the chosen broker supports MOC and LOC
   order types for the selected ETFs.  Interactive Brokers and most major
   brokers support these order types; however, the precise cut‑offs are
   determined by the exchange【604093045262205†L93-L110】.
3. **Monitoring and auditability:** maintain logs of decisions, orders and
   reconciliations.  Adhere to the security guidelines in `SECURITY.md` to
   protect credentials and ensure tamper evidence.
4. **Governance:** record all material decisions in an ADR; update the
   Validation Matrix and Traceability Index after every change.

## 3 Next Steps

* Finalise the **Configuration Schema** (see
  `docs/config/CONFIG_SCHEMA_CONCEPTUAL_v2.1.md`) to document all tunable
  parameters and strategy versions.
* Populate the **Validation Matrix** and **Traceability Index** with findings
  from the research summarised above.
* Define the **Acceptance Criteria** and **Runbook** to transition from
  planning to implementation.
* Continue research on broker‑specific order type support, margin
  requirements, and tax nuances.  Document any open questions in
  `docs/validation/OPEN_QUESTIONS_v2.1.md`.
