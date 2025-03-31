<template>
    <div class="container">
      <h1>Buscar Operadoras</h1>
      <div class="search-container">
        <input v-model="termo" placeholder="Digite o nome da operadora" />
        <button @click="buscar">Buscar</button>
      </div>
  
      <div v-if="resultados.length" class="results">
        <div v-for="(item, index) in resultados" :key="index" class="card">
          <h3>{{ item.Razao_Social }}</h3>
          <p><strong>Registro ANS:</strong> {{ item.Registro_ANS }}</p>
          <p><strong>Representante:</strong> {{ item.Representante }}</p>
          <p><strong>Data de Registro:</strong> {{ item.Data_Registro_ANS }}</p>
        </div>
      </div>
  
      <p v-if="erro" class="erro">{{ erro }}</p>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    data() {
      return {
        termo: "",
        resultados: [],
        erro: ""
      };
    },
    methods: {
      async buscar() {
        this.erro = "";
        this.resultados = [];
        if (!this.termo) {
          this.erro = "Por favor, digite um termo.";
          return;
        }
        try {
          const response = await axios.get(`http://127.0.0.1:5000/buscar?termo=${this.termo}`);
          this.resultados = response.data;
        } catch (error) {
          this.erro = "Erro ao buscar dados.";
        }
      }
    }
  };
  </script>
  
  <style>
  .container {
    text-align: center;
    font-family: Arial, sans-serif;
  }
  
  .search-container {
    margin-bottom: 20px;
  }
  
  input {
    padding: 10px;
    width: 250px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  
  button {
    padding: 10px 15px;
    margin-left: 5px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #0056b3;
  }
  
  .results {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    margin-top: 20px;
  }
  
  .card {
    background: white;
    border-radius: 15px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    padding: 15px;
    margin: 10px;
    width: 300px;
    text-align: left;
  }
  
  .card h3 {
    margin: 0;
    color: #333;
  }
  
  .card p {
    margin: 5px 0;
    color: #555;
  }
  
  .erro {
    color: red;
    margin-top: 20px;
  }
  </style>
  
