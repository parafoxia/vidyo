class VidyoError(Exception):
    """The base exception class."""

    pass


class ResponseNotOK(VidyoError):
    """Exception thrown when a request returned a non-OK status code."""

    pass
