from __future__ import absolute_import

from . import utils
from .si import inside_softimage
from .ma import inside_maya

if inside_softimage():
    from .si import show_qt, sianchor, SIWrapper
    anchor = sianchor
    Wrapper = SIWrapper
elif inside_maya():
    from .ma import show_qt, anchor, Wrapper
