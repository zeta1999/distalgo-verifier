from .ir import *

ir = [
    'Value',
    'Use',
    'Instruction',
    'Label',
    'Variable',
    'Send',
    'Start',
    'Setup',
    'New',
    'Config',
    'Tuple',
    'Clock',
    'Constant',
    'Property',
    'BinaryOp',
    'UnaryOp',
    'Assign',
    'Call',
    'CondBranch',
    'Branch',
    'PopOneElement',
    'Cardinality',
    'IsEmpty',
    'Return',
    'Integer',
    'Range',
    'SubScript',
    'Set',
    'List',
    'Received',
    'ProcessId',
    'RandomSelect',
    'Quantifier',
    'LogicOp',
    'Append',
]

__all__ = ir + ['BasicBlock', 'Module', 'Function', 'IRName']
