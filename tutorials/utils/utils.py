import yaml
import importlib
import fnmatch
import glob

from PIL import Image
from IPython.display import display


def select_subset(available, wanted=None):
    if wanted is None:
        available_default = None
        if isinstance(available, dict):
            available_default = [k for k, v in available.items() if v.get('included_by_default') or v.get('include_in_default_catalog_list')]
        return set(available_default) if available_default else set(available)
        
    wanted = set(wanted)
    output = set()

    for item in wanted:
        matched = fnmatch.filter(available, item)
        if not matched:
            raise KeyError("{} does not match any available names: {}".format(item, ', '.join(sorted(available))))
        output.update(matched)

    return tuple(sorted(output))


def interpret_result(test_result):
    print("Status code:")
    print(test_result.status_code)
    print()
    if test_result.inspect_only:
        print("No pass/fail criterion specified, inspection only")
    elif test_result.passed:
        print("Test passed!")
    else:
        print("Test failed!")
    print()
    print("Summary message:")
    print(test_result.summary)
    return 