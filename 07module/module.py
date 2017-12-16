# 模块  模块是一组python代码的集合  一个.py 文件就是一个模块
# 好处
# 提高代码的可维护性
# 相互调用
# package

import Hello
print(Hello.greeting('nico'))
print(Hello.greeting('rui'))
print(Hello.__private_1('rui'))