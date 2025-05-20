import streamlit as st
import requests

st.set_page_config(page_title="交易查詢助手", page_icon="💰")
st.title("📊 交易資料語言查詢展示")

question = st.text_input("請輸入查詢問題（例如：查 user_id 為 123 的成功交易總額）")

if st.button("查詢") and question:
    with st.spinner("正在查詢中..."):
        try:
            api_url = "https://你的-fastapi-api.com/ask"  # ← 改成你的後端 API
            response = requests.post(api_url, json={"question": question})
            data = response.json()

            if "sql" in data:
                st.subheader("🔍 自動產生的 SQL 查詢")
                st.code(data["sql"])

                st.subheader("📄 查詢結果")
                st.table(data["data"])
            else:
                st.error("查詢失敗：" + str(data))
        except Exception as e:
            st.error(f"請求失敗：{e}")
