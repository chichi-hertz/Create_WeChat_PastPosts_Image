- # 微信尾部往期精选图生成器

  本项目是一个使用 Python3 编写的微信尾部往期精选图生成器，用于自动生成一张带有文章标题的微信尾部往期精选图。

  原图：

  ![image-20230402201226730](C:\Users\pdh\AppData\Roaming\Typora\typora-user-images\image-20230402201226730.png)

  使用效果：

  <img src="D:\weixintest\往期推荐完成_B站出大新闻了！.png" alt="往期推荐完成_B站出大新闻了！" style="zoom:50%;" />

  还有一种效果，请参考http://t.csdn.cn/0wSRY

  ![image-20230402201354823](C:\Users\pdh\AppData\Roaming\Typora\typora-user-images\image-20230402201354823.png)

  ## 安装依赖

  本项目依赖于以下 Python 包，已经在 `requirements.txt` 文件中列出：

  - requests
  - lxml
  - Pillow
  - tkinter

  使用以下命令安装依赖：

  ```
  pip install -r requirements.txt
  ```

  ## 如何使用

  1. 运行 `setup.py` 文件。
  2. 在弹出的 GUI 窗口中，输入文章链接。
  3. 点击“一键生成”按钮，等待程序自动生成图片。
  4. 图片保存在执行文件所在目录下，并以文章标题命名。

  ## 代码结构

  - `main.py`: 包含 GUI 界面和主程序。
  - `create_footer_image()`: 根据文章标题和图片生成微信尾部往期精选图。
  - `download_image()`: 下载微信文章配图。
  - `get_article_title()`: 解析微信公众号文章标题。

  ## 注意事项

  - 本项目仅供学习使用，请勿将生成的图片用于商业用途。