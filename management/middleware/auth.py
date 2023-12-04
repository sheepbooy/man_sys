from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect


class AuthMiddleware(MiddlewareMixin):
    """页面验证是否登录"""

    def process_request(self, request):
        # 检查当前请求的 URL 是否以 /admin 开头
        if request.path_info.startswith('/admin/'):
            return

        # 其他排除的路径
        excluded_paths = ['/login/', '/image/code/', '/register/']
        if request.path_info in excluded_paths:
            return

        # 读取session信息，如果有信息，说明已经登录
        info_dict = request.session.get('info')
        if info_dict:
            return

        # 若没有登录,则重定向回登录页面
        return redirect('/login/')
