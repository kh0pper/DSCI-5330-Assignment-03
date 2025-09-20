# Assignment 3 Research Notes

## Requirements Recap
- Review Ford 10-Ks, shareholder reports, and verifiable external media to assess marketing approaches and outcomes; deliver memo and presentation tailored to these insights (notes/Assignment3_Instructions.txt:3)
- Provide evidence-backed conclusions on strategy effectiveness and articulate the role of business intelligence systems in Ford marketing (notes/Assignment3_Instructions.txt:5)

## Ford Marketing Approach (Primary Sources)
- Ford+ growth plan emphasizes “always-on” customer relationships, pairing vehicles with connected services across Ford Blue, Model e, and Ford Pro segments (notes/Ford_2024_Form_10-K.txt:281)
- Segment structure clarifies go-to-market focus: Ford Blue maintains ICE/hybrid portfolio, Model e incubates EV and software capabilities, and Ford Pro combines vehicles with digital fleet services such as telematics and charging (notes/Ford_2024_Form_10-K.txt:312)
- Dealer-led distribution remains core while Ford manages pricing, mix, and marketing incentives to defend share in a highly competitive environment (notes/Ford_2024_Form_10-K.txt:344)
- Proxy statement reinforces that effective marketing and communications are critical for loyalty and market share expansion—board governance treats marketing capability as a strategic skill (notes/Ford_2025_Proxy.txt:16736)

## Evidence on Marketing Outcomes
- **Ford Blue:** 2024 EBIT dropped to $5.3B as mix shifted away from high-margin trucks/SUVs and currency headwinds offset pricing, signalling need to fine-tune product marketing and launch execution (notes/Ford_2024_Form_10-K.txt:2942)
- **Ford Model e:** Revenue declined 35% and losses deepened due to lower net pricing amid EV competition, indicating current marketing offers and price positioning are struggling to convert demand (notes/Ford_2024_Form_10-K.txt:3008)
- **Ford Pro:** Revenue grew 15% with EBIT margin expanding to 13.5% on higher net pricing and fleet demand, showcasing effective commercial value proposition and bundled service marketing (notes/Ford_2024_Form_10-K.txt:3071)
- Marketing incentive programs (rebates, promotional financing, lease offers) are tracked as causal factors in segment profitability, underscoring need for data-driven spend allocation (notes/Ford_2024_Form_10-K.txt:3080)

## Business Intelligence Levers Already in Use
- Ford Pro’s telematics, software subscriptions, and charging services imply an integrated data platform that informs fleet optimization—key BI touchpoint for Assignment 3 deliverables (notes/Ford_2024_Form_10-K.txt:332)
- Digital services and connected vehicle technologies developed in Model e support enterprise-wide insights, providing customer usage data to refine marketing and CX strategies (notes/Ford_2024_Form_10-K.txt:325)

## External Media Insights (Sept 2025)
- USA Today frames “Ready, Set, Ford” as the company’s largest 2025 marketing push, positioned as an invitation to consumers and a signal of the pivot from product-first to human-first storytelling; rollout spans U.S. launch, targeted lifestyle messaging, and integration with Ford Philanthropy’s Building Together initiative (notes/USA_Today_Ready_Set_Ford.txt:40,46,70,84)
- Detroit News highlights the strategy’s resilience message amid economic headwinds, outlines the three lifestyle pillars (Build, Thrill, Adventure), and details how Ford plans to keep the campaign evergreen while balancing brand heritage, quality perceptions, and responsible AI use (notes/DetroitNews_Marketing_AI.txt:13,33,56,63,70,78)
- Ford’s own newsroom article emphasizes the internal commitments behind the campaign—four brand promises (Capability, Passion, Community, Trust), lifestyle-led planning, and showcasing hero products/services like Ford Pro to reignite aspiration (notes/FordNews_Introducing_Ready_Set_Ford.txt:19,51,74,85)

## Next Research Steps
1. Quantify marketing/advertising spend trends and promotional efficiency from Ford’s 10-K footnotes (and latest 10-Q once available).
2. Map “Ready, Set, Ford” lifestyle pillars to segment KPIs (Blue, Model e, Pro) to evaluate effectiveness and identify BI signals required to monitor each pillar.
3. Draft memo outline tying together internal performance data, campaign narrative, and BI opportunities; begin sourcing visuals for presentation deck.
4. Incorporate historic campaign benchmarks (2012 “Go Further”, 2025 “From America, For America”) from `data/external/historic_campaigns.csv` to compare against Ready Set Ford performance.

## Data Refresh Log – 22 Sep 2025
- Google Trends series regenerated; `Ford Pro` baseline trended 1 point lower on most historical weeks, signaling minor normalization rather than directional shift (data/external/google_trends_readysetford_us.csv).
- YouTube metrics summary refreshed; no material change in total views or engagement across six Ready Set Ford uploads (data/external/youtube_metrics.csv).
- Market stats extract reran with 10 rows (no new sources); ready for visual updates in deck.
- Visual assets exported for deck: Google Trends line chart, hashtag bar chart, and financial trend lines (`deck/visuals/`).
- Historic campaign table (`data/external/historic_campaigns.csv`) records 2012 “Go Further” and 2025 “From America, For America” benchmarks for Ready Set Ford storytelling.

## Source Links
- 2024 Form 10-K (filed Feb 6, 2025): https://www.sec.gov/Archives/edgar/data/37996/000003799625000013/f-20241231x10k.htm
- 2024 Annual Report (Ford investor relations): https://shareholder.ford.com/financials/annual-reports/default.aspx
- 2025 DEF 14A (filed Mar 28, 2025): https://www.sec.gov/Archives/edgar/data/37996/000110465925029100/tm2416981-6_def14a.htm
- USA Today – “Ford launches 'Ready, Set, Ford' campaign with biggest marketing push since 2012”: https://www.usatoday.com/story/cars/news/2025/09/13/ford-launches-marketing-campaign/86138025007/
- Ford From the Road – “Introducing: Ready Set Ford”: https://www.fromtheroad.ford.com/us/en/articles/2025/introducing-ready-set-ford
- The Detroit News – “Ford marketing chief talks economy, AI as automaker launches new global strategy”: https://www.detroitnews.com/story/business/autos/ford/2025/09/10/ford-marketing-chief-lisa-materazzo-ready-set-ford-strategy-campaign-advertising/86047640007/

## Class Insights
- Marketing Intelligence (HBSP Core Reading): stresses structured intelligence cycle (define decision problem, select research design, collect/triangulate secondary and primary data, translate into actionable insights). Emphasizes empathetic qualitative work, conjoint/perceptual mapping, and cautionary tales (New Coke) about ignoring emotional drivers.
- Session 6 decks: reinforce lifestyle-centric storytelling (Build/Thrill/Adventure) and need for integrated marketing intelligence systems that monitor market sentiment, fraud/ethics risks, and marketing ROI dashboards.
- Implication for project: combine Ford telemetry and secondary data with new primary research (surveys, immersive qualitative) to validate Ready Set Ford promises, capture emotional attachment, and ensure continuous feedback loops.

## Recent Industry Intelligence (Sept 2025)
- Ford Pro + ServiceTitan integration (Contractor Magazine): highlights direct pipeline between vehicle telematics and service software, reducing setup time and surfacing fuel/maintenance insights—evidence Ford is monetizing data services that align with the campaign’s capability promise.
- Southern Company & Ford Pro managed charging pilot (CBT News): demonstrates Ford Pro Intelligence enabling demand-response savings (0.5 MW during events) while maintaining uptime, providing proof points for the Build persona and EV ROI storytelling.
- J.D. Power 2024 Brand Loyalty Study: Ford achieved a 65.1% loyalty rate among truck owners (highest overall), while Honda SUV loyalty reached 64.2%, Toyota car loyalty 62.5%, Lexus premium SUV loyalty 60.2%, and Porsche premium car loyalty 57.5%.
- McKinsey Collectible Cars report (Feb 2025): niche segment valued at ~€800B with average auction prices around €65K and listing prices ~€56K, illustrating premium storytelling opportunities for heritage models.
- TechXplore review of automotive Industry 4.0 skills gaps: warns that digital transformations falter without human capital investment; informs recommendations around BI governance, training, and dealer enablement.

## Digital Signals (Sept 2025)
- Google Trends (US): interest in "Ready Set Ford" registered its first measurable activity mid-September 2025 (latest weekly index = 1 versus a long-run average near 0), while "Ford Pro" demand remains steady (average index ~29 after today’s normalization, peak 100).
- Twitter/X sample (25 posts, Sept 13-19, 2025): top hashtags include #Ford, #ReadySetFord, #Mustang, #SwapYourRide, #PlanetFord; content mixes campaign excitement with dealer promotions and service feedback.
- YouTube (official uploads): 60-second anthem (24.5K views/503 likes as of run) and alternate cut (611 views/13 likes) provide early viewership benchmarks; short-form clips still pending due to access limits.

## Financial Snapshot (2024 vs 2023)
- Revenue climbed to $185B (+5% YoY), while advertising spend declined to $2.8B (-9.7%), signalling tighter paid media outlays despite topline growth (data/sec/ford_metrics_wide.csv).
- SG&A fell to $10.9B (-8.6% YoY), freeing funds to reinvest in marketing intelligence systems and customer experience initiatives.
