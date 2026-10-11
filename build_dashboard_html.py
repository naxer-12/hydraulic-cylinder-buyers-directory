"""
HTML Dashboard Generator for Hydraulic Cylinder B2B Market Research
Generates a standalone, self-contained, high-performance, single-file HTML page.
Contains all 600 verified buyers (300 Gujarat + 300 Rest of India),
interactive filters, search, tier grouping, metrics cards, and CSV export.
"""

import json
import os
import html

def generate_html():
    with open("data/gujarat_buyers.json", "r", encoding="utf-8") as f:
        gujarat_data = json.load(f)
        
    with open("data/rest_of_india_buyers.json", "r", encoding="utf-8") as f:
        roi_data = json.load(f)

    # Tag region
    for d in gujarat_data:
        d["region"] = "Gujarat"
    for d in roi_data:
        d["region"] = "Rest of India"

    all_data = gujarat_data + roi_data

    # Calculate metrics
    total_count = len(all_data)
    gujarat_count = len(gujarat_data)
    roi_count = len(roi_data)
    t1_count = sum(1 for d in all_data if "Tier 1" in d["tier"])
    t2_count = sum(1 for d in all_data if "Tier 2" in d["tier"])
    t3_count = sum(1 for d in all_data if "Tier 3" in d["tier"])

    json_blob = json.dumps(all_data, ensure_ascii=False)

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hydraulic Cylinder OEM Buyers Directory - Gujarat & India (600 Targets)</title>
  <style>
    :root {{
      --bg-primary: #0f172a;
      --bg-secondary: #1e293b;
      --bg-tertiary: #334155;
      --surface: #1e293b;
      --surface-hover: #273549;
      --border: #334155;
      --border-focus: #3b82f6;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      --accent-blue: #3b82f6;
      --accent-blue-light: #60a5fa;
      --accent-cyan: #06b6d4;
      --badge-t1-bg: #451a03;
      --badge-t1-border: #b45309;
      --badge-t1-text: #fcd34d;
      --badge-t2-bg: #1e1b4b;
      --badge-t2-border: #4338ca;
      --badge-t2-text: #a5b4fc;
      --badge-t3-bg: #064e3b;
      --badge-t3-border: #047857;
      --badge-t3-text: #6ee7b7;
      --tag-bg: #0f172a;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      background-color: var(--bg-primary);
      color: var(--text-main);
      line-height: 1.5;
      padding-bottom: 60px;
    }}

    a {{
      color: var(--accent-blue-light);
      text-decoration: none;
      transition: color 0.15s ease;
    }}
    a:hover {{
      color: #93c5fd;
      text-decoration: underline;
    }}

    .container {{
      max-width: 1680px;
      margin: 0 auto;
      padding: 0 24px;
    }}

    /* Header */
    header {{
      background: linear-gradient(180deg, #1e293b 0%, #0f172a 100%);
      border-bottom: 1px solid var(--border);
      padding: 32px 0 24px 0;
      position: sticky;
      top: 0;
      z-index: 100;
      backdrop-filter: blur(12px);
    }}

    .header-top {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      flex-wrap: wrap;
      gap: 16px;
      margin-bottom: 24px;
    }}

    .header-title h1 {{
      font-size: 26px;
      font-weight: 700;
      letter-spacing: -0.02em;
      color: #ffffff;
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .header-title h1 span.pill {{
      font-size: 13px;
      background: #2563eb;
      color: #ffffff;
      padding: 3px 10px;
      border-radius: 9999px;
      font-weight: 600;
      letter-spacing: 0;
    }}

    .header-title p {{
      font-size: 14px;
      color: var(--text-muted);
      margin-top: 4px;
    }}

    .header-actions {{
      display: flex;
      gap: 12px;
      align-items: center;
    }}

    .btn {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 9px 16px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      border: 1px solid var(--border);
      background: var(--bg-secondary);
      color: var(--text-main);
      transition: all 0.15s ease;
    }}
    .btn:hover {{
      background: var(--surface-hover);
      border-color: #475569;
    }}
    .btn-primary {{
      background: #2563eb;
      border-color: #3b82f6;
      color: #ffffff;
    }}
    .btn-primary:hover {{
      background: #1d4ed8;
      border-color: #60a5fa;
    }}

    /* Metrics Bar */
    .metrics-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
      gap: 14px;
      margin-bottom: 24px;
    }}

    .metric-card {{
      background: var(--bg-secondary);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 16px 18px;
      display: flex;
      flex-direction: column;
      gap: 4px;
      position: relative;
      overflow: hidden;
    }}
    .metric-card::before {{
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      width: 4px;
      height: 100%;
      background: var(--accent-blue);
    }}
    .metric-card.t1::before {{ background: #f59e0b; }}
    .metric-card.t2::before {{ background: #818cf8; }}
    .metric-card.t3::before {{ background: #10b981; }}
    .metric-card.guj::before {{ background: #06b6d4; }}
    .metric-card.roi::before {{ background: #ec4899; }}

    .metric-label {{
      font-size: 12px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-muted);
    }}
    .metric-val {{
      font-size: 26px;
      font-weight: 700;
      color: #ffffff;
    }}
    .metric-sub {{
      font-size: 12px;
      color: var(--text-dim);
    }}

    /* Filter Toolbar */
    .controls-panel {{
      background: var(--bg-secondary);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 18px;
      margin-bottom: 24px;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}

    .search-row {{
      display: flex;
      gap: 12px;
      flex-wrap: wrap;
    }}

    .search-input-wrapper {{
      flex: 1;
      min-width: 280px;
      position: relative;
    }}

    .search-input {{
      width: 100%;
      background: #0f172a;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 11px 16px 11px 40px;
      font-size: 14px;
      color: var(--text-main);
      outline: none;
      transition: border-color 0.15s ease;
    }}
    .search-input:focus {{
      border-color: var(--border-focus);
      box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.2);
    }}
    .search-icon {{
      position: absolute;
      left: 14px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-dim);
      pointer-events: none;
    }}

    .filter-groups {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 16px;
    }}

    .filter-label {{
      font-size: 13px;
      font-weight: 600;
      color: var(--text-muted);
    }}

    .tab-pills {{
      display: inline-flex;
      background: #0f172a;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 3px;
      gap: 3px;
    }}

    .tab-pill {{
      padding: 6px 14px;
      font-size: 13px;
      font-weight: 600;
      border-radius: 6px;
      cursor: pointer;
      color: var(--text-muted);
      border: none;
      background: transparent;
      transition: all 0.15s ease;
    }}
    .tab-pill:hover {{
      color: #ffffff;
    }}
    .tab-pill.active {{
      background: #2563eb;
      color: #ffffff;
    }}

    .filter-chips {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }}

    .filter-chip {{
      padding: 5px 12px;
      font-size: 12px;
      font-weight: 600;
      border-radius: 9999px;
      border: 1px solid var(--border);
      background: #0f172a;
      color: var(--text-muted);
      cursor: pointer;
      transition: all 0.15s ease;
    }}
    .filter-chip:hover {{
      border-color: #475569;
      color: #ffffff;
    }}
    .filter-chip.active {{
      background: #1e293b;
      border-color: var(--border-focus);
      color: var(--accent-blue-light);
    }}

    /* Section Headers */
    .section-title-wrap {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin: 32px 0 16px 0;
      padding-bottom: 10px;
      border-bottom: 2px solid var(--border);
    }}
    .section-title {{
      font-size: 20px;
      font-weight: 700;
      color: #ffffff;
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .section-badge {{
      font-size: 12px;
      background: var(--bg-tertiary);
      color: var(--text-main);
      padding: 2px 10px;
      border-radius: 9999px;
      font-weight: 600;
    }}

    /* Table Design */
    .table-container {{
      background: var(--bg-secondary);
      border: 1px solid var(--border);
      border-radius: 12px;
      overflow-x: auto;
      margin-bottom: 32px;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
    }}

    table {{
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 13.5px;
      min-width: 1300px;
    }}

    thead {{
      background: #162032;
      border-bottom: 1px solid var(--border);
      position: sticky;
      top: 0;
      z-index: 10;
    }}

    th {{
      padding: 14px 16px;
      font-weight: 600;
      color: #94a3b8;
      text-transform: uppercase;
      font-size: 11.5px;
      letter-spacing: 0.05em;
      white-space: nowrap;
    }}

    tbody tr {{
      border-bottom: 1px solid #233146;
      transition: background-color 0.12s ease;
    }}
    tbody tr:hover {{
      background-color: var(--surface-hover);
    }}

    td {{
      padding: 16px;
      vertical-align: top;
      color: #cbd5e1;
    }}

    td.company-cell {{
      font-weight: 700;
      color: #ffffff;
      min-width: 220px;
    }}
    .company-location {{
      font-weight: 400;
      font-size: 12px;
      color: var(--text-dim);
      margin-top: 4px;
      display: flex;
      align-items: center;
      gap: 4px;
    }}

    /* Badges */
    .tier-badge {{
      display: inline-block;
      padding: 3px 9px;
      border-radius: 6px;
      font-size: 11.5px;
      font-weight: 700;
      letter-spacing: 0.02em;
      white-space: nowrap;
    }}
    .tier-1 {{
      background: var(--badge-t1-bg);
      border: 1px solid var(--badge-t1-border);
      color: var(--badge-t1-text);
    }}
    .tier-2 {{
      background: var(--badge-t2-bg);
      border: 1px solid var(--badge-t2-border);
      color: var(--badge-t2-text);
    }}
    .tier-3 {{
      background: var(--badge-t3-bg);
      border: 1px solid var(--badge-t3-border);
      color: var(--badge-t3-text);
    }}

    .turnover-val {{
      font-size: 11.5px;
      color: var(--text-muted);
      margin-top: 4px;
      font-weight: 500;
    }}

    .sector-tag {{
      display: inline-block;
      background: #111c2e;
      border: 1px solid #2a3a52;
      color: #93c5fd;
      padding: 2px 8px;
      border-radius: 4px;
      font-size: 11.5px;
      font-weight: 500;
      margin-bottom: 4px;
    }}

    .use-case-text {{
      font-size: 12.5px;
      color: #e2e8f0;
      line-height: 1.45;
      max-width: 380px;
    }}

    .contact-name {{
      font-weight: 600;
      color: #ffffff;
      font-size: 13.5px;
    }}
    .contact-desig {{
      font-size: 12px;
      color: var(--text-muted);
      margin-top: 2px;
    }}

    .linkedin-link {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: #0a66c2;
      color: #ffffff !important;
      padding: 4px 10px;
      border-radius: 6px;
      font-size: 11.5px;
      font-weight: 600;
      margin-top: 6px;
      text-decoration: none !important;
      transition: background 0.15s ease;
    }}
    .linkedin-link:hover {{
      background: #004182;
    }}

    .contact-channels {{
      font-size: 12px;
      color: #cbd5e1;
      display: flex;
      flex-direction: column;
      gap: 4px;
      min-width: 220px;
    }}

    .channel-item {{
      display: flex;
      align-items: flex-start;
      gap: 6px;
      word-break: break-all;
    }}

    .copy-btn {{
      background: transparent;
      border: none;
      color: var(--text-dim);
      cursor: pointer;
      padding: 2px;
      border-radius: 4px;
      transition: color 0.15s ease;
    }}
    .copy-btn:hover {{
      color: #ffffff;
    }}

    /* Empty state */
    .empty-state {{
      text-align: center;
      padding: 60px 20px;
      color: var(--text-muted);
    }}
    .empty-state h3 {{
      font-size: 18px;
      color: #ffffff;
      margin-bottom: 8px;
    }}

    /* Toast */
    #toast {{
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: #10b981;
      color: #ffffff;
      padding: 10px 18px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 600;
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.4);
      display: none;
      z-index: 1000;
    }}

    /* Footer */
    footer {{
      margin-top: 48px;
      border-top: 1px solid var(--border);
      padding-top: 24px;
      text-align: center;
      font-size: 13px;
      color: var(--text-dim);
    }}

    @media (max-width: 768px) {{
      .header-title h1 {{ font-size: 20px; }}
      .metrics-grid {{ grid-template-columns: 1fr 1fr; }}
      .controls-panel {{ padding: 14px; }}
    }}
  </style>
</head>
<body>

  <header>
    <div class="container">
      <div class="header-top">
        <div class="header-title">
          <h1>
            Hydraulic Cylinder OEM Buyers Directory
            <span class="pill">600 Verified OEMs</span>
          </h1>
          <p>B2B Market Research & Lead Generation Specialist Intelligence: Gujarat & Pan-India</p>
        </div>
        <div class="header-actions">
          <button class="btn" onclick="exportFilteredCSV()">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
            Export to CSV
          </button>
          <button class="btn btn-primary" onclick="resetFilters()">Reset Filters</button>
        </div>
      </div>

      <!-- Metrics Row -->
      <div class="metrics-grid">
        <div class="metric-card">
          <span class="metric-label">Total Verified Targets</span>
          <span class="metric-val">{total_count}</span>
          <span class="metric-sub">Active industrial OEM buyers</span>
        </div>
        <div class="metric-card guj">
          <span class="metric-label">Section 1: Gujarat</span>
          <span class="metric-val">{gujarat_count}</span>
          <span class="metric-sub">Ahmedabad, Rajkot, Vadodara, Surat</span>
        </div>
        <div class="metric-card roi">
          <span class="metric-label">Section 2: Rest of India</span>
          <span class="metric-val">{roi_count}</span>
          <span class="metric-sub">Pune, Chennai, NCR, Bengaluru, PB</span>
        </div>
        <div class="metric-card t1">
          <span class="metric-label">Tier 1 (> ₹1,000 Cr)</span>
          <span class="metric-val">{t1_count}</span>
          <span class="metric-sub">Heavy OEMs & Conglomerates</span>
        </div>
        <div class="metric-card t2">
          <span class="metric-label">Tier 2 (₹100 Cr – ₹1k Cr)</span>
          <span class="metric-val">{t2_count}</span>
          <span class="metric-sub">Established machinery builders</span>
        </div>
        <div class="metric-card t3">
          <span class="metric-label">Tier 3 (₹10 Cr – ₹100 Cr)</span>
          <span class="metric-val">{t3_count}</span>
          <span class="metric-sub">Specialized press/SPM builders</span>
        </div>
      </div>
    </div>
  </header>

  <main class="container" style="margin-top: 24px;">

    <!-- Controls Panel -->
    <div class="controls-panel">
      <div class="search-row">
        <div class="search-input-wrapper">
          <svg class="search-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
          <input type="text" id="searchInput" class="search-input" placeholder="Search by company, city, state, sector, procurement contact, or cylinder use case..." oninput="handleSearch()">
        </div>
      </div>

      <div class="filter-groups">
        <div style="display: flex; align-items: center; gap: 8px;">
          <span class="filter-label">Region:</span>
          <div class="tab-pills">
            <button class="tab-pill active" data-region="All" onclick="setRegionFilter('All')">All India (600)</button>
            <button class="tab-pill" data-region="Gujarat" onclick="setRegionFilter('Gujarat')">Gujarat (300)</button>
            <button class="tab-pill" data-region="Rest of India" onclick="setRegionFilter('Rest of India')">Rest of India (300)</button>
          </div>
        </div>

        <div style="display: flex; align-items: center; gap: 8px;">
          <span class="filter-label">Revenue Tier:</span>
          <div class="filter-chips">
            <button class="filter-chip active" data-tier="All" onclick="setTierFilter('All')">All Tiers</button>
            <button class="filter-chip" data-tier="Tier 1" onclick="setTierFilter('Tier 1')">Tier 1 (> ₹1,000 Cr)</button>
            <button class="filter-chip" data-tier="Tier 2" onclick="setTierFilter('Tier 2')">Tier 2 (₹100 Cr – ₹1k Cr)</button>
            <button class="filter-chip" data-tier="Tier 3" onclick="setTierFilter('Tier 3')">Tier 3 (₹10 Cr – ₹100 Cr)</button>
          </div>
        </div>
      </div>
    </div>

    <!-- Active Result Count -->
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px; font-size: 13px; color: var(--text-muted);">
      <span id="resultsCount">Showing 600 companies</span>
      <span style="font-size: 12px; color: var(--text-dim);">Live Database • Updated October 2026</span>
    </div>

    <!-- Section 1: Gujarat -->
    <div id="gujaratSection">
      <div class="section-title-wrap">
        <h2 class="section-title">
          Section 1: Gujarat Industrial Buyers (OEMs & Machine Builders)
          <span class="section-badge" id="gujaratBadge">300 Target Companies</span>
        </h2>
      </div>

      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Company & Hub</th>
              <th>Revenue Tier</th>
              <th>Sector & Primary Machinery</th>
              <th>Primary Hydraulic Cylinder Application</th>
              <th>Procurement Lead</th>
              <th>LinkedIn & Official Channels</th>
            </tr>
          </thead>
          <tbody id="gujaratTableBody">
            <!-- Populated via JS -->
          </tbody>
        </table>
      </div>
    </div>

    <!-- Section 2: Rest of India -->
    <div id="roiSection">
      <div class="section-title-wrap">
        <h2 class="section-title">
          Section 2: Rest of India Major Buyers (OEMs & Machinery Giants)
          <span class="section-badge" id="roiBadge">300 Target Companies</span>
        </h2>
      </div>

      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Company & Hub</th>
              <th>Revenue Tier</th>
              <th>Sector & Primary Machinery</th>
              <th>Primary Hydraulic Cylinder Application</th>
              <th>Procurement Lead</th>
              <th>LinkedIn & Official Channels</th>
            </tr>
          </thead>
          <tbody id="roiTableBody">
            <!-- Populated via JS -->
          </tbody>
        </table>
      </div>
    </div>

    <div id="noResults" class="empty-state" style="display: none;">
      <h3>No matching buyers found</h3>
      <p>Try clearing your search query or switching region/tier filters.</p>
    </div>

  </main>

  <footer>
    <div class="container">
      <p>B2B Market Research & Sourcing Intelligence Platform • Indian Industrial & Manufacturing Sector • 600 Target OEMs</p>
    </div>
  </footer>

  <div id="toast">Copied to clipboard!</div>

  <script>
    const database = {json_blob};

    let activeRegion = "All";
    let activeTier = "All";
    let searchQuery = "";

    function init() {{
      render();
    }}

    function setRegionFilter(region) {{
      activeRegion = region;
      document.querySelectorAll(".tab-pill").forEach(el => {{
        el.classList.toggle("active", el.dataset.region === region);
      }});
      render();
    }}

    function setTierFilter(tier) {{
      activeTier = tier;
      document.querySelectorAll(".filter-chip").forEach(el => {{
        el.classList.toggle("active", el.dataset.tier === tier);
      }});
      render();
    }}

    function handleSearch() {{
      searchQuery = document.getElementById("searchInput").value.trim().toLowerCase();
      render();
    }}

    function resetFilters() {{
      activeRegion = "All";
      activeTier = "All";
      searchQuery = "";
      document.getElementById("searchInput").value = "";
      document.querySelectorAll(".tab-pill").forEach(el => el.classList.toggle("active", el.dataset.region === "All"));
      document.querySelectorAll(".filter-chip").forEach(el => el.classList.toggle("active", el.dataset.tier === "All"));
      render();
    }}

    function filterData(list) {{
      return list.filter(item => {{
        // Region filter
        if (activeRegion !== "All" && item.region !== activeRegion) {{
          return false;
        }}
        // Tier filter
        if (activeTier !== "All" && !item.tier.includes(activeTier)) {{
          return false;
        }}
        // Search query
        if (searchQuery) {{
          const haystack = (
            item.name + " " +
            item.city + " " +
            item.sector + " " +
            item.use_case + " " +
            item.lead_name + " " +
            item.designation + " " +
            item.contact
          ).toLowerCase();
          if (!haystack.includes(searchQuery)) return false;
        }}
        return true;
      }});
    }}

    function renderRow(item) {{
      let tierClass = "tier-3";
      if (item.tier.includes("Tier 1")) tierClass = "tier-1";
      else if (item.tier.includes("Tier 2")) tierClass = "tier-2";

      return `
        <tr>
          <td class="company-cell">
            <div>${{item.name}}</div>
            <div class="company-location">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
              ${{item.city}}
            </div>
          </td>
          <td>
            <span class="tier-badge ${{tierClass}}">${{item.tier}}</span>
            <div class="turnover-val">${{item.turnover}}</div>
          </td>
          <td>
            <div class="sector-tag">${{item.sector}}</div>
          </td>
          <td>
            <div class="use-case-text">${{item.use_case}}</div>
          </td>
          <td>
            <div class="contact-name">${{item.lead_name}}</div>
            <div class="contact-desig">${{item.designation}}</div>
          </td>
          <td>
            <div class="contact-channels">
              <div class="channel-item">
                <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="margin-top:2px; flex-shrink:0;"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
                <span>${{item.contact}}</span>
                <button class="copy-btn" title="Copy Contact" onclick="copyText('${{item.contact.replace(/'/g, "\\\\\\'")}}')">
                  <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
                </button>
              </div>
              <a href="${{item.linkedin}}" target="_blank" rel="noopener noreferrer" class="linkedin-link">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
                LinkedIn Profile
              </a>
            </div>
          </td>
        </tr>
      `;
    }}

    function render() {{
      const filtered = filterData(database);

      const gujaratFiltered = filtered.filter(d => d.region === "Gujarat");
      const roiFiltered = filtered.filter(d => d.region === "Rest of India");

      document.getElementById("resultsCount").textContent = `Showing ${{filtered.length}} of ${{database.length}} buyers`;

      const gujSection = document.getElementById("gujaratSection");
      const roiSection = document.getElementById("roiSection");
      const noResults = document.getElementById("noResults");

      if (filtered.length === 0) {{
        gujSection.style.display = "none";
        roiSection.style.display = "none";
        noResults.style.display = "block";
        return;
      }} else {{
        noResults.style.display = "none";
      }}

      // Gujarat table
      if (gujaratFiltered.length > 0 && (activeRegion === "All" || activeRegion === "Gujarat")) {{
        gujSection.style.display = "block";
        document.getElementById("gujaratBadge").textContent = `${{gujaratFiltered.length}} Companies`;
        document.getElementById("gujaratTableBody").innerHTML = gujaratFiltered.map(renderRow).join("");
      }} else {{
        gujSection.style.display = "none";
      }}

      // Rest of India table
      if (roiFiltered.length > 0 && (activeRegion === "All" || activeRegion === "Rest of India")) {{
        roiSection.style.display = "block";
        document.getElementById("roiBadge").textContent = `${{roiFiltered.length}} Companies`;
        document.getElementById("roiTableBody").innerHTML = roiFiltered.map(renderRow).join("");
      }} else {{
        roiSection.style.display = "none";
      }}
    }}

    function copyText(text) {{
      navigator.clipboard.writeText(text).then(() => {{
        const toast = document.getElementById("toast");
        toast.textContent = "Copied to clipboard!";
        toast.style.display = "block";
        setTimeout(() => {{ toast.style.display = "none"; }}, 2000);
      }}).catch(err => {{
        console.error("Copy failed", err);
      }});
    }}

    function exportFilteredCSV() {{
      const filtered = filterData(database);
      if (filtered.length === 0) {{
        alert("No companies match your current filters.");
        return;
      }}

      const headers = [
        "Company Name",
        "Region",
        "City",
        "Turnover Tier",
        "Estimated Turnover",
        "Industry Sector",
        "Primary Hydraulic Cylinder Application",
        "Decision Maker Name",
        "Designation",
        "LinkedIn Profile",
        "Contact Phone / Email"
      ];

      const rows = filtered.map(d => [
        `"${{d.name.replace(/"/g, '""')}}"`,
        `"${{d.region}}"`,
        `"${{d.city.replace(/"/g, '""')}}"`,
        `"${{d.tier.replace(/"/g, '""')}}"`,
        `"${{d.turnover.replace(/"/g, '""')}}"`,
        `"${{d.sector.replace(/"/g, '""')}}"`,
        `"${{d.use_case.replace(/"/g, '""')}}"`,
        `"${{d.lead_name.replace(/"/g, '""')}}"`,
        `"${{d.designation.replace(/"/g, '""')}}"`,
        `"${{d.linkedin.replace(/"/g, '""')}}"`,
        `"${{d.contact.replace(/"/g, '""')}}"`
      ]);

      const csvContent = "data:text/csv;charset=utf-8," + [headers.join(","), ...rows.map(e => e.join(","))].join("\\n");
      const encodedUri = encodeURI(csvContent);
      const link = document.createElement("a");
      link.setAttribute("href", encodedUri);
      link.setAttribute("download", `Hydraulic_Cylinder_Buyers_${{activeRegion.replace(/\\s+/g, '_')}}_${{new Date().toISOString().split('T')[0]}}.csv`);
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }}

    window.onload = init;
  </script>
</body>
</html>
"""

    output_path = "/Users/jainamshah/hydraulic_cylinder/index.html"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    root_output_path = "/Users/jainamshah/hydraulic_cylinder_buyers_directory.html"
    with open(root_output_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Generated HTML dashboard at: {output_path}")
    print(f"Generated root HTML dashboard at: {root_output_path}")
    print(f"File size: {os.path.getsize(output_path)} bytes")

if __name__ == "__main__":
    generate_html()
