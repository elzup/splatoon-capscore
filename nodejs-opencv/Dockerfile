FROM node:12-slim

# opencv-devのインストール
RUN apt-get update -y && apt-get install -y libopencv-dev \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*