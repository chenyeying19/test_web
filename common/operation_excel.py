import pandas


# data = []
# # 读取表格
# table = pandas.read_excel('./test_data.xlsx')
#
# for i in table.index.values:
#     data_dic = table.loc[i].to_dict()
#     data.append(data_dic)
# print(data)

class Operation_Excel(object):
    def __init__( self, filepath ):
        self.table = pandas.read_excel(filepath)

    def get_table_info( self ):
        data = []
        for i in self.table.index.values:
            data_dic=self.table.loc[i].to_dict()
            data.append(data_dic)
        return data

if __name__ == '__main__':
    filepath='../data/test_data.xlsx'
    oper_excel = Operation_Excel(filepath)
    data=oper_excel.get_table_info()

    print(data)
