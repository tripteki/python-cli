from os.path import abspath, dirname
import toml

class Version:

    def __call__ (self) -> str:
        """
        :rtype: str
        """
        version = toml.load (abspath (dirname (abspath (__file__))+"/../pyproject.toml")).get ("project", {}). get ("version", "1.0.0")

        return version
