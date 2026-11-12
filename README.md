<p align="center"><img src="assets/logo.png" width="96" alt="Factdock logo"></p>

# Factdock MCP server

Factdock is a multilingual search engine for primary sources. It searches the web of the country you choose in that country's own language, and returns the original pages (official sites, academic papers, patent publications, company registries, medicine databases) with translated titles and summaries and their source URLs.

- **Endpoint:** `https://fact-dock.com/mcp` (remote, Streamable HTTP)
- **Sign-in:** OAuth 2.1 (dynamic client registration + PKCE), or a personal API key sent as `Authorization: Bearer fdu_...`
- **Account:** a Factdock account on a paid plan. Paid tools use the account's Factdock credits at the same price as in the Factdock app. The free `get_prices` tool lists current prices, and every result returns `credits_used`.
- **Nothing to install:** this repository only holds connection settings. The server runs at fact-dock.com.

## Tools

| Area | Tools |
|---|---|
| Web search by country or language sphere | `web_search` |
| Academic papers | `academic_search` |
| Patents | `patent_search`, `patent_detail` |
| Companies (registry, sanctions, risk) | `company_identify`, `company_report` |
| Trade compliance (HS codes, tariffs, export controls) | `trade_compliance_check`, `sourcing_search` |
| Economy and finance statistics | `finance_search` |
| Real estate | `realestate_market`, `realestate_registry` |
| Government and infrastructure projects | `gov_infra_search` |
| Contracts | `contract_review`, `contract_bilingual_compare`, `contract_draft_outline`, `contract_draft_generate` |
| Medicine databases | `medical_db_search`, `medical_db_detail` |
| Veterinary references | `vet_drug_risk_check`, `vet_intake_crosscheck`, `clinical_fact_search`, `clinical_hypothesis_search`, `clinical_web_context` |
| Infectious disease map | `epidemic_diseases`, `epidemic_risk` |
| Global Insights news feed | `insights_feed`, `insights_videos` |
| Prices | `get_prices` (free) |
| Receive a result that did not arrive | `get_pending_result` (free) |

The full tool list with descriptions is published at <https://fact-dock.com/.well-known/mcp/server-card.json>.

## Connect

### Claude Code

```bash
claude mcp add --transport http factdock https://fact-dock.com/mcp
```

### VS Code (GitHub Copilot)

`.vscode/mcp.json`:

```json
{
  "servers": {
    "factdock": { "type": "http", "url": "https://fact-dock.com/mcp" }
  }
}
```

### Cursor

`~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "factdock": { "url": "https://fact-dock.com/mcp" }
  }
}
```

### Cline

See [llms-install.md](llms-install.md). Cline settings (`cline_mcp_settings.json`):

```json
{
  "mcpServers": {
    "factdock": {
      "type": "streamableHttp",
      "url": "https://fact-dock.com/mcp",
      "headers": { "Authorization": "Bearer fdu_YOUR_KEY" }
    }
  }
}
```

### Antigravity CLI

```bash
agy plugin install https://github.com/taiwanchinese1/factdock-mcp
```

The plugin asks for `FACTDOCK_API_KEY` (a personal API key from <https://fact-dock.com/api-hub>).

### Gemini CLI

```bash
gemini extensions install https://github.com/taiwanchinese1/factdock-mcp
```

Sign in with your Factdock account when the browser opens.

### goose

Settings → Extensions → Add custom extension → Remote extension (Streamable HTTP), URL `https://fact-dock.com/mcp`.

### Dify

A Dify tool plugin is in [dify/factdock](dify/factdock). It connects to the Factdock Business API (`https://data.fact-dock.com`) with a Business API key and offers country web search, academic, patent, company, trade, infrastructure, finance and Insights tools.

Two more Dify plugins use the product-specific keys:

- [dify/factdock_insights](dify/factdock_insights): Insights news search and latest news, with an Insights API key.
- [dify/factdock_medical](dify/factdock_medical): approved human and veterinary drugs, drug records, FDA adverse event report counts and medical literature, with a Medical DB API key. For professionals; not medical advice.

### Other MCP clients

Any client that supports remote MCP servers over Streamable HTTP can use `https://fact-dock.com/mcp` with OAuth sign-in or a personal API key header.

## Personal API key

Create a key on the API page of your Factdock account: <https://fact-dock.com/api-hub>. The key is shown once. You can set an expiry and revoke it at any time.

## Building Factdock into your own product

The personal MCP server is for your own use and your own organization's internal work. To build Factdock search into a service for your customers, use the Factdock Business API: <https://fact-dock.com/en/product/business-api/>.

## Notes

- Results cover published information only. An empty result means "not found or not covered", not "safe".
- Factdock searches and shows published information for reference. It is not legal, medical, veterinary, financial or investment advice and does not replace a professional's judgement. Decisions should be made with a qualified professional, or by professionals using their own judgement.
- Some tools (veterinary references and medicine databases) require you to accept their terms once in the Factdock app before they can be used through MCP.

## Links

- Website: <https://fact-dock.com>
- Personal API and MCP: <https://fact-dock.com/en/product/personal-api/>
- Terms: <https://fact-dock.com/en/legal/terms/>
- Privacy: <https://fact-dock.com/en/legal/privacy/>
- Contact: info@fact-dock.com

The configuration files in this repository are released under the MIT License. The Factdock service itself is subject to the Factdock terms.
