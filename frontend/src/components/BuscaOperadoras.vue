<template>
  <div class="container">
    <h1>Buscar Operadoras</h1>
    <div class="search-container">
      <input v-model="termo" placeholder="Digite o termo de pesquisa" />
      <select v-model="campo">
        <option value="Razao_Social">Razão Social</option>
        <option value="Registro_ANS">Registro ANS</option>
        <option value="Representante">Representante</option>
      </select>
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

<script setup>
import { ref } from 'vue'
import axios from "axios";

const termo = ref("")
const campo = ref("Razao_Social")
const resultados = ref([])
const erro = ref("")

async function buscar() {
  erro.value = "";
  resultados.value = [];
  if (!termo.value) {
    erro.value = "Por favor, digite um termo.";
    return;
  }
  try {
    const response = await axios.get(`http://127.0.0.1:5000/buscar?termo=${termo.value}`);
    resultados.value = response.data;
  } catch (error) {
    erro.value = "Erro ao buscar dados.";
  }
}
</script>

<style>
.container {
  text-align: center;
  font-family: Arial, sans-serif;
  padding: 20px;
}

.search-container {
  margin-bottom: 20px;
  display: flex;
  gap: 10px;
  justify-content: center;
  align-items: center;
}

input {
  padding: 10px;
  width: 300px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 14px;
}

select {
  padding: 10px;
  width: 180px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 14px;
  background-color: white;
  cursor: pointer;
  appearance: none;
  background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
  background-repeat: no-repeat;
  background-position: right 10px center;
  background-size: 16px;
  padding-right: 40px;
}

select:hover {
  border-color: #007bff;
}

select:focus {
  outline: none;
  border-color: #007bff;
  box-shadow: 0 0 0 2px rgba(0,123,255,0.25);
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
  background: rgba(240, 245, 255, 0.85);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  border-radius: 15px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  padding: 20px;
  margin: 10px;
  width: 300px;
  text-align: left;
  border: 1px solid rgba(255, 255, 255, 0.5);
  transition: transform 0.2s ease;
}

.card:hover {
  transform: translateY(-5px);
  background: rgba(240, 245, 255, 0.95);
}

.card h3 {
  margin: 0;
  color: #2c3e50;
  font-size: 1.2em;
  margin-bottom: 10px;
}

.card p {
  margin: 8px 0;
  color: #34495e;
  font-size: 0.9em;
}

.erro {
  color: red;
  margin-top: 20px;
}
</style>
  
