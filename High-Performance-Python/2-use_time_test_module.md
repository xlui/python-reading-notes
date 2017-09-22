### 使用 Python 自带的时间测试模块

1. timeit 模块

示例：
```bash
python -m timeit -n 5 -r 5 -s "import file_to_be_tested"
```
timeit 会对语句循环执行 n 次（由 -n 参数指定）并计算平均值作为一个结果，重复 r 次（由 -r 参数指定）并选出最好的那个结果。  
必须用 -s 命令在设置阶段导入模块。  
如果不指定 -n 和 -r 运行 timeit，默认是循环 10 次重复 5 次。  

<br>

2. cProfile 模块

示例：
```bash
python -m cProfile -s cumulative file_to_be_tested.py
```
-s cumulative 开关告诉 cProfile 对每个函数累计花费的时间进行排序，这能让我们看到代码最慢的部分。  
可以通过 -o file_name 开关将结果生成为文件  

<br>

3. runsnakerun

runsnake 是一个可视化工具，用于显示 cProfile 创建的统计文件 -- 你只需要看它生成图像就可以快速意识到哪个函数的开销最大。  

