import os

def win_to_cygwin_path(path):
    """
    Convert a Windows path (C:\\foo\\bar) to Cygwin path (/cygdrive/c/foo/bar).
    Returns the original if already POSIX-style.
    """
    path = os.path.abspath(path)
    if len(path) >= 3 and path[1:3] in (':\\', ':/'):
        return '/cygdrive/' + path[0].lower() + path[2:].replace('\\', '/')
    return path.replace('\\', '/')
