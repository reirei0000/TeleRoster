import os
try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    # python-dotenv が無くても動作する（環境変数が既にセットされている場合）
    pass

from telethon import TelegramClient
from telethon.tl.types import User

# 環境変数から設定を取得します（セキュリティのためハードコードしない）
api_id = os.environ.get('TELEGRAM_API_ID')
api_hash = os.environ.get('TELEGRAM_API_HASH')
phone_number = os.environ.get('TELEGRAM_PHONE')  # 任意: +8190xxxxxxx など
group_username_env = os.environ.get('TELEGRAM_GROUP')  # 任意: ユーザー名/URL/数値ID
session_name = os.environ.get('TELEGRAM_SESSION', 'session_name')

if not api_id or not api_hash:
    raise RuntimeError('環境変数 TELEGRAM_API_ID と TELEGRAM_API_HASH を設定してください')

try:
    api_id = int(api_id)
except Exception:
    raise RuntimeError('TELEGRAM_API_ID は整数でなければなりません')

# group の識別子を解釈（数値なら int、それ以外は文字列のまま）
group_username = None
if group_username_env:
    try:
        group_username = int(group_username_env)
    except ValueError:
        group_username = group_username_env
# `TELEGRAM_GROUP` が設定されていない場合は明示的にエラーにする（必須）
if group_username is None:
    raise RuntimeError('環境変数 TELEGRAM_GROUP を設定してください（グループの URL/username/ID）')

client = TelegramClient(session_name, api_id, api_hash)

async def main():
    print("接続中...")
    
    # グループのエンティティ（情報）を取得
    group = await client.get_entity(group_username)
    
    print(f"グループ '{group.title}' のメンバーを取得します...")
    
    # メンバー一覧を反復処理
    async for user in client.iter_participants(group):
        if user.username:
            # print(f"{user.id},{user.username}")
            print(f"{user.username}")
        else:
            # Usernameが設定されていないユーザーもいます
            print(f"{user.id},{user.first_name},(No Username)")

# クライアントを開始
with client:
    client.loop.run_until_complete(main())
