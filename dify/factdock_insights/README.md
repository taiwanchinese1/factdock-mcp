# Factdock Insights for Dify

**Author:** factdock
**Version:** 0.0.1
**Type:** tool
**Source:** https://github.com/taiwanchinese1/factdock-mcp/tree/main/dify/factdock_insights

Factdock Insights collects official and industry news from primary sources in many countries: government and regulator announcements, approvals, safety notices, and company and pipeline news. This plugin returns those items with titles and summaries in the original language or in your language (languages in your contract), plus the original source URL and date for every item.

## Tools

| Tool | What it does |
|---|---|
| Search Insights news | Keyword search, with optional country, category and start date. |
| Latest Insights news | The newest items, with optional country, category and start date. |

Every result includes its source URL. An empty result means "not found or not covered".

## Setup

1. Create a Factdock **Insights** API key on the Factdock for Developers page: https://fact-dock.com/en/product/insights-api/
2. In Dify, install the Factdock Insights plugin, open **Tools > Factdock Insights > API key authorization**, and paste the key.
3. Add the tools to your agent or workflow.

Checking the key only lists the available tools and does not use credits.

## Credentials

- `factdock_api_key` (required): Factdock Insights API key, sent as `Authorization: Bearer <key>` to `https://data.fact-dock.com`.

## Pricing

Each call uses the key holder's Factdock API credits. Prices: https://fact-dock.com/en/product/insights-api/

## Connection requirements

- Outbound HTTPS to `https://data.fact-dock.com`.

## Notes

- Summaries are translated for reading; check the original source before relying on an item.
- Factdock shows published information for reference. It is not legal, medical, veterinary, financial or investment advice and does not replace a professional's judgement.
- For the multilingual search tools (country web search, papers, patents, company reports and more), see the separate Factdock plugin.

## Support

- Website: https://fact-dock.com
- Contact: info@fact-dock.com
- Privacy policy: https://fact-dock.com/en/legal/privacy/
