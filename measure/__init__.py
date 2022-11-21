from measure import _version
from measure.controller import MainController

# Version number based on git tags
__version__ = _version.get_versions()["version"]

# Change to static version for executable versions in order to display the correct software title
if __version__ == "0+unknown":
    __version__ = "0.1.5"

# Application controller
app = MainController()
