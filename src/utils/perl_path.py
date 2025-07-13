import os
import shutil
import json

def find_perl():
    """
    Returns the path to Perl, by checking:
    1. PERL_PATH env variable
    2. System PATH
    3. config.json (if present)
    Raises RuntimeError if not found.
    """
    env_perl = os.environ.get("PERL_PATH")
    if env_perl and os.path.exists(env_perl):
        return env_perl
    path_perl = shutil.which("perl")
    if path_perl:
        return path_perl
    config_path = "config.json"
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            config = json.load(f)
            config_perl = config.get("perl_path")
            if config_perl and os.path.exists(config_perl):
                return config_perl
    raise RuntimeError(
        "Perl interpreter not found. Please install Perl and make sure it's in your PATH, "
        "set the PERL_PATH environment variable, or specify 'perl_path' in config.json."
    )
