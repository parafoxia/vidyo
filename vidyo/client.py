import logging

import requests

from vidyo import ResponseNotOK
from vidyo.video import Video


class Client:
    __slots__ = ("_key",)

    def __init__(self, key: str) -> None:
        self._key = key

    @property
    def url(self):
        return (
            "https://www.googleapis.com/youtube/v3/videos"
            "?part=contentDetails%2Cid%2CliveStreamingDetails%2Clocalizations"
            "%2Cplayer%2CrecordingDetails%2Csnippet%2Cstatistics%2Cstatus"
            "%2CtopicDetails&key="
        ) + self._key

    def get_video(self, id_: str) -> Video:
        logging.info("Getting video information...")
        with requests.get(self.url + f"&id={id_}") as r:
            if not r.ok:
                raise ResponseNotOK(f"{r.status_code}: {r.reason}")
            return Video(r.json()["items"][0])
