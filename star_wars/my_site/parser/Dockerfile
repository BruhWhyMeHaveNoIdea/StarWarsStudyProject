FROM python:3.12-slim

WORKDIR /project/star_wars/my_site/parser

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "parser.py"]