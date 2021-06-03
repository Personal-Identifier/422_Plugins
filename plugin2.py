import volatility.plugins.common as common
import volatility.utils as utils
import volatility.win32 as win32

from volatility.renderers import TreeGrid

class MyPlugin(common.AbstractWindowsCommand):
    ''' My plugin '''

    def calculate(self):
        addr_space = utils.load_as(self._config)
        tasks = win32.tasks.pslist(addr_space)
        return tasks

    def generator(self, data):
        for task in data:
            yield (0, [
                int(task.UniqueProcessId),
                str(task.ImageFileName)
            ])

    def unified_output(self, data):
        tree = [
            ("PID", int),
            ("Name", str)
            ]
        return TreeGrid(tree, self.generator(data))
