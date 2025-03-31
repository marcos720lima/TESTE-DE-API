from flask import Flask, jsonify, request
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 


file_path = "Relatorio_cadop.csv"
df = pd.read_csv(file_path, sep=",", encoding="utf-8")


colunas_relevantes = ["Registro_ANS", "Razao_Social", "Representante", "Data_Registro_ANS"]

@app.route("/buscar", methods=["GET"])
def buscar_operadoras():
    termo = request.args.get("termo", "").strip().lower()
    print(f"Termo buscado: {termo}")  

    if not termo:
        return jsonify({"erro": "Informe um termo para busca"}), 400

    
    resultados = df[df["Razao_Social"].astype(str).str.lower().str.contains(termo, na=False)]

    
    retorno = resultados[colunas_relevantes] if not resultados.empty else []

    print(f"Resultados encontrados: {len(resultados)}") 

    return jsonify(retorno.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
