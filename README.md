node 版本 v16.15.0

npm 版本 9.6.0

python 版本 3.9.18

1. 第一次部署, 在 front_end 目录下使用命令 `npm install`
2. 每次运行, 在 back_end 目录下使用命令 `python app.py`; 在 front_end 目录下使用命令 `npm run start`.



推荐在mac运行，因为emoji字体全，有些布局也是依靠他来的

在windows上，可使用noto color emoji字体，他比较全，引入方法：在 `front_end/index.html`中插入

```
@import url('https://fonts.googleapis.com/css2?family=Noto+Color+Emoji&display=swap');
        body {
            font-family: 'Noto Color Emoji';
        }
```


以及下不下来就直接去要node_modules打的包
