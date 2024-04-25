from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

try:
    db = pd.read_csv("atendimentos.csv")
except FileNotFoundError:
    print("Arquivo CSV não encontrado.")
    db = None


@app.route("/api/v1/atendimentos", methods=["GET"])
def list_attendance():

    if db is None:
        return jsonify({"error": "Erro ao carregar o banco de dados"}), 400

    data_atendimento = request.args.get("data_atendimento")
    condicao_saude = request.args.get("condicao_saude")
    unidade = request.args.get("unidade")

    filtered_df = db
    if data_atendimento:
        filtered_df = filtered_df[filtered_df["data_atendimento"] == data_atendimento]
    if condicao_saude:
        filtered_df = filtered_df[
            filtered_df["condicao_saude"].str.contains(condicao_saude, case=False)
        ]
    if unidade:
        filtered_df = filtered_df[
            filtered_df["UNIDADE"].str.contains(unidade, case=False)
        ]

    result = filtered_df.to_json(orient="records")

    return result, 200
