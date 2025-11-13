FROM python:3.11-slim

WORKDIR /app

# 先装依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 再拷贝源代码
COPY train.py app.py ./

# 构建镜像时顺便把模型训练出来打包进去
RUN python train.py

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]