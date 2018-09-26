娃娃机，掉球机，篮球机测试工具;

测试方式两种：串口，网络远程测试;

设置测试次数，自动测试;

自动添加包头，包尾，异或校验值;

计算异或值;

支持自更改协议测试;

保存以房间号命名的TXT文件;

本项目基于Python3：基于PYQT5规划基本UI界面；调用serial库，检测串口状态；使用threading库定义守护线程，监听串口接收状态；requests库获取web页面回调状态。

time.sleep()延时数据发送，等待机器反应；QApplication.processEvents()使QTextEdit实时显示；
！[Alt text](https://github.com/jade7wei/Python/blob/master/picture/Auto_exe.png)
