# TeleRoster

Telegram のグループからメンバーのユーザー名一覧を取得する小さなスクリプトです（Telethon 使用）。

**Requirements**

- Python 3.8+
- 依存は `requirements.txt` に記載（`telethon`, `python-dotenv`）

**Setup**

1. https://my.telegram.org/apps で `API ID` と `API HASH` を取得します。
2. ルートの `.env.example` をコピーして `.env` を作成し、必要な値を設定します。

```bash
cp .env.example .env
# 編集: TELEGRAM_API_ID, TELEGRAM_API_HASH, TELEGRAM_GROUP を設定
pip install -r requirements.txt
```

**Environment variables**

- `TELEGRAM_API_ID` (必須)
- `TELEGRAM_API_HASH` (必須)
- `TELEGRAM_GROUP` (必須) — 公開グループの `username`（例: examplegroup）、t.me の URL、または数値 ID（例: -1001234567890）
- `TELEGRAM_PHONE` (任意) — 電話番号（ログインに必要な場合）
- `TELEGRAM_SESSION` (任意) — セッション名（デフォルト: `session_name`）

**TELEGRAM_GROUP の取得方法**

- 公開グループ: `https://t.me/<username>` の `<username>` を指定
- 招待リンク（プライベート）: 招待 URL（例: `https://t.me/+xxxxxxxxxxxxxx`）をそのまま指定
- 数値 ID を確認するには簡易スクリプトでエンティティの `id` を表示できます:

```bash
python3 - <<'PY'
from telethon.sync import TelegramClient
from dotenv import load_dotenv
import os
load_dotenv()
api_id = int(os.environ['TELEGRAM_API_ID'])
api_hash = os.environ['TELEGRAM_API_HASH']
with TelegramClient('tmp', api_id, api_hash) as client:
	ent = client.get_entity('https://t.me/examplegroup')
	print(ent.id)
PY
```

**Usage**

```bash
python3 teleroster.py
```

もしくは一時的に環境変数を指定して実行:

```bash
TELEGRAM_API_ID=123456 TELEGRAM_API_HASH=xxxxxxxx TELEGRAM_GROUP=examplegroup python3 teleroster.py
```

**Notes**

- `.env` をリポジトリに含めたくない場合は `.gitignore` に追加してください。
- スーパグループの数値 ID は `-100...` で始まることがあります。


