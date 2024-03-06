import os
import re
import yaml

class CableLib:
    re_s = re.compile(r'^[Ss](\d+)[x×](\d+)')

    @staticmethod
    def get_cable_paras(cable_size: str):
        mch = CableLib.re_s.match(cable_size)
        if mch is None:
            raise ValueError(f"Invalid cable size: {cable_size}")
        cable_size = mch.group()
        with open(os.path.join(os.path.dirname(__file__), 'S.yml'), 'r', encoding='u8') as file:
            cable_data = yaml.load(file, Loader=yaml.FullLoader)
        if cable_size not in cable_data.keys():
            raise ValueError(f"Invalid cable size: {cable_size}")
        return cable_data[cable_size]

if __name__ == "__main__":
    re_s = re.compile(r'^[Ss](\d+)[x×](\d+)')
    match = re_s.match('s1x3')
