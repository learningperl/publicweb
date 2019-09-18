# coding:utf8
from common.Excel import Reader
from keywords.web import Web


def runcase(line,func):
    """
    用来运行用例的函数
    :param line: 用例的数据
    :param func: 关键字的实例对象，提供可用的关键字
    :return: 无
    """
    if len(line[0])>1 or len(line[1]) > 1:
        # 分组信息不执行
        return

    if line[3] == 'openbrowser':
        func.openbrowser(line[4])
        return

    if line[3] == 'geturl':
        func.geturl(line[4])
        return

    if line[3] == 'moveto':
        func.moveto(line[4])
        return

    if line[3] == 'click':
        func.click(line[4])
        return

    if line[3] == 'input':
        func.input(line[4],line[5])
        return

    if line[3] == 'sleep':
        func.sleep(line[4])
        return

    if line[3] == 'gettext':
        func.gettext(line[4])
        return

    if line[3] == 'assertequals':
        func.assertequals(line[4],line[5])
        return

    if line[3] == 'intoiframe':
        func.intoiframe(line[4])
        return

    if line[3] == 'outiframe':
        func.outiframe()
        return


reader = Reader()
func = Web()
reader.open_excel('./lib/Web.xls')
sheetname = reader.get_sheets()
for sheet in sheetname:
    # 设置当前读取的sheet页面
    reader.set_sheet(sheet)
    for i in range(reader.rows):
        line = reader.readline()
        print(line)
        runcase(line,func)




