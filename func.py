import openpyxl as op


def getXlsx():
	wb = op.load_workbook('data.xlsx')
	sheet = wb.active
	dim = sheet.dimensions  # 表格维度
	cells = sheet[dim]  # 获取全部数据
	datas = {}  # 数据
	for row in cells:  # 遍历每一行的单元格
		i = 1
		for column in row:  # 遍历每一列的单元格
			if i == 1:
				i += 1
				col_name = column.value
				datas[col_name] = []
				continue
			datas[col_name].append(column.value)
	wb.close()
	return datas


def Search(key):
	datas = getXlsx()
	th = [list(datas)[0]] + datas.get(list(datas)[0])
	if datas.get(key):
		return [th, [key] + datas.get(key)]
	elif datas.get(int(key)):
		return [th, [key] + datas.get(int(key))]
	else:
		return None


if __name__ == '__main__':
	datas = {"ad": 1}
	print(datas.get("a"))
