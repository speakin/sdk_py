## 安装

    virtualenv -p python3 venv
    source venv/bin/activate
    cd openapi
    pip install -r requirements.txt
    python setup.py install
    cd tok
    python setup.py install

## 运行
    # 修改main.config中的bucket app的accessKey secretKey
    cd example
    python main.py
