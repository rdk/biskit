##
## Biskit, a toolkit for the manipulation of macromolecular structures
## Copyright (C) 2004-2007 Raik Gruenberg & Johan Leckner
##
## This program is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 3 of the
## License, or any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
## General Public License for more details.
##
## You find a copy of the GNU General Public License in the file
## license.txt along with this program; if not, write to the Free
## Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

__version__ = '3.0.0.a'

import logging

## public classes
try:
    ## default error handler
    from biskit.errorHandler import ErrorHandler
    EHandler = ErrorHandler()

##     from BisList import BisList, BisListError, ConditionError, AmbiguousMatch,\
##          ItemNotFound
##     from DictList import DictList

    from biskit.logFile import LogFile, StdLog, ErrLog
    from biskit.errors import BiskitError

##    from biskit.AmberCrdParser import AmberCrdParser, ParseError
##    from biskit.AmberRstParser import AmberRstParser
##     from Blast2Seq import Blast2Seq

##     from EDParser import EZDParser

    from biskit.pdbModel import PDBModel, PDBProfiles, PDBError
    from biskit.pcrModel import PCRModel

    from biskit.profileCollection import ProfileCollection, ProfileError
##     from ProfileMirror import ProfileMirror
    
    from biskit.pdbCleaner import PDBCleaner, CleanerError

##     from ModelList import ModelList
##     from CommandLine import CommandLine
    
    from biskit.amberResidues import AmberResidueType, AmberPrepParser
    from biskit.amberResidueLibrary import AmberResidueLibrary,\
                                           AmberResidueLibraryError
    
##     from atomCharger import AtomCharger
    

    from biskit.colorspectrum import ColorSpectrum, ColorError
##     from PDBDope import PDBDope
##     from Ramachandran import Ramachandran
    
    from .colorspectrum import ColorSpectrum, ColorError, colorRange
    from .matrixPlot import MatrixPlot
    
## ## PVM-dependent modules

##     from QualMaster import QualMaster
##     from StructureMaster import StructMaster
##     from StructureSlave import StructureSlave
##     from TrajFlexMaster import TrajFlexMaster, FlexError
    pass

except Exception as why:
    logging.warning('Could not import all biskit modules: ' + repr(why))
    raise

## clean up namespace
del logging

## facilitate access to core module classes
import biskit.core.localpath as LocalPath