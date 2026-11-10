# Privacy policy - Factdock Medical DB plugin for Dify

This plugin sends requests to the Factdock Business API (`https://data.fact-dock.com`), operated by Apia Business Affairs Co., Ltd.

## What is sent

- Your Factdock Business API key, as an `Authorization` header, to identify your account and charge API credits.
- The tool inputs you or your agent provide (for example a drug name, an active ingredient, an animal species or search words), which Factdock needs to run the search.

## What is not sent

- Do not enter patient names or other personal information in the tool inputs; the tools only need drug names, ingredients and search words.
- The plugin does not send your Dify conversations, files, workspace data or any other data beyond the tool inputs above.

## Storage

- The plugin itself stores nothing. Dify stores the API key encrypted as a credential.
- Factdock keeps account, credit and usage records (which tool was called, when, and the credits used). Search inputs and results are used to answer the request and are not used to train AI models.

## Third parties

Factdock searches public sources on the web and in official databases to answer a request. Details are in the Factdock privacy policy: https://fact-dock.com/en/legal/privacy/

## Contact

info@fact-dock.com
