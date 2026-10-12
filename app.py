from flask import Flask, render_template, request, jsonify
import pandas as pd
import re
from rapidfuzz import fuzz

app = Flask(__name__)

# -----------------------------
# LOAD EXCEL
# -----------------------------
def load_excel():
    try:
        file_path = r"D:\OneDrive - Systems Limited\EXcel DATA\data.xlsx"

        df = pd.read_excel(file_path, engine="openpyxl")
        df = df.copy()

        # Clean column names
        df.columns = df.columns.str.strip()

        # Fill only text columns
        object_cols = df.select_dtypes(include=["object"]).columns
        for col in object_cols:
            df[col] = df[col].fillna("Not Available")

        return df

    except Exception as e:
        print("Excel Error:", e)
        return pd.DataFrame()


# -----------------------------
# CLEAN TEXT
# -----------------------------
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"[^a-z0-9\s\-]", "", text)
    return text


# -----------------------------
# ENVIRONMENT MAP
# -----------------------------
ENV_MAP = {
    "prod": "gtlf-prod",
    "production": "gtlf-prod",

    "stage": "gtlf-stage1",
    "staging": "gtlf-stage1",

    "test": "gtlf-test",
    "uat": "gtlf-uat",

    "build": "gtlf-build-01",

    "dev01": "gtlf-dev01",
    "dev03": "gtlf-erp-dev03",
    "dev04": "gtlf-plq-dev04",
    "dev06": "hbsdfs-dev06"
}


# -----------------------------
# RESOLVE ENVIRONMENT
# -----------------------------
def resolve_environment(message):
    message = message.lower()

    for key, value in ENV_MAP.items():
        if key in message:
            return value

    return message


# -----------------------------
# FIND ENVIRONMENT
# -----------------------------
def find_environment(df, env_name):

    env_name = env_name.lower().replace(" ", "")

    for _, row in df.iterrows():

        db_env = str(
            row.get("Environment name", "")
        ).lower().replace(" ", "")

        if env_name == db_env:
            return row

        if env_name in db_env or db_env in env_name:
            return row

    return None


# -----------------------------
# DETECT INTENT
# -----------------------------
def detect_intent(message):

    message = message.lower()

    if "upgrade type" in message:
        return "upgrade_type"

    if "current platform version" in message:
        return "version"

    if "platform version" in message:
        return "version"

    if "version" in message:
        return "version"

    if "deployed on" in message:
        return "deployment"

    if "deployment" in message:
        return "deployment"

    if "deploy" in message:
        return "deployment"

    if "status" in message:
        return "status"

    if "refresh" in message:
        return "refresh"

    if "tier" in message:
        return "tier"

    if "type" in message:
        return "type"

    if "upgrade" in message:
        return "upgrade"

    if "details" in message or "all details" in message:
        return "details"

    return "unknown"


# -----------------------------
# HOME
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -----------------------------
# CHAT
# -----------------------------
@app.route("/chat", methods=["POST"])
def chat():

    df = load_excel()

    if df.empty:
        return jsonify({
            "reply": "Excel file not found or cannot be loaded."
        })

    message = request.json.get("message", "")
    message = clean_text(message)

    env_input = resolve_environment(message)

    env_row = find_environment(df, env_input)

    if env_row is None:
        return jsonify({
            "reply": "Environment not found. Try: prod, stage, test, build, dev01, dev03, dev04."
        })

    env_name = env_row.get("Environment name", "Unknown")

    intent = detect_intent(message)

    # STATUS
    if intent == "status":
        return jsonify({
            "reply": f"The status of <b>{env_name}</b> is <b>{env_row.get('Status', 'Not Available')}</b>"
        })

    # TYPE
    elif intent == "type":
        return jsonify({
            "reply": f"Type of <b>{env_name}</b>: <b>{env_row.get('Environment type', 'Not Available')}</b>"
        })

    # TIER
    elif intent == "tier":
        return jsonify({
            "reply": f"Tier of <b>{env_name}</b>: <b>{env_row.get('Environment Tier', 'Not Available')}</b>"
        })

    # VERSION
    elif intent == "version":
        return jsonify({
            "reply": f"The platform version of <b>{env_name}</b> is <b>{env_row.get('Current Platform Version', 'Not Available')}</b>"
        })

    # UPGRADE DATE
    elif intent == "upgrade":
        return jsonify({
            "reply": f"Last platform upgrade of <b>{env_name}</b>: <b>{env_row.get('Last Platform Upgrade Date', 'Not Available')}</b>"
        })

    # UPGRADE TYPE
    elif intent == "upgrade_type":
        return jsonify({
            "reply": f"Upgrade type of <b>{env_name}</b>: <b>{env_row.get('Upgrade Type', 'Not Available')}</b>"
        })

    # DB REFRESH
    elif intent == "refresh":
        return jsonify({
            "reply": f"Last DB refresh of <b>{env_name}</b>: <b>{env_row.get('Last DB refresh Date', 'Not Available')}</b>"
        })

    # DEPLOYMENT
    elif intent == "deployment":

        if "Deployed on" not in df.columns:
            return jsonify({
                "reply": f"'Deployed on' column not found. Available columns: {df.columns.tolist()}"
            })

        deployment_value = env_row.get("Deployed on", "Not Available")

        return jsonify({
            "reply": f"Deployment info for <b>{env_name}</b>: <b>{deployment_value}</b>"
        })

    # DETAILS
    elif intent == "details":
        return jsonify({
            "reply": f"""
            <b>Environment:</b> {env_name}<br>
            <b>Type:</b> {env_row.get('Environment type', 'Not Available')}<br>
            <b>Tier:</b> {env_row.get('Environment Tier', 'Not Available')}<br>
            <b>Version:</b> {env_row.get('Current Platform Version', 'Not Available')}<br>
            <b>Status:</b> {env_row.get('Status', 'Not Available')}<br>
            <b>Last Upgrade:</b> {env_row.get('Last Platform Upgrade Date', 'Not Available')}<br>
            <b>Upgrade Type:</b> {env_row.get('Upgrade Type', 'Not Available')}<br>
            <b>Last Refresh:</b> {env_row.get('Last DB refresh Date', 'Not Available')}<br>
            <b>Deployed On:</b> {env_row.get('Deployed on', 'Not Available')}
            """
        })

    # UNKNOWN
    return jsonify({
        "reply": f"I found <b>{env_name}</b>, but I didn't understand your request."
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)