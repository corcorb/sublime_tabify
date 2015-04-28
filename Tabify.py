import sublime, sublime_plugin

# An ST3 command to view tab-delimited files.
class TabifyCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    settings = self.view.settings()
    # set mode to tabs
    settings.set("translate_tabs_to_spaces", False)
    # set tab stop to "tabify_tab_size" or the default of 50
    tabify_tab_size = settings.get("tabify_tab_size", 50)
    settings.set("tab_size", tabify_tab_size)
    # Turn off word wrap
    settings.set("word_wrap", False)
