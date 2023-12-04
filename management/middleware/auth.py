from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect


class AuthMiddleware(MiddlewareMixin):
    """页面验证是否登录"""
    def process_request(self, request):
        # 需要排除无需登录就能访问的页面
        # request.path_info 获取当前用户请求的url
        if request.path_info in ['/login/', '/image/code/', '/register/']:
            return

        # 读取session信息，如果有信息，说明已经登录
        info_dict = request.session.get('info')
        if info_dict:
            return
        # 若没有登录,则重定向回登录页面
        return redirect('/login/')
