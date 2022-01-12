<template lang="html">
   <div class="container">
       <div class="row justify-content-sm-evenly">
           <div class="col text-start">
              <h2>Lista de Libros</h2>
                <div class="text-sm-center"><hr>
                  <b-table  striped hover :items="books" :fields="fields">
                  
                    <template slot="cell(action)" slot-scope="data">
                      <button class="btn-taller">
                      Editar
                      </button>
                      <b-button class="btn-taller_1">
                        Eliminar  
                      </b-button>
                    </template>             
                  
                  </b-table>
                </div>
           </div>
       </div>
   </div>
</template>

<script>
import axios from 'axios'

export default {
  data(){
    return {
      fields:[
        {key: 'title',label:'Titulo'},
        {key: 'description',label:'Descripcion'},
        {key:'action',label:'Acción'},
      ],
      books:[]
    }
  },
  methods: {
    getBooks(){
      const path = 'http://127.0.0.1:8000/api/v1/books/' 
      axios.get(path).then((response) => {
        this.books= response.data
      })
      .catch((error) => {
        console.log(error)
      })
    }

    
    },
  created(){
    this.getBooks()
  }

}
</script>

<style lang="css" scoped>


</style>