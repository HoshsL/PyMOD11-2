from typing import Dict
import openpyxl
import pickle
import os

workplace = os.getcwd()


def printRC(time: str):
    """
    读取RegionCode_[年份]\n
    参数\n
    time: str -> 年份编号 例: 2024年即 24\n
    """
    os.chdir(os.path.dirname(__file__))
    with open("../src/pymod112/RegionCode_" + time, "rb") as f:
        region_code: Dict[str, str] = pickle.load(f)  # 例{code:name}
    print(region_code)


def createRC(time: str):
    """
    创建RegionCode_[年份]\n
    参数\n
    time: str -> 年份编号 例: 2024年即 24\n

    导入xlsx表名为 RegionCode
    """

    os.chdir(os.path.dirname(__file__))

    rc = openpyxl.load_workbook("./xlsx/RegionCode_" + time + ".xlsx")

    load_dict = {}

    for row in rc["RegionCode"].rows:
        if row[0].value.isnumeric() and len(row[0].value) == 6:  # type: ignore
            load_dict[row[0].value] = row[1].value

    with open("../src/pymod112/RegionCode_" + time, "wb") as f:
        pickle.dump(load_dict, f)  # 例{code:name}


if __name__ == "__main__":
    createRC("24")
    printRC("24")
