"""
Workaround to debug on Windows since pelican.exe s are not Python scripts.

https://stackoverflow.com/questions/45930920/how-to-start-debugger-with-an-entry-point-script
"""

import pkg_resources
pelican_main = pkg_resources.load_entry_point('pelican', 'console_scripts', 'pelican')
pelican_main()
