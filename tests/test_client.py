import datetime as dt

import pytest  # type: ignore
from PIL import Image

import vidyo


@pytest.fixture()
def client() -> vidyo.Client:
    with open("./secrets/api-key", mode="r", encoding="utf-8") as f:
        key = f.read().strip("\n")

    return vidyo.Client(key)


def test_normal(client: vidyo.Client) -> None:
    v = client.get_video("jNQXAC9IVRw")
    assert v.id == "jNQXAC9IVRw"
    assert v.published == dt.datetime(2005, 4, 24, 3, 31, 52)
    assert v.channel.name == "jawed"
    assert v.channel.id == "UC4QobU6STFB0P71PMvOGN5A"
    assert v.title == "Me at the zoo"
    assert (
        v.description
        == "The first video on YouTube. While you wait for Part 2, listen to this great song: https://www.youtube.com/watch?v=zj82_v2R6ts"
    )
    assert v.tags == ["me at the zoo", "jawed karim", "first youtube video"]
    assert v.category_id == 1
    assert not v.live
    assert v.duration == dt.timedelta(seconds=19)
    assert not v.is_hd
    assert not v.is_3d
    assert v.captioned
    assert not v.is_360
    assert v.privacy == "public"
    assert v.license == "creativeCommon"
    assert v.embeddable
    assert not v.for_kids
    assert isinstance(v.views, int)
    assert isinstance(v.likes, int)
    assert isinstance(v.dislikes, int)
    assert isinstance(v.favourites, int)
    assert isinstance(v.comments, int)


def test_no_tags(client: vidyo.Client) -> None:
    v = client.get_video("ZOA-mLG3bqs")
    assert v.tags == []


def test_live_stream(client: vidyo.Client) -> None:
    v = client.get_video("5qap5aO4i9A")
    assert v.live


def test_hd_3d_360(client: vidyo.Client) -> None:
    v = client.get_video("rTM8vXtdIUA")
    assert v.is_hd
    assert v.is_3d
    assert v.is_360


def test_for_kids(client: vidyo.Client) -> None:
    v = client.get_video("tFoUuFq3vHw")
    assert v.for_kids


def test_ratings_off(client: vidyo.Client) -> None:
    v = client.get_video("ZgWsVQbXOfo")
    assert v.likes == -1
    assert v.dislikes == -1


def test_comments_off(client: vidyo.Client) -> None:
    v = client.get_video("m4ziIcbb4xI")
    assert v.comments == -1


def test_video_comparison(client: vidyo.Client) -> None:
    base = client.get_video("6Af6b_wyiwI")
    v1 = client.get_video("6Af6b_wyiwI")
    v2 = client.get_video("RiSImsDN6BE")
    assert base == v1
    assert base != v2
    assert base.channel == v1.channel
    assert base.channel != v2.channel


def test_thumbnail(client: vidyo.Client) -> None:
    v = client.get_video("6Af6b_wyiwI")
    assert isinstance(v.get_thumbnail(), Image.Image)
    assert v.get_thumbnail().width == 1280
    v = client.get_video("jNQXAC9IVRw")
    assert v.get_thumbnail().width == 480
