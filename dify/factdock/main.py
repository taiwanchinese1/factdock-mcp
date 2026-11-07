from dify_plugin import DifyPluginEnv, Plugin

# Some Factdock searches (country web search, patents, company reports) take up to about three minutes.
plugin = Plugin(DifyPluginEnv(MAX_REQUEST_TIMEOUT=240))

if __name__ == "__main__":
    plugin.run()
