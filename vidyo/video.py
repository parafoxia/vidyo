import datetime as dt
import io
import logging
import re

import requests
from PIL import Image

from vidyo.channel import PartialChannel
from vidyo.errors import ResponseNotOK

DUR_REGEX = re.compile(
    r"P([0-9]{1,2}D)?T?([0-9]{1,2}H)?([0-9]{1,2}M)?([0-9]{1,2}S)?"
)
DUR_MUL = (86400, 3600, 60, 1)


class Video:
    __slots__ = (
        "id",
        "date_published",
        "channel",
        "title",
        "description",
        "_thumbnails",
        "tags",
        "category",
        "category_id",
        "live",
        "duration",
        "is_3d",
        "is_hd",
        "captioned",
        "is_360",
        "privacy",
        "license",
        "embeddable",
        "for_kids",
        "views",
        "likes",
        "dislikes",
        "favourites",
        "comments",
    )

    def __init__(self, data: dict) -> None:
        snippet = data["snippet"]
        content = data["contentDetails"]
        status = data["status"]
        stats = data["statistics"]

        self._thumbnails = snippet["thumbnails"]

        self.id = data["id"]
        self.date_published = dt.datetime.fromisoformat(
            snippet["publishedAt"].strip("Z")
        )
        self.channel = PartialChannel(
            snippet["channelId"], snippet["channelTitle"]
        )
        self.title = snippet["title"]
        self.description = snippet["description"]
        self.tags = snippet.get("tags", [])
        self.category_id = int(snippet["categoryId"])
        self.live = snippet["liveBroadcastContent"] == "live"
        self.duration = self._parse_duration(content["duration"])
        self.is_3d = content["dimension"] == "3d"
        self.is_hd = content["definition"] == "hd"
        self.captioned = content["caption"] == "true"
        self.is_360 = content["projection"] == "360"
        self.privacy = status["privacyStatus"]
        self.license = status["license"]
        self.embeddable = status["embeddable"]
        self.for_kids = status["madeForKids"]
        self.views = int(stats.get("viewCount", -1))
        self.likes = int(stats.get("likeCount", -1))
        self.dislikes = int(stats.get("dislikeCount", -1))
        self.favourites = int(stats.get("favoriteCount", -1))
        self.comments = int(stats.get("commentCount", -1))

    def __str__(self) -> str:
        return self.id

    def __repr__(self) -> str:
        return f"<Video id={self.id} title={self.title} views={self.views}>"

    def __eq__(self, other) -> bool:
        return self.id == other.id

    def __ne__(self, other) -> bool:
        return self.id != other.id

    def _parse_duration(self, duration: str) -> dt.timedelta:
        m = DUR_REGEX.match(duration)
        secs = 0
        for i, g in enumerate(m.groups()):
            if g:
                secs += int(g[:-1]) * DUR_MUL[i]
        return dt.timedelta(seconds=secs)

    def get_thumbnail(self) -> None:
        logging.info("Getting thumbnail...")
        t = sorted(
            self._thumbnails.items(), key=lambda x: x[1]["width"], reverse=True
        )[0][1]
        logging.info(f"Highest resolution: {t['width']}x{t['height']}")
        with requests.get(t["url"]) as r:
            if not r.ok:
                raise ResponseNotOK(f"{r.status_code}: {r.reason}")
            return Image.open(io.BytesIO(r.content))
