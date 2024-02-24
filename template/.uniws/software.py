from uniws import *


def software() -> 'list[Software]':
    '''
    Populate the list of available `Software`. Any `us*` action uses the list
    to determine the available `Software`. Note that the appearance and
    behavior depend on the number of items:
     * If the list is empty, nothing is done during the construction.
     * If there is only one item, its fields will replace the application fields.
       This is to avoid specifying a single item in the command line, better UX.
     * If there are multiple items, the first positional argument is a subcommand,
       a software to use. `Software.name` is used for the list of possible values.
       In this case, the software must be stated explicitly in the command line,
       even if it is the only one that supports the specific action.

    If there is no `Software` that supports the given action, the application
    prints an error and returns an exit code 1.
    The list may be empty, if not needed.
    '''
    return []
