<div align="center">

<img src="assets/space-shooter.gif" width="100%" alt="A space shooter clearing my contribution graph" />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=800&size=46&duration=1800&pause=99999&color=E6EDF3&center=true&vCenter=true&repeat=false&width=700&height=72&lines=Arya+Prince" />
  <source media="(prefers-color-scheme: light)" srcset="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=800&size=46&duration=1800&pause=99999&color=0D1117&center=true&vCenter=true&repeat=false&width=700&height=72&lines=Arya+Prince" />
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=800&size=46&duration=1800&pause=99999&color=58A6FF&center=true&vCenter=true&repeat=false&width=700&height=72&lines=Arya+Prince" alt="Arya Prince" />
</picture>

**`backends`** · **`on-device ML`** · **`real-time vision`**

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=17&pause=1400&color=58A6FF&center=true&vCenter=true&width=780&height=34&lines=POST+%2Fbookings+returns+409+on+overlap;An+atomic+SET+NX+claims+the+capture+before+the+PSP+call;INT8+quantization%3A+7.07+MB+to+3.69+MB%2C+top-1+parity+held;33+ms%2Fframe+at+1080p%2C+30+fps" />
  <source media="(prefers-color-scheme: light)" srcset="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=17&pause=1400&color=0969DA&center=true&vCenter=true&width=780&height=34&lines=POST+%2Fbookings+returns+409+on+overlap;An+atomic+SET+NX+claims+the+capture+before+the+PSP+call;INT8+quantization%3A+7.07+MB+to+3.69+MB%2C+top-1+parity+held;33+ms%2Fframe+at+1080p%2C+30+fps" />
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=17&pause=1400&color=58A6FF&center=true&vCenter=true&width=780&height=34&lines=POST+%2Fbookings+returns+409+on+overlap;An+atomic+SET+NX+claims+the+capture+before+the+PSP+call;INT8+quantization%3A+7.07+MB+to+3.69+MB%2C+top-1+parity+held;33+ms%2Fframe+at+1080p%2C+30+fps" alt="What I work on" />
</picture>

<!-- Keep each badge row on ONE source line. GFM turns a newline between inline
     elements into a <br>, which stacks the badges vertically. -->
<img src="https://img.shields.io/badge/UC_Berkeley-003262?style=for-the-badge&logoColor=FDB515" alt="UC Berkeley" /> <img src="https://img.shields.io/badge/Data_Science_%2B_CS-1a4d8f?style=for-the-badge" alt="Data Science + CS" /> <img src="https://img.shields.io/badge/Class_of_2028-2563eb?style=for-the-badge" alt="Class of 2028" />

<a href="https://linkedin.com/in/arya-prince"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a> <a href="mailto:aryaprince@berkeley.edu"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" /></a> <img src="https://komarev.com/ghpvc/?username=kingaryaprince&style=for-the-badge&color=2563eb&label=PROFILE+VIEWS" alt="Profile views" />

<br />

<img src="assets/terminal.gif" width="94%" alt="Terminal session: whoami, live GitHub stats, what I am working on" />

</div>

## ~/now

- **CS 61A course staff**, UC Berkeley. 30+ students a week on interpreters, recursion, and environment diagrams.
- **Science and Beyond**, founder. AI and programming workshops for 100+ K-12 students.
- Third year, B.A. Data Science and Computer Science, May 2028. Berkeley, CA.

I mostly write backends and on-device ML, and I care about the parts that only show up when
something breaks: double bookings that return a 409, payment captures that stay single under
concurrency, models small enough to run with the network off.

## ~/recently

- **Parallax Defense** — software engineering intern, summer 2026. Real-time detection and
  tracking against a 33 ms/frame budget at 1080p/30fps. Wrote the detection-head decode and the
  IoU/CIoU/BCE losses in NumPy with 23 unit tests behind them, a socket-level egress guard armed
  before third-party imports that asserts zero non-loopback traffic, SHA-256 weight-integrity
  verification with tamper detection, and track-NMS for duplicate and ghost suppression.
- **Digital-twin sampling research** — CDSS, NIST-funded, spring 2026. Poisson-disk sampling with
  KDTree ball queries over TUM RGB-D scenes, swept across sampling radii and scored on 9 metrics.
  Cuts roughly 90% of point volume while holding coverage at 1.000, and ships an interactive HTML
  report the lab used to pick its operating point.
- **Technovation** — backend engineer on a 4-person team, spring 2026. Details below.

## ~/projects

| | What it is | Worth knowing |
|---|---|---|
| **[Relay](https://github.com/kingaryaprince/relay-travel-agent)** | Voice travel-disruption recovery agent. TypeScript, Next.js App Router, SSE streaming, 12 REST tool endpoints, and 5 role-specialized agent prompts that place outbound supplier calls. | The payment ledger claims each capture with an atomic Redis `SET NX` taken before the PSP call. 18 tests, including 10 concurrent captures that resolve to exactly one winner. Six provider adapters behind one interface plus a mock implementing the same contract, so it runs with no API keys. |
| **[On-Device Vision](https://github.com/kingaryaprince/on-device-vision)** | iOS image classifier. PyTorch MobileNetV2 converted to Core ML, SwiftUI camera app. | INT8 quantization took the model from 7.07 MB to 3.69 MB, a 1.92x cut, with top-1 parity verified. Fully offline, no network calls. |
| **[CropCast](https://github.com/ScienceAndBeyond/CropCast)** | Crop-yield prediction over 734 counties in 11 states, 2010–2024, joining USDA NASS QuickStats, gridMET, MODIS NDVI/EVI, and SoilGrids into 14 features across 6 crops. | Random Forest on an 80:20 temporal split (train 2010–2021, test 2022–2024) so no future year leaks backward. Corn hits test R² 0.764. A four-way ablation puts the mean relative test-R² gain from adding vegetation and soil over a climate-only baseline at 74% across the 6 crops. Presented at AGU 2025. |
| **[Technovation Backend](https://github.com/richahw/technovation-backend)** | FastAPI and PostgreSQL coaching platform built by a team of four. | 13 of the 26 REST endpoints, the 3-table schema, the webhook handlers, and both OAuth2 flows (Cal.com v2 and Google Calendar) with token refresh. `POST /bookings` returns 409 on overlap and degrades gracefully when Cal.com is down. |
| **[Wildfire Detection](https://github.com/kingaryaprince/wildfiredetect)** | Sentinel-2 wildfire detection, benchmarking a CNN, a lightweight CNN variant, and an SVM baseline against each other. | Scored on accuracy, precision, recall, F1, ROC-AUC, and confusion matrix, topping 85% accuracy, with DBSCAN collapsing repeat detections of the same fire. Funded by a $4.3k ESA Network of Resources grant. Presented at AGU 2023 with a TechRxiv preprint. |
| **[Science and Beyond](https://github.com/kingaryaprince/science-and-beyond-website)** | Site for the nonprofit. Next.js App Router with Sanity as a headless CMS. | Studio embedded at `/studio`, Portable Text rendering, and dynamic blog routes off the CMS, so the people writing the content never touch the repo. |
| **[Gradescope → Calendar](https://github.com/kingaryaprince/GradescopeGCALSync)** | Scrapes Gradescope and pushes new assignments into Google Calendar. | Selenium plus OAuth2, retry with backoff, driven from a CLI. Written because I kept missing deadlines. |

## ~/stack

<div align="center">

**Languages**

<img src="https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python" />
<img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" alt="TypeScript" />
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript" />
<img src="https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white" alt="Java" />
<img src="https://img.shields.io/badge/Swift-F54A2A?style=for-the-badge&logo=swift&logoColor=white" alt="Swift" />
<img src="https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logoColor=white" alt="SQL" />

**Backend & Data**

<img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />
<img src="https://img.shields.io/badge/Node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white" alt="Node.js" />
<img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />
<img src="https://img.shields.io/badge/Redis-FF4438?style=for-the-badge&logo=redis&logoColor=white" alt="Redis" />
<img src="https://img.shields.io/badge/OAuth2-EB5424?style=for-the-badge&logo=auth0&logoColor=white" alt="OAuth2" />
<img src="https://img.shields.io/badge/REST_%2B_SSE-02569B?style=for-the-badge&logoColor=white" alt="REST and SSE" />

**Frontend**

<img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" alt="React" />
<img src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white" alt="Next.js" />
<img src="https://img.shields.io/badge/SwiftUI-0071E3?style=for-the-badge&logo=swift&logoColor=white" alt="SwiftUI" />
<img src="https://img.shields.io/badge/Tailwind-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white" alt="Tailwind" />
<img src="https://img.shields.io/badge/Sanity-F03E2F?style=for-the-badge&logo=sanity&logoColor=white" alt="Sanity" />

**ML & Scientific**

<img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" alt="PyTorch" />
<img src="https://img.shields.io/badge/Core_ML-000000?style=for-the-badge&logo=apple&logoColor=white" alt="Core ML" />
<img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" alt="scikit-learn" />
<img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy" />
<img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="pandas" />
<img src="https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white" alt="Keras" />

**Tooling**

<img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git" />
<img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white" alt="GitHub Actions" />
<img src="https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white" alt="pytest" />
<img src="https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white" alt="Selenium" />
<img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" alt="Linux" />

</div>

## ~/elsewhere

Two AGU presentations, a TechRxiv preprint, and an ESA-funded remote sensing project sit behind
the wildfire and CropCast work above. Reach me at
[aryaprince@berkeley.edu](mailto:aryaprince@berkeley.edu).
