from flask import Flask, Response
import time

app = Flask(__name__)

# メトリクスを保持するための辞書
metrics = {
    'atomlite_weight': {'value': None, 'last_updated': None}
}

@app.route('/set_gauge/<value>')
def set_gauge(value):
    """Gaugeの値を設定するエンドポイント"""
    try:
        metrics['atomlite_weight']['value'] = float(value)
        metrics['atomlite_weight']['last_updated'] = time.time()
        return f'Gauge set to {value}'
    except ValueError:
        return 'Invalid value', 400

@app.route('/metrics')
def custom_metrics():
    """カスタムメトリクスを出力するエンドポイント"""
    gauges_output = []
    gauges_output.append('# HELP atomlite_weight Hot walter level\n')
    gauges_output.append('# TYPE atomlite_weight gauge\n')
    current_time = time.time()
    for name, info in metrics.items():
        # メトリックが有効かチェック（ここでは12秒以内に更新されていれば有効とみなす）
        if info['value'] is not None and (current_time - info['last_updated']) <= 12:
            gauges_output.append(f'{name} {info["value"]}\n')

    # `gauges_output`の内容を結合して1つのレスポンスとして返す
    response = ''.join(gauges_output) if gauges_output else '# No active gauges\n'
    return Response(response, mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
