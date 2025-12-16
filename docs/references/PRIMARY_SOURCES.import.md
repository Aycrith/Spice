# Primary Sources

This list catalogues authoritative references used to build and validate the
plan.  Each entry includes a brief description and citation lines (as
recorded in this repository’s context).  When citing a source in the plan,
link back to the corresponding entry here to avoid duplicating long
descriptions in the main documents.

## Exchange & execution rules

| ID | Source | Description | Key lines |
| --- | --- | --- | --- |
| PS1 | NYSE – Behind the Scenes – An Insider’s Guide to the NYSE Closing Auction | Explains the closing auction timeline: MOC/LOC orders can be modified or cancelled until **3:50 PM**; closing D orders can be modified until **3:59:50 PM**; trading ends at **4:00 PM**【604093045262205†L93-L110】. | 93–110 |
| PS2 | NYSE – Closing Process Fact Sheet (PDF) | Summarises the rules for MOC/LOC orders: can be entered until **3:50 PM**; after 3:50 they may only be entered on the contra‑side of an imbalance and cancellations allowed only for legitimate errors; no cancellations after **3:58 PM**【826894920304809†L0-L53】. | 0–53 |

## Settlement & regulation

| ID | Source | Description | Key lines |
| --- | --- | --- | --- |
| PS3 | FINRA – Shortening the Settlement Cycle to T+1 | FINRA explains that as of **28 May 2024** the standard settlement cycle for stocks, corporate bonds, ETFs and mutual funds has changed from T+2 to T+1; payment and delivery must occur on the next business day【634620779460672†L263-L320】. | 263–320 |
| PS4 | SEC Investor Bulletin – T+1 Standard Settlement Cycle | Defines settlement and notes that the SEC’s final rules shorten the settlement cycle to **T+1** effective **28 May 2024**; investors must deliver securities or payment one business day after the trade【228845885160452†L154-L200】. | 154–200 |

## Tax

| ID | Source | Description | Key lines |
| --- | --- | --- | --- |
| PS5 | Investor.gov – Glossary of Terms: Wash Sale | Defines a wash sale as selling a security at a loss and purchasing the same or a substantially identical security within 30 days before or after; the IRS prohibits deducting the loss【774704392547939†L223-L239】. | 223–239 |
| PS6 | Charles Schwab – What Is the Wash-Sale Rule? | Explains that buying a substantially identical asset within 30 days before or after a loss sale triggers the wash‑sale rule; the disallowed loss is added to the cost basis of the new shares; the rule applies to stocks, bonds, options, ETFs and mutual funds【238476208366191†L190-L218】. | 190–218 |

## Model validation & methodology

| ID | Source | Description | Key lines |
| --- | --- | --- | --- |
| PS7 | “The Probability of Backtest Overfitting” (Bailey et al., 2015) | Introduces combinatorially symmetric cross‑validation (CSCV) and the probability of backtest overfitting (PBO).  Algorithm partitions the performance matrix into equal subperiods and forms combinations of training and testing sets【639029512866022†L454-L557】; PBO is the fraction of logits that are positive【639029512866022†L590-L618】. | 454–557; 590–618 |

## Momentum crash research

| ID | Source | Description | Key lines |
| --- | --- | --- | --- |
| PS8 | “Momentum Crashes” (Daniel & Moskowitz, 2016) | Documents that momentum strategies exhibit high average returns but suffer occasional crashes during “panic” states when markets rebound; crashes are associated with time‑varying beta exposures【535019668254404†L50-L66】【535019668254404†L92-L190】. | 50–66; 92–190 |

## Security

| ID | Source | Description | Key lines |
| --- | --- | --- | --- |
| PS9 | Repository `SECURITY.md` (this project) | Emphasises storing secrets locally, never committing them to the repository, ensuring auditability and incident response alignment with NIST【813758299569681†L4-L22】. | 4–22 |

## Notes

* When citing a source in the plan or validation documents, reference the **ID**
  listed here (e.g., “PS3”) and include the relevant lines from the citation
  using the tether ID format.  Avoid quoting long passages directly in the
  plan; instead, summarise the key point and link to this list.
