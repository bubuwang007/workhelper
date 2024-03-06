from ..Mac import Mac
from ..Command import Command
from ..Processor import *

class Elements:
    def __init__(self, commands: Mac):
        self.commands = commands

    @prep7
    def E(self, *args) -> Command:
        '''Defines an element by node connectivity. Up to 8 nodes can be defined.'''
        if len(args)>8:
            raise ValueError('Too many arguments')
        return Command(f'E,{",".join(map(str,args))}')
    
    @prep7
    def EDELE(self, start='all', stop='', step='') -> Command:
        '''Deletes elements from the model.'''
        return Command(f'EDELE,{start},{stop},{step}')

    @prep7
    def EPLOT(self, *args) -> Command:
        '''Plots the selected elements.'''
        return Command(f'EPLOT')

    @prep7
    def ELIST(self, start='all', stop='', step='', nnkey=0, rkey=1, ptkey=1) -> Command:
        '''Lists the element numbers and types.
            NNKEY
                Node listing key:
                0 — List attribute references and nodes.
                1 — List attribute references but not nodes.
            RKEY
                Real constant listing key:
                0 — Do not show real constants for each element.
                1 — Show real constants for each element. This includes default values chosen for the element.
            PTKEY
                LS-DYNA part number listing key (applicable to ANSYS LS-DYNA only):
                0 — Do not show part ID number for each element.
                1 — Show part ID number for each element.
        '''
        return Command(f'ELIST,{start},{stop},{step},{nnkey},{rkey},{ptkey}')

    @prep7
    def INISTATE(self, action, *args) -> Command:
        '''Initializes the state of the selected elements.
            Action
                Specifies action for defining or manipulating initial state data:
                
                SET — 
                    Designate initial state coordinate system, data type, and material type parameters. 
                DEFINE — 
                    Specify the actual state values, and the corresponding element, integration point, or layer information.
                WRITE — 
                    Write the initial state values to a file when the SOLVE command is issued.
                READ — 
                    Read the initial state values from a file.
                LIST — 
                    Read out the initial state data.
                DELETE — 
                    Delete initial state data from a selected set of elements. 
            args
                Val1, Val2, ..., Val9
                Input values based on the Action type.
        '''
        return Command(f'INISTATE,{action},{",".join(map(str,args))}')

    @prep7
    def MAT(self, mat=1)-> Command:
        '''Sets the element material attribute pointer.
            MAT
                Assign this material number to subsequently defined elements (defaults to 1).
        '''
        return Command(f'MAT,{mat}')
    