import pandas as pd
from datetime import datetime


class Executor:
    def __init__(self, path):
        self.path = path
        pass

    def write_file(self, *args):
        dt = datetime.now().strftime("%d/%m/%y %H")
        ip = args[0]
        platform = args[1]
        str_format = "{},{},{}\n".format(dt, ip, platform)

        with open(self.path, "a") as file1:
            # Writing data to a file
            file1.writelines(str_format)

    def read_file(self):
        df = pd.read_table(self.path, delimiter=',',header=None)
        data = df.groupby([0, 1]).count().reset_index()
        data['tx'] = data.apply(lambda row: {"date": row[0], "ip": row[1], "hits": row[2]}, axis=1)
        return data['tx'].to_list()
