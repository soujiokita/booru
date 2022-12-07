import re
import aiohttp
from typing import Union
from random import shuffle, randint
from ..utils.parser import Api, better_object, parse_image, get_hostname

Booru = Api()


class Realbooru(object):
    """Realbooru wrapper

    Methods
    -------
    search : function
        Search and gets images from realbooru.

    search_image : function
        Gets images, image urls only from realbooru.

    """

    @staticmethod
    def append_object(raw_object: dict):
        """Extends new object to the raw dict

        Parameters
        ----------
        raw_object : dict
            The raw object returned by realbooru.

        Returns
        -------
        str
            The image url.
        """
        for i in range(len(raw_object)):
            if raw_object[i]["directory"] and "id" in raw_object[i]:
                raw_object[i][
                    "file_url"
                ] = f"{get_hostname(Booru.realbooru)}/images/{raw_object[i]['directory']}/{raw_object[i]['image']}"
                raw_object[i][
                    "post_url"
                ] = f"{get_hostname(Booru.realbooru)}/index.php?page=post&s=view&id={raw_object[i]['id']}"

        
            elif not raw_object[i]["directory"]:
                raw_object[i][
                    "file_url"
                ] = f"{get_hostname(Booru.realbooru)}/images/{raw_object[i]['image'][0:2]}/{raw_object[i]['image'][2:4]}/{raw_object[i]['image']}"
                raw_object[i][
                    "post_url"
                ] = f"{get_hostname(Booru.realbooru)}/index.php?page=post&s=view&id={raw_object[i]['id']}"
                
                raw_object[i][
                    "directory"
                ] = f"{raw_object[i]['image'][0:2]}/{raw_object[i]['image'][2:4]}"

            else:
                raw_object[i]["file_url"] = Booru.error_handling_cantparse
                raw_object[i][
                    "post_url"
                ] = f"{get_hostname(Booru.realbooru)}/index.php?page=post&s=view&id={raw_object[i]['id']}"

        return raw_object

    def __init__(self, api_key: str = "", user_id: str = ""):
        """Initializes realbooru.

        Parameters
        ----------
        api_key : str
            Your API Key which is accessible within your account options page

        user_id : str
            Your user ID, which is accessible on the account options/profile page.
        """

        if api_key and user_id == "":
            self.api_key = None
            self.user_id = None
        else:
            self.api_key = api_key
            self.user_id = user_id

        self.specs = {"api_key": self.api_key, "user_id": self.user_id}

    async def search(
        self,
        query: str,
        block: str = "",
        limit: int = 100,
        page: int = 1,
        random: bool = True,
        gacha: bool = False,
    ) -> Union[aiohttp.ClientResponse, str]:

        """Search method

        Parameters
        ----------
        query : str
            The query to search for.
        block : str
            The tags you want to block, separated by space.
        limit : int
            Expected number which is from pages
        page : int
            Expected number of page.
        random : bool
            Shuffle the whole dict, default is True.
        gacha : bool
            Get random single object, limit property will be ignored.

        Returns
        -------
        dict
            The json object (as string, you may need booru.resolve())
        """

        if limit > 1000:
            raise ValueError(Booru.error_handling_limit)
        elif block and re.findall(block, query):
            raise ValueError(Booru.error_handling_sameval)

        self.query = query
        self.specs["tags"] = self.query
        self.specs["limit"] = limit
        self.specs["pid"] = page
        self.specs["json"] = "1"

        async with aiohttp.ClientSession() as session:
            async with session.get(Booru.realbooru, params=self.specs) as resp:
                self.data = await resp.json(content_type=None)
                if not self.data:
                    raise ValueError(Booru.error_handling_null)

                self.final = self.data
                for i in range(len(self.final)):
                    self.final[i]["tags"] = self.final[i]["tags"].split(" ")

                self.final = [
                    i for i in self.final if not any(j in block for j in i["tags"])
                ]

                self.not_random = Realbooru.append_object(self.final)
                shuffle(self.not_random)

                try:
                    if gacha:
                        return better_object(
                            self.not_random[randint(0, len(self.not_random))]
                        )
                    elif random:
                        return better_object(self.not_random)
                    else:
                        return better_object(Realbooru.append_object(self.final))

                except Exception as e:
                    raise Exception(f"Failed to get data: {e}")

    async def search_image(
        self, query: str, block: str = "", limit: int = 100, page: int = 1
    ) -> Union[aiohttp.ClientResponse, str, None]:

        """Parses image only

        Parameters
        ----------
        query : str
            The query to search for.
        block : str
            The tags you want to block, separated by space.
        limit : int
            Expected number which is from pages
        page : int
            Expected number of page.

        Returns
        -------
        dict
            The json object (as string, you may need booru.resolve())

        """

        if limit > 1000:
            raise ValueError(Booru.error_handling_limit)
        if block and re.findall(block, query):
            raise ValueError(Booru.error_handling_sameval)

        self.query = query
        self.specs["tags"] = self.query
        self.specs["limit"] = limit
        self.specs["pid"] = page
        self.specs["json"] = "1"

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(Booru.realbooru, params=self.specs) as resp:
                    self.data = await resp.json(content_type=None)
                    if not self.data:
                        raise ValueError(Booru.error_handling_null)
                    self.final = self.data

                    for i in range(len(self.final)):
                        self.final[i]["tags"] = self.final[i]["tags"].split(" ")

                    self.final = [
                        i for i in self.final if not any(j in block for j in i["tags"])
                    ]

                    self.not_random = parse_image(Realbooru.append_object(self.final))
                    shuffle(self.not_random)
                    return better_object(self.not_random)

        except Exception as e:
            raise Exception(f"Failed to get data: {e}")
