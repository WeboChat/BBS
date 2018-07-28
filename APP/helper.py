#!/usr/bin/python3
# Author : Hily
# file: helper
# @Time: 18-7-28 上午9:10
import math


class PageHelper(object):
    """分页类实现"""
    def __init__(self, current_page=1, page_size=5, total=0, navigate_pages=5):
        self.current_page = current_page
        self.page_size = page_size
        self.total = total
        self.max_page = int(math.ceil(total / page_size))
        # 分页条需要显示的页数
        self.navigate_pages = navigate_pages

    # 是否有前一页
    def has_previous(self):
        return self.current_page > 1

    # 是否有后一页
    def has_next(self):
        return self.current_page < self.max_page

    # 需要显示的页码列表
    def navigate_page_nums(self):
        if self.navigate_pages >= self.max_page:
            navigate_page_nums = [i for i in range(1, self.max_page + 1)]
        else:
            start_page = self.current_page - self.navigate_pages // 2
            end_page = self.current_page + self.navigate_pages // 2
            # 防止页码越界
            # 最前navigate_pages页
            if start_page < 1:
                navigate_page_nums = [i for i in range(1, self.navigate_pages + 1)]
            # 最后navigate_pages页
            elif end_page > self.max_page:
                navigate_page_nums = [i for i in range(self.max_page - self.navigate_pages + 1, self.max_page + 1)]
            # 其它页码
            else:
                navigate_page_nums = [i for i in range(start_page, end_page + 1)]
        return navigate_page_nums

    # 当前页数据开始坐标
    def begin_index(self):
        return (self.current_page - 1) * self.page_size + 1

    # 当前页数据结束坐标
    def end_index(self):
        return self.current_page * self.page_size

    def __str__(self):
        return {
            'page': {
                'current_page': self.current_page,
                'page_size': self.page_size,
                'max_page': self.max_page,
                'total': self.total,
                'navigate_pages': self.navigate_pages,
            }
        }
