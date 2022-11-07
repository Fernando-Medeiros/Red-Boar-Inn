
class ArenaBattleLog:

    __log = {
        '_id': '',
        'winner': '',
        'loser': '',
        'date': '',
    }

    @property
    def return_log(self) -> dict:
        return self.__log