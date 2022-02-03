# AWS Cloudwatch에서 CSV 받기

## 1. INSTALL

- boto3이 설치 되어 있지 않은 경우 다음을 실행

```
pip install -r requirements.txt
```

혹은

```
pip install boto3
```

---

## 2. config.py 설정

- config.py에서 주석을 참고하여 설정

---

## 3. 실행

```
python cloudwatch_logs_to_csv.py
```

---

## 4. 고려사항

- csv는 행 제한수를 넘어가면 데이터를 파일을 따로 받던지 sheet 개념이 없기 때문에 excel로 변경 해야 함
