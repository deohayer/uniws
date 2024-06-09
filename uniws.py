# PYTHON_ARGCOMPLETE_OK

import sys

from .shell import *

# if DIR_UWS:
#     sys.path.insert(0, f'{DIR_UWS}/.uniws')
#     from hardware import hardware
#     from software import software
# else:
#     def hardware() -> 'list[Hardware]':
#         return []

#     def software() -> 'list[Software]':
#         return []


# class AppWorkspace(App):
#     '''
#     An application to initialize a uniform workspace: `uws`.
#     '''

#     def __init__(self) -> 'None':
#         super().__init__(
#             help='Initialize an empty workspace.',
#         )
#         self.arg_remote = Arg(
#             name='URI',
#             sopt='r',
#             lopt='remote',
#             help='A Git remote to set as the origin.',
#         )
#         self.args.append(self.arg_remote)
#         self.arg_branch = Arg(
#             name='NAME',
#             sopt='b',
#             lopt='branch',
#             help='A Git branch to set as the default.',
#         )
#         self.args.append(self.arg_branch)
#         self.arg_dir = Arg(
#             name='DIR',
#             count='?',
#             default=DIR_PWD,
#             help='A non-existing or empty directory.',
#         )
#         self.args.append(self.arg_dir)

#     def __call__(
#         self,
#         args: 'dict[Arg]' = None,
#         apps: 'list[App]' = None,
#     ) -> 'None':
#         dir = os.path.abspath(args[self.arg_dir])
#         if os.path.exists(dir):
#             if os.path.isdir(dir):
#                 if len(os.listdir(dir)) != 0:
#                     raise CallError(f'The directory is not empty: {dir}')
#             else:
#                 raise CallError(f'Not a directory: {dir}')
#         else:
#             os.makedirs(dir, 0o755)
#         branch = args[self.arg_branch]
#         branch = f'-b {branch}' if branch else ''
#         remote = args[self.arg_remote]
#         remote = f'git remote add origin {remote}' if remote else 'true'
#         sh(f'true'
#            f' && cp -RaT {os.path.dirname(__file__)}/template {dir}'
#            f' && cd {dir}'
#            f' && git init {branch}'
#            f' && {remote}'
#            f' && git add -A'
#            f' && git commit -m "Initial commit"'
#            f';')

def uniws() -> 'None':
    return
