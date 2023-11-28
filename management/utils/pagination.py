"""
自定义的分页组件

"""

from django.utils.safestring import mark_safe
import copy


class Pagination(object):
    def __init__(self, request, queryset, page_size=9, page_param="page", page_show=5):
        """
        :param request: 请求的对象
        :param queryset: 符合条件的数据(根据此数据进行分页处理)
        :param page_size: 每页显示多少条数据
        :param page_param: 获取在URL中传递的分页参数, 例如: /pretty/list/?page=21
        :param page_show: 页码显示前几页后几页
        """

        # 防止搜索出结果进行翻页时,URL参数没有了搜索参数
        query_dict = copy.deepcopy(request.GET)
        query_dict._mutable = True
        self.query_dict = query_dict

        self.page_param = page_param

        page = int(request.GET.get(page_param, 1))

        # 如果不是整数
        if type(page) != int:
            # 强制让页码为1
            page = 1
        elif page < 1:
            page = 1

        self.page = page

        self.start = (page - 1) * page_size
        self.end = page * page_size

        # 每页展示的数据行数
        self.page_queryset = queryset[self.start:self.end]

        total_data_count = queryset.count()  # 数据行数
        total_page_count, div = divmod(total_data_count, page_size)
        if div:
            total_page_count += 1
        self.total_page_count = total_page_count  # 总页码数量
        self.page_show = page_show  # 当前页前后展示的页码数量
        self.request = request

    def html(self):
        # 如果总页码数量大于 11
        if self.total_page_count > self.page_show * 2 + 1:
            # 如果当前页面页码位置小于等于5
            if self.page <= 5:
                start_page = 1
                end_page = self.page_show * 2 + 2
            # 否则,当前页面页码位置大于5时
            else:
                # 防止页码超出范围
                if self.page >= self.total_page_count - self.page_show:
                    start_page = self.total_page_count - self.page_show * 2
                    end_page = self.total_page_count + 1
                else:
                    # 计算出当前页的前5页和后5页
                    start_page = self.page - self.page_show
                    end_page = self.page + self.page_show + 1

        else:
            start_page = 1
            end_page = self.total_page_count + 1

        ######## 创建页码 ########
        # 页码

        page_str_list = []

        # 跳到首页
        self.query_dict.setlist(self.page_param, [1])
        self.head_page = '<li class="page-item"><a class="page-link" href="?{}" aria-label="Previous"><span aria-hidden="true">首页</span></a></li>'.format(
            self.query_dict.urlencode())
        page_str_list.append(self.head_page)

        # 跳到上10页
        # 如果当前页面小于 11, 防止超过最小页数
        if self.page < self.page_show * 2 + 1:
            self.query_dict.setlist(self.page_param, [1])
            prev = '<li  class="page-item"><a class="page-link" href="?{}">{}</a></li>'.format(
                self.query_dict.urlencode(), "<<")
            page_str_list.append(prev)
        else:
            self.query_dict.setlist(self.page_param, [self.page - 10])
            prev = '<li  class="page-item"><a class="page-link" href="?{}">{}</a></li>'.format(
                self.query_dict.urlencode(), "<<")
            page_str_list.append(prev)

        for i in range(start_page, end_page):
            # 如果是当前页,高亮显示页码颜色
            if self.page == i:
                self.query_dict.setlist(self.page_param, [i])
                ele = '<li class="active"><a class="page-link" href="?{}">{}</a></li>'.format(
                    self.query_dict.urlencode(), i)
            else:
                self.query_dict.setlist(self.page_param, [i])
                ele = '<li  class="page-item"><a class="page-link" href="?{}">{}</a></li>'.format(
                    self.query_dict.urlencode(), i)
            page_str_list.append(ele)

        # 跳到下10页
        # 如果当前页面页数 大于 最大页面数量减去(page_show*2+1),则直接跳到最后一页,防止超过最大页数
        if self.page >= self.total_page_count - self.page_show * 2 + 1:
            self.query_dict.setlist(self.page_param, [self.total_page_count])
            next = '<li  class="page-item"><a class="page-link" href="?{}">{}</a></li>'.format(
                self.query_dict.urlencode(), ">>")
            page_str_list.append(next)
        else:
            self.query_dict.setlist(self.page_param, [self.page + 10])
            next = '<li  class="page-item"><a class="page-link" href="?page={}">{}</a></li>'.format(
                self.query_dict.urlencode(), ">>")
            page_str_list.append(next)

        # 跳到尾页
        self.query_dict.setlist(self.page_param, [self.total_page_count])
        self.end_page = '<li  class="page-item"><a class="page-link" href="?{}" aria-label="Next"><span aria-hidden="true">尾页</span></a></li>'.format(
            self.query_dict.urlencode())
        page_str_list.append(self.end_page)

        self.page_string = mark_safe("".join(page_str_list))
