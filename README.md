## Arya Prince

Data Science and Computer Science at UC Berkeley, B.A. May 2028. I mostly write backends
and on-device ML, and I care about the parts that only show up when something breaks:
double bookings that return a 409, payment captures that stay single under concurrency,
models small enough to run with the network off.

Berkeley, CA · [LinkedIn](https://linkedin.com/in/arya-prince) · aryaprince@berkeley.edu

### Right now

- **Parallax Defense**, software engineering intern. Real-time detection and tracking on a
  33 ms/frame budget at 1080p/30fps. Wrote the detection-head decode and the IoU/CIoU/BCE
  losses in NumPy, then 19 pytest tests that brought the suite to 96 passing.
- **Digital-twin sampling research** (CDSS, NIST-funded). Poisson-disk sampling with KDTree
  ball queries over TUM RGB-D scenes, swept across sampling radii. Cuts roughly 90% of the
  point volume while holding coverage at 1.000, and ships an interactive HTML report the lab
  used to pick its operating point.
- **CS 61A course staff**, 30+ students a week on interpreters, recursion, and environment
  diagrams.
- **Science and Beyond**, founder. AI and programming workshops for 100+ K-12 students.

### Projects

| | What it is | Worth knowing |
|---|---|---|
| **[Relay](https://github.com/kingaryaprince/relay-travel-agent)** | Travel-disruption recovery agent. TypeScript, Next.js App Router, SSE streaming, 12 REST tool endpoints. | Payment ledger claims each capture with an atomic Redis `SET NX` before the PSP call. 18 tests, including 10 concurrent captures that resolve to exactly one winner. Swappable adapters, so it runs on mocks with no API keys. |
| **[On-Device Vision](https://github.com/kingaryaprince/on-device-vision)** | iOS image classifier. PyTorch MobileNetV2 converted to Core ML, SwiftUI camera app. | INT8 quantization took the model from 7.07 MB to 3.69 MB, a 1.92x cut, with top-1 parity verified. Fully offline, no network calls. |
| **[CropCast](https://github.com/ScienceAndBeyond/CropCast)** | Crop-yield prediction over 734 U.S. counties and 15 years, joining 20K+ records from NOAA, MODIS, and USDA NASS. | Random Forest at R² 0.76, a 74% improvement over baseline. Presented at AGU 2025. |
| **[Technovation Backend](https://github.com/richahw/technovation-backend)** | FastAPI and PostgreSQL coaching platform built by a team of four. | 13 of the 26 REST endpoints, the 3-table schema, and both OAuth2 flows (Cal.com v2 and Google Calendar) with token refresh. `POST /bookings` returns 409 on overlap and degrades gracefully when Cal.com is down. |
| **[Gradescope → Calendar Sync](https://github.com/kingaryaprince/GradescopeGCALSync)** | Scrapes Gradescope and pushes new assignments into Google Calendar. | Selenium plus OAuth2, retry with backoff, packaged as a Dockerized CLI. |
| **[Wildfire Detection](https://github.com/kingaryaprince/wildfiredetect)** | CNN over Sentinel-2 imagery, 85%+ accuracy, DBSCAN to collapse repeat detections of the same fire. | Funded by a $4.3k ESA Network of Resources grant. Presented at AGU 2023 with a TechRxiv preprint. |

### Stack

**Languages** Python · TypeScript / JavaScript · Java · Swift · SQL  
**Backend** FastAPI · Node · REST · OAuth2 · SSE · PostgreSQL · Redis  
**Frontend** React · Next.js  
**ML** PyTorch · Core ML · scikit-learn · NumPy · pandas · Keras  
**Tooling** Git · Docker · GitHub Actions · pytest · Linux

### Elsewhere

Two AGU presentations, a TechRxiv preprint, and an ESA-funded remote sensing project sit
behind the wildfire and CropCast work above. Reach me at aryaprince@berkeley.edu.
