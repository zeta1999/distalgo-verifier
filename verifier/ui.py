import argparse
import os
import sys

from .frontend import Parser, Translator
from .opt import *
from .target.tlaplus import CodeGen

DEBUG=True

def dpyfile_to_tla(infile, outfile=None):
    filename = os.path.basename(infile)
    with open(infile, "r") as f:
        source = f.read()
        parser = Parser()
        ast = parser.parse(source, infile)
        translator = Translator()
        modules = [translator.run(filename, ast)]
        pass_manager = PassManager()
        # add pass
        pass_manager.add_pass(BuildCFGPass())
        pass_manager.add_pass(SSAPass())
        pass_manager.add_pass(SimplifyCFGPass())
        pass_manager.add_pass(DumpFunction())
        pass_manager.run(modules)

        codegen = CodeGen()
        codegen.run(modules, outfile)

def main():
    """Main entry point when invoking compiler module from command line."""
    ap = argparse.ArgumentParser(description="DistAlgo to tla.")
    ap.add_argument('-o', help="Output file name.", dest="outfile")
    ap.add_argument('infile', help="DistPy input source file.")
    args = ap.parse_args()
    dpyfile_to_tla(args.infile, args.outfile)
