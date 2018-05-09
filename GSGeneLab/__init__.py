"""
Jupyter Externsion for interacting with the GneeLab GenomeSpace data manager
"""
import IPython

__author__ = 'Ted Liefeld'
__copyright__ = 'Copyright 2018, Regents of the University of California & Broad Institute'
__version__ = '0.1'
__status__ = 'Beta'
__license__ = 'BSD'

from .utils import GSGeneLabClient, singleton, loadGSGToolsToNBToolManager

class GSGeneLab:
    

    def __init__(self, origin=None, id=None, name=None, description=None, attributes=None, tags=None, version=None,
                 load=None, render=None, tool_dict={}):
       print("Loading GSGeneLab inside __init__")



    def load_ipython_extension(ipython):
        ipython.log.info("GSGeneLab ipython loaded!")


    def _jupyter_server_extension_paths():
        return [{
            "module": "GSGeneLab"
        }]



def _jupyter_nbextension_paths():
    return [dict(
        section="notebook",
        # the path is relative to the `my_fancy_module` directory
        src="static",
        # directory in the `nbextension/` namespace
        dest="GSGeneLab",
        # _also_ in the `nbextension/` namespace
        require="GSGeneLab/genelab")]


def load_jupyter_server_extension(gsglapp):
    gsglapp.log.info("====== ====== GSGeneLab enabled!")
    loadGSGToolsToNBToolManager()
