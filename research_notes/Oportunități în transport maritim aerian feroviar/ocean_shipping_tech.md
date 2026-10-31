# Ocean Shipping Software and Technology Landscape (as of late October 2026)

*Method note for the report writer: these notes come from about 37 web searches run on 31 Oct 2026. Full-page fetches failed for every news domain tried (cyprusshippingnews, shipandbunker, hklaw, logisticsmgmt, sea-intelligence, freightwaves, iccwbo, zerocarbonshipping): those hosts are not on this session's network allow-list. The shared web-search budget then ran out before I could search bulk/tanker tech, vessel ops, cyber, connectivity or the startup funding databases. So every cited figure comes from search-result summaries, not from reading the full article, and figures should be spot-checked before publication. Where I added knowledge from my training data (to about mid-2026) that I could not re-check this session, it sits ONLY under "Gaps" and is labelled "UNVERIFIED background". Data from before 2024 is flagged [pre-2024].*

---

## 1. Ocean freight market context 2025-2026 and what it means for software demand

### Takeaway
2026 did not turn out as the overcapacity slump everyone forecast in late 2025. A US-Israel war with Iran began in late February 2026 and the Strait of Hormuz was largely closed for months. Together with continued Red Sea risk and Asian port congestion, this pushed spot container rates to a 2026 peak of about $4,500-4,650/FEU on the Drewry WCI in July-August (the highest since September 2024). Carriers like Maersk swung from a loss warning to $2-4bn EBIT guidance. The structural overhang is still there: a record orderbook of about 13-13.7m TEU (38-40%+ of the fleet), with 8.5m TEU due in 2027-28, plus a phased Suez return (63% of Asia-Europe capacity back by late October 2026, full return expected Q1 2027). Together these point to a sharp rate correction and overcapacity in 2027-28. Schedule reliability collapsed to 49.9% in August 2026. USTR Section 301 port fees on Chinese ships are suspended until 9 Nov 2026, with an extension to 9 Jan 2027 proposed. For software buyers, this mix of volatility, regulatory churn and an expected margin squeeze rewards tools that cut cost or that price and route risk in real time.

### Cited Findings
**Rates and carrier profits**
- Drewry WCI for 22 Oct 2026 rose for a second straight week to its highest level in 15 weeks. The search snippet did not include the dollar figure — [Cyprus Shipping News, 26 Oct 2026](https://cyprusshippingnews.com/2026-10-26/drewry-world-container-index-22-oct/)
- WCI composite on 8 Jan 2026 was $2,557/FEU — [Cyprus Shipping News](https://cyprusshippingnews.com/2026/01/14/world-container-index-by-drewry/)
- In July 2026 the WCI hit about $4,639/FEU (+2% w/w), its highest since September 2024, after a run of about 10 straight weekly gains. A later reading slipped 2% to $4,547 (first decline after 10 weeks of increases). The two summaries conflict on sequence — [ShipUniverse "WCI hits another 2026 high"](https://www.shipuniverse.com/?p=16195); [ShipUniverse "rally cools"](https://www.shipuniverse.com/news/container-rate-rally-cools-as-drewry-wci-slips-from-peak-season-high/)
- A search summary of Drewry reposts puts the composite at $4,526/FEU (+4%) on 20 Aug 2026. I did not verify which repost carries this figure — [Hellenic Shipping News WCI reposts](https://www.hellenicshippingnews.com/?p=1144957)
- An undated Container News item: "WCI holds steady at $2,287 as carriers push for bunker surcharges", consistent with the fuel-cost spike in early 2026 — [Container News](https://container-news.com/wci-holds-steady-at-2287-as-carriers-push-for-bunker-surcharges/embed/)
- On 29 Jun 2026 Maersk raised 2026 underlying EBIT guidance to $2-4bn, from -$1.5bn to +$1bn, citing strong Far East demand and rising spot rates. It lifted its global container demand growth view to about 4% (was 2-4%) — [Fruitnet](https://www.fruitnet.com/eurofruit/maersk-upgrades-guidance-for-full-year-2026/271982.article); [WorldPorts "loss warning to USD 4bn profit outlook"](https://www.worldports.org/?p=762939)
- Maersk raised guidance a second time on 13 Aug 2026 — [AJOT](https://www.ajot.com/news/maersk-raises-outlook-again-as-strong-demand-freight-rates-lift-profit)
- Hapag-Lloyd raised its 2026 forecast on 13 Jul 2026, citing strong demand and spot rates. Full-year EBITDA guidance is reported at 2.7-3.7bn — [trans.info](https://trans.info/en/hapag-lloyd-profit-upgrade-490231)
- Q2 2026 EBITDA margins in liner shipping: CMA CGM 22.7%, Maersk 19.4%, Hapag-Lloyd 13.6% — [trans.info (DE)](https://trans.info/de/37-3-milliarden-us-dollar-im-containerverkehr-doch-die-margen-klaffen-auseinander-496473)
- Contrast with the late-2025 consensus: Xeneta said the US-China trade truce "will not revive weakening ocean container shipping market with freight rates still expected to fall in 2026" and warned of massive oversupply — [Xeneta](https://www.xeneta.com/news/us-china-trade-truce-will-not-revive-weakening-ocean-container-shipping-market-with-freight-rates-still-expected-to-fall-in-2026)
- The Red Sea return is putting 2026/27 contract rates under pressure — [Global Maritime Hub](https://globalmaritimehub.com/?p=17825)

**Iran war / Strait of Hormuz (main 2026 shock, mostly tanker/energy)**
- Before the war about 138 vessels a day transited Hormuz. In March 2026 daily transits in either direction did not exceed five ships. Source is an advocacy group (UANI) tracking shipping — [UANI Iran War Shipping Update, 31 Mar 2026](https://www.unitedagainstnucleariran.com/analysis/iran-war-shipping-update-march-31-2026)
- After a mid-April ceasefire Iran unblocked the Strait, then on 18 April said it was blocking it again because of the US naval blockade — [Free Malaysia Today, 18 Apr 2026](https://www.freemalaysiatoday.com/category/world/2026/04/18/convoy-of-tankers-seen-crossing-strait-of-hormuz); [UANI, 9 Apr 2026](https://www.unitedagainstnucleariran.com/analysis/iran-war-shipping-update-april-9-2026)
- Tankers began leaving Hormuz after being blocked for nearly three months (Reuters) — [Babel/Reuters](https://babel.ua/en/news/127244-reuters-tankers-begin-to-leave-strait-of-hormuz-after-being-blocked-for-nearly-three-months)
- In July 2026 the southern route stayed open despite Iran declaring the waterway closed — [gCaptain](https://gcaptain.com/hormuz-route-open-despite-iran-declaration-maritime-group-says/)
- In September 2026 the IRGC claimed two tankers "hit mines" in Hormuz; this was not independently verified — [Intellinews](https://www.intellinews.com/iran-s-irgc-says-two-tankers-hit-mines-in-strait-of-hormuz-465241/)
- Iran said it had blacklisted 45 tankers that broke its Hormuz crossing rules, threatening fines and confiscation — [Financial Express (BD)](https://thefinancialexpress.com.bd/world/iran-threatens-45-tankers-with-fines-confiscation-in-hormuz-escalation)
- Hormuz traffic "remains minimal" (Argus) — [Argus](https://www.argusmedia.com/pt/news-and-insights/latest-market-news/2799728-traffic-through-hormuz-remains-minimal)

**Red Sea / Suez status**
- Alphaliner (late Oct 2026): container lines have shifted 63% of Far East-Europe capacity back to the Suez route — [Ship & Bunker](https://shipandbunker.com/news/emea/932812-container-lines-shift-63-of-far-east-europe-capacity-back-to-suez-canal-alphaliner)
- Kuehne+Nagel's CEO expects most lines back on Suez by late Q1 or early Q2 2027. Linerlytica expects a full return by Q1 2027 — [Seatrade Maritime](https://www.seatrade-maritime.com/containers/full-suez-return-for-container-carriers-expected-by-q1-2027); [Baird Maritime](https://www.bairdmaritime.com/shipping/boxships/suez-canal-return-likely-by-early-2027-for-container-lines)
- BIMCO: boxship transits via the Red Sea/Suez are above 50% of the reference ("pre-Iran war") level. The Suez Canal Authority reported container ship net tonnage up 54.2% y/y in Jan-Aug 2026. COSCO's OOCL Portugal made a southbound transit in September 2026, the carrier's first since the crisis began — [gCaptain "gradual return hits key milestone"](https://gcaptain.com/the-gradual-return-of-ships-to-the-red-sea-hits-a-key-milestone/) (summary-level; exact attribution among the Suez articles not verified)
- Return plans were set back by the US-Israeli strikes on Iran in late February 2026. Houthi forces made gains along Yemen's coast near Bab el-Mandeb — [gCaptain](https://gcaptain.com/container-shipping-returns-to-suez-despite-rising-red-sea-risks/)

**Orderbook / overcapacity**
- Linerlytica: orderbook at a record 13m TEU, orderbook-to-fleet ratio 38.3%, the highest since the GFC — [WorldPorts](https://www.worldports.org/record-breaking-global-container-ship-order-book-surpasses-13-million-teu/)
- Another tally: 1,712 vessels, 13.7m TEU, more than 40% of the fleet. Alphaliner expects about 1,000 newbuilds totalling 8.5m TEU in 2027-28, "more than four times" the usual delivery volume for such a period. There is a shortage of demolition yard capacity (mostly India, Pakistan and Bangladesh). Maritime Strategies International expects overcapacity to be "a reality by 2028" — [Kuehne+Nagel news](https://mykn.kuehne-nagel.com/news/article/containership-orders-hit-record-high-despite); [Master Mariners AU](https://mastermariners.org.au/news-international/6910-containership-orders-hit-record-high-despite-looming-overcapacity-fears)
- Transport Intelligence: new orders in Jan-Apr 2026 exceeded 1.9m TEU. Linerlytica suggested 2026 orders could beat the 5.1m TEU annual record — [Logistics Management "Top 30 Ocean Carriers 2026"](https://www.logisticsmgmt.com/article/top_30_ocean_carriers_2026_walking_a_capacity_tightrope) (summary-level)

**Schedule reliability and the alliance reshuffle**
- Sea-Intelligence global schedule reliability: Jan 2026 62.4%, Feb 59.0%, June 62.6%, Aug 49.9%. August was the lowest since September 2022, down 5.9 points m/m, with Asian port congestion cited — [Sea-Intelligence Jan](https://www.sea-intelligence.com/press-room/373-2026-starts-with-global-schedule-reliability-of-62-4); [Feb](https://sea-intelligence.com/press-room/379-february-2026-global-schedule-reliability-falls-to-59-0); [June](https://sea-intelligence.com/press-room/400-global-schedule-reliability-drops-to-62-6-in-june-2026); [FreshPlaza, Aug](https://www.freshplaza.com/article/9878292/global-container-shipping-schedule-reliability-falls-to-lowest-level-since-2022/)
- Alliance reliability for Jul/Aug 2026: Gemini 77.8%, MSC (standalone) 70.1%, Ocean Alliance 48.3%, Premier Alliance 43.2% — [FreshPlaza](https://www.freshplaza.com/article/9878292/global-container-shipping-schedule-reliability-falls-to-lowest-level-since-2022/)
- Gemini peaked at 93.4% in May/Jun 2026 (MSC 80.7%). Apr/May was 89.5% (all arrivals) and 91.4% (trade arrivals); Feb/Mar was 76.8% — [Container News](https://container-news.com/sea%e2%80%91intelligence-global-schedule-reliability-drops-to-62-6-in-june-2026/); [Container News May](https://container-news.com/sea-intelligence-global-schedule-reliability-for-may-2026-the-highest-of-the-year/); [Sea-Intelligence Mar](https://sea-intelligence.com/press-room/384-march-2026-global-schedule-reliability-joint-highest-for-the-year)

**USTR Section 301 port fees / tariffs**
- The one-year suspension of the Section 301 maritime actions (port fees on Chinese-built and Chinese-operated ships, plus related items) expires at 11:59 pm ET on 9 Nov 2026. In late October USTR proposed extending it to 9 Jan 2027 (docket USTR-2026-0694, comments due 30 Oct 2026). One source says the proposal was not yet final — [Holland & Knight, 26 Oct 2026](https://www.hklaw.com/en/insights/publications/2026/10/ustr-proposes-2-month-extension-of-suspension-of-section-301); [gCaptain](https://gcaptain.com/ustr-proposes-extending-china-ship-port-fee-suspension-through-january-2027/); [ustariffrates](https://ustariffrates.com/news/section-301-double-deadline-november-9-port-fees-exclusions)
- **Conflict:** Seatrade's headline says the US has "formalised" the two-month suspension. Seatrade also reports that the suspension freezes a 100% duty on Chinese-made ship-to-shore cranes and port-infrastructure penalties — [Seatrade Maritime](https://seatrade-maritime.com/regulations/us-formalises-two-month-suspension-of-chinese-vessel-fees)
- The original suspension came as part of a US-China one-year truce. China's retaliatory port charges are governed separately — [Seatrade "one-year truce"](https://www.seatrade-maritime.com/ports-logistics/ustr-and-china-port-charges-one-year-truce); [Tradlinx](https://blogs.tradlinx.com/what-returns-on-november-10-when-the-china-ship-fee-suspension-expires/)
- Tariff-era volumes: OOCL transpacific liftings were 608,979 TEU in Q2 2026 (+21.5% y/y) and about +7.1% for H1. OOCL said tariffs were "more stable in 2026, so far" — [Seatrade Maritime](https://www.seatrade-maritime.com/containers/oocl-transpacific-volumes-rebound-in-second-quarter)
- [Likely 2025] After the tariffs, US container imports fell 13% y/y — [The Loadstar](https://theloadstar.com/post-tariff-us-container-imports-down-13-year-on-year/)

### Inferences
- **Demand driver 1: volatility.** Reliability swung from 62% to 50% within two months, and rates nearly doubled between January and July 2026. Shippers and forwarders need predictive ETAs, dynamic re-routing and fast rate re-benchmarking. Gemini's 77-93% versus Premier's 43% makes carrier choice (and the data to support it) a real procurement lever.
- **Demand driver 2: the coming margin squeeze.** Most analysts expect 2027-28 overcapacity, so carriers and forwarders will cut costs. That historically favours automation (document processing, back-office AI, procurement tools) over growth-oriented visibility spending. The 2023 downturn (Flexport layoffs etc.) is the precedent.
- **Demand driver 3: geopolitical routing risk.** Hormuz, Red Sea, Section 301 fees that depend on vessel build and ownership, and Iran's tanker blacklist all create a market for vessel-level risk scoring: which ship, built where, owned by whom, which route, what fees, what surcharges.
- Section 301 fee logic, if reinstated, needs per-vessel provenance data (build yard, operator nationality, fleet composition) at booking time. That is a data-engineering problem a small team can productise, but demand depends on whether the suspension lapses.

### Gaps
- No confirmed WCI dollar figure for late October 2026, and no Q3 2026 carrier results.
- No 2026 Alphaliner figure for fleet size or carrier market shares.
- The final status of the USTR extension (formalised or only proposed) conflicts between sources.
- The current state of Hormuz as of late October 2026 is not confirmed.
- UNVERIFIED background (training data, not checked this session):
  - The alliance structure since 1 Feb 2025: Gemini Cooperation (Maersk + Hapag-Lloyd, hub-and-spoke, >90% reliability target), Premier Alliance (ONE, HMM, Yang Ming, after Hapag left THE Alliance), Ocean Alliance (CMA CGM, COSCO/OOCL, Evergreen, extended to 2032), MSC standalone after 2M ended in January 2025. The cited Sea-Intelligence groupings are consistent with this.
  - USTR fee schedule (announced 17 Apr 2025, effective 14 Oct 2025): about $50/net ton for Chinese-owned/operated ships, rising annually to about $140 by 2028; for Chinese-built ships the higher of about $18/net ton or $120 per discharged container, rising by 2028; about $46/net ton for foreign-built car carriers; a cap of 5 charges per vessel per year. China retaliated with special fees on US-linked ships. Both were suspended from 10 Nov 2025 after the Trump-Xi meeting of 30 Oct 2025. Verify the figures against the Federal Register.
  - The status of the US IEEPA tariff litigation and any refund process is not verified. It matters for customs/tariff software demand.

---

## 2. Container shipping software: booking, digital forwarders, visibility, rate benchmarking, D&D, IoT

### Takeaway
The container software stack is consolidating around a few large aggregators:
- **WiseTech** (CargoWise) bought e2open, and with it the INTTRA booking network, in a deal announced in 2025 at $2.1bn equity / $3.25bn reported elsewhere.
- **Kpler** rolled up AIS and vessel data (MarineTraffic, FleetMon, Spire Maritime).
- **Visibility unicorns** project44 and FourKites are mature.
- **Freightos** is a small public marketplace: revenue of $7.7m a quarter despite $422m in gross booking value.

The digital forwarders that raised heavily in 2020-22 (Flexport, Forto, Zencargo, Beacon) show no 2025-26 funding events in the searches, so the "digital forwarder" model looks capital-constrained. The FMC detention and demurrage (D&D) billing rule, in force since May 2024 and partly vacated by the DC Circuit in September 2025, creates a compliance and dispute-automation niche.

### Cited Findings
**Booking platforms / network consolidation**
- WiseTech Global agreed to acquire e2open (owner of INTTRA) for about US$2.1bn, announced May 2025. Another outlet reports $3.25bn, likely including debt. Completion was expected subject to approvals — [STAT Times](https://www.stattimes.com/technology/wisetech-global-to-acquire-e2open-in-21-billion-deal-1355390); [SupplyChain247](https://www.supplychain247.com/article/wisetech-acquires-e2open-325-billion-supply-chain-deal/envista); [ASX announcement 26 May 2025](https://announcements.asx.com.au/asxpdf/20250526/pdf/06k2vxtpvjv24c.pdf)
- The Loadstar: the $2.1bn e2open purchase "will catapult WiseTech into a different dimension" — [The Loadstar](https://theloadstar.com/2-1bn-e2open-purchase-will-catapult-wisetech-into-a-different-dimension/)
- [pre-2024, 2018] When e2open bought INTTRA, about 1 in 4 ocean containers worldwide was booked through INTTRA, with more than 850,000 container orders initiated weekly — [Maritime Executive](https://maritime-executive.com/article/e2open-acquires-inttra-the-top-ocean-freight-platform)

**Digital freight forwarders / marketplaces**
- Freightos Q2 2026: 458k transactions (+15% y/y; growth was hit by Middle East disruption, but excluding Middle East routes it was in the 20-30% long-term model). Gross booking value was a record $422m (+33%), revenue $7.7m (+3%, a record), and cash $21m. WebCargo (the airline e-booking portal) drove growth; SaaS was below expectations — [PR Newswire Q2 2026](https://www.prnewswire.com/il/news-releases/freightos-reports-second-quarter-2026-results-302852762.html); [Container News](https://container-news.com/freightos-reports-increased-revenue-in-second-quarter-2026/)
- Freightos Q1 2026: 425k transactions (+15%, below its 446-451k guidance), GBV $343m (+24%), revenue $7.2m. FY2026 guidance was 1.81-1.84m transactions and $1.51-1.53bn GBV — [PR Newswire Q1 2026](https://www.prnewswire.com/il/news-releases/freightos-reports-first-quarter-2026-results-302781623.html)
- Freightos Q4 2025: a record 445k transactions (+27% y/y) — [Digital Commerce 360](https://www.digitalcommerce360.com/2026/02/23/freightos-revenue-transaction-volume-q4-2025/amp/)
- Flexport: last priced valuation $8bn (Feb 2022); latest round a $260m uncapped convertible note from Shopify (total raised about $2.7bn); 2024 revenue $2.1bn. It was named to TIME100 Most Influential Companies 2026 for tariff-related supply-chain tools, has been expanding fulfilment to Canada and the UK, and acquired Shopify Logistics — [StockAnalysis (Flexport profile, Sep 2026)](https://stockanalysis.com/private/flexport/)
- [pre-2024] Flexport cut about 20% of global headcount in October 2023 after an earlier round of cuts — [TechCrunch](https://techcrunch.com/?p=1941956); [FreightWaves](https://www.freightwaves.com/news/flexport-plans-to-lay-off-20-of-workforce-say-insiders); [trans.info](https://trans.info/en/report-flexport-plans-to-cut-another-20-of-workforce-amid-funding-woes-377733)
- [pre-2024] Forto's last disclosed round was a $250m Series D-II in March 2022; total raised about $616m — [Caplight](https://www.caplight.com/company/forto)
- [pre-2024] Zencargo raised $42m in May 2021 — [TechCrunch](https://techcrunch.com/2021/05/10/zencargo-raises-42m-to-expand-its-digital-first-freight-forwarding-platform-internationally/embed/)
- [pre-2024] Beacon (London) raised a $15m Series A (Bezos, 8VC) in 2020 and a $50.3m Series B in October 2021 (total about $70m) — [CB Insights](https://www.cbinsights.com/company/beacon-2/financials)

**Visibility / maritime data**
- [pre-2024] project44 raised $420m at a $2.2bn valuation (Goldman, TPG), acquired Ocean Insights (2021) for ocean tracking, and later ClearMetal — [STAT Times](https://www.stattimes.com/amp/supply-chain/project44-raises-420mn-from-goldman-tpg-valued-at-22bn-1307440); [MMH](https://www.mmh.com/article/project44_announces_acquisition_of_ocean_insights)
- Transport Intelligence: project44 "moves a step closer to IPO" (undated) — [Ti Insight](https://ti-insight.com/briefs/project44-redefines-visibility-and-moves-a-step-closer-to-ipo/)
- Kpler acquired MarineTraffic and FleetMon (2023). It agreed to buy Spire Maritime (satellite AIS) for $241m on 13 Nov 2024. After a lawsuit by Spire Global, the deal closed on 25 Apr 2025. The UK CMA continued investigating, and Spire's AIS customers (some of them Kpler competitors) raised antitrust concerns about losing data access — [Maritime Executive](https://maritime-executive.com/article/kpler-closes-spire-maritime-acquisition-as-uk-proceeds-with-investigation); [Baird Maritime](https://www.bairdmaritime.com/amp/story/shipping/spires-ship-tracking-customers-raise-antitrust-concerns-over-potential-sale-to-kpler); [WorldPorts](https://www.worldports.org/kpler-completes-acquisition-of-spire-maritime)

**Detention & demurrage (US FMC)**
- The FMC's final D&D billing rule (46 CFR Part 541) was issued on 23 Feb 2024 and took effect on 28 May 2024. Main provisions:
  - Carriers and marine terminal operators (MTOs) must invoice within 30 days of the last day charges accrue.
  - Required information fields are mandatory; a missing field eliminates the billed party's obligation to pay.
  - The bill may go to the contracting party or the consignee, but not to several parties at once.
  - The rule does not set D&D rates.
  - [FreightWaves](https://www.freightwaves.com/news/fmc-tightens-rules-on-charging-container-late-fees); [Maritime Executive](https://maritime-executive.com/article/fmc-publishes-new-rules-on-detention-and-demurrage-charges); [Gnosis Freight](https://www.gnosisfreight.com/post/fmc-ruling-on-demurrage-and-detention-requirements)
- On 23 Sep 2025 the DC Circuit vacated a key provision, the "properly issued invoices" section that limited whom carriers could bill (relevant to truckers). The FMC then removed that section from the CFR — [Husch Blackwell](https://www.huschblackwell.com/newsandinsights/appeals-court-decision-reshapes-detention-and-demurrage-billing-landscape-for-truckers); [AJOT](https://www.ajot.com/news/u.s-court-of-appeals-issues-decision-in-case-on-detention-and-demurrage-billing-practices); [Federal Register 2025-23920](https://public-inspection.federalregister.gov/2025-23920.pdf)
- A June 2026 item reports "new FMC rules on detention and demurrage come into force". It is unclear whether this is new 2026 rulemaking or a recap of the 2024 rule — [India Seatrade News](https://indiaseatradenews.com/new-fmc-rules-on-detention-and-demurrage-come-into-force/)

### Inferences
- **Booking/network layer: effectively locked.** WiseTech now combines CargoWise (forwarder ERP) with INTTRA (carrier booking/SI network). A new entrant should integrate with it, not compete.
- **AIS/vessel-position data: commoditised at the bottom, concentrated at the top.** Kpler controls MarineTraffic, FleetMon and Spire's satellite AIS. Startups that depend on Spire AIS face supplier risk, the issue the CMA probe highlighted. Building on AIS is fine; differentiation must come from models such as ETA, port congestion, risk scoring and emissions, or from proprietary document data.
- **Freightos economics show the take-rate problem in freight marketplaces.** $422m GBV produced $7.7m revenue, about 1.8%. A pure booking marketplace is a hard business for a small team.
- **The D&D rule creates a measurable, rules-based opportunity.** Invoices missing mandatory fields are legally unenforceable, and there is a 30-day invoicing window. Automated invoice auditing (parse invoice → check against 46 CFR 541 fields → match to container milestones → auto-dispute) has quantifiable ROI for US importers, BCOs and NVOCCs.

### Gaps
- No 2025-26 data found on project44, FourKites, Vizion, Portcast, GoComet, Terminal49, Shipsgo, Searates, Container xChange, Raft, Expedock, Magaya, Descartes or CargoWise pricing.
- No data on Xeneta's 2026 funding or product, or on FBX-based derivatives.
- No current status found for Forto, Zencargo or Beacon (possible down-rounds, pivots or acquisitions).
- Whether the WiseTech-e2open deal has closed is not confirmed in the results.
- No data on container IoT penetration.
- UNVERIFIED background:
  - Hapag-Lloyd fitted its dry-container fleet with Nexxiot real-time trackers (the "Hapag-Lloyd LIVE" programme, about 2021-2024).
  - Traxens is backed by CMA CGM and MSC; Maersk runs Remote Container Management for reefers.
  - WiseTech: a governance crisis around founder Richard White (2024-25) and a 2025 change to the CargoWise commercial model that angered some forwarders. Both point to openings for "CargoWise-alternative" forwarder software, especially in the mid-market and LatAm.
  - Freightos listed via SPAC on Nasdaq (ticker CRGO) in January 2023.
  - Flexport timeline: Dave Clark was CEO from September 2022 to September 2023, when Ryan Petersen returned; Flexport bought Shopify Logistics/Deliverr (2023) and Convoy's technology assets (October 2023).

---

## 3. Electronic Bill of Lading (eBL): standards, adoption, legal status, blockers

### Takeaway
eBL adoption is rising but still small by volume: about 1% of BLs in 2021, about 5-6% in early 2025, and about 11% in 2025-26 according to the UK Master of the Rolls (Aug 2026) and Breakbulk News. That is far short of the DCSA carriers' pledge of 100% by 2030. The bottlenecks are now:
- banks: only about 22% use eBLs at all in 2026, unchanged from 2024
- forwarders: about 29% in 2024
- platform interoperability
- legal recognition: few MLETR enactments; the US and China are reportedly not MLETR jurisdictions

### Cited Findings
- In February 2023, DCSA member carriers committed to 100% eBL adoption by 2030 [pre-2024] — [Logistics Management](https://www.logisticsmgmt.com/article/digital_container_shipping_association_members_herald_commitment_to_ebl_by)
- FIT Alliance 2026 survey (published 21 Oct 2026):
  - 22.2% of banks report at least partial eBL use, broadly flat versus 21.1% in 2024.
  - The Alliance now names interoperability as the top priority.
  - [ICC](https://iccwbo.org/news-publications/news/electronic-bill-of-lading-adoption-grows-as-focus-shifts-to-interoperability/); [AJOT](https://www.ajot.com/news/electronic-bill-of-lading-adoption-grows-as-focus-shifts-to-interoperability)
- FIT Alliance 2024 survey:
  - Overall adoption (eBL alone or alongside paper) rose from 33.0% to 49.2%.
  - Freight forwarders lagged at 29.4%.
  - Terminals and owners/carriers (bulk and container) were above 73%.
  - [ICC](https://iccwbo.org/news-publications/news/survey-shows-steady-rise-of-global-adoption-of-electronic-bills-of-lading/)
- Volume-based measures:
  - DCSA: eBL adoption "doubles to 5%" but barriers remain — [GTR](https://www.gtreview.com/news/digital-trade/ebl-adoption-doubles-to-5-but-barriers-to-digitisation-remain-dcsa-finds/)
  - About 5.7% of bills were issued electronically in early 2025 — [GetTransport guide](https://blog.gettransport.com/trends-in-logistic/electronic-bill-of-lading-2026-interoperability-guide/)
  - Adoption reached 11% in 2025 — [Breakbulk News](https://breakbulk.news/?p=45793)
- UK Master of the Rolls (August 2026 speech): global eBL uptake rose from about 1% in 2021 to about 11% in 2026, and "only a few countries" have enacted MLETR — [Judiciary UK](https://www.judiciary.uk/speech-by-the-master-of-the-rolls-getting-the-paper-out-of-international-trade-and-finance-why-not-now/)
- DCSA: "hidden frictions slow progress in eBL adoption" — [WorldPorts](https://www.worldports.org/?p=606163)
- June 2026: five eBL platforms had implemented version 2 of the DCSA Standard Annex for eBL Platform Interoperability, which lets an eBL move between platforms while preserving carrier liability cover. This comes from a search summary; the exact source among the results is uncertain — [GetTransport guide](https://blog.gettransport.com/trends-in-logistic/electronic-bill-of-lading-2026-interoperability-guide/); [FIDI Focus](https://www.fidifocus.org/on-the-wire/electronic-bills-of-lading-accelerate-as-industry-shifts-towards-digitalising-global-trade/)
- MLETR status (sources conflict):
  - The ICC DSI tracker, as cited by Trade Finance Global, lists Belize, Germany, Mexico, Papua New Guinea, Paraguay, Timor-Leste, the UK and the USA as having passed or enacted MLETR-type legislation — [Trade Finance Global](https://www.tradefinanceglobal.com/posts/status-update-mletr-adoption-in-the-g7-and-emerging-markets)
  - France joined the "MLETR club" with the titre transférable électronique — [Trade Finance Global](https://www.tradefinanceglobal.com/posts/france-joins-mletr-club-recognisingtitre-transferable-electronique)
  - Other sources list Bahrain (first), Kiribati, Abu Dhabi Global Market and Singapore — [ICC Academy](https://icc.academy/?p=22131); [Maritime Gateway](https://www.maritimegateway.com/advancing-ebl-adoption-and-the-role-of-mletr/)
  - A 2026 guide says the Netherlands is transposing MLETR, Japan is preparing Commercial Code amendments and India is consulting, and that the United States and China have not enacted MLETR. This contradicts the TFG list on the US. The likely explanation: US state-law UCC provisions allow electronic documents of title, while there is no federal MLETR enactment — [GetTransport guide](https://blog.gettransport.com/trends-in-logistic/electronic-bill-of-lading-2026-interoperability-guide/)
- CargoX markets compliance with both MLETR and the UK Electronic Trade Documents Act (ETDA) — [CargoX](https://cargox.io/content-hub/ensuring-compliance-with-mletr-and-etda)

### Inferences
- **Carriers are not the bottleneck; the parties downstream of the carrier are.** Owners/carriers sit above 73% on the user metric, while forwarders are at 29% and banks at 22%. eBL volume is stuck around 5-11% because the party who holds the BL (forwarder, bank, consignee) often cannot receive it.
- **Openings for small teams** (rather than "build another eBL platform", which is crowded):
  - interoperability middleware on the DCSA PINT/interoperability annex
  - eBL "receive-and-manage" wallets for small forwarders and consignees
  - bank-side document checking (LC compliance checking of eBL plus commercial documents)
  - NVOCC/house-BL digitisation
- **Fraud is a demand driver.** Paper BL fraud and duplicate-financing fraud push banks toward title registries. But bank adoption is flat, so legal certainty (MLETR) and LC rules are the real blockers, not technology.

### Gaps
- No carrier-level 2026 eBL share by DCSA member, and no confirmation whether the interim 50%-by-2027 milestone (UNVERIFIED background: the February 2023 DCSA pledge was 50% within 5 years and 100% within 10) is on track.
- No platform market shares or pricing per BL.
- No authoritative UNCITRAL status list was retrieved.
- UNVERIFIED background:
  - The UK ETDA 2023 came into force on 20 Sep 2023. Singapore amended its Electronic Transactions Act in 2021. Bahrain (2018) was first to enact MLETR.
  - In the US, UCC Article 7 (2003 revision) permits electronic documents of title under state law, but federal bills-of-lading law has not been modernised.
  - Platforms include WAVE BL, essDOCS (reportedly acquired by ICE and rebranded ICE Digital Trade), Bolero, CargoX, edoxOnline, IQAX (COSCO/OOCL-linked, GSBN ecosystem), Secro, Enigio, and TradeTrust (Singapore IMDA framework, not a platform). IG P&I clubs approve platforms for cover.
  - Likely blockers: per-BL fees, onboarding of consignees and banks, UCP600/eUCP practice, customs and authorities still requiring paper in some LatAm and Asian jurisdictions, and too many closed platforms.

---

## 4. Bulk/tanker/chartering tech: chartering, voyage management, laytime/demurrage, bunkers, sanctions screening

### Takeaway
I could gather little verified 2026 material here before the search budget ran out. The cited findings confirm the main structural shifts: Kpler's consolidation of maritime data, the 2026 Hormuz crisis (which sharply increased the need for tanker risk, sanctions and route intelligence), and bunker-cost volatility. Bulk and tanker workflows (fixtures by email, laytime and demurrage claims, bunker procurement) remain document- and email-heavy, which suits LLM-based extraction. Incumbents include Veson IMOS (the voyage-management system of record), Kpler (data), and Signal Ocean, Shipfix and Sedna (chartering and email intelligence).

### Cited Findings
- Kpler owns MarineTraffic, FleetMon (2023) and Spire Maritime satellite AIS ($241m, closed April 2025). This makes it the dominant combined commodity-flow and AIS data provider. The UK CMA investigated the deal — [Maritime Executive](https://maritime-executive.com/article/kpler-closes-spire-maritime-acquisition-as-uk-proceeds-with-investigation); [Ship Technology](https://www.ship-technology.com/news/kpler-maritime-spire-maritime-acquisition/)
- Hormuz disruption in 2026: transits fell from about 138 a day to 5 or fewer in March. Hundreds of ships were trapped in the Gulf, forcing Gulf producers to cut output. A US-coordinated effort shuttled tankers through the Strait to supertankers waiting outside. Iran blacklisted 45 tankers — [UANI](https://www.unitedagainstnucleariran.com/analysis/iran-war-shipping-update-march-31-2026); [Financial Express](https://thefinancialexpress.com.bd/world/iran-threatens-45-tankers-with-fines-confiscation-in-hormuz-escalation); [gCaptain](https://gcaptain.com/hormuz-at-near-standstill-as-iran-warns-ships-to-keep-to-its-waters/)
- Carriers pushed bunker surcharges in 2026 (Drewry WCI commentary) — [Container News](https://container-news.com/wci-holds-steady-at-2287-as-carriers-push-for-bunker-surcharges/embed/)
- KPI OceanConnect frames EU ETS allowance (EUA) procurement as a strategic bunker-desk activity ("September is the deadline but strategy is the bigger story"). Bunker suppliers are bundling EUAs with fuel — [Manifold Times](https://www.manifoldtimes.com/news/kpi-oceanconnect-on-euas-september-is-the-deadline-but-strategy-is-the-bigger-story/)

### Inferences
- **Sanctions and dark-fleet screening** is a growth market in 2026. Iran, Russia and Venezuela, plus Iran's own counter-blacklist, mean charterers, banks, insurers and traders must screen vessels for AIS gaps, ship-to-ship transfers, flag hopping and ownership changes. Data access (AIS) is concentrated in Kpler, which creates both a dependency risk and a reason for alternative data such as SAR satellite imagery, port-call records and registries.
- **Laytime/demurrage claims in bulk and tanker** are high-value per claim (often tens to hundreds of thousands of dollars), document-heavy (statements of facts, NORs, charter party clauses) and rules-based. That makes them well suited to LLM extraction plus deterministic calculation. A small team could reach owners, operators and charterers without displacing IMOS, by integrating with it.
- **Email-native chartering** is still standard (position lists, cargo orders). Several startups tackle it; the opening is likely in verticals (e.g., Handysize/Supramax, LatAm grain, Black Sea; corridor specifics are covered by other researchers) or in workflow automation, not another data terminal.

### Gaps
- No 2025-26 verified facts were gathered on Veson Nautical, Signal Ocean, Shipfix, Sedna, Marcura/DA-Desk, ShipNet, Dataloy, Vortexa, Windward, Pole Star, Lloyd's List Intelligence or S&P MIRA, nor on bunker procurement platforms (Integr8, ZeroNorth bunker, BunkerEx) or laytime automation vendors. The search budget was exhausted.
- No verified 2026 figures on shadow-fleet size or on the EU/UK/G7 price-cap level.
- UNVERIFIED background:
  - G7 Russian crude price cap of $60/bbl from December 2022. The EU and UK moved to a dynamic cap (about 15% below market average) of $47.60 from September 2025, with a further reduction reported for early 2026.
  - Windward (Israel/UK) was taken private by FTV Capital around late 2024.
  - Veson acquired Q88 (2020) and Oceanbolt (2021).
  - Marcura reportedly acquired Shipfix (about 2023).
  - All of the above need checking.

---

## 5. Ship management & vessel operations: fleet ERP, performance/weather routing, crew, cyber, connectivity

### Takeaway
No vessel-ops-specific 2025-26 sources were retrieved (search budget exhausted). Structurally, three regulatory and technology shifts expand the market for onboard and shore software, and incumbents (Kongsberg, Wärtsilä, DNV, StormGeo, ZeroNorth) are strong in performance and routing:
- IACS cyber unified requirements (E26/E27) for new ships
- LEO broadband (Starlink and others), which makes continuous ship-shore data feasible
- CII ratings tied to operational efficiency

### Cited Findings
- EU ETS and FuelEU make voyage-level fuel and emissions data a P&L item ("EU carbon rules start hitting voyage P&L"). This creates demand for performance and emissions monitoring tied to commercial ops — [ShipUniverse](https://www.shipuniverse.com/?p=11606)
- Gemini's hub-and-spoke network reached 89-93% reliability in spring 2026, versus 43-48% for Premier and Ocean in Jul/Aug 2026. Operational design and execution software clearly matter for outcomes — [Container News](https://container-news.com/sea-intelligence-global-schedule-reliability-for-may-2026-the-highest-of-the-year/); [FreshPlaza](https://www.freshplaza.com/article/9878292/global-container-shipping-schedule-reliability-falls-to-lowest-level-since-2022/)

### Inferences
- Onboard software was historically limited by expensive VSAT bandwidth. With LEO connectivity, cloud-native fleet apps (real-time performance, remote maintenance, crew apps, cyber monitoring) become feasible. This lowers barriers for software-only entrants that previously needed hardware or edge deployments.
- Cyber compliance for new ships (E26/E27) mostly falls on yards, makers and class. The ongoing operational demand (asset inventory, OT network monitoring, incident reporting for managers running mixed fleets) is a possible niche, but it is crowded by OT-security vendors and class societies.

### Gaps
- No verified data on ZeroNorth (funding or acquisitions), StormGeo ownership, Wärtsilä/Kongsberg software revenue, Nautilus Labs' fate, Bearing AI, Orca AI, Sofar Ocean, fleet ERP vendors (ShipNet, Helm, BASS, Danaos, Hanseaticsoft, Star IPS, SERTICA) or crew platforms. No Starlink maritime vessel counts.
- UNVERIFIED background:
  - IACS UR E26 (cyber resilience of ships) and E27 (cyber resilience of onboard systems and equipment) are mandatory for ships contracted for construction on or after 1 Jul 2024.
  - A US Coast Guard final rule on Marine Transportation System cybersecurity was published in January 2025 (effective July 2025, phased requirements).
  - ZeroNorth (a Maersk Tankers spin-off) merged with Alpha Ori Technologies around 2023.
  - StormGeo has been owned by Alfa Laval since 2019.
  - Nautilus Labs (NYC, vessel performance ML) is reported to have shut down or wound down around 2024. Not verified; please check before citing as a failure case.

---

## 6. Decarbonization compliance demand: IMO CII/EEXI, IMO Net-Zero Framework, EU ETS, FuelEU, MRV

### Takeaway
EU rules are the live, money-moving regime:
- **EU ETS:** 70% of 2025 emissions are due for surrender by 30 Sep 2026, and 100% of 2026 emissions (now including methane and N2O) are due in 2027.
- **FuelEU Maritime:** the first compliance year (2025) closed with about 92% of ships using pooling, at surplus prices around €200-210/tCO2e that fell to about €170 after the April 2026 deadline.

IMO's global Net-Zero Framework (NZF) was approved in April 2025 but adjourned in October 2025 by a 57-49 vote. It is still not adopted: decision points are ISWG-GHG 23 (23-27 Nov), MEPC 85 (30 Nov-3 Dec) and the resumed extraordinary session on 4 Dec 2026. Software demand is shifting from monitoring/reporting (largely served) to optimisation, trading and pooling (an emerging market): EUA procurement and transfer, FuelEU pool matching, voyage-level cost pass-through and verifiable fuel provenance.

### Cited Findings
**IMO Net-Zero Framework**
- October 2025 extraordinary MEPC session: delegates voted 57-49 to adjourn adoption for one year. The US, Saudi Arabia and Russia objected to adoption; most EU states and the UK voted in favour — [DNV](https://www.dnv.com/news/2025/decision-on-the-imo-net-zero-framework-delayed-for-one-year/); [CIMAC](https://www.cimac.com/news-press/news/extraordinary-imo-mepc-meeting-fails-to-adopt-net-zero-framework.html); [Container News](https://container-news.com/imo-defers-adoption-of-net-zero-framework-to-2026/)
- MEPC 84 (spring 2026): a majority reaffirmed the NZF as the basis for further work, and further talks to "strengthen" it were agreed. Adoption will be "in November at the earliest". Schedule: ISWG-GHG 23 on 23-27 Nov 2026, MEPC 85 on 30 Nov-3 Dec 2026, resumed Second Extraordinary Session on 4 Dec 2026 — [Ammonia Energy Association](https://ammoniaenergy.org/articles/mepc84-support-for-net-zero-framework-stabilizes-ahead-of-key-decision-point-in-late-2026/); [Hill Dickinson](https://www.hilldickinson.com/our-view/articles/imo-s-net-zero-framework-adoption-adjourned-and-consensus-building-continues/); [Seatrade Cruise](https://www.seatrade-cruise.com/environmental-health/imo-net-zero-framework-decision-deferred-to-november)
- Commentary heading into December: "Can December deliver a breakthrough?"; "NZF survives assault but adoption remains uncertain" — [Hellenic Shipping News/Engine](https://www.hellenicshippingnews.com/?p=1147741); [Datamar News](https://datamarnews.com/noticias/imo-net-zero-framework-survives-assault-but-adoption-remains-uncertain/)
- Adoption threshold: one summary says adoption needs acceptance by two-thirds of the 108 MARPOL Annex VI Parties, representing at least 50% of world gross tonnage. My understanding is that the IMO procedure is a two-thirds majority of Parties present and voting to adopt, then tacit acceptance unless objected to by one-third of Parties or by Parties with at least 50% of GT. Verify — [ShipUniverse](https://www.shipuniverse.com/news/imo-net-zero-rules-stay-alive-but-the-adoption-path-is-still-unsteady/)

**EU ETS (maritime)**
- Phase-in: 40% of 2024 emissions, 70% of 2025 emissions, 100% of 2026 emissions. Methane and N2O are included from 2026. The penalty is €100 per missing allowance plus the obligation to buy the shortfall — [HFW ETS factsheet](https://www.hfw.com/downloads/004998-HFW-ETS-Factsheet.pdf); [Synergy Marine](https://www.synergymarinegroup.com/blog/eu-ets-compliance-shipping-companies/)
- Surrender deadline for maritime is 30 September (sources differ: ABS cites 30 April from the general ETS text) — [Manifold Times / KPI OceanConnect](https://www.manifoldtimes.com/news/kpi-oceanconnect-on-euas-september-is-the-deadline-but-strategy-is-the-bigger-story/); [ABS regulatory note](https://ww2.eagle.org/content/dam/eagle/regulatory-news/2022/ABS%20Regulatory%20News%20-%20EU%20ETS%20Amendments.pdf)
- EmissionLink warns shipowners of growing financial risk from delayed EUA transfers by charterers and commercial operators. This is a contractual and cash-flow pain point (the ETS Directive makes the ISM company liable, with pass-through clauses to the commercial operator) — [Manifold Times](https://www.manifoldtimes.com/news/emissionlink-warns-shipowners-of-growing-financial-risk-from-delayed-eua-transfers/)
- OceanScore estimated Asian owners faced more than €1bn in emissions liabilities for EU-bound voyages (earlier estimate at roughly €78/EUA) — [Hellenic Shipping News](https://www.hellenicshippingnews.com/?p=1029191); [Container News](https://container-news.com/asian-ship-owners-to-face-over-us1-billion-emissions-liabilities-for-eu-bound-voyages/)
- Ship & Bunker runs an EU ETS cost-of-compliance tracker — [Ship & Bunker EU ETS](https://coop.shipandbunker.com/eu-ets)

**FuelEU Maritime (from 1 Jan 2025)**
- First compliance year: about 92% of vessels used pooling and 2% used borrowing. The average surplus price was about €208/tCO2e (Skuld analysis) and fairly stable — [Ship & Bunker](https://shipandbunker.com/news/world/687374-92-of-vessels-chose-pooling-in-first-year-of-fueleu-compliance-analysis)
- Pool prices held around €200/tCO2e through 2025 and hit an all-time low of about €170 in May 2026, after the April pooling deadline — [Global Maritime Forum "Countdown" figures](https://www.zerocarbonshipping.com/files/countdown-what-did-we-learn-from-the-first-year-of-fueleu-figures.pdf); [Countdown article](https://www.zerocarbonshipping.com/news/countdown-what-did-we-learn-from-the-first-year-of-fueleu)
- OceanScore Pool-Price Index (OPX): about €213 in early 2026 after additional 2025 surplus was released, about €219 by February 2026. The OceanScore site header shows "OPX (2026) €172.80", which looks like a later live value — [Hellenic Shipping News](https://www.hellenicshippingnews.com/monthly-oceanscore-pool-price-index-opx-february-2026/); [OceanScore](https://oceanscore.com/insights/oceanscore-pool-price-index-market-commentary-february-2026/)
- The deadline to enter ships into 2025 pools was 30 Apr 2026 — [Skuld](https://www.skuld.com/topics/environment/air-pollution/europe/timeline-to-achieve-compliance-under-fueleu-for-the-2025-reporting-year)
- "FuelEU pooling may be working too well": about 7% of ships switched fuels or paid penalties; overcompliance by a few LNG and biofuel ships covers many others — [Kuehne+Nagel news](https://mykn.kuehne-nagel.com/news/article/fueleu-pooling-may-be-working-too-well)
- The Kickster FuelEU Marketplace reports falling pooling prices and rising adoption in the first cycle — [Hellenic Shipping News](https://www.hellenicshippingnews.com/first-fueleu-maritime-cycle-reveals-falling-pooling-prices-and-rising-market-adoption-says-kickster-fueleu-marketplace/)
- Argus launched FuelEU GHG-reduction price assessments, which shows that a priced compliance commodity now exists — [Argus](https://argusmedia.com/en/about-argus/media-centre/press-releases/argus-launches-fueleu-greenhouse-gas-reduction-prices)
- Vendors visible in results: OceanScore (pooling/ETS), Kickster (FuelEU marketplace), EmissionLink (EUA transfer), KPI OceanConnect (EUA plus bunkers), Argus (price reporting) — sources above.

### Inferences
- **MRV and reporting are table stakes.** Class societies (DNV Veracity, ABS, LR, BV) and established vendors already serve them. The live money is in:
  - (a) EUA cash-flow and contractual pass-through between owners, managers and charterers: invoicing, collateral, transfer tracking, BIMCO ETS-clause automation
  - (b) FuelEU pool formation and matching, an optimisation problem across fleets with fuel-type and voyage uncertainty
  - (c) integrated "carbon P&L per voyage" for chartering decisions (ETS + FuelEU + future IMO GFI remedial units)
  - (d) fuel provenance and verification of biofuel/LNG/methanol certificates (PoS/ISCC) against fraud
- **IMO NZF uncertainty cuts both ways.** If adopted in December 2026, a global GFI and remedial-unit market (entry into force likely about 2028) would create a much larger, global compliance-trading market. If it fails again, the EU regime stays the main paid driver and the 2026 US opposition persists. A product should be regime-agnostic: an emissions ledger plus an optimisation engine that can plug in EU or IMO rules.
- Falling FuelEU surplus prices (from about €208 to about €170) suggest a structurally long market in early years. Pooling margins for intermediaries will compress, so marketplaces alone are thin; the value is in data and optimisation embedded in commercial ops.

### Gaps
- No 2026 EUA price level and no aggregate shipping EUA surrender data for the 2025 year.
- No list of FuelEU verifier and software market shares.
- Whether MEPC 84 changed the NZF draft text (e.g., GFI levels, price of remedial units) is not verified.
- CII/EEXI status not verified.
- UNVERIFIED background:
  - NZF as approved at MEPC 83 (April 2025): a GHG Fuel Intensity (GFI) standard with base and direct-compliance targets, with tiered remedial units at about $380/tCO2e (tier 2) and $100/tCO2e (tier 1) and a Net-Zero Fund.
  - CII reduction factors reach 11% versus 2019 in 2026; reported MEPC 83 extension of factors for 2027-2030.
  - FuelEU GHG intensity reduction of 2% (2025-29), 6% (2030), 14.5% (2035), rising to 80% (2050). Penalty about €2,400 per tonne of VLSFO-equivalent energy deficit. Shore-power obligation for container and passenger ships at TEN-T ports from 2030.
  - EU ETS extension to offshore vessels over 5,000 GT from 2027. MRV extended to general cargo/offshore vessels of 400-5,000 GT from 2025.

---

## 7. Biggest unsolved pain points (carriers, forwarders, shippers, owners/managers)

### Takeaway
The verified pain points are:
- chronic schedule unreliability: 49.9-62.6% in 2026, with the gap between alliances wider than the gap between years
- D&D billing disputes under a partly vacated FMC rule
- documentation still mostly paper: about 11% eBL adoption, banks at 22%
- compliance cash-flow friction from ETS and FuelEU
- extreme rate volatility, with the WCI nearly doubling from January to July 2026

Small forwarders are adopting digital booking (Freightos/WebCargo transactions +15-27% y/y), but they lack affordable integrated tooling. Fraud, insurance/claims and LatAm specifics could not be verified with 2026 sources in this session.

### Cited Findings
- Reliability: global 62.4% (Jan), 59.0% (Feb), 62.6% (Jun), 49.9% (Aug 2026, lowest since September 2022, Asian port congestion). By alliance in Jul/Aug: Gemini 77.8% versus Premier 43.2% — [Sea-Intelligence](https://www.sea-intelligence.com/press-room/373-2026-starts-with-global-schedule-reliability-of-62-4); [FreshPlaza](https://www.freshplaza.com/article/9878292/global-container-shipping-schedule-reliability-falls-to-lowest-level-since-2022/)
- D&D: the FMC rule voids invoices missing required fields, and the 2025 court vacatur changed who can be billed. US practitioners still describe D&D as a dispute-heavy area — [FreightWaves](https://www.freightwaves.com/news/fmc-tightens-rules-on-charging-container-late-fees); [Husch Blackwell](https://www.huschblackwell.com/newsandinsights/appeals-court-decision-reshapes-detention-and-demurrage-billing-landscape-for-truckers); [Barbri CLE "D&D practices and disputes: recent developments" (Sep 2025)](https://www.barbri.com/course/professional-development/cle/demurrage-and-detention-practices-and-disputes-recent-develo_2025-09-16)
- Documentation: about 11% eBL uptake in 2026, forwarders 29.4% (2024), banks 22.2% (2026), and DCSA's "hidden frictions" — [Judiciary UK](https://www.judiciary.uk/speech-by-the-master-of-the-rolls-getting-the-paper-out-of-international-trade-and-finance-why-not-now/); [ICC 2024](https://iccwbo.org/news-publications/news/survey-shows-steady-rise-of-global-adoption-of-electronic-bills-of-lading/); [ICC 2026](https://iccwbo.org/news-publications/news/electronic-bill-of-lading-adoption-grows-as-focus-shifts-to-interoperability/); [WorldPorts](https://www.worldports.org/?p=606163)
- Compliance cash flow: delayed EUA transfers create financial risk for owners — [Manifold Times](https://www.manifoldtimes.com/news/emissionlink-warns-shipowners-of-growing-financial-risk-from-delayed-eua-transfers/)
- Small and mid forwarders' digitisation: WebCargo is Freightos' largest GBV contributor. Freightos SaaS revenue came in below expectations in Q2 2026, which suggests forwarders adopt transactional tools faster than they pay for SaaS seats — [PR Newswire Q2 2026](https://www.prnewswire.com/il/news-releases/freightos-reports-second-quarter-2026-results-302852762.html)
- Asia: port congestion in Asia drove the August 2026 reliability collapse — [FreshPlaza](https://www.freshplaza.com/article/9878292/global-container-shipping-schedule-reliability-falls-to-lowest-level-since-2022/)
- Section 301 uncertainty: shippers were advised to watch for vessel swaps around the January deadline, because fee exposure depends on which vessel carries the cargo — [Tradlinx](https://blogs.tradlinx.com/china-linked-vessel-fees-why-shippers-should-watch-for-january-vessel-swaps/)

### Inferences
- **Data fragmentation is the common root.** Schedules, container events, invoices, BLs, emissions and vessel provenance live in different systems, PDFs and emails. Gemini's results suggest reliability is partly a network-design choice. For shippers, the actionable layer is carrier/service selection plus buffer planning backed by data, which is a modelling problem.
- **Back-office document processing remains the cheapest pain to address with LLMs** for forwarders: arrival notices, invoices, D&D bills, BL drafts, commercial invoices and packing lists. This explains the many AI-for-forwarders startups (unverified names in Gaps).
- **Fraud.** Paper BLs, fake bunker certificates (FuelEU biofuel credits) and sanctions evasion via document manipulation are converging. A verification layer (document authenticity plus vessel-behaviour cross-checks) is a coherent technical product.

### Gaps
- No 2026 data on BL/document fraud losses, cargo insurance and claims tech (e.g., marine insurers' digital claims), or marine insurance market changes from the Iran war (war-risk premiums).
- No LatAm-specific forwarder tooling data (e.g., Magaya, Nuvocargo, local customs integrations in Brazil, Mexico, Colombia).
- No quantification of D&D charges paid in 2025-26.
- Florida-LatAm, California-Asia and Black Sea corridors are covered by other researchers.

---

## 8. Startups funded, acquired or failed 2022-2026 in ocean tech

### Takeaway
2022-2026 saw consolidation by large platforms (WiseTech-e2open/INTTRA, Kpler-MarineTraffic/FleetMon/Spire) and retrenchment of 2020-22 venture darlings (Flexport's repeated layoffs; no fresh Forto, Zencargo or Beacon rounds found). The only listed pure-play, Freightos, has sub-$35m annual revenue. Blockchain consortia failed (TradeLens; UNVERIFIED background). The searches turned up no new 2025-26 mega-rounds in ocean tech; the capital went to M&A by incumbents instead.

### Cited Findings
- WiseTech to acquire e2open (and INTTRA), about $2.1bn equity, announced May 2025 — [ASX](https://announcements.asx.com.au/asxpdf/20250526/pdf/06k2vxtpvjv24c.pdf); [STAT Times](https://www.stattimes.com/technology/wisetech-global-to-acquire-e2open-in-21-billion-deal-1355390)
- Kpler: MarineTraffic and FleetMon (2023); Spire Maritime ($241m, announced November 2024, closed 25 Apr 2025 after litigation, under UK CMA scrutiny) — [Maritime Executive](https://maritime-executive.com/article/kpler-closes-spire-maritime-acquisition-as-uk-proceeds-with-investigation); [WorldPorts](https://www.worldports.org/kpler-wraps-up-spire-maritime-acquisition)
- Flexport: about 20% layoffs (October 2023, after earlier cuts); $260m Shopify convertible note; 2024 revenue about $2.1bn versus an $8bn 2022 valuation; acquired Shopify Logistics; TIME100 2026 — [TechCrunch](https://techcrunch.com/?p=1941956); [StockAnalysis](https://stockanalysis.com/private/flexport/)
- Freightos (Nasdaq-listed): Q2 2026 revenue $7.7m, $21m cash, aiming for breakeven — [PR Newswire](https://www.prnewswire.com/il/news-releases/freightos-reports-second-quarter-2026-results-302852762.html)
- [pre-2024] project44: $420m raise at a $2.2bn valuation; acquired Ocean Insights and ClearMetal (2021) — [STAT Times](https://www.stattimes.com/amp/supply-chain/project44-raises-420mn-from-goldman-tpg-valued-at-22bn-1307440); [MMH](https://www.mmh.com/article/project44_announces_acquisition_of_ocean_insights)
- [pre-2024] Last disclosed rounds for Forto ($250m, March 2022), Zencargo ($42m, 2021) and Beacon ($50.3m Series B, October 2021) — [Caplight](https://www.caplight.com/company/forto); [TechCrunch](https://techcrunch.com/2021/05/10/zencargo-raises-42m-to-expand-its-digital-first-freight-forwarding-platform-internationally/embed/); [CB Insights](https://www.cbinsights.com/company/beacon-2/financials)

### Inferences
- **Exit paths exist mainly via acquisition** by WiseTech, Kpler, Descartes, DP World, class societies, Veson or large forwarders. A startup should be designed as an acquirable data or workflow module that plugs into these platforms.
- **The digital-forwarder model (asset-light forwarder with software) proved capital-intensive and cyclical.** Pure-software plays that sell to forwarders look more capital-efficient than becoming one.

### Gaps
- Crunchbase, Thetius and Sifted funding data for 2024-26 could not be searched (budget exhausted), so there is no 2025-26 deal list for maritime tech venture rounds.
- UNVERIFIED background (check before citing):
  - TradeLens (Maersk/IBM) discontinuation was announced on 29 Nov 2022 and the service shut in Q1 2023, mainly because rival carriers would not join a Maersk-led platform.
  - The trade-finance blockchains we.trade (2022) and Marco Polo (insolvency, 2023) also failed.
  - Flexport timeline: Dave Clark served as CEO (2022-23); Flexport acquired Convoy's technology assets (October 2023).
  - Windward was taken private by FTV Capital (about late 2024).
  - ZeroNorth merged with Alpha Ori Technologies (about 2023).
  - Nautilus Labs reportedly wound down (about 2024).
  - Maersk's digital forwarding brand Twill status is unclear.
  - DP World acquired Searates (about 2021).

---

## 9. White spaces for a small technical team vs. areas locked up by giants

### Takeaway
Avoid building:
- another booking network (WiseTech/INTTRA)
- a raw AIS or position-data business (Kpler/Spire)
- a generic visibility dashboard (project44/FourKites)
- a forwarder ERP head-on (CargoWise)
- a new eBL title registry (more than 10 platforms already, adoption limited by banks and law)

The best openings for a data/ML/software founder are narrow, rules-heavy, document-heavy workflows with clear dollar outcomes, where regulation changed recently and incumbents are horizontal:
1. D&D invoice audit and dispute automation, anchored in 46 CFR 541
2. EU ETS/FuelEU cash-flow and pooling optimisation, regime-agnostic so it can absorb IMO NZF if adopted in December 2026
3. Bulk/tanker laytime and demurrage claims automation
4. Vessel-level risk and provenance scoring (sanctions, Section 301 exposure, war-risk routing)
5. eBL interoperability and "last-mile" receiving tools for forwarders and banks
6. Predictive schedule and carrier-selection analytics for mid-size shippers, given the 2026 reliability gap between alliances

### Cited Findings (evidence underpinning the white-space assessment)
- Locked-up layers: WiseTech plus e2open/INTTRA (booking network) — [The Loadstar](https://theloadstar.com/2-1bn-e2open-purchase-will-catapult-wisetech-into-a-different-dimension/); Kpler plus MarineTraffic/FleetMon/Spire (AIS) — [Maritime Executive](https://maritime-executive.com/article/kpler-closes-spire-maritime-acquisition-as-uk-proceeds-with-investigation)
- Regulatory hooks with hard rules: the FMC 30-day invoicing rule and mandatory fields (a missing field voids the charge) — [FreightWaves](https://www.freightwaves.com/news/fmc-tightens-rules-on-charging-container-late-fees); ETS at 100% from 2026 emissions plus CH4/N2O — [HFW](https://www.hfw.com/downloads/004998-HFW-ETS-Factsheet.pdf); 92% of ships in FuelEU pools — [Ship & Bunker](https://shipandbunker.com/news/world/687374-92-of-vessels-chose-pooling-in-first-year-of-fueleu-compliance-analysis); EUA transfer delays — [Manifold Times](https://www.manifoldtimes.com/news/emissionlink-warns-shipowners-of-growing-financial-risk-from-delayed-eua-transfers/)
- IMO NZF pending on 4 Dec 2026 — [Ammonia Energy](https://ammoniaenergy.org/articles/mepc84-support-for-net-zero-framework-stabilizes-ahead-of-key-decision-point-in-late-2026/)
- eBL bottleneck at forwarders and banks, with interoperability as the stated priority — [ICC 2026](https://iccwbo.org/news-publications/news/electronic-bill-of-lading-adoption-grows-as-focus-shifts-to-interoperability/)
- Reliability gap between alliances (Gemini 77.8% vs Premier 43.2%) and global reliability of 49.9% — [FreshPlaza](https://www.freshplaza.com/article/9878292/global-container-shipping-schedule-reliability-falls-to-lowest-level-since-2022/)
- Section 301 fees depend on vessel provenance, and shippers are watching vessel swaps — [Tradlinx](https://blogs.tradlinx.com/china-linked-vessel-fees-why-shippers-should-watch-for-january-vessel-swaps/)
- Geopolitical tanker risk (Iran blacklist of 45 tankers, Hormuz closures) — [Financial Express](https://thefinancialexpress.com.bd/world/iran-threatens-45-tankers-with-fines-confiscation-in-hormuz-escalation)
- Marketplace economics are thin (Freightos: about 1.8% revenue on GBV) — [PR Newswire](https://www.prnewswire.com/il/news-releases/freightos-reports-second-quarter-2026-results-302852762.html)

### Inferences
- **D&D audit (US importers, NVOCCs, BCOs).**
  - Inputs: carrier and MTO invoices (PDF/EDI), container milestone events (AIS plus carrier T&T APIs), tariff and free-time rules.
  - Output: auto-dispute packages citing missing 46 CFR 541 fields, late invoices (over 30 days) and service failures.
  - Moat: labelled dispute outcomes, plus carrier-specific invoice parsers.
  - Risk: the FMC rules changed in 2025, and carriers may improve invoice compliance over time.
- **Carbon-compliance ops layer (owners, managers, charterers in Europe).**
  - Scope: EUA liability per voyage, charterer pass-through invoicing and collection, FuelEU pool optimisation (mixed-integer and stochastic optimisation across ships and fuels), and audit-ready data lineage from noon reports and bunker delivery notes.
  - Differentiator: plugging into IMOS and fleet systems, versus standalone MRV tools.
  - Timing: 2026 is the first 100% ETS year and the second FuelEU year. The IMO decision on 4 Dec 2026 could expand the total addressable market (TAM) globally.
- **Laytime/demurrage and claims automation (bulk/tanker).**
  - What it does: LLM extraction from statements of facts, NORs and charter-party clauses, followed by deterministic laytime calculation.
  - Value: high per claim; buyers are commercial operators and P&I and FD&D clubs.
  - Competitors: incumbent modules in Veson and Marcura (unverified). Opening for accuracy-led, integration-first entrants.
- **Vessel risk and provenance scoring.**
  - What it does: fuses AIS (bought from multiple providers to avoid Kpler lock-in), registries, port-state control, ownership graphs and SAR imagery.
  - Questions answered: "Is this ship sanctioned or shadow-fleet?", "Will it trigger USTR fees?", "What is its war-risk exposure on this route?"
  - Buyers: charterers, banks, insurers, traders, forwarders.
  - Risk: Windward, Kpler, Pole Star, S&P and LLI are entrenched in sanctions compliance, so niche by buyer type (e.g., forwarders/NVOCCs, LatAm traders) or by question (USTR fee exposure).
- **Forwarder and bank "last mile" eBL tools.**
  - Product: a lightweight receiver wallet plus DCSA interoperability and LC document checking.
  - Risk: depends on the platforms' interoperability progress (5 platforms on interop v2 as of June 2026) and on MLETR-style laws.
- **Mid-size shipper carrier and service selection.**
  - What it does: predict actual transit-time distributions by service and alliance, and feed buffer stock and contract allocation.
  - Data: Sea-Intelligence-style schedule data plus own AIS-derived arrival data.
  - Risk: visibility platforms are adding predictive ETA; differentiate on procurement decision support (with Xeneta-style rate data) rather than tracking.
- **General point.** With 2027-28 overcapacity likely, buyers will favour tools sold on hard ROI (money recovered, penalties avoided, cost cut) over "visibility". Sales cycles with carriers are long, so forwarders, BCOs, managers and charterers are the faster buyers.

### Gaps
- No pricing benchmarks (ACV) for D&D audit, emissions SaaS or claims tools were found.
- No verified competitor list for D&D audit startups (UNVERIFIED names: Terminal49, Vizion D&D alerts, Container xChange, Expedock, DP World CargoesFlow) or for laytime automation.
- No verification of how much incumbents (Veson, CargoWise, project44) have already shipped in these niches in 2025-26.
- A follow-up session with a restored search budget and allow-listed news domains should check: Thetius 2025/26 investment reports, Crunchbase rounds (Vizion, Portcast, Raft, Expedock, Bearing, Sofar, Orca AI, Shipfix, Signal Ocean, ZeroNorth, OceanScore, Kickster, Container xChange), Nautilus Labs' fate, Windward/FTV, Veson 2025-26 M&A, the IMO MEPC 85 outcome (4 Dec 2026), the USTR final notice, and the late-October WCI figure.
