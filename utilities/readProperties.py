import configparser

config = configparser.RawConfigParser()
# config.read(".\\Configurations\\config.ini")
config.read(".//Configurations/config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common_info', 'baseURL')
        # Allan is a man
        return url

    @staticmethod
    def getUseremail():
        username = config.get('common_info', 'useremail')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common_info', 'password')
        return password
