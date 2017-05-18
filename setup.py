
from distutils.core import setup
import py2exe
import os
path = os.getcwd()+"/"
text_files = [path+"counts.txt", path+"dataTypes.txt", path+"inventory.txt"]
setup(
    windows=["__init__.py"],
    data_files=[("", text_files)],
    #options={"py2exe": {"unbuffered": True, "optimize": 2, "excludes": ["email"]}}
)
