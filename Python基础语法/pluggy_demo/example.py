"""
博文：https://www.cnblogs.com/ypppt/p/13371060.html
"""

import pluggy


hookspec = pluggy.HookspecMarker('example')
hookimpl = pluggy.HookimplMarker('example')


class MySpec(object):
    """
    A hook specification namespace.
    """

    @hookspec
    def myhook(self, arg, arg2):
        """
        My special little hook that you can customize.
        :param arg:
        :param arg2:
        :return:
        """


class Plugin(object):
    """
    A hook implementation namespace.
    """

    @hookimpl
    def myhook(self, arg, arg2):
        print("inside Plugin.myhook()")
        return arg + arg2


class Plugin2(object):
    """
    A 2nd hook implementation namespace.
    """

    @hookimpl
    def myhook(self, arg, arg2):
        print("inside Plugin2.myhook()")
        return arg - arg2


# create a manager and add the spec
pm = pluggy.PluginManager('example')
pm.add_hookspecs(MySpec)


# register plugins
"""
默认情况下，hook的调用顺序遵循注册时的顺序LIFO（后进先出），hookimpl允许通过tryfirst, trylast*选项调整这一项顺序。
"""
pm.register(Plugin())
pm.register(Plugin2())

# call our `myhook` hook
results = pm.hook.myhook(arg=1,arg2=2)
print(results)
