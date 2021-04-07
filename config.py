import configparser

class Config():
    @staticmethod
    def get():
        parameters = {}
        config = configparser.ConfigParser()
        config.read("config.ini")
        for section in config:
            parameters[section] = {}
            for field in config[section]:
                try:
                    parameters[section][field] = int(config[section][field])
                except:
                    parameters[section][field] = config[section][field]

        return parameters





