from nslsii import configure_base
from IPython import get_ipython

configure_base(get_ipython().user_ns, 'local')
bec.disable_plots()

# Optional: set any metadata that rarely changes.
RE.md['beamline_id'] = 'TES-sirepo'
