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
    """An object containing video information.

    Args:
        data (dict): Response data from the YouTube Data API. This should be the first element in the :code:`items` list.

    Attributes:
        id (str): The video ID.
        published (datetime.datetime): The date and time and the video was published.
        channel (PartialChannel): The YouTube channel to which the video was published.
        title (str): The video title.
        description (str): The video's description.
        tags (list[str]): A list of the video's tags. If there are none, this is an empty list.
        category_id (int): The video's category's ID.
        live (bool): Whether the video is currently live. This could mean it is a premiere or a live stream.
        duration (datetime.timedelta): The video's duration.
        is_3d (bool): Whether the video was uploaded in 3D.
        is_hd (bool): Whether there is a HD version of the video available (720p or above).
        captioned (bool): Whether there are captions available on the video.
        is_360 (bool): Whether the video was recorded in 360 degrees.
        privacy (str): The video's privacy status. Can be "public", "unlisted", or "private".
        license (str): The video's license. Can be either "youtube" or "creativeCommon".
        embeddable (bool): Whether the video is embeddable.
        for_kids (bool): Whether the video is marked as "Made For Kids".
        views (int): The number of views the video has. If this is not available, this will be -1.
        likes (int): The number of likes the video has. If ratings are disabled, this will be -1.
        dislikes (int): The number of dislikes the video has. If ratings are disabled, this will be -1.
        favourites (int): The number of favourites the video has. If this is not available, this will be -1.
        comments (int): The number of comments the video has. If comments are disabled, this will be -1.
    """

    __slots__ = (
        "id",
        "published",
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
        self.published = dt.datetime.fromisoformat(
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

    def get_thumbnail(self) -> Image.Image:
        """Gets the highest resolution thumbnail available.

        Returns:
            PIL.Image.Image: A Pillow image.

        Raises:
            ResponseNotOK: The request returned a non-OK status code.
        """
        logging.info("Getting thumbnail...")
        t = sorted(
            self._thumbnails.items(), key=lambda x: x[1]["width"], reverse=True
        )[0][1]
        logging.info(f"Highest resolution: {t['width']}x{t['height']}")
        with requests.get(t["url"]) as r:
            if not r.ok:
                raise ResponseNotOK(f"{r.status_code}: {r.reason}")
            return Image.open(io.BytesIO(r.content))
