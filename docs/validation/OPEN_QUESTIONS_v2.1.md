# OPEN_QUESTIONS v2.1

**Last updated:** 2025-12-15

| Priority | Question | Why it matters | Options | How to answer (research/test) | Decision lock impact |
|---|---|---|---|---|---|
| P0 | Which broker/account type (cash vs margin) will be used? | Determines settlement feasibility and order policies | IBKR/other; cash/margin | Broker docs + paper tests; verify T+1 behaviors | Broker/account change may affect constraints |
| P0 | What data provider supplies adjusted prices and what are timestamp semantics? | Lookahead risk + data reliability | Paid EOD vs free; multi-source | Provider docs + availability tests | Provider change may force re-validation |
| P0 | Venue + broker cutoffs for chosen order types? | Prevent cutoff misses/rejects | Open-auction vs fallback | Broker+exchange verification; paper tests | Timing/order policy changes may be gated |
| P0 | Exact ETF universe and min history? | Inception bias + robustness | Fixed small list vs expanding | Document inception dates; inception-aware backtests | Universe change = Strategy Change |
| P1 | Default defensive asset and stress fallback behavior? | Tail behavior clarity | Cash-like ETF; hold prior; HALT | Stress tests including crash scenarios | Defensive logic change = Strategy Change |
| P1 | PBO threshold and search scope? | Prevent false positives | Conservative vs permissive | Pilot CSCV/PBO runs | Research gate policy |
| P1 | Account context (taxable vs IRA) and wash-sale posture? | Reporting and net returns | IRA vs taxable with flags | Decide account context; define minimum reporting | Affects ops requirements |
| P2 | Conformance drift thresholds? | Live readiness | Tight vs moderate | Empirically set from paper phase | Governance tuning |
