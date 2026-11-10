# Factdock Medical DB for Dify

**Author:** factdock
**Version:** 0.0.1
**Type:** tool
**Source:** https://github.com/taiwanchinese1/factdock-mcp/tree/main/dify/factdock_medical

Factdock Medical DB gives agents and workflows access to official medicine databases for human and veterinary drugs: approved products and labels from national authorities, adverse-event report counts from public U.S. FDA systems, and published medical and veterinary literature. Every result is the original record with its source URL.

## Tools

| Tool | What it does |
|---|---|
| Search approved drugs | Find human or veterinary drugs by product name, generic name or active ingredient, in any language. |
| Get drug record | The full official record for one drug (label sections, ingredients, authority, source URL). |
| Adverse event report counts | Reaction terms and report counts for an active ingredient from FDA FAERS (human) and FDA CVM (veterinary). |
| Search medical literature | Published medical and veterinary papers with journal, year and links. |

An empty result means "not found or not covered", not "safe". Adverse event report counts do not show that a drug caused an event.

## Setup

1. Create a Factdock **Medical DB** API key on the Factdock for Developers page: https://fact-dock.com/en/product/medical-db-api/
2. In Dify, install the Factdock Medical DB plugin, open **Tools > Factdock Medical DB > API key authorization**, and paste the key.
3. On the Factdock for Developers page, confirm the medical data notice once (results are reference information and final decisions are made by a qualified professional). Until then, the tools return a message asking for this confirmation and use no credits.
4. Add the tools to your agent or workflow.

Checking the key only lists the available tools and does not use credits.

## Credentials

- `factdock_api_key` (required): Factdock Medical DB API key, sent as `Authorization: Bearer <key>` to `https://data.fact-dock.com`.

## Pricing

Each call uses the key holder's Factdock API credits. Prices: https://fact-dock.com/en/product/medical-db-api/

## Connection requirements

- Outbound HTTPS to `https://data.fact-dock.com`.

## Important

- This plugin is a reference tool for doctors, dentists, veterinarians, pharmacists and other professionals. It is not medical or veterinary advice and does not replace a professional's judgement, diagnosis or the official product label.
- Records are returned in their original language as published by each authority.

## Support

- Website: https://fact-dock.com
- Contact: info@fact-dock.com
- Privacy policy: https://fact-dock.com/en/legal/privacy/
