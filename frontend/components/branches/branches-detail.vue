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
            <a class="breadcrumb-item" href="#">Home</a>
            <a class="breadcrumb-item" href="#">Branches</a>
            <a class="breadcrumb-item active" href="#">{{ source }}/{{ branch }}</a>
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
              <tr v-for="branch in commits">
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
    name: "BranchDetail",
    props: ["source", "branch"],
    data: function () {
      return {
        commits: [
          {
            "commit": "dfsfsff"
          }
        ]
      }
    },
    methods: {
    }
  }
</script>

<style scoped>

</style>
