# PYTHON_ARGCOMPLETE_OK

from argapp.cli import Arg, App, Bundle, Main
from .core import *


class UniwsInit(App):
    def __init__(self) -> 'None':
        super().__init__(
            name='init',
            help='Initialize a workspace.',
        )

    def __call__(self, bundle: 'Bundle') -> 'None':
        super().__call__(bundle)


class UniwsHardware(App):
    def __init__(self) -> 'None':
        super().__init__(
            name='hw',
            help='Hardware manipulation.',
        )

    def __call__(self, bundle: 'Bundle') -> 'None':
        super().__call__(bundle)


class UniwsSoftware(App):
    def __init__(self) -> 'None':
        super().__init__(
            name='sw',
            help='Software manipulation.',
        )

    def __call__(self, bundle: 'Bundle') -> 'None':
        super().__call__(bundle)


class UniwsMain(Main):
    def __init__(self) -> 'None':
        super().__init__(
            name='uniws',
            help='The primary application.',
        )
        self.add(UniwsInit())
        self.add(UniwsHardware())
        self.add(UniwsSoftware())


#
# Entry points.
#


def uniws():
    '''
    The primary application.
    '''
    UniwsMain()()


def uha():
    '''
    Shortcut: uniws hw attach.
    '''


def uhd():
    '''
    Shortcut: uniws hw detach.
    '''


def uho():
    '''
    Shortcut: uniws hw off.
    '''


def uhb():
    '''
    Shortcut: uniws hw boot.
    '''


def uhs():
    '''
    Shortcut: uniws hw shell.
    '''


def uhg():
    '''
    Shortcut: uniws hw get.
    '''


def uhp():
    '''
    Shortcut: uniws hw put.
    '''


def uhw():
    '''
    Shortcut: uniws hw watch.
    '''


def usf():
    '''
    Shortcut: uniws sw fetch.
    '''


def usp():
    '''
    Shortcut: uniws sw patch.
    '''


def usb():
    '''
    Shortcut: uniws sw build.
    '''


def usi():
    '''
    Shortcut: uniws sw install.
    '''


def ust():
    '''
    Shortcut: uniws sw test.
    '''


def usd():
    '''
    Shortcut: uniws sw deploy.
    '''


def usc():
    '''
    Shortcut: uniws sw clean.
    '''


def usr():
    '''
    Shortcut: uniws sw reset.
    '''


def usw():
    '''
    Shortcut: uniws sw wipe.
    '''
