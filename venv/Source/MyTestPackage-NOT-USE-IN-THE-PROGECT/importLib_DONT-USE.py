import importlib.util

def importLib(pathImportFile):
    spec = importlib.util.spec_from_file_location("", pathImportFile)
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    return  foo
