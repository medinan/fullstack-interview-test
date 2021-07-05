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
            <a class="breadcrumb-item" href="/branches/">Branches</a>
            <a class="breadcrumb-item active" href="#">{{ source }}/{{ branch }}</a>
          </nav>
          <table class="table">
            <thead>
            <tr>
              <th scope="col">hash</th>
              <th scope="col">message</th>
              <th scope="col">author</th>
              <th scope="col">date</th>
              <th scope="col">actions</th>
            </tr>
            </thead>
            <tbody>
              <tr v-for="commit in details.commits">
                <td>{{commit.hash}}</td>
                <td>{{commit.message}}</td>
                <td>{{commit.author}}</td>
                <td>{{commit.date}}</td>
                <td><NuxtLink :to="'/branches/' + source + '/' + branch + '/' + commit.hash ">view detail</NuxtLink></td>
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
    mounted: function () {
      this.getCommits();
    },
    data: function () {
      return {
        details: []
      }
    },
    methods: {
      getCommits: function () {
        const url = "/api/v1/branches/" + this.source + "_" + this.branch
        let self = this;
        this.$axios.get(url, {
          dataType: "json",
          headers: {"Content-type": "application/json"}
        }).then(function (response) {
          console.log(response.data);
          self.details = response.data;
        })
      }
    }
  }
</script>

<style scoped>

</style>
