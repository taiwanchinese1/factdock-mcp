# Factdock for Dify

**Author:** factdock
**Version:** 0.0.1
**Type:** tool
**Source:** https://github.com/taiwanchinese1/factdock-mcp/tree/main/dify/factdock

Factdock is a multilingual search engine for primary sources. It searches each country's official sites, academic papers, patents, company and trade information in that country's own language, and returns the original sources with URLs, dates and translated titles and summaries.

## Tools

| Tool | What it does |
|---|---|
| Country web search | Searches one country (in its own language) or one language sphere. Choose official, commercial, local-voice or academic sources. |
| Academic paper search | Scholarly databases ranked by evidence tier, top results translated. |
| Patent search | One patent office, or the 5 major offices (US, JP, CN, KR, EP) together. |
| Company risk report | Due-diligence report with basic facts, legal, misconduct and reputation, sources and a risk level. |
| Trade and compliance check | Import rules (tariffs, documents, certifications) for a product, or sanctions screening of a company. |
| Government and infrastructure projects | Public plans, tenders and projects by country and sector. |
| Country finance indicators | Official macro and market indicators for up to 3 countries. |
| Insights news search | Official and industry news from primary sources. |

Every result includes its source URL. An empty result means "not found or not covered", not "safe".

## Setup

1. Create a Factdock Business API key on the Factdock for Developers page: https://fact-dock.com/en/product/business-api/
   - The search tools need a **Platform** key. An **Insights** key works with Insights news search.
2. In Dify, install the Factdock plugin, open **Tools 竊・Factdock 竊・Authorize**, and paste the key.
3. Add the tools to your agent or workflow.

Checking the key only lists the available tools and does not use credits.

## Credentials

- `factdock_api_key` (required): Factdock Business API key, sent as `Authorization: Bearer <key>` to `https://data.fact-dock.com`.

## Pricing

Each search uses the key holder's Factdock API credits at the business price. Every result includes `credits_used`. Prices: https://fact-dock.com/en/product/business-api/

## Connection requirements

- Outbound HTTPS to `https://data.fact-dock.com`.
- Some searches (country web search, patents, company reports) can take up to about three minutes.

## Notes

- For country, patent-office and company tools, choose the country yourself; the agent should not guess it.
- Factdock searches and shows published information for reference. It is not legal, medical, veterinary, financial or investment advice and does not replace a professional's judgement.

## Support

- Website: https://fact-dock.com
- Contact: info@fact-dock.com
- Privacy policy: https://fact-dock.com/en/legal/privacy/
