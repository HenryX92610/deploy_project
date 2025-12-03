FROM nginx:latest

# 删除默认配置
RUN rm /etc/nginx/conf.d/default.conf

# 拷贝你的 nginx 配置
COPY nginx.conf /etc/nginx/conf.d/default.conf

