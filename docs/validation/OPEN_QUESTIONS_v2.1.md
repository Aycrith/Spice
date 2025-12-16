# OPEN_QUESTIONS v2.1

**Last updated:** 2025-12-15

| Priority | Question | Why it matters | Options | How to answer (research/test) | Decision lock impact |
|---|---|---|---|---|---|
| P0 | Which broker/account type (cash vs margin) will be used? | Determines settlement feasibility and order policies | **POC path:** SimBroker (no external broker). **Stage 2+ path:** IBKR/other; cash/margin | Broker docs + paper tests; verify T+1 behaviors. For POC: define SimBroker contract + deterministic simulation rules | Broker/account change may affect constraints (Stage 2+). SimBroker does not lock broker selection |
| P0 | What data provider supplies adjusted prices and what are timestamp semantics? | Lookahead risk + data reliability | **POC path:** free/legal EOD sources + multi-source QA. **Stage 2+ path:** paid EOD vs broker-provided vs hybrid | Provider docs + availability tests. Stage 0 availability suite + corporate-action QA | Provider change may force re-validation |
| P0 | Venue + broker cutoffs for chosen order types? | Prevent cutoff misses/rejects | Open-auction vs fallback | Broker+exchange verification; paper tests | Timing/order policy changes may be gated |
| P0 | Exact ETF universe and min history? | Inception bias + robustness | Fixed small list vs expanding | Document inception dates; inception-aware backtests | Universe change = Strategy Change |
| P1 | Default defensive asset and stress fallback behavior? | Tail behavior clarity | Cash-like ETF; hold prior; HALT | Stress tests including crash scenarios | Defensive logic change = Strategy Change |
| P1 | PBO threshold and search scope? | Prevent false positives | Conservative vs permissive | Pilot CSCV/PBO runs | Research gate policy |
| P1 | Account context (taxable vs IRA) and wash-sale posture? | Reporting and net returns | IRA vs taxable with flags | Decide account context; define minimum reporting | Affects ops requirements |
| P2 | Conformance drift thresholds? | Live readiness | Tight vs moderate | Empirically set from paper phase | Governance tuning |

## Notes

- Sponsor constraint (2025-12-16): proof-of-concept should avoid paid services and avoid injecting funds. This supports a strong “Decision Portfolio Demo” but may not satisfy Stage 2 conformance requirements as currently written.
- See `docs/package/appendix/OPEN_QUESTIONS_SOLUTIONS.md` for an actionable, stage-consistent resolution playbook.
