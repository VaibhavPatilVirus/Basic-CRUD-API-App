#Get docker image.
FROM python:3.8-slim
#Set working directory.
WORKDIR /app
#Copy all files to working dir.
COPY . /app
#Install app dependencies.
RUN pip install --no-cache-dir -r dependencies.txt
#Expose container port outside the container.
EXPOSE 5000
#Run app
CMD ["python", "app.py"]