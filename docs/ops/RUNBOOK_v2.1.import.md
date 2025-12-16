# Runbook v2.1 – Monthly Rebalance Operations

This runbook describes the operational steps for executing the monthly
rebalance of the cross‑asset momentum rotation strategy.  It assumes
implementation code exists to compute rankings and interface with the broker.
Times are given in **Eastern Time (ET)**.  Adjust for the user’s local time
(America/New_York) as necessary.

## 1 Schedule overview

| Time | Task | Notes |
| --- | --- | --- |
| **−2 business days** | Initiate cash transfer into brokerage account. | Funds must clear by trade date to meet T+1 settlement obligations【634620779460672†L263-L320】. |
| **09:30 AM – rebalance day** | Collect latest price data. | Verify completeness and accuracy. |
| **10:00 AM** | Generate ranking using 12‑1 momentum. | Use data up to the previous day’s close.  Record results in a log. |
| **2:30 PM** | Finalise orders for top two ETFs. | Confirm position sizes respect risk policy. |
| **3:30 PM** | Begin preparing order entry. | Log into broker platform; verify account balances and positions. |
| **3:45 PM** | Enter MOC or LOC orders. | Ensure orders are complete and correct; price limits (if any) must reflect current market. |
| **3:50 PM** | **Order entry cut‑off for MOC/LOC**【604093045262205†L93-L110】【826894920304809†L0-L53】. | After this time, MOC/LOC orders can only be entered to offset an imbalance; modification/cancellation is restricted. |
| **3:58 PM** | Cancellation cut‑off for MOC/LOC orders【826894920304809†L0-L53】. | Do not attempt to cancel orders unless a legitimate error is discovered. |
| **3:59:50 PM** | Cut‑off for closing D order entry/modification【604093045262205†L93-L110】. | Applies if LOC orders have price limits. |
| **4:00 PM** | Market close; auction completes【604093045262205†L93-L110】. | Confirm order executions; download execution report. |
| **After 4:00 PM** | Reconcile executions and update portfolio records. | Compare executed shares and prices to expectations; log any deviations. |
| **T+1** | Settlement and funding confirmation【634620779460672†L263-L320】. | Verify cash debit/credit; ensure new positions appear in account. |

## 2 Detailed procedures

### 2.1 Pre‑rebalance

1. **Funding:** two business days before the rebalance, initiate an ACH or wire
   transfer into the brokerage account.  Document the transfer and expected
   settlement date.  If selling positions in the current rebalance, note that
   proceeds will be available on T+1 for the following rebalance.
2. **Data checks:** on rebalance day, collect daily total return data for all
   ETFs in the universe.  Cross‑check against a secondary source to detect
   anomalies.  Save data to an immutable log.
3. **Ranking calculation:** compute 12‑1 momentum returns and rank assets.
   Record the ranking and any tie‑breakers.  If a tie occurs for the second
   position, choose the asset with lower volatility.
4. **Risk assessment:** evaluate the portfolio’s current drawdown and the
   30‑day realised volatility of the equity market.  If volatility exceeds the
   threshold specified in the config (default 30 %), scale positions down
   proportionally (e.g., reduce allocation from 50/50 to 30/30).

### 2.2 Order entry and execution

1. **Login and verification:** log into the broker platform at least 30 minutes
   before the cut‑off.  Verify cash balances and existing positions.  Review
   any pending orders or account alerts.
2. **Enter orders:** create MOC orders (or LOC orders with price limits)
   for the ETFs selected.  Use the quantity determined by the ranking and risk
   policy.  Double‑check symbol, quantity and order type.
3. **Submit orders:** send the orders **before 3:50 PM ET**.  The exchange
   rules stipulate that MOC/LOC orders entered after this time are only
   accepted if they offset an imbalance; modifications and cancellations are
   restricted【604093045262205†L93-L110】.  Document the exact submission time.
4. **Monitor orders:** watch for any broker messages or imbalance indications.
   Unless a legitimate error is found, do **not** cancel the order after
   3:58 PM【826894920304809†L0-L53】.
5. **Confirm execution:** after the 4:00 PM close, retrieve execution reports
   from the broker.  Verify that the filled quantity matches the order and
   record the closing price.

### 2.3 Post‑trade

1. **Reconciliation:** update the portfolio ledger with executed trades,
   including transaction costs and taxes.  Compare positions against the
   expected allocations.  Investigate any discrepancies immediately.
2. **Logging:** store execution confirmations, ranking results and notes in
   secure, immutable storage.  Avoid storing any secrets in the repository
   (see SECURITY.md【813758299569681†L4-L22】).
3. **Wash‑sale checks:** analyse whether any sold positions were repurchased
   within the 30‑day window.  If a wash‑sale is detected, adjust the cost
   basis accordingly and update the tax log【774704392547939†L223-L239】.
4. **Prepare for next cycle:** review any incidents or anomalies and record
   them in the open questions or ADRs.  Schedule funding for the next
   rebalance.

## 3 Exception handling

1. **System outage:** if the broker platform is unavailable, attempt to
   place orders via a backup channel (e.g., phone brokerage).  Document the
   outage and outcome.
2. **Data errors:** if a data error is discovered after the ranking but before
   order submission, pause the rebalance and investigate.  If the error
   materially changes the ranking, update the plan accordingly.
3. **High market volatility:** if intraday volatility spikes above the
   risk threshold, consider delaying order submission or reducing order size.
   Record the decision in an ADR.

## 4 Audit and continuous improvement

* After each rebalance, conduct a **post‑mortem** to evaluate the process.  Review
  timing adherence, slippage, funding adequacy, and any near misses.
* Document lessons learned and propose improvements via ADRs.  Update this
  runbook as necessary to reflect new knowledge or regulatory changes.
