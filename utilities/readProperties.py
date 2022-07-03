import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def readConfigFile():
        config = configparser.RawConfigParser()
        config.read(".\\Configurations\\config.ini")
        return config

    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url
