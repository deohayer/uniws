def __pwd() -> 'str':
    return os.path.abspath(os.getenv('PWD'))


def __root() -> 'str':
    result = __pwd()
    while result != '/':
        if os.path.exists(f'{result}/.uniws'):
            return result
        result = os.path.dirname(result)
    return ''


DIR_PWD = __pwd()
'''
The current working directory.
'''

DIR_UWS = __root()
'''
The workspace root.
The first directory that contains a `.uniws` subdirectory.
'''

DIR_UNI = f'{DIR_UWS}/.uniws'
'''
`DIR_UWS/.uniws`
'''

DIR_BIN = f'{DIR_UWS}/bin'
'''
`DIR_UWS/bin`
'''

DIR_ETC = f'{DIR_UWS}/etc'
'''
`DIR_UWS/etc`
'''

DIR_LIB = f'{DIR_UWS}/lib'
'''
`DIR_UWS/lib`
'''

DIR_TMP = f'{DIR_UWS}/tmp'
'''
`DIR_UWS/tmp`
'''


class Hardware(App):
    '''
    A hardware representation, `name` serves as a unique identifier
    and as a value for a command line argument, if multiple hardwares
    are available.

    The `app_*` application fields correspond to the `uh*` commands,
    and can be identified by the first letter.
    Implement them as any other `App` - uniws takes care of the rest.
    Note that the `App.name` will be set to `Hardware.name`, though.

    It is not necessary to implement everything. Not applicable fields
    may be left as is (`None`).

    The fields are only suggestions and hints what to do. There are no
    UI/UX expectations, so the actual implementation can do whatever.
    '''

    def __init__(self, name: 'str') -> 'None':
        super().__init__(name=name)
        self.app_connect: 'App' = None
        self.app_power: 'App' = None
        self.app_upload: 'App' = None
        self.app_download: 'App' = None
        self.app_shell: 'App' = None
        self.app_action: 'App' = None


class Software(App):
    '''
    A software representation, `name` serves as a unique identifier
    and as a value for a command line argument, if multiple softwares
    are available.

    The `app_*` application fields correspond to the `us*` commands,
    and can be identified by the first letter.
    Implement them as any other `App` - uniws takes care of the rest.
    Note that the `App.name` will be set to `Software.name`, though.

    It is not necessary to implement everything. Not applicable fields
    may be left as is (`None`).

    The fields are only suggestions and hints what to do. There are no
    UI/UX expectations, so the actual implementation can do whatever.
    '''

    def __init__(self, name: 'str') -> 'None':
        super().__init__(name=name)
        self.app_download: 'App' = None
        self.app_build: 'App' = None
        self.app_install: 'App' = None
        self.app_test: 'App' = None
        self.app_clean: 'App' = None
        self.app_action: 'App' = None

