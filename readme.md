- # 微信尾部往期精选图生成器

  本项目是一个使用 Python3 编写的微信尾部往期精选图生成器，用于自动生成一张带有文章标题的微信尾部往期精选图。

  原图：

  ![image-20230402201226730](https://github.com/chichi-hertz/Create_WeChat_PastPosts_Image/blob/master/img/image-20230402201226730.png)

  使用效果：

  ![%E5%BE%80%E6%9C%9F%E6%8E%A8%E8%8D%90%E5%AE%8C%E6%88%90_B%E7%AB%99%E5%87%BA%E5%A4%A7%E6%96%B0%E9%97%BB%E4%BA%86%EF%BC%81.png](https://github.com/chichi-hertz/Create_WeChat_PastPosts_Image/blob/master/img/%E5%BE%80%E6%9C%9F%E6%8E%A8%E8%8D%90%E5%AE%8C%E6%88%90_B%E7%AB%99%E5%87%BA%E5%A4%A7%E6%96%B0%E9%97%BB%E4%BA%86%EF%BC%81.png)

  还有一种效果，请参考http://t.csdn.cn/0wSRY

  ![image-20230402201354823](https://github.com/chichi-hertz/Create_WeChat_PastPosts_Image/blob/master/img/image-20230402201354823.png)

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
