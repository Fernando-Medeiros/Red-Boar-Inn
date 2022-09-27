
class Post:
    __post = {
        "_id": "",
        "date": "",
        "charname": "",
        "sprite": "",
        "info": ""
    }

    @property
    def return_post(self) -> dict:
        return self.__post