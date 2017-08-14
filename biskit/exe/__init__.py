## see: https://www.python.org/dev/peps/pep-0366/
## allow relative imports when calling module as main script for testing
if __name__ == "__main__" and __package__ is None:
    import biskit.exe
    __package__ = "biskit.exe"

from .exeConfig import ExeConfig, ExeConfigError
from .exeConfigCache import ExeConfigCache
from .executor import Executor, TemplateError

from .tmalign import TMAlign

##     from Pymoler import Pymoler

##     from XplorInput import XplorInput, XplorInputError
##     from Xplorer import Xplorer, XplorerError, RunError
##     from MatrixPlot import MatrixPlot

##     from Hmmer import Hmmer
##     from SurfaceRacer import SurfaceRacer, SurfaceRacer_Error
##     from DSSP import Dssp, Dssp_Error

##     from reduce import Reduce
##     from delphi import Delphi, DelphiError