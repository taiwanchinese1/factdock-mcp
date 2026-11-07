# Installing the Factdock MCP server

Factdock is a remote MCP server. There is nothing to download, build or run locally.

1. The user needs a Factdock account on a paid plan, and a personal API key created at https://fact-dock.com/api-hub (it starts with `fdu_`). Ask the user to paste the key; do not create an account for them.
2. Add this entry to the MCP settings file:

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

3. Replace `fdu_YOUR_KEY` with the user's key.
4. Check the connection by calling the free `get_prices` tool. It uses no credits.

Notes:
- Paid tools use the user's Factdock credits. Each tool description ends with its price.
- `web_search` needs a `zone`: a country code such as `cc_JP`, or a language sphere. Confirm the country or language with the user.
- Veterinary and medicine-database tools need a one-time agreement in the Factdock app first.
