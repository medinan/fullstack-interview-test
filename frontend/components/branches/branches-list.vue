<template>
  <div class="main-wrapper">
    <div class="main">
      <div class="main-inner">
        <div class="page-title">
          <div class="container">
            <h1>BRANCHES</h1>
            <!-- /.page-title-actions -->
          </div>
          <!-- /.container-->
        </div>
        <!-- /.page-title -->
        <div class="container">
          <nav class="breadcrumb">
            <a class="breadcrumb-item" href="/">Home</a>
            <span class="breadcrumb-item active">branches</span>
          </nav>
          <table class="table">
            <thead>
            <tr>
              <th scope="col">Source</th>
              <th scope="col">Name</th>
              <th scope="col">Actions</th>
            </tr>
            </thead>
            <tbody>
              <tr v-for="branch in branches">
                <td>{{branch.source}}</td>
                <td>{{branch.name}}</td>
                <td><NuxtLink :to="'/branches/' + branch.source + '/' + branch.name">view detail</NuxtLink></td>
              </tr>

            </tbody>
          </table>
          <!-- /.row -->
        </div>
        <!-- /.container-fluid -->
      </div>
      <!-- /.main-inner -->
    </div>
    <!-- /.main -->
  </div>
</template>

<script>

  export default {
    name: "BranchesList",
    mounted: function () {
      this.getBranches();
    },
    data: function () {
      return {
        branches: []
      }
    },
    methods: {
      getBranches: function () {
        const url = "/api/v1/branches/"
        let self = this;
        this.$axios.get(url, {
          dataType: "json",
          headers: {"Content-type": "application/json"}
        }).then(function (response) {
          console.log(response.data);
          self.branches = response.data;
        })
      }
    }
  }
</script>

<style scoped>

</style>
