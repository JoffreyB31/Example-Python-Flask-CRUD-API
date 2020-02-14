<template>
  <div id="app">
    <div>
      <input v-model="dogName" placeholder="Nom" />
    </div>
    <div>
      <input v-model.number="dogAge" placeholder="Age" />
    </div>
    <input type="submit" value="Ajouter" @click="addDog" />
    <table>
      <thead>
        <tr>
          <th v-for="key in columns" :key="'dog' + key">
            {{ key }}
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="dog in dogs" :key="dog.id">
          <td>{{ dog.id }}</td>
          <td>{{ dog.name }}</td>
          <td>{{ dog.age }}</td>
          <button @click="removeDog(dog.id)">X</button>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "App",
  data() {
    return {
      api: "http://localhost:5000/api",
      columns: ["id", "name", "age"],
      dogName: null,
      dogAge: null,
      dogs: []
    };
  },

  mounted() {
    this.fetchData();
  },

  methods: {
    addDog() {
      const params = {
        name: this.dogName,
        age: this.dogAge
      };

      axios
        .post(this.api + "/dogs", params)
        .then(() => {
          this.fetchData();
        })
        .catch(err => {
          console.log(err);
        });
    },

    fetchData() {
      axios
        .get(this.api + "/dogs")
        .then(res => {
          this.dogs = res.data;
        })
        .catch(err => {
          console.log(err);
        });
    },
    removeDog(id) {
      axios
        .delete(`${this.api}/dogs/${id}`)
        .then(() => {
          this.fetchData();
        })
        .catch(err => {
          console.log(err);
        });
    }
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

table {
  margin: 0 auto;
  margin-top: 100px;
  width: 300px;
  border: 2px solid #42b983;
  border-radius: 3px;
  background-color: #fff;
}
</style>
