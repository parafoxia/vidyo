import logging

import requests

from vidyo import ResponseNotOK
from vidyo.video import Video


class Client:
    """The client class.

    Args:
        key (str): The API key for the YouTube Data API.
    """

    __slots__ = ("_key",)

    def __init__(self, key: str) -> None:
        self._key = key

    @property
    def _pre_url(self):
        return (
            "https://www.googleapis.com/youtube/v3/videos"
            "?part=contentDetails%2Cid%2CliveStreamingDetails%2Clocalizations"
            "%2Cplayer%2CrecordingDetails%2Csnippet%2Cstatistics%2Cstatus"
            "%2CtopicDetails&key="
        ) + self._key

    def get_video(self, id_: str) -> Video:
        """Executes an API request to get video information.

        Args:
            id_ (str): The video ID to get information for.

        Returns:
            Video: An object containing video information.

        Raises:
            ResponseNotOK: The request returned a non-OK status code.
        """
        logging.info("Getting video information...")
        with requests.get(self._pre_url + f"&id={id_}") as r:
            if not r.ok:
                raise ResponseNotOK(f"{r.status_code}: {r.reason}")
            return Video(r.json()["items"][0])
