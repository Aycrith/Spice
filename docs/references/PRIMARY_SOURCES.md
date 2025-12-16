# Primary Sources and Authoritative References

This file centralizes the primary/authoritative sources that underpin operational constraints and research-methodology requirements.

## Exchange auctions and cutoff rules

### NYSE
- **NYSE Closing Process (fact sheet, PDF)** — Market-on-Close (MOC) and Limit-on-Close (LOC) entry/cancel constraints and key times.
  - Source: https://www.nyse.com/publicdocs/nyse/NYSE_Auctions_Closing_Process_Fact_Sheet.pdf
- **NYSE Opening and Closing Auctions (fact sheet, PDF)** — Updated ruleset summary for auctions.
  - Source: https://www.nyse.com/publicdocs/nyse/markets/nyse/NYSE_Opening_and_Closing_Auctions_Fact_Sheet.pdf

### Nasdaq
- **The Nasdaq Opening and Closing Crosses (quick guide, PDF)** — Key cutoffs for MOO/MOC and LOO/LOC.
  - Source: https://www.nasdaqtrader.com/content/technicalsupport/specifications/TradingProducts/openclosequickguide.pdf
- **Nasdaq crosses FAQs (PDF)** — Detailed Q&A on cutoffs and behavior.
  - Source: https://nasdaqtrader.com/content/productsservices/trading/crosses/openclose_faqs.pdf

## Broker documentation (order types and constraints)

### Interactive Brokers (IBKR)
- **Order Types and Algos (landing page)** — catalog of broker-supported order types.
  - Source: https://www.interactivebrokers.com/en/trading/ordertypes.php
- **IBKR API Order Types** — API-facing documentation for order types and minimal required fields.
  - Source: https://www.interactivebrokers.com/campus/ibkr-api-page/order-types/

## Settlement (U.S. T+1)

### U.S. Securities and Exchange Commission (SEC)
- **Investor.gov bulletin: New T+1 settlement cycle** — compliance date and investor-facing impact.
  - Source: https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/new-t1-settlement-cycle-what-investors-need-know-investor-bulletin
- **SEC FAQ: Shortening the Securities Transaction Settlement Cycle** — regulatory FAQ on the change.
  - Source: https://www.sec.gov/exams/educationhelpguidesfaqs/t1-faq

## Tax (wash sales)

### Internal Revenue Service (IRS)
- **IRS Publication 550 (PDF)** — wash sale rules ("substantially identical", 30-day window) and related tax mechanics.
  - Source: https://www.irs.gov/pub/irs-pdf/p550.pdf

## Research integrity and methodology

### Backtest overfitting controls (CSCV / PBO)
- **Bailey et al., "The Probability of Backtest Overfitting" (PDF)** — foundational paper for PBO/CSCV framing.
  - Source: https://www.davidhbailey.com/dhbpapers/backtest-prob.pdf

### Momentum crash regimes
- **Daniel & Moskowitz, "Momentum Crashes" (NBER PDF)** — documented crash regimes and partial forecastability characteristics.
  - Source: https://www.nber.org/system/files/working_papers/w20439/w20439.pdf

### Anti-lookahead / time-frontier modeling (reference model)
- **QuantConnect: Understanding Time** — illustrates bar availability vs timestamps and the risk of lookahead from daily bars.
  - Source: https://www.quantconnect.com/docs/v1/key-concepts/understanding-time
- **QuantConnect: Time Modeling (Periods / Time Frontier / TimeSlices)** — explicit guidance on avoiding lookahead bias.
  - Sources:
    - https://www.quantconnect.com/docs/v2/writing-algorithms/key-concepts/time-modeling/periods
    - https://www.quantconnect.com/docs/v2/writing-algorithms/key-concepts/time-modeling/timeslices

## Notes

- Treat these sources as the starting point for binding operational assumptions.
- Any contradictory source discovered later must be recorded in the Open Questions log and resolved via an ADR.
