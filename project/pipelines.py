# coding! utf-8
# 这是管道文件
import os
import json
import requests
import datetime
import openpyxl
from openpyxl.styles import PatternFill, colors
from scrapy.utils.project import get_project_settings


class YYPipeline(object):

    def __init__(self):
        self.words = get_project_settings().get('WORDS')
        self.excel_file = get_project_settings().get('EXCEL_FILE')
        sheet_name = '记录'
        if not os.path.isfile(self.excel_file):
            self.workbook = openpyxl.Workbook()
            self.workbook.remove(self.workbook['Sheet'])
        else:
            self.workbook = openpyxl.load_workbook(self.excel_file)
        if sheet_name in self.workbook.sheetnames:
            self.sheet = self.workbook[sheet_name]
        else:
            self.sheet = self.workbook.create_sheet(sheet_name)
        self.sheet.cell(1, 1, '项目名称')
        self.sheet.cell(1, 2, '采购单位')
        self.sheet.cell(1, 3, '发布时间')
        self.sheet.cell(1, 4, '原文地址')
        self.sheet.cell(1, 5, '数据来源')
        self.workbook.save(self.excel_file)

    def process_item(self, item, spider):
        row = self.sheet.max_row + 1
        if self.verify_useful(item):
            self.sheet.cell(row, 1, item['name'])
            self.sheet.cell(row, 2, item['time'])
            self.sheet.cell(row, 3, item['unit'])
            self.sheet.cell(row, 4, item['address'])
            self.sheet.cell(row, 5, item['sources'])
        return item

    def close_spider(self, spider):
        self.workbook.save(self.excel_file)

    # 验证文章是否是符合需求的
    def verify_useful(self, item):
        date = datetime.datetime.strptime(item['time'], '%Y-%m-%d %H:%M')
        now = datetime.datetime.now().date()
        now_zero = datetime.datetime.now().replace(year=now.year, month=now.month, day=now.day, hour=0, minute=0, second=0)
        day = (date - now_zero).days
        if day >= 1 or day < 0:
            return False
        res = requests.get(item['address'])
        res.encoding = 'utf-8'
        for w in self.words:
            if w in res:
                return True
        # return False
        # TODO
        return True
