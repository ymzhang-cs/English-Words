# English-Words
 
File ```ask.exe``` is the executable form of ```ask.py``` in Windows OS by pyinstaller. You can downloaded it and use directly.

文件```ask.exe```是```ask.py```在Windows平台上的可执行形式(用pyinstaller制作)。可直接下载使用。

## Compile/编译

```
pip install pyinstaller
pyinstaller -F ask.py
```

## Way to Use/使用方法

Put ```wordList.txt``` in the same directory as ```ask.exe``` (or ```ask.py``` also works). Just run ```ask.exe``` (or ```ask.py```).

将```wordList.txt```放于```ask.exe```（或```ask.py```也可以）的同一目录。运行```ask.exe```（或```ask.py```）即可。

## Format of WordList/WordList的格式

```
外语@母语
ForeignLanguage@NativeLanguage

Example:
a@一个
example@例子
an example@一个例子
Bonjour@你好
こんにちは@Hello
etc.
```
