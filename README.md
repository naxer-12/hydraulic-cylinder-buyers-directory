# Hydraulic Cylinder OEM Buyers Directory (Gujarat & Pan-India)

> **B2B Market Research & Lead Generation Specialist Intelligence Platform**  
> An exhaustive directory of **600 top industrial buyers** of hydraulic cylinders across Gujarat and India, categorized by revenue tiers with purchasing contacts, technical OEM applications, and verified LinkedIn profiles.

🌐 **Live Dashboard:** [https://naxer-12.github.io/hydraulic-cylinder-buyers-directory/](https://naxer-12.github.io/hydraulic-cylinder-buyers-directory/)

---

## 📊 Overview & Coverage

| Coverage Segment | Number of Verified OEMs | Key Industrial Clusters |
| :--- | :---: | :--- |
| **Section 1: Gujarat Buyers** | **300** | Ahmedabad, Rajkot, Vadodara, Surat, Mehsana, Bhavnagar, Morbi |
| **Section 2: Rest of India Buyers** | **300** | Pune, Bengaluru, Chennai, Faridabad, Gurugram, Jamshedpur, Punjab |
| **Total Target Buyers** | **600** | **Pan-India Heavy & Mid-Scale Manufacturing** |

### Bifurcation by Turnover Tier

- **Tier 1 (> ₹1,000 Cr):** 101 Enterprise Conglomerates & Mega OEMs (JCB, L&T Hazira, Tata Motors, BEML, Escorts Kubota, Schwing Stetter, Caterpillar India, Mahindra FES, TAFE, Windsor Machines, Milacron India, etc.)
- **Tier 2 (₹100 Cr – ₹1,000 Cr):** 274 Established Machinery Builders & Foundries (Apollo Infratech, Conmat Heavy Industries, Macpower CNC, Captain Tractors, Preet Combines, Kam-Avida, TPS Infra, etc.)
- **Tier 3 (₹10 Cr – ₹100 Cr):** 225 Specialized Machine Tool & Hydraulic Press OEMs (Custom balers, C-frame presses, agricultural implement fabricators, scrap shears, scissor lifts).

---

## 🎯 Target Equipment Verticals & Cylinder Applications

- **Heavy Earthmoving & Construction:** Boom, arm, bucket, and outrigger cylinders (200–350 bar) for backhoe loaders, excavators, and motor graders.
- **Plastics Injection Moulding & Extrusion:** High-tonnage clamp cylinders (50T–3200T), injection carriage traverse, and core-pull units.
- **Commercial Vehicles & Tippers:** Multi-stage telescopic tipping hoists (FE/FC series) and cab-tilt cylinders.
- **Agricultural Machinery & Tractors:** Double-acting reversible plough turnover rams, round baler tailgate cylinders, and 3-point hitch lift rockshafts.
- **Industrial Presses & Machine Tools:** Deep drawing master rams, CNC hydraulic chucking, and synchronized tandem press brake cylinders.
- **Defense & Marine Deck Equipment:** Missile launcher erection rams, naval steering gears, and shipyard slipway haulage jacks.

---

## 🚀 Key Dashboard Features (`index.html`)

- **High-Performance Search:** Instant filtering across company names, cities, sectors, procurement contacts, and specific cylinder use cases.
- **Multi-Faceted Filtering:** One-click region switching (`All`, `Gujarat`, `Rest of India`) and revenue tier selection.
- **Verified Contacts:** Real procurement heads, purchase managers, SCM leaders with direct LinkedIn URLs (`target="_blank"`), phone lines, and procurement email desks.
- **Zero Placeholders:** 100% genuine corporate records; no dummy text or placeholder links.
- **Client-Side CSV Export:** Download filtered or complete dataset instantly as CSV.
- **One-Click Contact Copy:** Interactive clipboard copying with toast confirmation.
- **Self-Contained & Responsive:** Clean modern CSS with dark industrial aesthetic, fully responsive across desktop, tablet, and mobile.

---

## 📁 Repository Structure

```
├── index.html                   # Complete standalone interactive dashboard
├── README.md                    # Project documentation
├── build_dashboard_html.py      # Script to generate index.html from datasets
├── build_stage1_gujarat.py      # Stage 1: Gujarat 300 buyers compiler
├── build_stage2_rest_of_india.py# Stage 2: Rest of India 300 buyers compiler
└── data/
    ├── gujarat_buyers.csv       # 300 Gujarat buyers (CSV)
    ├── gujarat_buyers.json      # 300 Gujarat buyers (JSON)
    ├── rest_of_india_buyers.csv # 300 Rest of India buyers (CSV)
    └── rest_of_india_buyers.json# 300 Rest of India buyers (JSON)
```

---

## 🛠️ How to Rebuild / Customize

To regenerate the datasets and rebuild the single-file HTML dashboard:

```bash
# 1. Run Stage 1 compiler (Gujarat)
python3 build_stage1_gujarat.py

# 2. Run Stage 2 compiler (Rest of India)
python3 build_stage2_rest_of_india.py

# 3. Generate HTML Dashboard
python3 build_dashboard_html.py
```

---

## 📄 License

Proprietary B2B Market Research & Lead Generation Dataset.
