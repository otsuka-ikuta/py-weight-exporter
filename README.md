# Python Weight server

## 準備

```sh
python3 -m venv venv
source bin/activate
pip install flask
pip install pyinstaller

pyinstaller -F -c py-weight-exporter.py
./deploy.sh
```

## 校正手順

1. 秤に何も載せずに電源を入れる
2. ポットの水を満杯にした状態で Aボタンを押す

## 懸念事項

1. 停電したら毎回校正手順を行わないと異常アラームとなる

## Eof
