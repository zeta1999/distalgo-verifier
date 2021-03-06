#!/usr/bin/env python3

def iter_instructions(function):
    for block in function.basicblocks:
        for inst in block.ir:
            yield inst

class Pass(object):
    def __init__(self):
        self.pass_manager = None

    def init(self):
        pass

    def run(self, modules):
        pass

class ModulePass(Pass):
    def __init__(self):
        super().__init__()

    def run(self, modules):
        for module in modules:
            self.run_on_module(module)

    def run_on_module(self, module):
        pass

class FunctionPass(ModulePass):
    def __init__(self):
        super().__init__()

    def run_on_module(self, module):
        for function in module.functions:
            self.run_on_function(function)

    def run_on_function(self, function):
        pass

class BasicBlockPass(FunctionPass):
    def __init__(self):
        super().__init__()

    def run_on_function(self, function):
        for block in function.basicblocks:
            self.run_on_block(block)

    def run_on_block(self, block):
        pass
