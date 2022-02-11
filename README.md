# py-playwright

## コンテナ内からmac内のchromiumを動かす

plywrightをインストールしておく
```
npm install playwright-core
```

サーバーを立てる
```
npx playwright run-server 8080
```

コンテナを立ち上げて、コンテナ内で実行
```
python test_remote.py
```
