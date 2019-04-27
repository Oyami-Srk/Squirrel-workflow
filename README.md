# Rime 工作流
---
### Info

![Alfrime](alfrime.png)

图标来自[la rime](https://github.com/rime/librime)以及[Alfred](https://www.alfredapp.com)
脚本依赖于[pypinyin](https://github.com/mozillazg/python-pinyin)

Rime tool for Alfred

请注意~~一定~~要安装`pypinyin`~~，以及`custom_phrase.txt`尾部留有**空行**~~

目前使用Workflow自带的文本追加，不需要手动留有空行。

~~不要一次使用太多的重新部署，部署过程需要时间，如果在此时间内运行重新部署~~

~~会导致输入法关闭，只能重新登录重启输入法~~

~~输入法部署完毕的标志：显示A或者中的那个小框框~~

现在的原理是发送鼠须管自带的部署快捷键，应该不会存在以上利用`pkill`的问题


修改脚本来适应你自己的输入方案，本人是自然码，可以调整到其他双拼或者全拼（未测试）

如果不想安装`pypinyin`，请保证输入两个参数（词，码）


在终端输入以下命令并输入密码来安装pypinyin：

`sudo /usr/bin/python -m ensurepip`

`sudo /usr/bin/python -m pip install pypinyin`


本脚本应用于**自然码**，通过*极少的*修改也可作用于其他双拼或者全拼方案

默认的`gap_space`是`False`，意味着每个字之间的拼音码是没有空格的

如果`gap_space`为`True`，每个字之间的拼音码就是有空格的

例：`gap_space`为`False` -> 北京 bzjy

例：`gap_space`为`True`  -> 北京 bz jy

同上，默认的`IsCodeReformating`是`False`，意味着不会自动转码三字及以上的词。

比如说“我爱你”在默认状态下输出的码是“woaini”，但开启此选项后会转码为“wani”

取首字和第二字的声母加上末字的声母和韵母。

四字及以上的词规则是取首三字的声母和末字的声母，比如说：

“生生不息” -> “uubx”

“床前明月光疑是地上霜” -> “iqmu”


工作流变量中的`AutoReDepoly`为`True`时会**自动**在添加完自定义程序后重新部署


---
### Usage

导入，使用，一气呵成

`rime-add-custom.py`的使用方法与workflow相同，可以在终端中执行，若想贡献此仓库，请提交代码到`rime-add-custom.py`


衷心感谢您的使用